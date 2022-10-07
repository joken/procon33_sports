# procon33_sports

## 開始準備
`python backup.py`
保存用のバックアップファイルをクリーンアップする.

`python analyzed_yomi.py`
読みデータの解析を行い`yomi.json`に格納する.
(`yomi.json`データ容量が大きいためgithubには元の読みデータのみをあげている)


## 実行
`python main.py <match> <stage> -j 0 -s`

- match: 試合の番号
- stage: 問題番号
- -j (int): プロセスの開始番号
- -s: 試合の初回時処理用のフラグ

## 本番環境で使用予定のファイル
- `main.py`: 実行用ファイル
- `backup.py`: 途中結果の保存ライブラリ
- `backup/*.json`: backup.pyの保存先
- `analyzed_yomi.py`: 読み音声のケプストラム分析用プログラム
- `yomi.json`: 読み音声のケプストラム分析後のデータ
- `config.ini`: 問題サーバへのアクセス用の設定ファイル
- `interaction.json`: 解答の出力用データ
- `http_req/http_req_lib.py`:問題サーバへの送受信用ライブラリ
- `analyze/analyzed.py`: ケプストラム分析用ライブラリ
- `comparison/conparison.py`: 読みデータごとの類似度計算ライブラリ
- `chooser/chooser.py`: 札選択用ライブラリ
- `origin_data/JKspeech/*.wav`: 読み音声の元データ
