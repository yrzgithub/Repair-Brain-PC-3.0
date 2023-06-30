from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenmmheight()

root.wm_geometry(f"600x450+{(screen_width//2)-300}+{(screen_height//2)}")

img_path = "D://My Apps//Repair Brain//Version 2//Repair Brain Python//temp//photo.jpg"
pil_image = Image.open(fp=img_path)
photo_image = PhotoImage(image=pil_image)

c = Canvas(root)
c.pack(expand=True,fill=BOTH)
c.create_image(0,0,image=photo_image)

sign_label = Label(root,text="Login To Repair Brain",font=("Times New Roman",30))
sign_label.place(relx=.5,rely=.12,anchor=CENTER)



root.mainloop()