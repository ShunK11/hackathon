import requests
import sqlite3
import datetime
import json

dbname = ('example.db')#データベース名.db拡張子で設定
conn = sqlite3.connect(dbname, isolation_level=None)#データベースを作成、自動コミット機能ON

headers = {'Content-Type': 'application/json;charset=UTF-8'}
bot_id = '2464_sample'
data = {
    'bot_id': bot_id,
    'app_kind': 'Test',
    'notification': False
}
url = u'https://api-sunaba.xaiml.docomo-dialog.com/registration'
response = requests.post(url, headers=headers, data=json.dumps(data))

app_id = response.json()['app_id']  # アプリIDの取得

def talk_api(message):
    text = message
    url = u'https://api-sunaba.xaiml.docomo-dialog.com/dialogue'
    data = {
        'language': 'ja-JP',
        "initTopicId": "kataraiTrial",
        "initTalkingFlag": False,
        'bot_id': bot_id,
        'app_id': app_id,
        'voiceText': text
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        return response.json()['systemText']['expression']
    except:
        print(response.json())
        return "ごめんなさい。もう一度教えて下さい。"

def main():
    d_today = datetime.date.today()
    cursor = conn.cursor()
    sql = """SELECT * FROM schedule"""
    cursor.execute(sql)
    sche = cursor.fetchall()
    for sc in sche:
        data = sc[0].split('-')
        date = datetime.date(int(data[0]), int(data[1]), int(data[2]))
        if date == d_today:
            print("今日の予定：" + sc[2])
        else:
            print("今日の予定はありません")
    while(True):
        print("自分：", end="")
        message = input()
        if message == "スケジュール作成":
            print('西暦は？')
            year = input()
            year = year.replace('年','-')
            print("日にちは？")
            date = input()
            date = year + date.replace('月','-').replace('日','')
            print("内容は？")
            event = input()
            cursor = conn.cursor() #カーソルオブジェクトを作成
            sql = """INSERT INTO schedule VALUES(?, ?)"""  # ?は後で値を受け取るよという意味
            data = ((date, event))  # 挿入するレコードを指定
            cursor.execute(sql, data)  # executeコマンドでSQL文を実行
            conn.commit()  # コミットする
        elif message == 'スケジュール確認':
            cursor = conn.cursor()
            sql = """SELECT * FROM schedule"""
            cursor.execute(sql)
            for row in cursor.fetchall():
                print('----------------')
                for r in row:
                    print(r)
            print('----------------')
        else:
            print("BOT：" + talk_api(message))
if __name__ == "__main__":
    main()
