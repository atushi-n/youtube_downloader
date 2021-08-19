import youtube_dl
import tkinter
import threading


def dl():
    ydl_opts = {"outtmpl": txt_2.get() + ".mp4"}  # 辞書形式のオプション
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:  # with文で手間なく開く
        ydl.download([txt_1.get()])  # ダウンロード

def btn_click():
    threading.Thread(target=dl()).start()




root = tkinter.Tk()#フレーム
root.title("youtube_downloader")
root.geometry("300x300")

label1 = tkinter.Label(root, text='URL')
label1.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)

label2 = tkinter.Label(root, text='ファイル名')
label2.place(relx=0.1, rely=0.3, relwidth=0.1, relheight=0.1)

txt_1 = tkinter.Entry(root)
txt_1.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)
txt_2 = tkinter.Entry(root)
txt_2.place(relx=0.3, rely=0.3, relwidth=0.1, relheight=0.1)

btn = tkinter.Button(root, text='ダウンロード', command=btn_click)
btn.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
root.mainloop()
