#Creating radio button
from tkinter import*
root = Tk()
root.title("Title Here")
#This is function
def callback():
    print("Click")
b1 = Button(root, text="One", command=callback)
b2 = Button(root, text="Two", command=callback)
b3 = Button(root, text="Three", command=callback)
b4 = Button(root, text="Four", command=callback)
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=0)
b4.grid(row=1, column=1)
root.mainloop()
