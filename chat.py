import requests
import sqlite3
import datetime
import json

# dbname = ('example.db')#データベース名.db拡張子で設定
# conn = sqlite3.connect(dbname, isolation_level=None)#データベースを作成、自動コミット機能ON
conn = sqlite3.connect('example.db', 
detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

# "TIMESTAMP"コンバータ関数 をそのまま ”DATETIME” にも使う
sqlite3.dbapi2.converters['DATETIME'] = sqlite3.dbapi2.converters['TIMESTAMP']
# cur = conn.cursor()
# cur.execute("create table schedule(event text, date datetime)")

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
    talk_api('テスト')
    d_today = datetime.date.today()
    dd_today = datetime.datetime.today()
    cur = conn.cursor()
    sql = """SELECT * FROM schedule"""
    cur.execute(sql)
    sche = cur.fetchall()
    for sc in sche:
        if str(d_today) in str(sc[1]) and dd_today < sc[1]:
            print('----------------')
            print("日時：" + str(sc[1]))
            print("今日の予定：" + sc[0])
            print('----------------')
    while(True):
        print("自分：", end="")
        message = input()
        if message == "スケジュール作成":
            print("日付は？(2014-01-02 23:45:00)")
            date = input()
            print("内容は？")
            event = input()
            cur = conn.cursor() #カーソルオブジェクトを作成
            sql = """INSERT INTO schedule VALUES(?, ?)"""  # ?は後で値を受け取るよという意味
            data = ((event, date))  # 挿入するレコードを指定
            cur.execute(sql, data)  # executeコマンドでSQL文を実行
            conn.commit()  # コミットする
        elif message == 'スケジュール確認':
            cur = conn.cursor()
            sql = """SELECT * FROM schedule"""
            cur.execute(sql)
            for row in cur.fetchall():
                print('----------------')
                for r in row:
                    print(r)
            print('----------------')
        else:
            print("BOT：" + talk_api(message))
if __name__ == "__main__":
    main()
