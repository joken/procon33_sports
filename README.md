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
