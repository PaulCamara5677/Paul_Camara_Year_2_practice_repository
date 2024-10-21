from tkinter import *
root = Tk()
root.title("First App")
root.geometry("400x200")
1 = Label(root, text = "Hello!",
          fg="red"
          bg="#FFFFFF"
          font=('Roboto',25))
1.pack()
11 = Label(root, text = "My name is Paul Yram Barolome Camara",
           fg="Blue",
           bg="#FFFFFF",
           font=('Roboto',10))
11.pack()
12 = Label(root, text="I am studying in Bath Spa University Ras Al Khaimah Education Zone Campus",
           fg="#FFFFFF", bg="#000000" , font=('Roboto',8))
12.pack()
Label(root, text="Check buttons to select multiple options.").pack()
C1 = Checkbutton(root, text = "Gaming")
C2 = Checkbutton(root, text = "Video editing")
C1.pack(anchor = W )
C2.pack(anchor = W )
root.mainloop
        