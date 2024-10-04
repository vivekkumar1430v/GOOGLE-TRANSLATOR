from tkinter import *
from tkinter import ttk 
# ttkcombo box ko lati hai
from googletrans import translator,LANGUAGES


def change  (
    text="type",
    src="english",
    dest="hindi",):
    
    text1=text
    sec1=src
    dest1=dest
    trans=translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text
def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg =sor_txt.get(1.0,END )
    textget= change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root =Tk()
root.title("translator")
root.geometry("500x700")
root.config(bg='skyblue')

lab_txt=Label(root,text="translator",font=("time new roman",40,bold),bg=yellow)
lab_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="source Text",font=("time new roman",20,bold),fg=Black,bg=Green)
lab_txt.place(x=100,y=100,height=20,width=300)

sor_txt=Text(frame,font=("time new roman",20,bold),wrap=WORD)
sor_txt.place(x=10,y=130,height=150,width=480)

list_text =list[LANGUAGES.values()]

comb_sor =ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=100)
comb_sor.set("english")

button_change= Button(frame,text="translate",relief=RAISED,command=data)
comb_sor.place(x=120,y=300,height=40,width=100)

comb_dest =ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=100)
comb_dest.set("HINDI")

lab_txt=Label(root,text="source Text",font=("time new roman",20,bold),fg=Black,bg=Green)
lab_txt.place(x=100,y=100,height=20,width=300)

dest_txt=Text(frame,font=("time new roman",20,bold),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)





root.mainlook()