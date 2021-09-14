import tkinter as tk
from tkinter import ttk
import datetime
import calendar

year_list = ['2020', '2021']
month_list = [str(date).zfill(2) for date in range(1, 13)]
date_list = [str(date).zfill(2) for date in range(1, 32)]
hours_list = [str(date).zfill(2) for date in range(24)]
minutes_list = [str(date).zfill(2) for date in range(60)]
seconds_list = [str(date).zfill(2) for date in range(60)]


def change_date():
    def inner(self):
        last_day = calendar.monthrange(int(cb_year.get()), int(cb_month.get()))[1]
        if int(cb_date.get()) > last_day:
            cb_date.set(str(last_day).zfill(2))
        cb_date.config(values=[str(date).zfill(2) for date in range(1, last_day+1)])

        # datetimeå`éÆÇ≈èoóÕ
        # date = cb_year.get()+'-'+cb_month.get()+'-'+cb_date.get()+' '+cb_hours.get()+':'+cb_minutes.get()+':'+cb_seconds.get()
        # print("Date = ", date)
    return inner


root = tk.Tk()
root.title('Date Picker')


cb_year = ttk.Combobox(root, values=year_list, width=5, state='readonly')
cb_year.set(year_list[0])
cb_year.bind('<<ComboboxSelected>>', change_date())
cb_year.pack(side='left')

label_slash = ttk.Label(root, text='/')
label_slash.pack(side='left')

cb_month = ttk.Combobox(root, values=month_list, width=5, state='readonly')
cb_month.set(month_list[0])
cb_month.bind('<<ComboboxSelected>>', change_date())
cb_month.pack(side='left')

label_slash = ttk.Label(root, text='/')
label_slash.pack(side='left')

cb_date = ttk.Combobox(root, values=date_list, width=5, state='readonly')
cb_date.set(date_list[0])
cb_date.pack(side='left')

label_space = ttk.Label(root, text=' ')
label_space.pack(side='left')

cb_hours = ttk.Combobox(root, values=hours_list, width=5, state='readonly')
cb_hours.set(hours_list[0])
cb_hours.pack(side='left')

label_colon = ttk.Label(root, text=':')
label_colon.pack(side='left')

cb_minutes = ttk.Combobox(root, values=minutes_list, width=5, state='readonly')
cb_minutes.set(minutes_list[0])
cb_minutes.pack(side='left')

label_colon = ttk.Label(root, text=':')
label_colon.pack(side='left')

cb_seconds = ttk.Combobox(root, values=seconds_list, width=5, state='readonly')
cb_seconds.set(seconds_list[0])
cb_seconds.pack(side='left')

root.mainloop()