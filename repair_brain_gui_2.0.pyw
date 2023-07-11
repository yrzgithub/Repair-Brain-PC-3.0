print("Loading started")

from tkinter import *
from threading import Thread
from PIL import Image
from PIL.ImageTk import PhotoImage
from pickle import load,dump 
from datetime import datetime
from os.path import isfile,expanduser,isdir
from os import listdir,system,remove,mkdir
from time import sleep
from random import choice
from tkinter.filedialog import askopenfilenames
from shutil import copy
from winsound import MessageBeep
from matplotlib import pyplot
from webbrowser import open_new_tab
from collections import OrderedDict
from sys import exit
from webbrowser import open_new_tab
from user import *
from os.path import isfile
import pyperclip
import vlc

print("Loading completed")

box_title = "Repair Brain"
screen_name = "Repair Brain"
plot_name_accuracy_plot = "Accuracy plot"
plot_name_habit_replace = "Replace plot"

key_lastly_opened = "lastly_opened"
key_lastly_relapsed = "lastly_relapsed"
key_lastly_noted_change = "lastly_noted_change"
key_lastly_noted_side_effect = "lastly_noted_side_effect"
key_start_time = "start_time"
key_next_step = "next_step"
key_replace_habits = "replace_habits"
key_plot_accuracy = "accuracy_plot"
key_last_accuracy_percent = "last_accuracy_percent"
key_positive_effects  = "Positive Effects"
key_negative_Effects = "Negative Effects"
key_next_steps = "Next Steps"

app_data = "pkls\\app_data.pkl"

icon_name = "icon\\favicon.ico"
gif_path_loading = "images\\loading.gif"
gif_path_connecting = "images\\connecting.gif"

bgm_folder = "bgm"

contact_data = {"Instagram":"https://www.instagram.com/alpha_yr/","Linked In":"https://www.linkedin.com/in/sanjay-kumar-y-r-6a88b6207","Github":"https://github.com/yrzgithub","FaceBook":"https://www.facebook.com/y.r.kumar.1232"}
git_link = "https://github.com/yrzgithub/Repair-Brain"
yt_coding_channel_link = "https://www.youtube.com/channel/UCPOkSZ7GGwgVjVQqP2MjviA"
yt_personal_channel = "https://www.youtube.com/channel/UC6wZDLRN5RPimxqIdoR6g_g"
developer_mail = "seenusanjay20102002@gmail.com"

database_link = "https://repair-brain-20-default-rtdb.firebaseio.com/versions.json"
database_url = "https://repair-brain-20-default-rtdb.firebaseio.com"

week_days = ("Mon","Tue","Wed","Thur","Fri","Sat","Sun")

msg_root = None
replace_habits = None
check_btn_vars = None
tp_root = None
stop_thread = False
data_base = None
user = None
data = None
percent = None

max_replace_habit_len = 7
min_replace_habit_len = 3
show_plot_after = 7 # days
current_version_name = 2.0
today = datetime.now().weekday()


bgms = listdir(bgm_folder)
bgm = choice(bgms)
print("Selected BGM : ",bgm)

dir_list = ("pkls","text")
for dir in dir_list:
    if not isdir(dir):
        mkdir(dir)
        print(dir," created")

vlc_instane = vlc.Instance()
player = vlc_instane.media_player_new()
media = vlc_instane.media_new(f"bgm\\{bgm}")
player.set_media(media)





MessageBeep()

root = Tk(screenName="main_screen")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenmmheight()

root.wm_geometry(f"600x450+{(screen_width//2)-300}+{(screen_height//2)}")
root.wm_iconbitmap(bitmap=icon_name)
root.wm_title(box_title)

free_img = Image.open(fp="images\\free.jpg").resize(size=(230,230))
free_img = PhotoImage(image=free_img)

hand_cuffed_img = Image.open(fp="images\\hand_cuffed.jpg").resize(size=(230,230))
hand_cuffed_img = PhotoImage(image=hand_cuffed_img)

loading_image = Image.open("images\\loading.gif")
loading_image = PhotoImage(loading_image)

root.config(bg="pink")

top_string = StringVar()
top_string.set("Are you Free or Addicted?")

edit_button_var = StringVar()
done_button_var = StringVar()
txt_done_btn_var = StringVar()

days_gone = IntVar()
hours_gone = IntVar()
minutes_gone = IntVar()
seconds_gone = IntVar()

frame_ask = Frame()
frame_show_data = Frame()
frame_edit = Frame()
frame_accuracy = Frame()
frame_login = Frame()
frame_signin = Frame()



frames_loading = []
frames_connecting = []

def get_frames(gif_path,frames):
    # gif frames
    gif = Image.open(gif_path)

    while True:
        frames.append(PhotoImage(gif))
        try:
            gif.seek(len(frames))
        except EOFError:
            break


    print("No of frames : ",len(frames))


def time_manager():
    start_time = data[key_start_time]
    root_exists = True
    while root_exists and not stop_thread:
        time_now = datetime.now()
        diff = time_now - start_time
        diff_days = diff.days
        diff_seconds = diff.total_seconds()
        diff_hours = int(diff_seconds//3600) % 24
        hours_float = diff_seconds % 3600
        diff_minutes = int(hours_float//60)
        diff_seconds = int(hours_float%60)
        try:
            root_exists = root.winfo_exists()
            days_gone.set(diff_days)
            hours_gone.set(diff_hours)
            minutes_gone.set(diff_minutes)
            seconds_gone.set(diff_seconds)
        except:
            break
        sleep(1)
    


def data_file(mode="rb",path=None,to_write=None):
    out = None

    with open(path,mode) as file:
        if mode=="rb":
            out = load(file)

        elif mode == "wb":
            dump(to_write,file)

        elif mode=="r":
            out = file.read()

        else:
            file.write(to_write)

        file.close()

    return out


def update_app(msg_root,link):
    msg_root.destroy()
    open_new_tab(link)
    msgbox(r"Follow the instructions in this github page")
    

def msgbox(msg,master=root,title=box_title,destroy_root=False,entry=False,width=650,height=200):
    msg_root = Toplevel(master=master)
    msg_root.wm_geometry(f"{width}x{height}+{(screen_width//2)-(width)//2}+{(screen_height//2)+(height)//2}")
    msg_root.wm_iconbitmap(bitmap=icon_name)
    msg_root.wm_title(title)
    msg_root.wm_resizable(False,False)

    if entry:
        create = Entry(msg_root,font=("Times New Roman",18),fg="grey",justify=CENTER) 
        create.insert(INSERT,msg)
        create.bind("<Button>",lambda e : entry_button_click(create))

    else:
        create = Label(msg_root,font=("Times New Roman",18),text=msg)
        
    create.place(relx=.5,rely=.3,anchor=CENTER,relwidth=.9)
    ok_msg_btn = Button(msg_root,text="Ok",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue",command = msg_root.destroy if not destroy_root else root.destroy)
    ok_msg_btn.place(relx=0.5,rely=0.8,width=50,height=30,anchor=CENTER)

    MessageBeep()

    return msg_root,ok_msg_btn,create


def check_version():
    try:
        database_data = User.get_database_reference().child("versions").child("latest_versions").get().val()
        # print(User.get_database_reference().get().val())
        latest_version_name = database_data["name"]
        print("Connected to data base")
        assert current_version_name<latest_version_name
        msg_root,ok_msg_btn,create = msgbox("New Version Available")
        latest_version_link = database_data["link"]
        ok_msg_btn.configure(text="update",command=lambda : update_app(msg_root,latest_version_link))
        ok_msg_btn.place(relx=0.5,rely=0.73,anchor=CENTER,width=90,height=40)

    except AssertionError as e:
        print(e)
        print("Already in the latest version")

    except Exception as e:
        print(str(e))
        return msgbox("Can't connect to database")

    else:
        print("Connected to database")


def next():
    global side_effect_entry,next_step_entry,change_entry

    frame_ask.destroy()

    lastly_relapsed = data[key_lastly_relapsed]
    last_change = data[key_lastly_noted_change]
    last_side_effect = data[key_lastly_noted_side_effect]
    next_step = data[key_next_step]

    lastly_relapsed_format = "Not Found"
    if type(lastly_relapsed) == datetime:lastly_relapsed_format = lastly_relapsed.strftime("%d:%m:%y")

    top = Frame(frame_show_data)
    top.place(relx=.5,rely=.08,anchor=CENTER)

    time_gone_label = Label(top,text="Time gone :",font=("Times New Roman",19),anchor=CENTER)
    time_gone_label.grid(row=0,column=1)

    Label(top,textvariable=days_gone,font=("Times New Roman",19),anchor=CENTER).grid(row=0,column=2)

    time_gone_days = Label(top,text="days",font=("Times New Roman",19),anchor=CENTER)
    time_gone_days.grid(row=0,column=3)

    Label(top,textvariable=hours_gone,font=("Times New Roman",19),anchor=CENTER).grid(row=0,column=4)

    time_gone_hours = Label(top,text="hours",font=("Times New Roman",19),anchor=CENTER)
    time_gone_hours.grid(row=0,column=5)

    Label(top,textvariable=minutes_gone,font=("Times New Roman",19),anchor=CENTER).grid(row=0,column=6)

    time_gone_minutes = Label(top,text="min",font=("Times New Roman",19),anchor=CENTER)
    time_gone_minutes.grid(row=0,column=7)

    Label(top,textvariable=seconds_gone,font=("Times New Roman",19),anchor=CENTER).grid(row=0,column=8)

    time_gone_sec = Label(top,text="sec",font=("Times New Roman",19),anchor=CENTER)
    time_gone_sec.grid(row=0,column=9)

    lastly_relapsed_label = Label(frame_show_data,text=f"Lastly relapsed : {lastly_relapsed_format}",font=("Times New Roman",18),anchor=CENTER)
    lastly_relapsed_label.place(relx=.5,rely=.18,anchor=CENTER)

    next_step = Label(frame_show_data,text=f"Next Step : {next_step}",font=("Times New Roman",18),anchor=CENTER)
    next_step.place(relx=.5,rely=.28,anchor=CENTER)

    lastly_noted_change_label = Label(frame_show_data,text=f"Lastly noted + ve effect : {last_change}",font=("Times New Roman",18),anchor=CENTER)
    lastly_noted_change_label.place(relx=.5,rely=.37,anchor=CENTER)

    lastly_noted_side_effect_label = Label(frame_show_data,text=f"Lastly noted -ve effect : {last_side_effect}",font=("Times New Roman",18),anchor=CENTER)
    lastly_noted_side_effect_label.place(relx=.5,rely=.47,anchor=CENTER)

    ok_button = Button(frame_show_data,text="Next",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue",command=ok_button_click)
    ok_button.place(relx=.63,rely=.88,anchor=CENTER,relwidth=.155,relheight=.09)

    show_changes_side_effects = Button(frame_show_data,text="Effects",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue",command=show_changes_side_effects_click)
    show_changes_side_effects.place(relx=.37,rely=.88,anchor=CENTER,relwidth=.155,relheight=.09)

    change_entry = Entry(frame_show_data,font=("Times New Roman",15),fg="grey",justify=CENTER)
    change_entry.insert(0,"Enter the positive effect")
    change_entry.place(relx=.28,rely=.6,anchor=CENTER,relwidth=.4,relheight=.08)

    side_effect_entry = Entry(frame_show_data,font=("Times New Roman",15),fg="grey",justify=CENTER)
    side_effect_entry.insert(0,"Enter the negative effect")
    side_effect_entry.place(relx=.72,rely=.6,anchor=CENTER,relwidth=.4,relheight=.08)

    next_step_entry = Entry(frame_show_data,font=("Times New Roman",15),fg="grey",justify=CENTER)
    next_step_entry.insert(0,"Enter the next step")
    next_step_entry.place(relx=.5,rely=.73,anchor=CENTER,relwidth=.7,relheight=.08)

    change_entry.bind("<Button>",lambda event : entry_button_click(change_entry))
    side_effect_entry.bind("<Button>",lambda event : entry_button_click(side_effect_entry))
    next_step_entry.bind("<Button>",lambda event : entry_button_click(next_step_entry))

    frame_show_data.place(relheight=1,relwidth=1)


def relaped_click():   # addicted
    data[key_lastly_relapsed] = data[key_start_time] = data[key_lastly_opened] = datetime.now()
    next()
    time_manager_thread = Thread(target=time_manager)
    time_manager_thread.start()


def no_button_click():   # free
    root.bind("<space>",stop_player)
    player.play()
    next()
    time_manager_thread = Thread(target=time_manager)
    time_manager_thread.start()


def add_to_database(effect_type,effect):
    global data
    time_now = datetime.now().strftime("%a,%b %d %Y")
    print("Add to data base : ",effect_type,effect)
    data[effect_type][effect]  = time_now
    key_name = effect_type + " list"
    print(data[key_name].append(effect))


def save_current_effect_change_data():
    side_effect = side_effect_entry.get().strip()
    change = change_entry.get().strip()
    next_step = next_step_entry.get().strip()
    if is_valid_entry(side_effect_entry,"Enter the negative effect"):
        data[key_lastly_noted_side_effect] =  side_effect
        add_to_database(key_negative_Effects,side_effect)
        print("Entry changes saved")

    if is_valid_entry(change_entry,"Enter the positive effect"):
        data[key_lastly_noted_change] = change
        add_to_database(key_positive_effects,change)
        print("Entry changes saved")
        
    if is_valid_entry(next_step_entry,"Enter the next step"):
        data[key_next_step] = next_step
        add_to_database(key_next_steps,next_step)
        print("Entry changes saved")


def show_changes_side_effects_click(destroy=True):
    global text_widget,edit_button,done_button,next_steps,changes,effects,stop_thread

    stop_thread = True
    player.stop()
    root.unbind(stop_player)

    if destroy:
        save_current_effect_change_data()
        frame_show_data.destroy()

    edit_button_var.set("Edit")
    done_button_var.set("Next")

    # put cpmmand = "edit_steps() to modify the txt file"
    
    edit_button = Button(frame_edit,textvariable=edit_button_var,command = lambda : open_new_tab("https://www.google.com"),font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue")
    edit_button.place(relx=.4,anchor=CENTER,rely=.95,relheight=.08)

    done_button = Button(frame_edit,textvariable=done_button_var,command = lambda : accuracy_frame(frame_edit),font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue")
    done_button.place(relx=.6,anchor=CENTER,rely=.95,relheight=.08)

    # txt_format = f"{key_next_steps} :\n\n   {next_steps}\n\n\n {key_positive_effects} :\n\n   {changes}\n\n\n{key_negative_Effects} :\n\n   {effects}"

    positive_effects_list = data[key_positive_effects+" list"]
    negative_effects_list = data[key_negative_Effects+" list"]
    next_steps_list = data[key_next_steps+" list"]

    changes = [f"{effect} ({data[key_positive_effects][effect]})" for effect in positive_effects_list]
    effects = [f"{effect} ({data[key_negative_Effects][effect]})" for effect in negative_effects_list]
    next_steps = [f"{effect} ({data[key_next_steps][effect]})" for effect in next_steps_list]

    changes_str = ""
    for eff in changes:
        changes_str+=eff + "\n   "

    effects_str = ""
    for eff in effects:
        effects_str+=eff + "\n   "

    next_str = ""
    for eff in next_steps:
        next_str+=eff + "\n   "

    txt_format = f"{key_positive_effects} :\n\n   {changes_str}\n\n\n{key_negative_Effects} :\n\n   {effects_str}\n\n\n{key_next_steps} :\n\n   {next_str}"
    text_widget = Text(frame_edit,font=("Times New Roman",20),padx=5,pady=5)
    text_widget.insert(END,txt_format)
    text_widget.configure(state=DISABLED)
    text_widget.place(relheight=.9,relwidth=1)
    frame_edit.place(relheight=1,relwidth=1)


def edit_steps():
    done_button_var.set("Next")
    edit_button_var.set("Save")
    text_widget.bind("<Button-1>",func=lambda e : edit_button_var.set("Save"))
    text_widget.bind("<Key>",func=lambda e : edit_button_var.set("Save"))
    text_widget.configure(state=NORMAL)
    text_widget.delete(1.0,END)
    text_widget.insert(END,f" Next Step :\n\n   {next_steps}")
    # edit_button.configure(command = lambda : save_txt(txt_next_step))
    done_button.configure(command = lambda : edit_changes())


def edit_changes():
    done_button_var.set("Next")
    edit_button_var.set("Save")
    text_widget.delete(1.0,END)
    text_widget.insert(END,f" Positive Effects :\n\n   {changes}")
    # edit_button.configure(command = lambda : save_txt(txt_changes))
    done_button.configure(command = lambda : edit_effects())


def edit_effects():
    done_button_var.set("Next")
    edit_button_var.set("Save")
    text_widget.delete(1.0,END)
    text_widget.insert(END,f" Side Effects :\n\n   {effects}")
    done_button.configure(command = lambda : accuracy_frame(frame_edit))
    # edit_button.configure(command=lambda : save_txt(txt_effects))


def tp_root_check(checked_vars):
    if checked_vars[0].get()==1:
        for btn_var in checked_vars:
            btn_var.set(1)
                


def add_habit_frame(msg="Enter the new habit"):
    global days_list,check_btn_vars_tp,days_var_dict,tp_root

    add_button.configure(state=DISABLED,bg="grey",disabledforeground="white")
    done_button.configure(state=DISABLED,bg="grey",disabledforeground="white")

    if len(data[key_replace_habits])>=max_replace_habit_len:
        msgbox(title=box_title,msg="Maximum limit reached")
        try:
            add_button.configure(state=NORMAL,bg="blue",disabledforeground="white")
            done_button.configure(state=NORMAL,bg="blue",disabledforeground="white")
        except:
            pass
        return
    
    days_list = ("All","Sun","Mon","Tue","Wed","Thur","Fri","Sat")
    check_btn_vars_tp = []
    checked_btns = []
    days_var_dict = {}

    tp_root = Toplevel()
    screen_width = tp_root.winfo_screenwidth()
    screen_height = tp_root.winfo_screenmmheight()

    tp_root.wm_geometry(f"400x300+{(screen_width//2)-200}+{(screen_height//2)+100}")
    tp_root.wm_iconbitmap(bitmap=icon_name)
    tp_root.wm_title(box_title)

    new_habit_entry = Entry(tp_root,font=("Times New Roman",15),fg="grey",justify=CENTER)
    new_habit_entry.insert(END,msg)
    new_habit_entry.bind("<Button>",lambda e: entry_button_click(new_habit_entry))
    new_habit_entry.place(relx=.5,rely=.1,anchor=CENTER,relwidth=.75)

    week_days_frame = Frame(tp_root,bg="white")
    rows = 4

    for r in range(rows):
        week_days_frame.rowconfigure(r,weight=1)

    week_days_frame.columnconfigure(0,weight=1)
    week_days_frame.columnconfigure(1,weight=2)
    week_days_frame.columnconfigure(2,weight=1)
    week_days_frame.columnconfigure(3,weight=2)

    week_days_frame.place(relx=.5,rely=.22,anchor=N,relwidth=.8,relheight=.5)

    for n in range(len(days_list)//2):
        int_var = IntVar()
        int_var.set(0)
        check_btn_vars_tp.append(int_var)
        days_var_dict[days_list[n]] = int_var

        day_name_label_l = Label(week_days_frame,text=days_list[n],font=("Times New Roman",18),anchor=CENTER,bg="white")
        check_box_l = Checkbutton(week_days_frame,bg="white",onvalue=1,offvalue=0,command=lambda : tp_root_check(check_btn_vars_tp),variable=int_var)

        day_name_label_l.grid(row=n,column=0)
        check_box_l.grid(row=n,column=1)

        int_var = IntVar()
        int_var.set(0)
        check_btn_vars_tp.append(int_var)
        days_var_dict[days_list[n+4]] = int_var

        day_name_label_r = Label(week_days_frame,text=days_list[n+4],font=("Times New Roman",18),anchor=CENTER,bg="white")
        check_box_r = Checkbutton(week_days_frame,bg="white",onvalue=1,offvalue=0,command=lambda : tp_root_check(check_btn_vars_tp),variable=int_var)

        checked_btns.append(check_box_l)
        checked_btns.append(check_box_r)

        day_name_label_r.grid(row=n,column=2)
        check_box_r.grid(row=n,column=3)

    done = Button(tp_root,text="Ok",font=("Times New Roman",18,"bold"),cursor="hand2",command=lambda : add_replace_habits(tp_root,new_habit_entry),background="blue",foreground="white",activeforeground="white",activebackground="blue")
    done.place(relx=.5,rely=.85,anchor=CENTER,relheight=.1,relwidth=.2)

    tp_root.protocol("WM_DELETE_WINDOW",lambda : add_replace_habits(tp_root,new_habit_entry))

    MessageBeep()

    return tp_root,done,new_habit_entry


def on_window_close_tp(tp_root):
    add_button.configure(state=NORMAL,bg="blue",disabledforeground="white")
    done_button.configure(state=NORMAL,bg="blue",disabledforeground="white")
    tp_root.destroy()


def add_replace_habits(tp,habit_entry):
    replace_habits_dict = data[key_replace_habits]

    new_habit = habit_entry.get()

    tp.destroy()

    if new_habit is not None and new_habit!="" and new_habit!="Enter the new habit" and new_habit!=f"Atleast {min_replace_habit_len} habits required":
        check_days = []
        days_var_dict.pop("All")
        for key,val in days_var_dict.items():
            if val.get()==1:
                check_days.append(key)
                
        if len(check_days)==0:
            msg_root,msg_ok_btn,create = msgbox(title=box_title,msg="Days not selected")
            msg_ok_btn.configure(command=lambda : msg_root_del(msg_root))
            msg_root.protocol("WM_DELETE_WINDOW",lambda : msg_root_del(msg_root))
            return
        
        else:
            replace_habits_dict[new_habit] = {"days_data":{datetime.now().strftime("%d-%m-%y"):0},"show_on" : check_days}
            accuracy_frame(frame_accuracy,False)

    else:
        msg_root,msg_ok_btn,create = msgbox(title=box_title,msg="Invalid habit name")
        msg_ok_btn.configure(command=lambda :  msg_root_del(msg_root))
        msg_root.protocol("WM_DELETE_WINDOW",lambda : msg_root_del(msg_root))
        return


def msg_root_del(msg_root):
    msg_root.destroy()
    accuracy_frame(frame_accuracy,False)


def stick_labels(labels,int_vars):
    for label,var in zip(labels,int_vars):
        if var.get()==1:
            label.configure(font=("Times New Roman",22,"overstrike"))
        else:
            label.configure(font=("Times New Roman",22))


def remove_habits(int_vars):
    replace_habits_dict = data[key_replace_habits]
    replace_habits = list(data[key_replace_habits].keys())

    for index,var in enumerate(int_vars):
        if var.get()==1:
            replace_habits_dict.pop(replace_habits[index])
    
    on_window_close()


def change_replace_habits():
    global int_var_list

    if user is None:
        return msgbox("Login is required")

    replace_habits_dict = data[key_replace_habits]
    replace_habits_len = len(replace_habits_dict)
    labels_list = []
    int_var_list = []

    change_replace_habits_frame = Frame(root)
    replace_habits_list_frame = Frame(change_replace_habits_frame,bg="white")

    top = Label(change_replace_habits_frame,text="Select the habits to remove",font=("Times New Roman",25,"bold"),anchor=CENTER)

    cols = 2
    for col in range(cols):
        replace_habits_list_frame.grid_columnconfigure(col,weight=1)

    for row in range(replace_habits_len):
        replace_habits_list_frame.grid_rowconfigure(row,weight=1)
    
    for n,key in enumerate(replace_habits_dict):
        int_var = IntVar()
        int_var.set(0)

        label = Label(replace_habits_list_frame,text=key,font=("Times New Roman",22),bg="white")
        labels_list.append(label)
        label.grid(row=n,column=0)

        Checkbutton(replace_habits_list_frame,bg="white",command=lambda : stick_labels(labels_list,int_var_list),onvalue=1,offvalue=0,variable=int_var).grid(row=n,column=1)
        int_var_list.append(int_var)

    remove_button = Button(change_replace_habits_frame,command = lambda : remove_habits(int_var_list),text="Remove",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue")
    exit_button = Button(change_replace_habits_frame,command=on_window_close,text="Exit",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue")

    top.place(relx=.5,rely=.1,anchor=CENTER)
    replace_habits_list_frame.place(relx=.5,rely=.49,anchor=CENTER,relwidth=.8,relheight=.6 * (replace_habits_len/max_replace_habit_len))
    remove_button.place(relx=.37,rely=.88,anchor=CENTER,relwidth=.155,relheight=.09)
    exit_button.place(relx=.63,rely=.88,anchor=CENTER,relwidth=.155,relheight=.09)

    change_replace_habits_frame.place(relheight=1,relwidth=1)


def calc_accuracy(check_vars,enabled_len,top_string,percentage_diff_var):
    global percent

    checked_length = len(list(filter(lambda v : v.get()==1,check_vars)))
    percent = int((checked_length*100)/enabled_len)
    percent_difference = percent - data[key_last_accuracy_percent]

    top_string.set(f"Replacing accuracy : {percent}%")

    if percent_difference==0 : 
        percentage_diff_var.set("( 0 )")
        percentage_difference_widget.configure(fg="green")

    elif percent_difference>0 : 
        percentage_diff_var.set(f"({percent_difference}↑)")
        percentage_difference_widget.configure(fg="green")

    else : 
        percentage_diff_var.set(f"({-percent_difference}↓)")
        percentage_difference_widget.configure(fg="red")


def marquee(label,habit,txt_var):
    habit = habit[1:] + habit[0]
    txt_var.set(habit)
    label.after(1000,lambda : marquee(label,habit,txt_var))


def accuracy_frame(frame,destroy=True):
    global stop_thread,add_button,percentage_difference_widget,percent,replace_habits,check_btn_vars,done_button,top

    stop_thread = True
    player.stop()

    if destroy : 
        frame.destroy()
    else:
        frame.place_forget()

    replace_habits = data[key_replace_habits]
    #replace_habits_filtered = dict(filter(lambda entry : True if week_days[today] in entry[1]["show_on"] else False,replace_habits.items()))
    replace_habits_len = len(replace_habits)

    top_string = StringVar()
    top_string.set("Replacing accuracy : __%")

    percent_diff_var = StringVar()

    top = Label(frame_accuracy,textvariable=top_string,font=("Times New Roman",25),anchor=CENTER)
    top.place(relx=.5,rely=0.1,anchor=CENTER)

    percentage_difference_widget = Label(frame_accuracy,textvariable=percent_diff_var,font=("Times New Roman",18),anchor=CENTER)
    percentage_difference_widget.place(relx=.87,rely=0.1,anchor=CENTER)

    add_button = Button(frame_accuracy,command=lambda : add_habit_frame(),text="Add",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue")
    done_button = Button(frame_accuracy,text="Done",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue",command=on_window_close)

    marquee_txt_vars = []
    check_btn_vars = []

    frames_collection = Frame(frame_accuracy,bg="white")
    frames_collection.place(relx=.5,rely=.49,anchor=CENTER,relwidth=.8,relheight=.6 * (replace_habits_len/max_replace_habit_len))

    rows = replace_habits_len
    columns = 2

    enabled_count = 0

    for index in range(rows):
        frames_collection.rowconfigure(index,weight=1)

    for index in range(columns):
        frames_collection.columnconfigure(index,weight=1)


    for n,habit in enumerate(replace_habits):
        txt_var = StringVar(frames_collection)
        txt_var.set(habit)

        check_var = IntVar(frames_collection)
        check_var.set(0)
        check_btn_vars.append(check_var)

        state = NORMAL if week_days[today] in replace_habits[habit]["show_on"] else DISABLED 
        if state==NORMAL:
            enabled_count+=1

        habit_name_label = Label(frames_collection,textvariable=txt_var,font=("Times New Roman",22),justify=RIGHT,state=state)
        habit_name_label.grid(row=n,column=0)

        habit_check_btn = Checkbutton(frames_collection,onvalue=1,offvalue=0,variable=check_var,command=lambda : calc_accuracy(check_btn_vars,enabled_count,top_string,percent_diff_var),state=state)
        habit_check_btn.grid(row=n,column=1)

        if state:
            habit_name_label.configure(bg="white")
            habit_check_btn.configure(bg="white")
            
        else:
            habit_name_label.configure(fg="grey",bg="grey")
            habit_check_btn.configure(fg="grey",bg="grey")

        if len(habit)>15:
            marquee_txt_vars.append(habit)
            marquee(habit_name_label,habit+(" ")*20,txt_var)

    add_button.place(relx=.37,rely=.88,anchor=CENTER,relwidth=.155,relheight=.09)
    done_button.place(relx=.63,rely=.88,anchor=CENTER,relwidth=.155,relheight=.09)

    frame_accuracy.place(relheight=1,relwidth=1)

    if len(data[key_replace_habits])<min_replace_habit_len:    
        add_habit_frame(msg=f"Atleast {min_replace_habit_len} habits required")
        

def show_all():
    show_changes_side_effects_click(False)


def ok_button_click():
    save_current_effect_change_data()
    accuracy_frame(frame_show_data)


def convert_data(key):
    global data_java
    dict_time = data_java[key]

    if(type(dict_time)==datetime):
        time = {"year":dict_time.year,"month":dict_time.month,"day":dict_time.day,"hour":dict_time.hour,"minute":dict_time.minute,"second":dict_time.second}
        data_java[key] = time
        data_java["replace_habits_list"] = list(data_java[key_replace_habits].keys())
        return data_java

    else:
        print(dict_time)


def plot_data(key_plot_name,day_name,perc):
    list_date = data[key_plot_name]["date"]
    list_value = data[key_plot_name]["value"]

    if len(list_date)>0 and list_date[-1]==day_name:
        list_date.pop()
        list_value.pop()

    if day_name in list_date:
        show_plot(clear=True,warn=False)
    
    list_date.append(day_name)
    list_value.append(perc)
    return len(list_date)


def on_window_close():
    global percent,stop_thread,data_java

    stop_thread = True

    if data is None: 
        root.destroy()
        exit(0)

    time_now = datetime.now()
    data[key_lastly_opened] = time_now

    print(data[key_plot_accuracy])

    len_plot = len(data[key_plot_accuracy]["date"])

    print("Plot data length",len_plot)

    replace_habits = data[key_replace_habits].keys()

    if replace_habits is not None and check_btn_vars is not None and percent is not None:
        print("Saving habit count data..")
        formated_time_now = time_now.strftime("%d-%m-%y")
        for habit,intvar in zip(replace_habits,check_btn_vars):
            print(data[key_replace_habits][habit])
            data[key_replace_habits][habit]["days_data"][formated_time_now] = intvar.get()
    
    if percent is None:
        percent = 0

    plot_data(key_plot_accuracy,week_days[today],percent)
    data[key_last_accuracy_percent] = percent

    if len_plot>show_plot_after or today==6:
        show_plot(clear=True,warn=False)

    player.stop()

    data_java = data
    
    convert_data("lastly_opened")
    convert_data("start_time")
    convert_data("lastly_relapsed")


    if user!=None:
        
        def run_on_thread():
            canvas = show_gif(root,frames_connecting)
            
            success = user.write_to_data_base(data_java)

            canvas.destroy()

            print(success)

            if not success:
                root.withdraw()
                msg_root,btn,label = msgbox("Data not updated")
                msg_root.protocol("WM_DELETE_WINDOW",root.destroy)
                btn.configure(command=root.destroy)
        
            else:
                print("Else called")
                root.withdraw()
                root.after(500,root.destroy)


        Thread(target=run_on_thread).start()

    else:
        root.destroy()



def entry_button_click(entry):
    player.stop()
    entry.delete(0,END)
    entry.configure(fg="black")


def is_valid_entry(entry,text):
    entry_data = entry.get().strip()
    return entry_data!=text and entry_data!="" and not entry_data.isspace()


def stop_player(event):
    player.pause()


def show_main_menu(event):
    main_menu.tk_popup(x = event.x_root+10,y=event.y_root+5)


def add_songs():
    bgm_files = listdir(bgm_folder)
    ask_files_path = askopenfilenames(title="Select music files",filetypes=[("Audio files","*.mp3")])

    if len(ask_files_path)==0:
        msgbox(title=box_title,msg="No song selected")
        return 

    for file_path in ask_files_path:
        file_name = file_path.rsplit("/",1)[-1]
        if file_name not in bgm_files:
            dst = copy(file_path,bgm_folder)
            print(f"{file_name} copied to {dst}")
        else:
            print(f"{file_name} - File already found")
        
    msgbox(title=box_title,msg="Songs Added")
    

def on_edit_note_click():
    txt_done_btn_var.set("Save")


def on_note_close(tpr):
    tpr.destroy()
    root.deiconify()

    
def run_on_start():
    start_up_folder_path = expanduser("~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    system("explorer.exe "+start_up_folder_path)
    msgbox(title=box_title,msg="Create shortcut for .pyw or .exe file here (start up folder)")


def contact_developer(media_name):
    if media_name=="Email":
        pyperclip.copy(developer_mail)
    else:
        open_new_tab(url=contact_data[media_name])


def show_plot(clear=False,warn=True):
    if user is None:
        return msgbox("Login is required")


    colors = ["red","cyan","blue","yellow","green","magenta"]

    date = data[key_plot_accuracy]["date"]
    value = data[key_plot_accuracy]["value"]

    if len(date)<2:
        if warn:
            return msgbox("Plot data is insufficient")
        else:
            return

    relplace_habits_dict = data[key_replace_habits]
    x_names = relplace_habits_dict.keys()
    y_values = [(sum(relplace_habits_dict[key]["days_data"].values())*100)//len(relplace_habits_dict[key]["show_on"]) for key in x_names]

    if len(x_names)==0:
        x_names = ["Example"]

    pyplot.subplot(2,1,1)
    pyplot.gca().title.set_text("Accuracy Plot")
    pyplot.xlabel("Day")
    pyplot.ylabel("Percentage")
    pyplot.ylim(0,100) 
    pyplot.plot_date(date,value,linestyle="-",color=choice(colors),label="Accuracy")
    pyplot.legend()

    pyplot.subplot(2,1,2)

    pyplot.gca().title.set_text("Habits Plot")
    pyplot.xlabel("Habit")
    pyplot.ylabel("Percentage")
    pyplot.ylim(0,100)
    pyplot.bar(x=x_names,height=y_values,color=colors)
    
    pyplot.tight_layout(h_pad=1,w_pad=1)
    pyplot.show()

    if clear:
        date.clear()
        value.clear()
        
        for key in relplace_habits_dict.keys():
            if "days_data" in relplace_habits_dict[key]:
                relplace_habits_dict[key]["days_data"] = {}


def reset(show_message=True):
    global data,data_base,data_java

    if user==None and show_message:
        return msgbox("Login before reset")
    
    player.stop()
    
    root.withdraw()
    
    data_java = start()
    convert_data("lastly_opened")
    convert_data("start_time")
    convert_data("lastly_relapsed")
    
    success = user.write_to_data_base(data_java)
    if not success and show_message:
        return msgbox("Can't connect to database")

    logout()

    if show_message : msgbox(title=box_title,msg="Successfully reseted",destroy_root=True)


def login(username_or_email,password):

    user_name_txt = username_or_email.get().strip()
    password_str = password.get().strip()

    if not is_valid_entry(username_or_email,"Enter the Username or Email"):
        return msgbox("Invalid Username")

    if not is_valid_entry(password,"Enter your Password"):
        return msgbox("Invalid password")
    


    def run_on_thread():
        global data_base,user

        canvas = show_gif(frame_login,frames_connecting)


        if "@gmail.com" in user_name_txt:
            user = User(username=None,email=user_name_txt,password=None,name=None,last_name=None)
            success,msg = user.login_with_email(password_str)
            email = True

        else:
            email = False
            user = User(username=user_name_txt,email=None,password=None,name=None,last_name=None)
            success,msg = user.login_with_username(password_str)


        if success:
            if user.is_user_verified():     
                save_data = {}

                save_data["password"] = password_str 
                save_data["email"] = user.email

                data_file(mode="wb",to_write=save_data,path=app_data)

                print("Login details saved")

                get_database_data()

                ask_frame_window()

            else:
                canvas.destroy()
                return msgbox("Email Not Verified")
            
        else:
            canvas.destroy()
            return msgbox(msg)



    Thread(target=run_on_thread).start()  
    
    
def show_gif(frame,frames):
   
    canvas = Canvas(frame,width=root.winfo_width(),height=root.winfo_height(),bg="white")
    canvas.pack(fill=BOTH,expand=1,anchor=CENTER)

    def run(index):
        try:
            canvas.delete("all")
            index = (index+1) % len(frames)
            frame = frames[index]

            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()

            image_width = frame.width()
            image_height = frame.height()

            x = (canvas_width - image_width)//2
            y = (canvas_height - image_height)//2

            print("Running")

            canvas.create_image(x,y,anchor=NW,image=frame)
            canvas.after(500,lambda : run(index))
        
        except:
            pass

    run(0)

    return canvas


def forget_password_fun():
    box_root,button,email_box = msgbox(msg="Enter your E-mail",entry=True)


    def run_on_thread():
        email = email_box.get().strip()
        if not is_valid_entry(email_box,"Enter your E-mail"):
            box_root.destroy()
            return msgbox(msg="Invalid E-mail",entry=False)
        
        canvas = show_gif(box_root,frames_connecting)

        success,msg = User.send_password_reset_link(email)


        def open_gmail():
            if success:
                Thread(target=open_new_tab,args=("https://www.gmail.com",)).start()


        canvas.destroy()

        MessageBeep()

        label = Label(box_root,text=msg,font=("Times New Roman",18))
        ok_msg_btn = Button(box_root,text="Ok",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue",command = lambda : [box_root.destroy(),open_gmail(),login_window()])
        
        label.place(relx=.5,rely=.3,anchor=CENTER,relwidth=.9)
        ok_msg_btn.place(relx=0.5,rely=0.8,width=50,height=30,anchor=CENTER)


    button.configure(command=Thread(target=run_on_thread).start)
    


def login_window():
    global frame_login
    
    frame_login.update_idletasks()

    title = Label(frame_login,text="Login In To Repair Brain",font=("Times New Roman",22,"bold"),fg="black",bg="pink")

    email_or_username = Entry(frame_login,font=("Times New Roman",15),fg="grey",justify=CENTER) 
    password = Entry(frame_login,font=("Times New Roman",15),fg="grey",justify=CENTER) 

    forget_password = Button(frame_login,font=("Times New Roman",13,"bold"),text="Forget password",border=0,cursor="hand2",bg="pink",fg="blue",activebackground="pink",activeforeground="red",command=forget_password_fun)

    sign_up = Button(frame_login,text="Sign Up",font=("Times New Roman",18,"bold"),command = sign_in_window ,cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue")
    login_button = Button(frame_login,text="Login",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue",command = lambda : login(email_or_username,password))

    email_or_username.bind("<Button>",lambda event : entry_button_click(email_or_username))
    password.bind("<Button>",lambda event : [entry_button_click(password),password.config(show="*")])

    title.place(relx=.5,rely=.17,anchor=CENTER)

    email_or_username.place(relx=.5,rely=.37,anchor=CENTER,relheight=.07,relwidth=.7)

    password.place(relx=.5,rely=.52,anchor=CENTER,relheight=.07,relwidth=.7)

    forget_password.place(relx=.15,rely=.62,anchor=W)

    sign_up.place(relx=.37,rely=.77,anchor=CENTER,relheight=.09,relwidth=.17)
    login_button.place(relx=.63,rely=.77,anchor=CENTER,relheight=.09,relwidth=.17)

    frame_login.pack(fill=BOTH,expand=1)

    frame_login.configure(bg="pink")

    email_or_username.insert(INSERT,"Enter the Username or Email")
    password.insert(INSERT,"Enter your Password")


def logout():
    global frame_login,user,data

    user = None
    data = None

    print("Loging out")

    player.stop()

    if isfile(app_data):
        remove(app_data)
        
    if frame_login.winfo_exists():
        frame_login.destroy()

    frame_login = Frame()
    login_window()


def sign_in_window():
    global root,frame_signin

    # first_name, last_name. email, password

    if not frame_signin.winfo_exists():
        frame_signin = Frame()

    frame_login.pack_forget()

    first_name_var = StringVar()
    last_name_var = StringVar()

    user_name_var = StringVar()

    email_id_var = StringVar()

    password_var = StringVar()
    password_check_var = StringVar()

    show_password_var = IntVar()

    first_name_var.set("First Name")
    last_name_var.set("Last Name")

    user_name_var.set("Username")

    email_id_var.set("E-mail Id")

    password_var.set("Password")
    password_check_var.set("Verify Password")


    frame_signin.configure(bg="pink")



    def on_click_show_password(password_entry):
        if show_password_var.get()==0:
            password_entry.config(show="*")

        else:
            password_entry.config(show="")


    show_password_var.set(0)


    login_label = Label(frame_signin,text="Sign In To Repair Brain",font=("Times New Roman",22,"bold"),fg="black",bg="pink")

    first_name_entry = Entry(frame_signin,textvariable=first_name_var,font=("Times New Roman",15),fg="grey",justify=CENTER) 
    last_name_entry = Entry(frame_signin,textvariable=last_name_var,font=("Times New Roman",15),fg="grey",justify=CENTER) 

    user_name_entry = Entry(frame_signin,textvariable=user_name_var,font=("Times New Roman",15),fg="grey",width=root.winfo_width(),justify=CENTER) 

    email_id_entry = Entry(frame_signin,textvariable=email_id_var,font=("Times New Roman",15),fg="grey",justify=CENTER) 

    password_entry = Entry(frame_signin,textvariable=password_var,font=("Times New Roman",15),fg="grey",justify=CENTER) 
    show_password_check = Checkbutton(frame_signin,onvalue=1,offvalue=0,command=lambda : on_click_show_password(password_entry),variable=show_password_var,anchor=CENTER,bg="pink")
    show_password_label = Label(frame_signin,text="Show Password",font=("Times New Roman",8),fg="black",bg="pink",anchor=CENTER)

    check_password_entry = Entry(frame_signin,textvariable=password_check_var,font=("Times New Roman",15),fg="grey",justify=CENTER) 

    entries = [first_name_entry,last_name_entry,user_name_entry,email_id_entry,password_entry,check_password_entry]

    cancel_button = Button(frame_signin,text="Cancel",font=("Times New Roman",18,"bold"),command= lambda : on_window_close(),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue")
    sign_in = Button(frame_signin,command = lambda : sign_in_fn(entries),text="Sign In",font=("Times New Roman",18,"bold"),cursor="hand2",background="blue",foreground="white",activeforeground="white",activebackground="blue")


    def decorate_text():
        if not is_valid_entry(first_name_entry,"First Name"):
            return

        if not is_valid_entry(last_name_entry,"Last Name"):
            return
    

        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if not first_name.istitle():
             first_name = first_name.title()
             first_name_var.set(first_name)
            
        if not last_name.isupper():
            last_name = last_name.upper()
            last_name_var.set(last_name)


    first_name_entry.bind("<Button>",lambda event : entry_button_click(first_name_entry))
    last_name_entry.bind("<Button>",lambda event : entry_button_click(last_name_entry))
    user_name_entry.bind("<Button>",lambda event : [entry_button_click(user_name_entry),decorate_text()])
    email_id_entry.bind("<Button>",lambda event : [entry_button_click(email_id_entry),decorate_text()])

    check_password_entry.bind("<Button>",lambda event : [entry_button_click(check_password_entry),check_password_entry.configure(show="*"),decorate_text()])
    password_entry.bind("<Button>",lambda event : [entry_button_click(password_entry),password_entry.configure(show="*"),decorate_text()])


    rows = 8.2

    login_label.place(relx=.5,rely=0.09,relwidth=.7,anchor=CENTER)

    first_name_entry.place(relx=.25,rely=2/rows,relwidth=.4,relheight=.07,anchor=CENTER)
    last_name_entry.place(relx=.75,rely=2/rows,relwidth=.4,relheight=.07,anchor=CENTER)

    user_name_entry.place(relx=.5,rely=3/rows,relwidth=.7,relheight=.07,anchor=CENTER)

    email_id_entry.place(relx=.5,rely=4/rows,relwidth=.7,relheight=.07,anchor=CENTER)

    password_entry.place(relx=.5,rely=5/rows,relwidth=.7,relheight=.07,anchor=CENTER)
    show_password_check.place(relx=.92,rely=5/rows-0.020,anchor=CENTER)
    show_password_label.place(relx=.92,rely=5/rows+0.025,relheight=.07,anchor=CENTER)

    check_password_entry.place(relx=.5,rely=6/rows,relwidth=.7,relheight=.07,anchor=CENTER)

    sign_in.place(relx=.625,rely=7/rows+.03,relwidth=.15,relheight=.09,anchor=CENTER)
    cancel_button.place(relx=.375,rely=7/rows+.03,relwidth=.15,relheight=.09,anchor=CENTER)

    frame_signin.pack(fill=BOTH,expand=1)


def sign_in_fn(entries):
    first_name_entry,last_name_entry,user_name_entry,email_id_entry,password_entry,check_password_entry = entries

    firstname = first_name_entry.get().title()
    lastname = last_name_entry.get().upper()
    username = user_name_entry.get()
    email = email_id_entry.get()
    password = password_entry.get()
    check_password = check_password_entry.get()


    if not is_valid_entry(first_name_entry,"First Name"):
        return msgbox("Invalid First Name")

    if not is_valid_entry(last_name_entry,"Last Name"):
        return msgbox("Invalid Last Name")

    if not is_valid_entry(user_name_entry,"Username"):
        return msgbox("Invalid Username")

    if not is_valid_entry(email_id_entry,"E-mail Id"):
        return msgbox("Invalid Email Id")

    if not is_valid_entry(password_entry,"Password"):
        return msgbox("Invalid password")

    if not is_valid_entry(check_password_entry,"Verify Password") or password!=check_password:
        return msgbox("Invalid or Passwords didn't match")
    
    if len(password)<6:
        return msgbox("Altleast 6 characters required for password")
    


    def on_window_delete(box):
        box.destroy()
        Thread(target=open_new_tab,args=("https://www.gmail.com",)).start()


    def run_on_thread():
        global data_java ,data_base,user,data

        canvas = show_gif(frame_signin,frames_connecting)

        user = User(username=username,name=firstname,last_name=lastname,email=email,password=password)
        user_created,msg = user.create_user_account()

        if not user_created:
            canvas.destroy()
            msgbox(msg)
        
        else:
            logout()

            data_java = start()
            data = start()

            print(data_java)

            convert_data("lastly_opened")
            convert_data("start_time")
            convert_data("lastly_relapsed")

            user.write_to_data_base(data_java)

            user.send_verification_link()
            box,button,entry =  msgbox("Verification link has been sent")
            button.configure(command = lambda : Thread(target=on_window_delete,args=(box,)).start())
            canvas.destroy()
            frame_signin.destroy()


    Thread(target=run_on_thread).start()



def ask_frame_window():
    global frame_ask
    
    frame_login.destroy()

    if not frame_ask.winfo_exists():
        frame_ask = Frame()

    top = Label(frame_ask,textvariable=top_string,font=("Times New Roman",38),anchor=CENTER)

    relapsed_button = Button(frame_ask,cursor="hand2",image=hand_cuffed_img,border=0,command=relaped_click)
    not_relapsed_button = Button(frame_ask,cursor="hand2",image=free_img,border=0,command=no_button_click)

    top.place(relx=.5,rely=.16,anchor=CENTER,relwidth=1)
    not_relapsed_button.place(relx=.27,rely=.6,anchor=CENTER)
    relapsed_button.place(relx=.73,rely=.6,anchor=CENTER)
    
    frame_ask.place(relheight=1,relwidth=1)


def start():
    data = {}
    data[key_lastly_opened] = data[key_start_time] =  datetime.now()
    data[key_lastly_relapsed] = data[key_lastly_noted_change] = data[key_lastly_noted_side_effect] = data[key_next_step] = "Not Found"
    data[key_replace_habits] = OrderedDict() # { habit :{show_at:int,days_data:{}}}
    data[key_plot_accuracy] = {"date":[],"value":[]}
    data[key_last_accuracy_percent] = 0
    data[key_positive_effects] = {}
    data[key_negative_Effects] = {}
    data[key_next_steps] = {}
    data[key_positive_effects+" list"] = []
    data[key_negative_Effects+" list"] = []
    data[key_next_steps+" list"] = []
    
    return data


def get_database_data():
    global data

    data = start()

    data_base = User.get_database_reference()
    data_net_database = data_base.child(user.uid).get().val()

    if data_net_database is None:
        return

    lastly_opened = data_net_database[key_lastly_opened]
    lastly_relapsed = data_net_database[key_lastly_relapsed]
    start_time = data_net_database[key_start_time]
    data_net_database[key_lastly_opened] = dict_to_datatime(lastly_opened)
    data_net_database[key_lastly_relapsed] = dict_to_datatime(lastly_relapsed)
    data_net_database[key_start_time] = dict_to_datatime(start_time)

    data.update(data_net_database)


def dict_to_datatime(dict):
    if type(dict)==str:
        return dict

    day = dict["day"]
    hour = dict["hour"]
    minute = dict["minute"]
    month = dict["month"]
    year = dict["year"]
    second = dict["second"]

    return datetime(day=day,hour=hour,minute=minute,month=month,year=year,second=second)



data_base = None

frames_thread = Thread(target = lambda :[get_frames(gif_path_connecting,frames_connecting)])
frames_thread.start()


def connect():
    global user

    if isfile(app_data):   
        canvas = Canvas()
        canvas.create_image((root.winfo_width()-loading_image.width())//2,(root.winfo_height()-loading_image.height())//2,image=loading_image,anchor=NW)
        canvas.pack(expand=1,fill=BOTH)

        frames_thread.join()

        # print(frames_connecting)

        canvas.destroy()

        canvas = show_gif(root,frames_connecting)
        login_data = data_file(path=app_data)
        email = login_data["email"]
        password = login_data["password"]
        user = User(username=None,email=email,password=password,name=None,last_name=None)
        (success,msg) = user.login_with_email(password)
        if success:
            get_database_data()
            ask_frame_window()

        else:
            logout()

        canvas.destroy()


    else:
        print("user data not found")
        login_window()



connect_thread = Thread(target=connect)
update_thread = Thread(target=check_version)

connect_thread.start()
update_thread.start()


       
open_menu = Menu(root,tearoff=0,font=("Times New Roman",12))

# menu_open_file = Menu(open_menu,tearoff=0,font=("Times New Roman",12))
# menu_open_file.add_command(label="Notes",command = lambda : system(f"explorer.exe {txt_notes}"))
# menu_open_file.add_command(label="Next Steps",command = lambda : system(f"explorer.exe {txt_next_step}"))
# menu_open_file.add_command(label="Positive effects",command = lambda : system(f"explorer.exe {txt_changes}"))
# menu_open_file.add_command(label="Negative effects",command = lambda : system(f"explorer.exe {txt_effects}"))

# menu_open_folder = Menu(open_menu,tearoff=0,font=("Times New Roman",12))
# menu_open_folder.add_command(label="bgm",command = lambda : system(f"explorer.exe {bgm_folder}"))
# menu_open_folder.add_command(label="text",command = lambda : system(f"explorer.exe text"))

# open_menu.add_cascade(label="File",menu=menu_open_file)
# open_menu.add_cascade(label="Folder",menu=menu_open_folder) 

settings_menu = Menu(root,tearoff=0,font=("Times New Roman",12))
settings_menu.add_command(label="Add songs",command=add_songs)  
settings_menu.add_command(label="Run on start",command=run_on_start)

settings_menu.add_command(label="Remove replace habits",command=change_replace_habits) 
settings_menu.add_command(label="Reset",command=reset)
settings_menu.add_command(label="Logout",command=logout)

contact_developer_menu = Menu(root,tearoff=0,font=("Times New Roman",12))

youtube_menu = Menu(contact_developer_menu,tearoff=0,font=("Times New Roman",12))
youtube_menu.add_command(label="Coding",command=lambda : open_new_tab(yt_coding_channel_link))
youtube_menu.add_command(label="Info & Fun",command = lambda : open_new_tab(yt_personal_channel))

contact_developer_menu.add_command(label="Instagram",command= lambda : contact_developer("Instagram"))
contact_developer_menu.add_command(label="Linked In",command= lambda : contact_developer("Linked In"))
contact_developer_menu.add_command(label="Github",command= lambda : contact_developer("Github"))
contact_developer_menu.add_command(label="Facebook",command= lambda : contact_developer("FaceBook"))
contact_developer_menu.add_cascade(label="Youtube",menu=youtube_menu)

email_menu = Menu(contact_developer_menu,tearoff=0,font=("Times New Roman",12))
email_menu.add_command(label="copy Mail ID",command=lambda : contact_developer("Email"))
contact_developer_menu.add_cascade(label="Email",menu=email_menu)

main_menu = Menu(root,tearoff=0,font=("Times New Roman",12))  
# main_menu.add_cascade(label="Open",menu=open_menu)

main_menu.add_cascade(label="Settings",menu=settings_menu)
main_menu.add_command(label="Show plot",command=show_plot)
main_menu.add_command(label="Open in Github",command=lambda : open_new_tab(git_link))
main_menu.add_cascade(label="Developer Contact",menu=contact_developer_menu)  

root.bind("<Button-3>",show_main_menu)
root.protocol("WM_DELETE_WINDOW",on_window_close)
root.mainloop()