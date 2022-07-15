from t1 import Time
import datetime
import tkinter as tk
def start():
    def run(t):
        next(t)
        lbHour.config(text=f"{t.hour:02}")
        lbMinute.config(text=f"{t.minute:02}")
        lbSecond.config(text=f"{t.second:02}")
        btStart.after(1000, lambda : run(t))


    now=datetime.datetime.now()
    t=Time(now.hour,
           now.minute,
           now.second)

    btStart.after(1000, lambda : run(t))
    
if __name__=="__main__":
    root=tk.Tk()
    frLb=tk.Frame(master=root)
    frLb.pack()

    lbHour=tk.Label(master=frLb,
                text="HH",
                bg='blue',
                fg='yellow',
##                padx=10,
                pady=10,
                font=('arial',20,'bold'))
    lbHour.pack(side=tk.LEFT)

    tk.Label(master=frLb,
                text=":",
                bg='blue',
                fg='yellow',
##                padx=10,
                pady=10,
                font=('arial',20,'bold')
             ).pack(side=tk.LEFT)

    lbMinute=tk.Label(master=frLb,
                text="MM",
                bg='blue',
                fg='yellow',
##                padx=10,
                pady=10,
                font=('arial',20,'bold'))
    lbMinute.pack(side=tk.LEFT)

    tk.Label(master=frLb,
                text=":",
                bg='blue',
                fg='yellow',
##                padx=10,
                pady=10,
                font=('arial',20,'bold')
             ).pack(side=tk.LEFT)

    lbSecond=tk.Label(master=frLb,
                text="SS",
                bg='blue',
                fg='yellow',
##                padx=10,
                pady=10,
                font=('arial',20,'bold'))
    lbSecond.pack(side=tk.LEFT)

    frBtn=tk.Frame(master=root)
    frBtn.pack()

    btStart=tk.Button(master=frBtn,
                text="شروع",
                bg='gray',
                fg='black',
##                padx=50,
                pady=2,
                font=('arial',20,'bold'),
                command=start,      
                )
    btStart.pack(side='left')

    btExit=tk.Button(master=frBtn,
                text="خروج",
                bg='gray',
                fg='black',
##                padx=50,
                pady=2,
                font=('arial',20,'bold'),
                command=root.destroy)
    btExit.pack(side='left')

    

##    for i in range(60):
##        print(next(t))
    root.mainloop()
