from tkinter import *
from PIL.ImageTk import PhotoImage
from PIL import Image

loading_path = "images\\clouds sky.gif"

root = Tk()

canvas = Canvas(root)
canvas.pack(fill=BOTH,expand=1)

img = Image.open(loading_path)

frames = []

while True:
    frames.append(PhotoImage(img))

    try:
        img.seek(len(frames))
    
    except EOFError:
        break

print(frames)


def run(index):
    canvas.delete("all")
    index = (index+1) % len(frames)
    print(index)
    canvas.create_image(0,0,anchor = "nw",image=frames[index])
    canvas.after(1000,lambda : run(index))

run(0)

root.mainloop()