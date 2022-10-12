from tkinter import *
import math

window = Tk()
window.geometry("312x324")
window.title("Circle Calculator")


data_input = StringVar()

def diameter(*args):
    try:
        data = int(input_field.get())
        diameter_num= 2 * data
        data_input.set(diameter_num)
    except ValueError:
        data_input.set("ERROR!")
        pass
def area(*args):
    try:
        data = int(input_field.get())
        area_num= math.pi * (data ** 2)
        data_input.set(area_num)
    except ValueError:
        data_input.set("ERROR!")
        pass
def perimeter(*args):
    try:
        data = int(input_field.get())
        perimeter_num= 2 * math.pi * data
        data_input.set(perimeter_num)
    except ValueError:
        data_input.set("ERROR!")
        pass
def clear1_btn():
    input_field.delete(0, END)
    output_field.delete(0, END)


conv_frame = Frame(width=312, height=50, bd=0)
conv_frame.pack(side=TOP)
lbl = Label(conv_frame, text = "Enter:", font = ("Verdana", 12))
lbl.grid(row=0, column=0, pady=0, sticky=W)
lbl2 = Label(conv_frame, text = "Result:", font = ("Verdana", 12))
lbl2.grid(row=2, column=0, pady=0, sticky=W)
lbl_rad = Frame(width=312, height=50, bd=0)
lbl_rad.pack()
lblrad =Label(lbl_rad, text = "Radius", font = ("Verdana", 12))
lblrad.grid(row=3, column=0, pady=0,)


input_field = Entry(conv_frame, font=('arial', 18, 'bold'), width=50)
input_field.grid(row=1, column=0, pady=10)
output_field = Entry(conv_frame, font=('arial', 18, 'bold'), width=50, textvariable=data_input)
output_field.grid(row=3, column=0, pady=10)

frame_btn = Frame(width=13, height=3,bg="#7FFFD4")
frame_btn.pack()
area_btn = Button(frame_btn, text="Area", width=13, height=3, bd=0, bg="#00FFFF", command=lambda: area())
area_btn.grid(row=6, column=0, padx=1, pady=1)
perimeter_btn = Button(frame_btn, text="Perimeter", width=13, height=3, bd=0,bg="#00FFFF", command=lambda: perimeter())
perimeter_btn.grid(row=6, column=1, padx=1, pady=1)
diameter_btn = Button(frame_btn, text="Diameter", width=13, height=3, bd=0, bg="#00FFFF", command=lambda: diameter())
diameter_btn.grid(row=6, column=2, padx=1, pady=1)

lbl_rad = Frame(width=312, height=50, bd=0)
lbl_rad.pack()
lblrad = Label(lbl_rad, text = "Diameter", font = ("Verdana", 12))
lblrad.grid(row=8, column=0, pady=0, sticky=W)

def radius(*args):
    try:
        data = int(input_field.get())
        radius_num= data / 2
        data_input.set(radius_num)
    except ValueError:
        data_input.set("ERROR!")
        pass
def area2(*args):
    try:
        data = int(input_field.get())
        area_num2= math.pi *( data * data) / 4
        data_input.set(area_num2)
    except ValueError:
        data_input.set("ERROR!")
        pass
def perimeter2(*args):
    try:
        data = int(input_field.get())
        perimeter_num2= math.pi * data
        data_input.set(perimeter_num2)
    except ValueError:
        data_input.set("ERROR!")
        pass

frame_btn2 = Frame(width=13, height=3,bg="#7FFFD4")
frame_btn2.pack()
radius_btn = Button(frame_btn2, text="Radius", width=13, height=3, bd=0, bg="#00FFFF", command=lambda: radius())
radius_btn.grid(row=10, column=3, padx=1, pady=1)
area_btn2 = Button(frame_btn2, text="Area", width=13, height=3, bd=0, bg="#00FFFF", command=lambda: area2())
area_btn2.grid(row=10, column=0, padx=1, pady=1)
perimeter_btn2 = Button(frame_btn2, text="Perimeter", width=13, height=3, bd=0, bg="#00FFFF", command=lambda: perimeter2())
perimeter_btn2.grid(row=10, column=2, padx=1, pady=1)




window.mainloop()