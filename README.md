# news_summarizer

- URLを渡すとbodyのtextを取ってきて日本語で要約してくれるプログラムです。

## 実行方法
- requirements.txtの依存モジュールをインストール
  - VScodeでPython拡張機能を入れた状態でrequirements.txtを開くといい感じにやってくれます
- .envを作ってご自身のOpenAI APIキーを入力
- コマンドラインで`python smr.py`すると動きます

## 免責
- トークン制限に引っかかりやすいので注意。今後対応します。→対応しました
- requestsモジュールでエラーの起きるURLを複数確認しています。原因調査中
