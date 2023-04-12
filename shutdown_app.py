from tkinter import*
import os                                                               # operate the system

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")    


st=Tk()                                                                 #tk is class and st it's object               
st.title("Shutdown App")                                                #for title
st.geometry("500x500")                                                  # for geometry 
st.config(bg="Red")                                                   # for background colour

r_button = Button(st,text="Restart",font=("Time New Roman",20,"bold"),   #when we use button to call function then use command
                  relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=60,width=200)

rt_button = Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=60,width=200)

lg_button = Button(st,text="Log-out",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=60,width=200)

St_button = Button(st,text="Shutdown",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=shutdown)
St_button.place(x=150,y=370,height=60,width=200)


st.mainloop()                                                           #for graphic