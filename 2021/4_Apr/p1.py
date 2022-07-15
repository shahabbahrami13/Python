import tkinter as tk
def inc():
    global count
    count+=1    
    lb.config(text=str(count))
    if count>=0:
        lb.config(bg='#FF0000')
##    print('increase',count)
    
def dec():
    global count
    count-=1
    lb.config(text=str(count))
    if count<0:
        lb.config(bg='blue')
##    print('decrease',count)
    
count=0

top=tk.Tk()
top.title('شمارنده')

top.geometry('600x800+100+100')
top.config(bg='purple')
top.config(bg='#AA00AA')
top.config(bg='#33FFFF')

lb=tk.Label(master=top,
            text="Hello",
            bg='blue',
            fg='yellow',
            padx=50,
            pady=10,
            font=('arial',20,'bold'))
lb.pack(side=tk.TOP)

frBtn=tk.Frame()
frBtn.pack(side=tk.TOP)

btDec=tk.Button(master=frBtn,
            text="کاهش",
            bg='gray',
            fg='black',
            padx=50,
            pady=10,
            font=('arial',20,'bold'),
            command=dec    )

btDec.pack(side='left')

btInc=tk.Button(master=frBtn,
            text="افزايش",
            bg='gray',
            fg='white',
            padx=50,
            pady=10,
            font=('arial',20,'bold'),
            command=inc)

btInc.pack(side='right')

##lb1=tk.Label(master=top1,
##            text="How are u?",
##            bg='yellow',
##            fg='Blue',
##            font=('arial',20,'bold'))
##lb1.pack(side='left')
##


top.mainloop()
