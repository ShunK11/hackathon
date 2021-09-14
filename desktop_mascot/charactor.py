import tkinter as tk 
import cv2
import PIL.Image, PIL.ImageTk
import time
import schedule

class UI:
    def __init__(self):
        #UIの初期化
        self.baseGround = tk.Tk()
        #最大サイズで表示
        self.baseGround.state('zoomed')
        #フォントサイズ
        self.baseGround.option_add('*font',['MS Pゴシック', 16])

        #UIの縦横の取得
        self.baseGround.update_idletasks()
        self.baseGround_Width=self.baseGround.winfo_width()
        #タスクバーに被るため調整有
        self.baseGround_Height=self.baseGround.winfo_height()-10

        #ウィンドウを透明化
        self.baseGround.configure(bg='blue')
        self.baseGround.wm_attributes("-transparentcolor", "blue")

        self.baseGround.overrideredirect(1)


        #-----------------------------------------------------#
        #動画をTkinterで動かす用
        #-----------------------------------------------------#
        """
        # open video source (by default this will try to open the computer webcam)
        self.video_source = 'test.mp4'
        self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(self.baseGround, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
 
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
        """
        
        #-----------------------------------------------------#
        #画像をTkinterで
        #-----------------------------------------------------#        
        #キャラクター描画
        #画像読み込み
        charactor_Img = tk.PhotoImage(file="irasutoya.png")
        self.charactor_Img_Width = charactor_Img.width()
        self.charactor_Img_Height =charactor_Img.height()

        #画像書き込み
        canvas = tk.Canvas(self.baseGround,bg="blue",width=400, height=600,highlightthickness=0)
        canvas.place(x=self.baseGround_Width-self.charactor_Img_Width, y=self.baseGround_Height-self.charactor_Img_Height)
        canvas.create_image(0, 0, image=charactor_Img, anchor=tk.NW)

        #-----------------------------------------------------#
        #吹き出し描画
        #-----------------------------------------------------#
        fukidashi_Img = tk.PhotoImage(file="fukidashi.png")        
        self.fukidashi_Img_Width = fukidashi_Img.width()
        self.fukidashi_Img_Height =fukidashi_Img.height()        

        #画像書き込み
        canvas = tk.Canvas(self.baseGround,bg="blue",width=self.fukidashi_Img_Width, height=self.fukidashi_Img_Height,highlightthickness=0)
        canvas.place(x=self.baseGround_Width-self.charactor_Img_Width-self.fukidashi_Img_Width+50, y=self.baseGround_Height-self.charactor_Img_Height-self.fukidashi_Img_Height+50)
        canvas.create_image(0, 0, image=fukidashi_Img, anchor=tk.NW)        

        #-----------------------------------------------------#
        #テキストボックス配置
        #-----------------------------------------------------#
        # 入力場所
        self.entry = tk.Entry(width=20,bd=4)
        self.entry.place(x=self.baseGround_Width-self.charactor_Img_Width-self.fukidashi_Img_Width+75,y=self.baseGround_Height-self.charactor_Img_Height-self.fukidashi_Img_Height+180)

        # 送信ボタン
        sendbutton = tk.Button(text='送信')
        sendbutton.place(x=self.baseGround_Width-self.charactor_Img_Width-self.fukidashi_Img_Width+340,y=self.baseGround_Height-self.charactor_Img_Height-self.fukidashi_Img_Height+175)
        sendbutton['command'] = self.send_Btn_Action

        # スケジュール登録ボタン
        schedulebutton = tk.Button(text='登録')
        schedulebutton.place(x=self.baseGround_Width-self.charactor_Img_Width-self.fukidashi_Img_Width+420,y=self.baseGround_Height-self.charactor_Img_Height-self.fukidashi_Img_Height+175)
        schedulebutton['command'] = self.submit_Btn_Action

        #-----------------------------------------------------#
        #テキストを表示
        #-----------------------------------------------------#
        self.text = tk.StringVar()
        self.text.set('')
        self.message = tk.Label(textvariable=self.text,bg="white")
        self.message.place(x=self.baseGround_Width-self.charactor_Img_Width-self.fukidashi_Img_Width+70,y=self.baseGround_Height-self.charactor_Img_Height-self.fukidashi_Img_Height+70) 
        
        self.baseGround.mainloop()
    
    #吹き出し内のテキストメッセージを更新する
    def change_message(self,input_message):        
        self.text.set(input_message)

    #送信ボタン
    def send_Btn_Action(self):
        val = self.entry.get()
        self.change_message(val)
        
        #テキストメッセージを空白に
        self.entry.delete(0,tk.END)

    #スケジュール登録ボタン
    def submit_Btn_Action(self):
        schedule.main()



    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
 
    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
        else:
            self.video_source = 'test.mp4'
            self.vid = MyVideoCapture(self.video_source)

 
        self.baseGround.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (None, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        


if __name__ == '__main__' :
    #UIクラスのインスタンス化
    base_UI=UI()