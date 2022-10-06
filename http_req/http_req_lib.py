import chunk
from code import interact
import configparser
import requests
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from numpy import hamming
import numpy as np
import time
import json
import os

# <<<---------------(http_req.py以外のプログラムから使用可能)--------------------

def AutomaticRequestChunksPath(init_chunk):
    init_chunk = int(init_chunk)
    # ConfigParserのインスタンス（特定の機能を持った変数）を取得
    config = configparser.ConfigParser()
    json_op = open('interaction.json', 'r')
    interaction = json.load(json_op)
    # config.iniを読み出し
    # 引数削減のため，プログラム内でconfig.iniを参照
    config.read("config.ini")
    token = str(config["http_req"]["token"])
    domain = str(config["http_req"]["domain"])
    interval = float(config["http_req"]["interval_AutomaticGetting"])
    interval_AutomaticAnswerPost = float(config["http_req"]["interval_AutomaticAnswerPost"])
    isAutoGetFiles = config["http_req"].getboolean("isAutoGetFiles")
    isEnableAutomaticTransition = config["http_req"].getboolean("isEnableAutomaticTransition")
    #分割データのリスト
    chunk_list = []
    #分割データのパスを記述したリスト
    path_list = []
    request_url_chunk = domain + "/problem/chunks?n=" + str(init_chunk)
    # POSTリクエスト
    print(">",end='',flush=True)
<<<<<<< HEAD
    # response = requests.post(request_url_chunk,headers={"procon-token": token})
    response = requests.get(domain + "/problem?token="+token)
=======
    response = requests.post(request_url_chunk,headers={"procon-token": token})
>>>>>>> origin/main
    #ステータスコードチェッカー
    if(response.status_code != 200):
        # dos判定の回避
        time.sleep(interval)
        if(response.status_code == 400):print(".",end="",flush=True)
        else:print("_",end='',flush=True)
        AutomaticRequestChunksPath(init_chunk)
    else:
        print("!")
        # アクセスが成功した場合
        print("chunks:")
        # ファイル名の格納
        for i in range(init_chunk):
<<<<<<< HEAD
            chunk_list.append(str(response.json()['chunks'][str(i)]))
=======
            chunk_list.append(str(response.json()['chunks'][i]))
>>>>>>> origin/main
            print(response.json()['chunks'][i])
        print()

        #音声ファイルの自動取得 -> 有効でないとファイルのパスが返らない
        if(isAutoGetFiles):
            # for i in range(init_chunk):
            #     print("> "+str(i)+": "+str(chunk_list[i]))
            #     path_list.append("./wave_files/"+str(chunk_list[i]))
            path_list = AutoGetFilesPath(init_chunk,chunk_list,token)
            #自動回答POST遷移 -> 無効を推奨
            if(isEnableAutomaticTransition):
                AutomaticAnswerPost(domain,token,interval_AutomaticAnswerPost)
        else:
            interaction['chunk_list'] = chunk_list
            output_json = open('interaction.json', 'w')
            json.dump(interaction, output_json, indent=4)
            for i in range(init_chunk):
                path_list.append("./wave_files/"+str(chunk_list[i]))
    return path_list

def RequestAdditional():
    config = configparser.ConfigParser()
    config.read("config.ini")
    token = str(config['http_req']['token'])
    domain = str(config["http_req"]["domain"])
    json_op = open('interaction.json', 'r')
    interval = float(config["http_req"]["interval_AutomaticGetting"])
    interaction = json.load(json_op)
    chunk_path = ""
    #分割データパス情報が残っているか(yes)
    if(len(interaction['path_list']) != 0):
        # interaction.jsonから分割データ情報を取り込む
        chunk_path = interaction['path_list'][0]
        # 1分割データのみリクエスト
        print(">",end='',flush=True)
        response = requests.get("https://procon33-practice.kosen.work/problem/chunks/" + chunk_path[13:] + "?token=" + token)
        # リクエストループ
        if(response.status_code != 200):
            # dos判定の回避
            time.sleep(interval)
            if(response.status_code == 400):print(".",end="",flush=True)
            else:
                print("_",end='',flush=True)
                ClearChunkPathList()
            RequestAdditional()
        else:
            print("!")
            os.makedirs("./wave_files", exist_ok=True)
            del interaction['path_list'][0]
            output_json = open('interaction.json', 'w')
            json.dump(interaction, output_json, indent=4)
            with open(chunk_path,"wb") as w_file:
                w_file.write(response.content)
            w_file.close()
            print("status: " + str(response.status_code))
            print("> Have added 1 chunk.")
    #分割データパス情報がない場合
    else:
        print(">",end='',flush=True)
        response = requests.get(domain + "/problem?token="+token)
        # リクエストループ
        if(response.status_code != 200):
            # dos判定の回避
            time.sleep(interval)
            if(response.status_code == 400):print(".",end="",flush=True)
            else:
                print("_",end='',flush=True)
                ClearChunkPathList()
            RequestAdditional()
        else:
            print("!")
            #全ての分割データをjsonへ格納する
            interaction['path_list'] = AutomaticRequestChunksPath(int(response.json()['chunks']))

            # interaction.jsonから分割データ情報を取り込む
            chunk_path = interaction['path_list'][0]
            os.makedirs("./wave_files", exist_ok=True)
            # 1分割データのみリクエスト
            response = requests.get("https://procon33-practice.kosen.work/problem/chunks/" + chunk_path[13:] + "?token=" + token)
            # 配列から要素を削除
            del interaction['path_list'][0]

            output_json = open('interaction.json', 'w')
            json.dump(interaction, output_json, indent=4)
            with open(chunk_path,"wb") as w_file:
                w_file.write(response.content)
            w_file.close()
            print("status: " + str(response.status_code))
            print("> Have added 1 chunk.")
    return chunk_path

def ClearChunkPathList():
    json_op = open('interaction.json', 'r')
    interaction = json.load(json_op)
    interaction['path_list'].clear()
    output_json = open('interaction.json', 'w')
    json.dump(interaction, output_json, indent=4)

# ------------------(http_req.py以外のプログラムから使用可能)-------------------->>>


def AutoGetFiles(n,chunk_list,token):
    os.makedirs("./wave_files", exist_ok=True)
    for i in range(n):
        response = requests.get("https://procon33-practice.kosen.work/problem/chunks/" + chunk_list[i] + "?token=" + token)
        file_name = "./wave_files/" + chunk_list[i]
        with open(file_name,'wb') as w_file:
            w_file.write(response.content)
        w_file.close()
        print("status: " + str(response.status_code))
    print()

def AutoGetFilesPath(n,chunk_list,token):
    os.makedirs("./wave_files", exist_ok=True)
    path_list = []
    for i in range(n):
        response = requests.get("https://procon33-practice.kosen.work/problem/chunks/" + chunk_list[i] + "?token=" + token)
        file_name = "./wave_files/" + chunk_list[i]
        with open(file_name,"wb") as w_file:
            w_file.write(response.content)
        w_file.close()
        path_list.append("./wave_files/"+chunk_list[i])
        print("status: " + str(response.status_code))
    return path_list

def status_code_check(response):
    if(response.status_code != 200):
        if(response.status_code == 400):
            print(response.text)
            exit( 1 )
        else:
            print("Perhaps, Server is Down")
            exit( 1 )

def AutomaticGetting(domain,token,isAutoGetFiles,init_chunk,interval,isEnableAutomaticTransition,interval_AutomaticAnswerPost):
    chunk_list = []
    request_url_chunk = domain + "/problem/chunks?n=" + str(init_chunk)
    # POSTリクエスト
    print(">",end='',flush=True)
    response = requests.post(request_url_chunk,headers={"procon-token": token})
    #ステータスコードチェッカー
    if(response.status_code != 200):
        # dos判定の回避
        time.sleep(interval)
        if(response.status_code == 400):print(".",end="",flush=True)
        else:print("_",end='',flush=True)
        AutomaticGetting(domain,token,isAutoGetFiles,init_chunk,interval,isEnableAutomaticTransition,interval_AutomaticAnswerPost)
    else:
        print("!")
        # アクセスが成功した場合
        print("chunks:")
        # ファイル名の格納
        for i in range(init_chunk):
            chunk_list.append(str(response.json()['chunks'][i]))
            print(response.json()['chunks'][i])
        print()

        #音声ファイルの自動取得
        if(isAutoGetFiles):
            AutoGetFiles(init_chunk,chunk_list,token)
            if(isEnableAutomaticTransition):
                AutomaticAnswerPost(domain,token,interval_AutomaticAnswerPost)

def AutomaticAnswerPost(domain,token,interval):
    json_op = open('interaction.json', 'r')
    interaction = json.load(json_op)
    if(interaction["isEnableAnswerPostMode"]):
        print("!")
        # --- problemの取得用request --- 
        response = requests.get(domain + "/problem?token="+token)
        #ステータスコードチェッカー
        status_code_check(response)
        ans_array = interaction["answer"]
        ans_array_len = len(ans_array)
        if(ans_array_len < 2):
            print("arg error: argments is needed more!")
            exit( 1 )
        #リクエストボディ作成
        request_body = {"problem_id": str(response.json()['id']),"answers": ans_array}
        print(request_body)

        # --- post用request --- 
        response = requests.post(domain + "/problem",json=request_body,headers={"Content-Type": "application/json", "procon-token": token})
        #ステータスコードチェッカー
        status_code_check(response)
        print("problem_id   :" + str(response.json()['problem_id']))
        print("answers      :" + str(response.json()['answers']))
        print("accepted_at  :" + str(response.json()['accepted_at']))
        print("post request is successful!!!"+"\n")

        #jsonのフラグをfalseにする！！！！
        interaction["isEnableAnswerPostMode"] = False

        output_json = open('interaction.json', 'w')
        json.dump(interaction, output_json, indent=4)

    else:
        print("-",end="",flush=True)
        time.sleep(interval)
        AutomaticAnswerPost(domain,token,interval)

def FFT(x):
    N = x.shape[0]
    if N==1:
        return x[0]
    
    x_even = x[0:N:2]
    x_odd = x[1:N:2]
    
    X_even = FFT(x_even)
    X_odd = FFT(x_odd)
    
    W = []
    for t in range(N//2):
        W.append(np.exp(-1j * ((2*np.pi*t) / N)))
    W = np.array(W)
    
    X = np.zeros(N, dtype="complex")
    X[0:N//2] = X_even + W*X_odd
    X[N//2:N] = X_even - W*X_odd
    
    return X

def STFT(x, win_length, hop=0.5):
    hop_length = int(win_length * hop)
    
    pad_first = x[:hop_length]
    pad_last = x[-hop_length:][::-1]
    x_pad = np.concatenate([pad_first, x, pad_last])

    N = x_pad.shape[0]

    M = int(win_length//2) + 1

    T = int((N - hop_length)/hop_length)

    han = hamming(win_length)
    
    spec = np.zeros((M,T), dtype="complex")
    
    for t in range(T):
        windowed_x = x_pad[t*hop_length:t*hop_length+win_length] * han
        
        spec[:,t] = FFT(windowed_x)[:int(win_length//2)+1]
    return spec

def AnalyzeSpec(wave_file):
    y, sr = librosa.load("./" + wave_file + ".wav")

    spec = STFT(y, 1024, 0.5)
    spec_db = librosa.amplitude_to_db(np.abs(spec))
    librosa.display.specshow(spec_db, y_axis="log")
    plt.show()

# if(__name__ == "__main__"):
#     print("This source code is for the library of functions only!")

