import tkinter as tk
def f():
    print(var1.get())

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))
   
master = tk.Tk()
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var1.set(True)
tk.Checkbutton(master, text="male", variable=var1,
               command=f).grid(row=0, sticky=tk.W)
tk.Checkbutton(master, text="female", variable=var2).grid(row=1, sticky=tk.W)

tk.Button(master, text='Quit',
          command=master.destroy).grid(row=3, sticky=tk.W, pady=4)
tk.Button(master, text='Show',
          command=var_states).grid(row=4, sticky=tk.W, pady=4)

tk.mainloop()
