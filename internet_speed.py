from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps"
    up = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title(" Internet Speed Test ")

sp.config(bg="blue")
sp.geometry("600x800")

Lab = Label(sp,text= " Internet Speed Test", font=(" Time New Roman", 40,"bold"), bg="blue",fg="white")
Lab.place(x=50,y=40,height =50,width=500)

Lab = Label(sp,text= " Download Speed ", font=(" Time New Roman", 40,"bold"))
Lab.place(x=50,y=130,height =50,width=500)

Lab_down = Label(sp,text= " 10 ", font=(" Time New Roman", 40,"bold"))
Lab_down.place(x=50,y=200,height =50,width=500)

Lab = Label(sp,text= " Upload Speed ", font=(" Time New Roman", 40,"bold"))
Lab.place(x=50,y=290,height =50,width=500)

Lab_up = Label(sp,text= " 20 ", font=(" Time New Roman", 40,"bold"))
Lab_up.place(x=50,y=360,height =50,width=500)

button = Button(sp,text ="Check Speed ",font=(" Time New Roman", 40,"bold"),relief=RAISED,bg = "red",command=speedcheck)
button.place(x=50,y=460,height =50,width=500)


sp.mainloop()