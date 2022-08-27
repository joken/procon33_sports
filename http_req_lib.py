import requests

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