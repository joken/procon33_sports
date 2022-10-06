import sys
import http_req_lib as funcs

argc = len(sys.argv)
cmd = sys.argv[0]

# $ python3 test.py r と入力した場合
if(sys.argv[1] == 'r'):
<<<<<<< HEAD
    funcs.ClearChunkPathList()
=======
>>>>>>> origin/main
    a = funcs.AutomaticRequestChunksPath(sys.argv[2])
# $ python3 test.py a と入力した場合
elif(sys.argv[1] == 'a'):
    a = funcs.RequestAdditional()
# $ python3 test.py c と入力した場合
elif(sys.argv[1] == 'c'):
    a = funcs.ClearChunkPathList()
else:
    exit(1)

print("戻り値："+str(a))