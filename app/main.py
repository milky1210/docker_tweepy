from datetime import datetime, timedelta, timezone
from pathlib import Path

import tweepy_utils as tweepy_utils

# 日本標準時 (JST) タイムゾーンを定義
JST = timezone(timedelta(hours=9))

# ディレクトリのパス
tweet_data_dir = Path("tweet_data")

# 現在の日付をJSTで取得
current_date = datetime.now(JST)

# 午後かどうかを判定
is_pm = current_date.hour >= 12

# パスを生成
if is_pm:
    img_path = tweet_data_dir / current_date.strftime("%Y-%m-%d") / "pm.jpeg"
    txt_path = tweet_data_dir / current_date.strftime("%Y-%m-%d") / "pm.txt"
else:
    img_path = tweet_data_dir / current_date.strftime("%Y-%m-%d") / "am.jpeg"
    txt_path = tweet_data_dir / current_date.strftime("%Y-%m-%d") / "am.txt"



# ファイルを読み込み、内容を文字列として格納
if not txt_path.exists():
    print(f"Error(404): {txt_path} is not found.")
if not txt_path.exists():
    print(f"Error(404): {img_path} is not found.")
with txt_path.open("r", encoding="utf-8") as file:
    tweet_txt = file.read()

tweepy_utils.tweet_img(img_path, tweet_txt)
