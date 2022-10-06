# インターフェイス周りに関するreadme
# <<- http_req.py ->>
## *usage*
```
$ python3 http_req.py [arg1] [arg2] [arg3] ...
```
・arg1は 'm' か 'p' か 'c' か 'a' を指定  
｜-'m'で試合情報(GET /match)を取得できる．  
｜-'p'で問題情報(GET /problem)を取得できる．  
｜-'c'では取得チャンク数を指定し，ファイル名の配列を取得する．  
｜　　 実行後，isAutoGetFilesフラグがTrueならそのまま音声ファイルが自動取得される．  
｜　　 取得したファイルはchunk[X].wavで保存される．  
｜    arg2にてチャンク数の代わりに'a'を指定することで，自動取得モードに入る．  
｜    自動取得モードでは，init_chunkで指定されたチャンク数で自動取得が行われる．  
｜    自動取得モードの出力ログにて，'>'はリクエスト中，'.'はBad Request，'_'はBad Gateway，'!'はSuccessを表す．  
｜-'a'ではPOSTによる回答を行う（POST /problem）．実行すると  
｜　　 入力待ち状態になるので，表示指定のフォーマットで，問題id，絵札のidを入力する．  
｜    isEnableAutomaticAnswerPostが有効なら自動回答POSTモードに遷移する．  
｜    出力ログにて，'-'は回答POST待ち状態，'!'は回答POST開始を表す．  
｜-'s'ではスペクトログラムの生成を行う．arg2で音声ファイル名（.wavは除く）を指定する．  

・arg2では，arg1が'c'ならチャンク数(2~5)または自動化フラグ文字'a'を指定，arg1が's'なら音声ファイル名を指定する．  

## *note*  
各設定用変数はconfig.iniに格納している  
他プログラムとの連携データはinteraction.jsonに格納している  
intervalは1以上が好ましいかも？  
 - 練習でよく見るstatus codeについて，  
    400は"Bad Request"で，感覚的にはサーバが閉じられる前後に出やすい．  
    502は"Bad Gateway"でサーバが閉じてる．  


# http_req_lib.py(ライブラリ)の外部プログラムから参照可能な関数

・`AutomaticRequestChunksPath(`*`int init_chunk`*`)`  
    引数　：分割数(int型)  
    戻り値：取得した音声ファイルのパス(./wave_files/*)(string型配列)  

・`RequestAdditional()`  
    引数　：void  
    戻り値：取得した音声ファイルのパス(./wave_files/*)(string型)    

・`ClearChunkPathList()`  
    引数　：void  
    戻り値：void  

## *usage*
・`AutomaticRequestChunksPath`  
指定した分割数(init_chunk)の分割データ情報を取得するための関数．  
config.iniで"isAutoGetFiles = True"としておくことで，自動で音声ファイルをDLし，  
./wave_files/ディレクトリに格納，さらにそれらのパスの配列(string)を返す．  

```
ex.)はじめに分割データが２つ欲しい場合：
    AutomaticRequestChunksPath(2)
    追加で分割データが1つ欲しい場合
    AutomaticRequestChunksPath(はじめに取得した分割データ数 + 1)    ...etc
```

・`RequestAdditional`  
一つずつ音声ファイルのDLが可能な関数．  
関数を実行するたびに./wave_files/内に新しい分割データが追加される．
データの管理に独立したjson内配列(path_list)を使うため，AutomaticRequestChunksPath関数と併用すると，  
分割データが重複する場合がある．  
また，リクエスト中にサーバが閉じたと判断した場合，自動でClearChunkPathList関数が実行される．  
（判断条件は，ステータスコードが200か400以外の場合）

・`ClearChunkPathList`  
RequestAdditional関数に残っている過去に取得した分割データ情報をクリアするための関数．  
問題データが変わる前に実行される必要がある（クリアを忘れると永遠に">.>."が続く可能性がある）．  

# interaction.json
・`answer`  
答えとなる絵札idの配列．answerにデータを格納した後，isEnableAnswerPostModeをtrueにすることで  
回答POSTモードが起動し，自動で回答POSTが行われる．回答POSTが完了するとisEnableAnswerPostMode = falseとなり，  
再び回答POSTが可能になる．  

・`isEnableAnswerPostMode`  
回答POSTモードか否かのbool型を格納する．  
falseで回答POSTモードでない状態，回答POST可能状態．  
trueで回答POSTモード状態．  

・`chunk_list`  
AutomaticRequestChunksPath関数で取得した分割データ名を格納する配列．  

・`path_list`  
分割データのパスを格納する配列で，RequestAdditional関数専用．  
