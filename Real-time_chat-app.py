import socket
import time
import threading
from tkinter import *
 
root=Tk()
root.geometry("300x500")
root.config(bg="black")
 
def func():
    t=threading.Thread(target=recv)
    t.start()
 
 
def recv():
    listensocket=socket.socket()
    port=3050
    maxconnection=99
    ip=socket.gethostname()
    print(ip)
 
    listensocket.bind(('',port))
    listensocket.listen(maxconnection)
    (clientsocket,address)=listensocket.accept()
     
    while True:
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            lstbx.insert(0,"Client : "+sendermessage)
 
 
s=0
 
def sendmsg():
    global s
    if s==0:
        s=socket.socket()
        hostname='LAPTOP-60E7NCMJ'
        port=4050
        s.connect((hostname,port))
        msg=messagebox.get()
        lstbx.insert(0,"You : "+msg)
        s.send(msg.encode())
    else:
        msg=messagebox.get()
        lstbx.insert(0,"You : "+msg)
        s.send(msg.encode())
 
 
def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()
 
 
 
 
startchatimage=PhotoImage(file='start.png')
 
buttons=Button(root,image=startchatimage,command=func,borderwidth=0)
buttons.place(x=90,y=10)
 
message=StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
messagebox.place(x=10,y=444)
 
sendmessageimg=PhotoImage(file='send.png')
 
sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
sendmessagebutton.place(x=260,y=440)
 
lstbx=Listbox(root,height=20,width=43)
lstbx.place(x=15,y=80)
 
user_name = Label(root,text =" Number" ,width=10)
 
root.mainloop()

'''
1) This works if both system are connected on same network
2) python script on the second system will have exactly the same code except 
port number in computer 1 receive connection = port number in sending section of computer 2 , 
port number in computer 2 receive connection = port number in sending section of computer 1 
hostname in computer 2 sending = ip variable in computer 1 script  ,
hostname in computer 1 sending = ip variable in computer 2 script'''
