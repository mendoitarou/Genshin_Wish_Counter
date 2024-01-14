import sys,os
import tkinter, tkinter.filedialog, tkinter.messagebox, tkinter.simpledialog
import json

# initializetion
title = "No Title."
wish_type = 'character'
character_ceiling_count = 90
character_pu_ceiling_count = 180
weapon_ceiling_count = 80
weapon_pu_ceiling_count = 240
all_count = 0
now_count = 0
count_ceiling = character_ceiling_count - all_count
file_path = ""

# File_Load_Setup
fTyp = [("Genshin Wish Counter Save File","*.gwcsf")]
iDir = os.path.abspath(os.path.dirname(__file__))

def File_Load(event):
    global now_count,all_count,count_ceiling,file_path
    #print("FileLoad!")
    file_path = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    if file_path != '':
        f = open(file_path, "r", encoding="utf-8_sig")
        load_json = json.load(f)
        title = load_json["title"]
        wish_type = load_json["wish_type"]
        all_count = load_json["all_count"]
        now_count = load_json["now_count"]
        # Update_Contents
        if wish_type == 'character':
            Counter_Title["text"] = f'{title}(キャラガチャ)'
        if wish_type == 'weapon':
            Counter_Title["text"] = f'{title}(武器ガチャ)'
        if wish_type == 'character':
            count_ceiling = character_ceiling_count - all_count
        if wish_type == 'weapon':
            count_ceiling = weapon_ceiling_count - all_count
        full_counter["text"] = f'{count_ceiling}'
        all_counter["text"] = f'{all_count}'
        now_counter["text"] = f'{now_count}'
        tkinter.messagebox.showinfo('Genshin Wish Counter','ファイルを読み込みました。')
    else:
        tkinter.messagebox.showinfo('Genshin Wish Counter','ファイルを読み込みませんでした。')

# File_Save
def File_Save(event):
    #print("File_Save")
    file_path = tkinter.filedialog.asksaveasfilename(filetypes = [("Genshin Wish Counter Save File", ".gwcsf")],defaultextension = "gwcsf")
    if file_path != '':
        write_json = {}
        write_json["title"] = title
        write_json["wish_type"] = wish_type
        write_json["all_count"] = all_count
        write_json["now_count"] = now_count
        f2 = open(file_path, "w", encoding="utf-8_sig")
        json.dump(write_json,f2)
        tkinter.messagebox.showinfo('Genshin Wish Counter','ファイルを保存しました。')
    else:
        tkinter.messagebox.showinfo('Genshin Wish Counter','ファイルを保存しませんでした。')

# Wish_Type_Change
def Wish_Type_Change(event):
    global title,wish_type
    #print("Wish_Type_Change")
    response = tkinter.messagebox.askyesno('Genshin Wish Counter', u'ガチャ種類変更\nキャラガチャの場合: はい\n武器ガチャの場合: いいえ\nを選択してください。')
    if response != None:
        if response == True:
            wish_type = 'character'
        if response == False:
            wish_type = 'weapon'
        if wish_type == 'character':
            Counter_Title["text"] = f'{title}(キャラガチャ)'
        if wish_type == 'weapon':
            Counter_Title["text"] = f'{title}(武器ガチャ)'
        if wish_type == 'character':
            count_ceiling = character_ceiling_count - all_count
        if wish_type == 'weapon':
            count_ceiling = weapon_ceiling_count - all_count
        full_counter["text"] = f'{count_ceiling}'
            

#Title_Edit
def Title_Edit(event):
    global title
    #print("Title_Edit!")
    input_title = tkinter.simpledialog.askstring('Genshin Wish Counter', 'タイトルを入力してください。')
    #print(input_title)
    if input_title != None:
        title = input_title
        if wish_type == 'character':
            Counter_Title["text"] = f'{title}(キャラガチャ)'
        if wish_type == 'weapon':
            Counter_Title["text"] = f'{title}(武器ガチャ)'
        tkinter.messagebox.showinfo('Genshin Wish Counter','変更しました。')
    else:
        tkinter.messagebox.showinfo('Genshin Wish Counter','変更しませんでした。')

# Counter_Change
def counter_change_1up(event):
    global now_count,all_count,count_ceiling
    now_count = now_count + 1
    all_count = all_count + 1
    if wish_type == 'character':
        if all_count < 90:
            full_counter_Title["text"] = '星5天井まで残り回数'
            count_ceiling = character_ceiling_count - all_count
        else:
            full_counter_Title["text"] = 'PU天井まで残り回数'
            count_ceiling = character_pu_ceiling_count - all_count
    if wish_type == 'weapon':
        if all_count < 90:
            full_counter_Title["text"] = '星5天井まで残り回数'
            count_ceiling = weapon_ceiling_count - all_count
        else:
            full_counter_Title["text"] = 'PU天井まで残り回数'
            count_ceiling = weapon_pu_ceiling_count - all_count
    full_counter["text"] = f'{count_ceiling}'
    all_counter["text"] = f'{all_count}'
    now_counter["text"] = f'{now_count}'

def counter_change_10up(event):
    global now_count,all_count,count_ceiling
    now_count = now_count + 10
    all_count = all_count + 10
    if wish_type == 'character':
        if all_count < 90:
            full_counter_Title["text"] = '星5天井まで残り回数'
            count_ceiling = character_ceiling_count - all_count
        else:
            full_counter_Title["text"] = 'PU天井まで残り回数'
            count_ceiling = character_pu_ceiling_count - all_count
    if wish_type == 'weapon':
        if all_count < 90:
            full_counter_Title["text"] = '星5天井まで残り回数'
            count_ceiling = weapon_ceiling_count - all_count
        else:
            full_counter_Title["text"] = 'PU天井まで残り回数'
            count_ceiling = weapon_pu_ceiling_count - all_count
    full_counter["text"] = f'{count_ceiling}'
    all_counter["text"] = f'{all_count}'
    now_counter["text"] = f'{now_count}'

def counter_change_1down(event):
    global now_count,all_count,count_ceiling
    now_count = now_count - 1
    all_count = all_count - 1
    if wish_type == 'character':
        if all_count < 90:
            full_counter_Title["text"] = '星5天井まで残り回数'
            count_ceiling = character_ceiling_count - all_count
        else:
            full_counter_Title["text"] = 'PU天井まで残り回数'
            count_ceiling = character_pu_ceiling_count - all_count
    if wish_type == 'weapon':
        if all_count < 90:
            full_counter_Title["text"] = '星5天井まで残り回数'
            count_ceiling = weapon_ceiling_count - all_count
        else:
            full_counter_Title["text"] = 'PU天井まで残り回数'
            count_ceiling = weapon_pu_ceiling_count - all_count
    full_counter["text"] = f'{count_ceiling}'
    all_counter["text"] = f'{all_count}'
    now_counter["text"] = f'{now_count}'

def counter_change_10down(event):
    global now_count,all_count,count_ceiling
    now_count = now_count - 10
    all_count = all_count - 10
    if wish_type == 'character':
        if all_count < 90:
            full_counter_Title["text"] = '星5天井まで残り回数'
            count_ceiling = character_ceiling_count - all_count
        else:
            full_counter_Title["text"] = 'PU天井まで残り回数'
            count_ceiling = character_pu_ceiling_count - all_count
    if wish_type == 'weapon':
        if all_count < 90:
            full_counter_Title["text"] = '星5天井まで残り回数'
            count_ceiling = weapon_ceiling_count - all_count
        else:
            full_counter_Title["text"] = 'PU天井まで残り回数'
            count_ceiling = weapon_pu_ceiling_count - all_count
    full_counter["text"] = f'{count_ceiling}'
    all_counter["text"] = f'{all_count}'
    now_counter["text"] = f'{now_count}'

def counter_reset(event):
    global now_count,all_count,count_ceiling
    now_count = 0
    all_count = 0
    if wish_type == 'character':
        full_counter_Title["text"] = '星5天井まで残り回数'
        count_ceiling = character_ceiling_count - all_count
    if wish_type == 'weapon':
        full_counter_Title["text"] = '星5天井まで残り回数'
        count_ceiling = weapon_ceiling_count - all_count
    full_counter["text"] = f'{count_ceiling}'
    all_counter["text"] = f'{all_count}'
    now_counter["text"] = f'{now_count}'

root = tkinter.Tk()

root.title(u"Genshin Wish Counter")
root.geometry("330x200")
root.resizable(width=False,height=False)# ウィンドウサイズ固定

# Counter_Title
Counter_Title = tkinter.Label(text=f'{title}')
Counter_Title.place(x=0,y=0)#画面左端

# File_Load_Button
File_Load_Button = tkinter.Button(text=u'ファイル読み込み')
File_Load_Button.bind("<Button-1>",File_Load)
File_Load_Button.place(x=5,y=140)#画面右端

# File_Save_Button
File_Save_Button = tkinter.Button(text=u'ファイル保存')
File_Save_Button.bind("<Button-1>",File_Save)
File_Save_Button.place(x=100,y=140)

# Wish_Type_Change_Button
Wish_Type_Change_Button = tkinter.Button(text=u'ガチャ種類変更')
Wish_Type_Change_Button.bind("<Button-1>",Wish_Type_Change)
Wish_Type_Change_Button.place(x=5,y=170)

# Title_Edit_Button
Title_Edit_Button = tkinter.Button(text=u'タイトル変更')
Title_Edit_Button.bind("<Button-1>",Title_Edit)
Title_Edit_Button.place(x=100,y=170)

# Counter_Show
full_counter_Title = tkinter.Label(text=u'星5天井まで残り回数')
full_counter = tkinter.Label(text=f'{count_ceiling}')
all_counter_Title = tkinter.Label(text=u'累計回数')
all_counter = tkinter.Label(text=f'{all_count}')
now_counter_Title = tkinter.Label(text=u'現在回数')
now_counter = tkinter.Label(text=f'{now_count}')

full_counter_Title.place(x=15,y=30)
all_counter_Title.place(x=160,y=30)
now_counter_Title.place(x=255,y=30)
full_counter.place(x=60,y=50)
all_counter.place(x=180,y=50)
now_counter.place(x=275,y=50)

# Counter_Button
counter_up_down_Text = tkinter.Label(text=u'現在回数変更: ')
counter_1_up_Button = tkinter.Button(text=u'+1')
counter_1_up_Button.bind("<Button-1>",counter_change_1up)
counter_10_up_Button = tkinter.Button(text=u'+10')
counter_10_up_Button.bind("<Button-1>",counter_change_10up)
counter_1_down_Button = tkinter.Button(text=u'-1')
counter_1_down_Button.bind("<Button-1>",counter_change_1down)
counter_10_down_Button = tkinter.Button(text=u'-10')
counter_10_down_Button.bind("<Button-1>",counter_change_10down)
counter_reset_Button = tkinter.Button(text=u'リセット')
counter_reset_Button.bind("<Button-1>",counter_reset)

counter_up_down_Text.place(x=0,y=70)
counter_1_down_Button.place(x=10,y=90)
counter_1_up_Button.place(x=40,y=90)
counter_10_down_Button.place(x=80,y=90)
counter_10_up_Button.place(x=115,y=90)
counter_reset_Button.place(x=155,y=90)

root.mainloop()