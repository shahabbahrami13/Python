import tkinter as tk
def inc():
    global count
    count=(count+10)%256    
    lb.config(text=str(count),
              bg=f'#{count:02x}0000')
    
def dec():
    global count
    count=(count-10)%256
    lb.config(text=str(count),
              bg=f'#{count:02x}0000')

count=0

top=tk.Tk()
top.title('شمارنده')

top.geometry('500x300+200+200')
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
