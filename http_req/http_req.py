from fileinput import close
from multiprocessing.spawn import import_main_path
from operator import truediv
from signal import valid_signals
import requests
import sys
import http_req_lib as funcs

#define
token = "92c099e3eb98b70cf60e4bc63b5f54fac4c3b51da4f57cbf1b7668c0f8d625fa"
domain = "https://procon33-practice.kosen.work"
argc = len(sys.argv)
cmd = sys.argv[0]
isAutoGetFiles = True


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

    #回答POST
    elif(sys.argv[1] == "a"):
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
        print("accepted_at  :" + str(response.json()['accepted_at'])+"\n")
    else:
        print("arg error: The first arg is invalid!")
        exit( 1 )

