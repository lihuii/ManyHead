# GUI for ManyHead
# coding: utf-8
import os
import tkFileDialog

from random import randint
from Tkinter import Tk, Checkbutton, Radiobutton, Button, Label, PhotoImage, TOP
import Tkinter
import play

os.chdir(os.getcwd())

def splash():
    root = Tkinter.Tk()
    # show no frame
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print width, height
    root.geometry('%dx%d+%d+%d' % (width*0.4, height*0.8, width*0.3, height*0.1))
    # 保存成gif格式
    # 但是没法显示动图，待解决。
    image_file = os.getcwd() + "/splash.gif"
    # assert os.path.exists(image_file)
    # use Tkinter's PhotoImage for .gif files
    image = Tkinter.PhotoImage(file=image_file)
    canvas = Tkinter.Canvas(root, height=height*0.8, width=width*0.8, bg="white")
    canvas.create_image(width*0.8/4, height*0.8/2, image=image)
    canvas.pack()
    # 设置splash显示的时间，单位是毫秒（milliseconds）
    root.after(5000, root.destroy)
    root.mainloop()
    
        
def change_head():
    head_filename = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')

def add_head():
    head_img = PhotoImage(file='images/%s.gif' % randint(1, 7))
    Button(root, image=head_img).pack()
    #head_bt.pack(side=TOP)

def play_head():
    game(head_filename)
    
def app():
    root = Tk()
    root.geometry("500x500+100+200")

    lb1 = Label(root, text="I have many head...Choose one:")
    heads = Radiobutton(root, )
    music_cb = Checkbutton(root, text="music")
    fullscreen_cb = Checkbutton(root, text="fullscreen")
    #全屏勾选，音乐勾选。
    bt1 = Button(root, text="START", command=play_head)
    bt2 = Button(root, text="MoreHead", command=add_head)

    music_cb.pack()
    fullscreen_cb.pack()
    lb1.pack()
    bt1.pack()
    bt2.pack()
    root.mainloop()

if __name__ == "__main__":
    splash()
    app()