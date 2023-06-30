from tkinter import *
from PIL.ImageTk import PhotoImage
from PIL import Image


gif_path = "images\\clouds sky.gif"


root = Tk()

canvas = Canvas(root)
canvas.pack(fill=BOTH,expand=1)

img = Image.open(gif_path)

frames = []
while True:
    try:
        frames.append(PhotoImage(img))
        img.seek(len(frames))
    except:
        break

print(frames)

def update(index):
    canvas.delete("all")
    canvas.create_image(0,0,anchor="nw",image = frames[index])
    index = (index+1)%len(frames)
    canvas.after(1000,lambda : update(index))


update(0)
root.mainloop()
