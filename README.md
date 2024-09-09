# docker_tweepy

## 環境
- docker
- XのAPI

## ビルド
プロジェクトフォルダ内で、
``` bash
docker compose up docker_tweepy -d
docker compose exec docker_tweepy python main.py
```
を実行することで、
- tweet_data/YYYY-MM-DD/(am/pm).jpeg
- tweet_data/YYYY-MM-DD/(am/pm).png
に保存された画像とテキストのペアを
config.pyにて、記載されたXのAPIにて、ツイートを実行することができる。
