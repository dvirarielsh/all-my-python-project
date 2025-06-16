import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
import io
class Node:
    next=None
    prev=None
    image=None
    def __init__(self,prev=None,image=None,next=None):
        self.next=next
        self.prev=prev
        self.image=image
    def getnext(self):
        return self.next
    def getprev(self):
        return self.prev
    def getimage(self):
        return self.image
    def setnext(self,next):
        self.next=next
    def setprev(self,prev):
        self.prev=prev
    def setimage(self,image):
        self.image=image
file_path =image= imageorg= label= gray1= blur1= uplodefile1= restart1 =next1 =prev1=pil_image = node =canny1= download=None
a=0
def startwindow():
    window.title("Draw")
    window.geometry("1000x1000")
    window.configure(bg="black")
def uplodefile():
    global imageorg,file_path,a
    file_path = filedialog.askopenfilename()  # פותח את חלון בחירת הקובץ ומחזיר את הנתיב של הקובץ שנבחר
    if file_path:
        global image,label,pil_image
        pil_image = Image.open(file_path)
        image=imageorg = ImageTk.PhotoImage(pil_image)
        a=1
        if label is None:
            label = tk.Label(window, image=image)
            label.place(x=0, y=50, width=1000, height=1000)
            a=1
        else:
            label.config(image=image)
            a=1
        label.image = image  #שמירת רפרנס לתמונה
def convert_cv(image):
    pil_image = ImageTk.getimage(image)
    cv_image = np.array(pil_image)
    cv_image = cv.cvtColor(cv_image, cv.COLOR_RGB2BGR)
    return cv_image
def convartpli(image):
    A_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    B = Image.fromarray(A_rgb)
    photo = ImageTk.PhotoImage(B)
    return photo
def convert_cv1(image):
    pil_image = ImageTk.getimage(image)
    cv_image = np.array(pil_image)
    cv_image = cv.cvtColor(cv_image, cv.COLOR_RGB2BGR)
    return cv_image
def on_closing():
    window.destroy()
def gray():
    global a,image,label
    if a==1:
        image = convert_cv(image)
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        updatelabel()
        setnode()
def restart():
    global imageorg,image,label,node,a
    if a==1:
        image = imageorg
        label.config(image=imageorg)
        label.image = imageorg
        label.update()
def blur():
    global a,image,label,node
    if a==1:
        image = convert_cv(image)
        image = cv.GaussianBlur(image, (3, 3), 3)
        updatelabel()
        setnode()
def canny():
    global a,image,label,node
    if a==1:
        image = convert_cv(image)
        image = cv.Canny(image, 500, 500)
        updatelabel()
        setnode()
def next():
    global image,label,node
    if node is not None and node.getnext() is not None:
        node = node.getnext()
        image = node.getimage()
        label.config(image=image)
        label.image = image
        label.update()
def prev():
    global image,label,node
    if node is not None and node.getprev() is not None:
        node = node.getprev()
        image = node.getimage()
        label.config(image=image)
        label.image = image
        label.update()
def createbuttons():
    global uplodefile1, gray1, blur1, restart1,next1,prev1,canny1,download
    uplodefile1 =tk.Button(window, text="uplode file", command= uplodefile).place(x=0, y=0, width=100, height=50)
    gray1 =tk.Button(window, text="gray", command= gray).place(x=100, y=0, width=100, height=50)
    blur1 =tk.Button(window, text="blur", command= blur).place(x=200, y=0, width=100, height=50)
    restart1 =tk.Button(window, text="restart", command= restart).place(x=300, y=0, width=100, height=50)
    canny1 =tk.Button(window, text="canny", command= canny).place(x=400, y=0, width=100, height=50)
    prev1= tk.Button(window, text="prev", command= prev).place(x=500, y=0, width=100, height=50)
    next1 = tk.Button(window, text="next", command= next).place(x=600, y=0, width=100, height=50)
    download = tk.Button(window, text="download", command= save_image).place(x=700, y=0, width=100, height=50)
def setnode():
    global node
    if node is not None:
            node.setnext(Node(node,image))
            node=node.getnext()
    else:
        node = Node(image=imageorg)
        node.setnext(Node(node,image))
        node=node.getnext()
def updatelabel():
    global image,label
    image = convartpli(image)
    label.config(image=image)
    label.image = image
    label.update()
def photoimage_to_png():
    global image
    photoimage = image
    img = ImageTk.getimage(photoimage)
    png_image = io.BytesIO()
    img.save(png_image, format='PNG')
    png_image.seek(0)  # להחזיר את מצביע ה-BytesIO לתחילת הקובץ
    img_png = Image.open(png_image)
    return img_png
def save_image( default_filename="image.png"):
    root = tk.Tk()
    root.withdraw()
    image = photoimage_to_png()
    file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                             filetypes=[("PNG files", "*.png")],
                                             initialfile=default_filename)
    if file_path:
        image.save(file_path, "PNG")
        print(f"Image saved to {file_path}")
    else:
        print("Save operation was cancelled.")
window = tk.Tk()
startwindow()
window.protocol("WM_DELETE_WINDOW", on_closing) 
createbuttons()
window.mainloop()



