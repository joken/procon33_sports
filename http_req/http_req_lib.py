import requests
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from numpy import hamming
import numpy as np
import time


def AutoGetFiles(n,chunk_list,token):
    for i in range(n):
        file_name = "chunk" + str(i) + ".wav"
        response = requests.get("https://procon33-practice.kosen.work/problem/chunks/" + chunk_list[i] + "?token=" + token)
        with open(file_name,"wb") as w_file:
            w_file.write(response.content)
        w_file.close()
        """        with open("file_test","w") as t:
            t.write(str(vars(response)))"""
        print("status: " + str(response.status_code))

def status_code_check(response):
    if(response.status_code != 200):
        if(response.status_code == 400):
            print(response.text)
            exit( 1 )
        else:
            print("Perhaps, Server is Down")
            exit( 1 )

def AutomaticGetting(domain,token,isAutoGetFiles,init_chunk,interval):
    chunk_list = []
    request_url_chunk = domain + "/problem/chunks?n=" + str(init_chunk)
    # POSTリクエスト
    print("send request")
    response = requests.post(request_url_chunk,headers={"procon-token": token})
    #ステータスコードチェッカー
    if(response.status_code != 200):
        # dos判定の回避
        time.sleep(interval)
        print("status code is ["+str(response.status_code)+"] Now Retrying...")
        AutomaticGetting(domain,token,isAutoGetFiles,init_chunk,interval)
    else:
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
