import tkinter as tk
def f():
    print(v.get(),vIDE.get())
root = tk.Tk()

v = tk.StringVar()
v.set("Perl")

vIDE = tk.StringVar()
vIDE.set("EClipse")


frLng=tk.Frame(master=root)
frLng.pack(anchor=tk.W)

tk.Label(frLng, 
        text="""Choose a 
programming language:""",
        justify = tk.LEFT,
        padx = 20,
        font=(30,), 
         ).pack()

tk.Radiobutton(frLng, 
               text="Python",
               padx = 20, 
               variable=v, 
               font=(30,),
               command=f,
               indicatoron=0,
               width=20,
               value="Python").pack(anchor=tk.SW)

tk.Radiobutton(frLng, 
               text="Perl",
               padx = 20, 
               variable=v, 
               font=(30,),
               command=f,
               indicatoron=0,
               width=20,
               value="Perl").pack(anchor=tk.SW)

tk.Radiobutton(frLng, 
               text="Java",
               padx = 20, 
               variable=v, 
               font=(30,),
               command=f,
               indicatoron=0,
               width=20,
               value="Java").pack(anchor=tk.SW)

frIDE=tk.Frame(master=root)
frIDE.pack(anchor=tk.W)


tk.Label(frIDE, 
        text="""Choose an IDE:""",
        justify = tk.LEFT,
        padx = 20,
        font=(30,), 
         ).pack()

tk.Radiobutton(frIDE, 
               text="VS Code",
               padx = 20, 
               variable=vIDE, 
                font=(30,),
               command=f,
               value="VS Code").pack(anchor=tk.SW)

tk.Radiobutton(frIDE, 
               text="EClipse",
               padx = 20, 
               variable=vIDE, 
               font=(30,),
               command=f,
               value="EClipse").pack(anchor=tk.SW)


root.mainloop()
