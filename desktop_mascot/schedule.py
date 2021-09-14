import tkinter as tk
from tkinter import ttk
import datetime
import calendar

class data_Picker:
    def __init__(self):
        #今日の日付を取得
        Today = datetime.datetime.now()

        self.year_list = [str(date).zfill(2) for date in range(Today.year, Today.year+50)]
        self.month_list = [str(date).zfill(2) for date in range(1, 13)]
        self.date_list = [str(date).zfill(2) for date in range(1, 32)]
        self.hours_list = [str(date).zfill(2) for date in range(24)]
        self.minutes_list = [str(date).zfill(2) for date in range(60)]

        self.cb_year = None
        self.cb_month = None
        self.cb_date = None

        self.root = tk.Tk()
        self.root.geometry("500x140")
        self.root.title('スケジュール登録')

        #フォントサイズ
        self.root.option_add('*font',['MS Pゴシック', 16])

        self.cb_year = ttk.Combobox(self.root, values=self.year_list, width=5, state='readonly')
        self.cb_year.set(Today.year)
        self.cb_year.bind('<<ComboboxSelected>>', self.change_date)
        self.cb_year.pack(side='left',anchor=tk.N,padx=3,pady=10)

        self.label_slash = ttk.Label(self.root, text='/')
        self.label_slash.pack(side='left',anchor=tk.N,padx=3,pady=10)

        self.cb_month = ttk.Combobox(self.root, values=self.month_list, width=5, state='readonly')
        self.cb_month.set(str(Today.month).zfill(2))
        self.cb_month.bind('<<ComboboxSelected>>', self.change_date)
        self.cb_month.pack(side='left',anchor=tk.N,padx=3,pady=10)

        self.label_slash = ttk.Label(self.root, text='/')
        self.label_slash.pack(side='left',anchor=tk.N,padx=3,pady=10)

        self.cb_date = ttk.Combobox(self.root, values=self.date_list, width=5, state='readonly')
        self.cb_date.set(str(Today.day).zfill(2))
        self.cb_date.pack(side='left',anchor=tk.N,padx=3,pady=10)

        self.label_space = ttk.Label(self.root, text=' ')
        self.label_space.pack(side='left',anchor=tk.N,padx=3,pady=10)

        self.cb_hours = ttk.Combobox(self.root, values=self.hours_list, width=5, state='readonly')
        self.cb_hours.set(str(Today.hour).zfill(2))
        self.cb_hours.pack(side='left',anchor=tk.N,padx=3,pady=10)

        self.label_colon = ttk.Label(self.root, text=':')
        self.label_colon.pack(side='left',anchor=tk.N,padx=3,pady=10)

        self.cb_minutes = ttk.Combobox(self.root, values=self.minutes_list, width=5, state='readonly')
        self.cb_minutes.set(str(Today.minute).zfill(2))
        self.cb_minutes.pack(side='left',anchor=tk.N,padx=3,pady=10)

        #テキストボックス
        self.text_box = tk.Text(self.root,height=2,width=35)
        self.text_box.place(x=10,y=60)

        #登録配置
        registerButton = tk.Button(self.root,text='登録')
        registerButton.place(x=420,y=65)
        registerButton['command'] = self.register_Btn_Action


        self.root.mainloop()

    #-----------------------------------------------------#
    #スケジュールの登録ボタンの動作
    #黒柳のプログラムと組み合わせるときにでも
    #-----------------------------------------------------#
    def register_Btn_Action(self):
        print(self.cb_year.get()) #年
        print(self.cb_month.get()) #月
        print(self.cb_date.get()) #日
        print(self.cb_hours.get()) #時
        print(self.cb_minutes.get()) #分
        print(self.text_box.get(1.0,"end")) #内容

        #テキストメッセージを空白に
        self.text_box.delete("1.0","end")

    def change_date(self,event):
        if self.cb_year == None or self.cb_month == None or self.cb_date == None:
            pass
        else:
            last_day = calendar.monthrange(int(self.cb_year.get()), int(self.cb_month.get()))[1]
            if int(self.cb_date.get()) > last_day:
                self.cb_date.set(str(last_day).zfill(2))
            self.cb_date.config(values=[str(date).zfill(2) for date in range(1, last_day+1)])

        # datetime形式で出力
        # date = cb_year.get()+'-'+cb_month.get()+'-'+cb_date.get()+' '+cb_hours.get()+':'+cb_minutes.get()+':'+cb_seconds.get()
        # print("Date = ", date)

def main():
    data_Picker()

if __name__ == '__main__':
    data_Picker()