from tkinter import *
from tkinter import filedialog as fd
from rgb_to_binary import convert_to_binary as ctb
from denoise import denoise
from edge_detection import edge_detection
from filter import closing, opening, erosion, dilation, hitmiss
from tkinter import messagebox
pathname= ""
# function brose
def browse():
    filetypes = (('Jpg files', '*.jpg'), ('Png files', '*.png'), ('Jpeg file', '*.jpeg'))
    filename = fd.askopenfile(title='Choose a file to open', initialdir='/Users/nguyenthuan/PycharmProjects/xla/image', filetypes=filetypes)
    return   filename.name

window = Tk()
window.title("Xu ly anh")
window.geometry("500x500")

def convert_to_binary():
    a = browse()
    print("helo")
    print(type(a))
    ctb(a)
def o():
    a = browse()
    opening(a)
def c():
    a = browse()
    closing(a)
def hm():
    a = browse()
    hitmiss(a)
def e():
    a = browse()
    erosion(a)
def dl():
    a = browse()
    dilation(a)
def dn():
    a = browse()
    denoise(a)
def ed():
    a = browse()
    edge_detection(a)


# button
btt1 = Button(window, text="Convert to Binary Image", width=20, height=5, command=convert_to_binary)
btt2 = Button(window, text="Opening", width=20, height=5, command=o)
btt3 = Button(window, text="Closing", width=20, height=5, command=c)
btt4 = Button(window, text="Erosion", width=20, height=5, command=e)
btt5 = Button(window, text="Dilation", width=20, height=5, command=dl)
btt6 = Button(window, text="Denoising", width=20, height=5, command=dn)
btt7 = Button(window, text="Edge Detection", width=20, height=5, command=ed)


btt1.place(x=10, y=10)
btt2.place(x=10, y=60)
btt3.place(x=10, y=110)
btt4.place(x=10, y=160)
btt5.place(x=10, y=210)
btt6.place(x=10, y=260)
btt7.place(x=10, y=310)
window.mainloop()