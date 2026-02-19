import tkinter as tk

root=tk.Tk()
root.title("Calculator")
root.geometry("300x400")

root.configure(bg="black")

display=tk.Entry(root, font=("Arial",20), justify="right", bg="white")
display.grid(row=0, column=0, columnspan=4, pady=10, sticky="we")

def click(value):
    display.insert(tk.END, value)
def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result=eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

buttons=['7','8','9','/',
         '4','5','6','*',
         '1','2','3','-',
         '0','C','=','+']
row=1
col=0
for b in buttons:
    if b.isdigit():
        btn=tk.Button(root, text=b, width=5, height=2, bg="#777777", fg="white", command=lambda x=b: click(x))
    elif b=="C":
        btn=tk.Button(root, text=b, width=5, height=2, bg="#607D8B", fg="white", command=clear)
    elif b=="=":
        btn=tk.Button(root, text=b, width=5, height=2, bg="#607D8B", fg="white", command=calculate)
    else:
        btn=tk.Button(root, text=b, width=5, height=2, bg="#607D8B", fg="white", command=lambda x=b: click(x))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col+=1
    if col>3:
        col=0
        row+=1
root.mainloop()