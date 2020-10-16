import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
import time
from tkinter.filedialog import *
root= tk.Tk()
per=0
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(root, length=390, style='black.Horizontal.TProgressbar', mode = 'determinate')
canvas1.create_window(202, 250, window=bar)

  

label1 = tk.Label(root, text='YouTube Downloader')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Paste The Link Of YouTube Video')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def processdownload(stream=None,chunk=None ,bytes_remaining=None):
    global per 
    per = 100*((filesi-bytes_remaining)/filesi)
    button1['text']="{}".format(per)
    button1['state']="disable"
def oncomplete(stream=None ,file_path=None):
    messagebox.showinfo("message","file has been downloaded")
    entry1.delete("0","end")
    button1['text']="Download"
    button1['state']= "active"
    
def getSquareRoot ():
    global filesi

    path_to_save = askdirectory()
    if path_to_save is None :
        return 
    youtube_video_url = entry1.get()
    
    try:
         yt_obj = YouTube(youtube_video_url)
         
         filters = yt_obj.streams.first()
         filesi  = filters.filesize
        
         yt_obj.register_on_progress_callback(processdownload)
         yt_obj.register_on_complete_callback(oncomplete)
         # download the highest quality video
         filters.download(output_path=path_to_save)
         
    except Exception as e:
        print(e)
    

button1 = tk.Button(text='Download', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))

canvas1.create_window(200, 180, window=button1)

root.mainloop()