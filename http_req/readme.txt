<usage>
$ python3 http_req.py [arg1] [arg2] [arg3] ...

・arg1は 'm' か 'p' か 'c' か 'a' を指定
｜-'m'で試合情報(GET /match)を取得できる．
｜-'p'で問題情報(GET /problem)を取得できる．
｜-'c'では分割数を指定し，ファイル名を取得するモードを指定する．
｜　　 実行後，isAutoGetFilesフラグがTrueならそのまま音声ファイルが自動取得される．
｜　　 取得したファイルはchunk[X].wavで保存される．
｜-'a'ではPOSTによる回答を行う（POST /problem）．実行すると
　　　 入力待ち状態になるので，表示指定のフォーマットで，問題id，絵札のidを入力する．

・arg2では，チャンク数を指定する．