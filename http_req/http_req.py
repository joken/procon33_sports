from fileinput import close
from multiprocessing.spawn import import_main_path
from operator import truediv
from signal import valid_signals
import requests
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
import sys
import http_req_lib as funcs
import configparser

# ConfigParserのインスタンス（特定の機能を持った変数）を取得
config = configparser.ConfigParser()
# config.iniを読み出し
config.read("config.ini")

#define
token = str(config["http_req"]["token"])
domain = str(config["http_req"]["domain"])
argc = len(sys.argv)
cmd = sys.argv[0]
isAutoGetFiles = config["http_req"].getboolean("isAutoGetFiles")
isEnableAutomaticAnswerPost = config["http_req"].getboolean("isEnableAutomaticAnswerPost")
isEnableAutomaticTransition = config["http_req"].getboolean("isEnableAutomaticTransition")
interval_AutomaticGetting = float(config["http_req"]["interval_AutomaticGetting"])
interval_AutomaticAnswerPost = float(config["http_req"]["interval_AutomaticAnswerPost"])
init_chunk = int(config["http_req"]["init_chunk"])

if(argc < 2):
    print("Usage: ", cmd, "argments is needed more!")
    exit(1)
else:
    # 試合情報/matchの取得
    if(sys.argv[1] == "m"):
        response = requests.get(domain + "/match?token="+token)
        #ステータスコードチェッカー
        funcs.status_code_check(response)
        print("problems     :" + str(response.json()['problems']))
        print("bonus_factor :" + str(response.json()['bonus_factor']))
        print("penalty      :" + str(response.json()['penalty']) + "\n")

    #問題情報/problemの取得
    elif(sys.argv[1] == "p"):
        response = requests.get(domain + "/problem?token="+token)
        #ステータスコードチェッカー
        funcs.status_code_check(response)
        print("id           :" + str(response.json()['id']))
        print("chunks       :" + str(response.json()['chunks']))
        print("starts_at    :" + str(response.json()['starts_at']))
        print("time_limit   :" + str(response.json()['time_limit']))
        print("data         :" + str(response.json()['data']) + "\n")

    #取得する分割データの指定(チャンクデータの取得)
    elif(sys.argv[1] == "c"):
        #分割データ名を保持する
        chunk_list = []

        #チャンク指定の確認
        if(argc < 3):
            print("arg error: Please specify the number of divisions!\n")
            exit( 1 )
        #チャンク数かモード指定か
        if(sys.argv[2] == 'a'):
            #自動取得モード
            funcs.AutomaticGetting(domain,token,isAutoGetFiles,init_chunk,interval_AutomaticGetting,isEnableAutomaticTransition,interval_AutomaticAnswerPost)

        else:
            request_url_chunk = domain + "/problem/chunks?n=" + sys.argv[2]
            # POSTリクエスト
            response = requests.post(request_url_chunk,headers={"procon-token": token})
            #ステータスコードチェッカー
            funcs.status_code_check(response)
            print("chunks:")
            # ファイル名の格納
            for i in range(int(sys.argv[2])):
                chunk_list.append(str(response.json()['chunks'][i]))
                print(response.json()['chunks'][i])
            print()

            #音声ファイルの自動取得
            if(isAutoGetFiles):
                funcs.AutoGetFiles(int(sys.argv[2]),chunk_list,token)
                if(isEnableAutomaticTransition):
                    funcs.AutomaticAnswerPost(domain,token,interval_AutomaticAnswerPost)

    #回答POST
    elif(sys.argv[1] == "a"):
        #自動回答POSTを行うか
        if(isEnableAutomaticAnswerPost):
            funcs.AutomaticAnswerPost(domain,token,interval_AutomaticAnswerPost)
        else:
            print(">> Please enter in the following format.")
            print("[problem_id] [answer_picture_id] [answer_picture_id] ... (3 <= num <= 20) ")
            answer = input("answer >>")
            ans_array = list(map(str, answer.strip().split()))
            ans_array_len = len(ans_array)
            if(ans_array_len < 2):
                print("arg error: argments is needed more!")
                exit( 1 )
            else:
                #回答の答え（answer）部分のみの配列
                ans_picture = ans_array[1:ans_array_len]
            #リクエストボディ作成
            request_body = {"problem_id": ans_array[0],"answers": ans_picture}
            print(request_body)
            response = requests.post(domain + "/problem",json=request_body,headers={"Content-Type": "application/json", "procon-token": token})
            #ステータスコードチェッカー
            funcs.status_code_check(response)
            print("problem_id   :" + str(response.json()['problem_id']))
            print("answers      :" + str(response.json()['answers']))
            print("accepted_at  :" + str(response.json()['accepted_at']))
            print("post request is successful!!!"+"\n")

    #STFTによるスペクトログラム生成
    elif(sys.argv[1] == "s"):
        if(argc < 3):
            print("arg error: argments is needed more!")
            exit( 1 )
        print("now analyzing...")
        funcs.AnalyzeSpec(sys.argv[2])
    else:
        print("arg error: The first arg is invalid!")
        exit( 1 )