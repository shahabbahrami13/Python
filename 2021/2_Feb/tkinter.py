import tkinter as tk
def f():
    print(var1.get())
master = tk.Tk()
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var1.set(True)
tk.Checkbutton(master, text="male", variable=var1,
               command=f).grid(row=0, sticky=tk.W)
tk.Checkbutton(master, text="female", variable=var2).grid(row=1, sticky=tk.W)
tk.mainloop()


