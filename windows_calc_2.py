#imports here
from math import*
from tkinter import *
from PIL import ImageTk, Image, ImageEnhance




root = Tk()
root.title("Calc bright")


e = Entry(root, width=50, borderwidth=0)
e.grid(row=0, column=0, columnspan=4, padx=60, pady=40)

# Defining each button function
def button_action(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))



def button_clear():
    e.delete(0, END)

def button_add():
    global f_num
    global math
    math = "addition"
    f_num = int(e.get())
    e.delete(0, END)

def button_subtract():
    global f_num
    global math
    math = "subtraction"
    f_num = int(e.get())
    e.delete(0, END)

def button_multiply():
    global f_num
    global math
    math = "multiplication"
    f_num = int(e.get())
    e.delete(0, END)

def button_divide():
    global f_num
    global math
    math = "division"
    f_num = int(e.get())
    e.delete(0, END)

def button_mod():
    global f_num
    global math
    math = "modulation"
    f_num = int(e.get())
    e.delete(0, END)

def button_power():
    global f_num
    global math
    math = "power"
    f_num = int(e.get())
    e.delete(0, END)

def button_sqrt():
    global f_num
    global math
    try:
        number = float(e.get()) 
        e.delete(0, END)  
        e.insert(0, sqrt(number)) 
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

def button_factorial():
    try:
        number = int(e.get())
        e.delete(0, END)
        e.insert(0, factorial(number))  
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")


# Equal button function
def button_equal():
    try:
        second_num = float(e.get())
        e.delete(0, END)

        if math == "addition":
            e.insert(0, f_num + second_num)
        elif math == "subtraction":
            e.insert(0, f_num - second_num)
        elif math == "multiplication":
            e.insert(0, f_num * second_num)
        elif math == "division":
            if second_num == 0:
                e.insert(0, "Error ") 
            else:
                e.insert(0, f_num / second_num)
        elif math == "modulation":
            e.insert(0, f_num % second_num)
        elif math == "power":
            e.insert(0, f_num ** second_num)
        elif math == "square root":
            e.insert(0, sqrt(f_num))  
    except ValueError:
        e.insert(0, "Error ")

  

#resizing and loading images
def load_image(file_name, enhancement_factor=1.5):


    image = Image.open(file_name).resize((60,40))
    original_img = ImageTk.PhotoImage(image)

    enhancer = ImageEnhance.Brightness(image)  
    brightened_img = ImageTk.PhotoImage(enhancer.enhance(enhancement_factor))  
    return original_img, brightened_img


def on_enter(event, button, brightened_img):
    button.config(image = brightened_img)



def on_leave(event, button, original_img):
    button.config(image = original_img)




# Load images for buttons
one_img, one_img_bright = load_image('1_btn.png',enhancement_factor=1.5)

two_img, two_img_bright = load_image('2_btn.png',enhancement_factor=1.5)

three_img, three_img_bright = load_image('3_btn.png',enhancement_factor=1.5)

four_img, four_img_bright = load_image('4_btn.png',enhancement_factor=1.5)

five_img, five_img_bright = load_image('5_btn.png',enhancement_factor=1.5)

six_img, six_img_bright = load_image('6_btn.png',enhancement_factor=1.5)

seven_img, seven_img_bright = load_image('7_btn.png',enhancement_factor=1.5)

eight_img, eight_img_bright = load_image('8_btn.png',enhancement_factor=1.5)

nine_img, nine_img_bright = load_image('9_btn.png',enhancement_factor=1.5)

zero_img, zero_img_bright = load_image('0_btn.png',enhancement_factor=1.5)

add_img, add_img_bright = load_image('add_btn.png',enhancement_factor=1.5)

sub_img, sub_img_bright = load_image('sub_btn.png',enhancement_factor=1.5)

equal_img, equal_img_bright = load_image('equal_btn.png',enhancement_factor=1.5)

multi_img, multi_img_bright = load_image('multi_btn.png',enhancement_factor=1.5)

div_img, div_img_bright = load_image('div_btn.png',enhancement_factor=1.5)

mod_img, mod_img_bright = load_image('mod_btn.png',enhancement_factor=1.5)

pwr_img, pwr_img_bright = load_image('x_pwr_y.png',enhancement_factor=1.5)

sqrt_img, sqrt_img_bright = load_image('sqrt_btn.png',enhancement_factor=1.5)

clear_img, clear_img_bright = load_image('clear_btn.png',enhancement_factor=1.5)

factorial_img, factorial_img_bright = load_image('factorial_btn.png',enhancement_factor=1.5)

# Create and place buttons
button_1 = Button(root, image=one_img, padx=40, pady=20, command=lambda: button_action(1))
button_2 = Button(root, image=two_img, padx=40, pady=20, command=lambda: button_action(2))
button_3 = Button(root, image=three_img, padx=40, pady=20, command=lambda: button_action(3))
button_4 = Button(root, image=four_img, padx=40, pady=20, command=lambda: button_action(4))
button_5 = Button(root, image=five_img, padx=40, pady=20, command=lambda: button_action(5))
button_6 = Button(root, image=six_img, padx=40, pady=20, command=lambda: button_action(6))
button_7 = Button(root, image=seven_img, padx=40, pady=20, command=lambda: button_action(7))
button_8 = Button(root, image=eight_img, padx=40, pady=20, command=lambda: button_action(8))
button_9 = Button(root, image=nine_img, padx=40, pady=20, command=lambda: button_action(9))
button_0 = Button(root, image=zero_img, padx=40, pady=20, command=lambda: button_action(0))

button_add = Button(root, image=add_img, padx=39, pady=20, command=button_add)
button_equal = Button(root, image=equal_img, padx=39, pady=20, command=button_equal)
button_clear = Button(root, image=clear_img, padx=39, pady=20, command=button_clear)
button_sub = Button(root, image=sub_img, padx=40, pady=20, command=button_subtract)
button_multi = Button(root, image=multi_img, padx=40, pady=20, command=button_multiply)
button_div = Button(root, image=div_img, padx=39, pady=20, command=button_divide)
button_mod = Button(root, image=mod_img, padx=39, pady=20, command=button_mod)
button_pwr = Button(root, image=pwr_img, padx=39, pady=20, command=button_power)
sqrt_button = Button(root, image=sqrt_img, padx=39, pady=20, command=button_sqrt)
clear_button = Button(root, image=clear_img, padx=39, pady=20, command=button_clear)
factorial_button = Button(root, image=factorial_img, padx=39, pady=20, command=button_factorial)


#Brightening buttons on events
button_1.bind("<Enter>", lambda event: on_enter(event, button_1, one_img_bright))
button_1.bind("<Leave>", lambda event: on_leave(event, button_1, one_img))

button_2.bind("<Enter>", lambda event: on_enter(event, button_2, two_img_bright))
button_2.bind("<Leave>", lambda event: on_leave(event, button_2, two_img))

button_3.bind("<Enter>", lambda event: on_enter(event, button_3, three_img_bright))
button_3.bind("<Leave>", lambda event: on_leave(event, button_3, three_img))

button_4.bind("<Enter>", lambda event: on_enter(event, button_4, four_img_bright))
button_4.bind("<Leave>", lambda event: on_leave(event, button_4, four_img))

button_5.bind("<Enter>", lambda event: on_enter(event, button_5, five_img_bright))
button_5.bind("<Leave>", lambda event: on_leave(event, button_5, five_img))

button_6.bind("<Enter>", lambda event: on_enter(event, button_6, six_img_bright))
button_6.bind("<Leave>", lambda event: on_leave(event, button_6, six_img))

button_7.bind("<Enter>", lambda event: on_enter(event, button_7, seven_img_bright))
button_7.bind("<Leave>", lambda event: on_leave(event, button_7, seven_img))

button_8.bind("<Enter>", lambda event: on_enter(event, button_8, eight_img_bright))
button_8.bind("<Leave>", lambda event: on_leave(event, button_8, eight_img))

button_9.bind("<Enter>", lambda event: on_enter(event, button_9, nine_img_bright))
button_9.bind("<Leave>", lambda event: on_leave(event, button_9, nine_img))

button_0.bind("<Enter>", lambda event: on_enter(event, button_0, zero_img_bright))
button_0.bind("<Leave>", lambda event: on_leave(event, button_0, zero_img))

button_add.bind("<Enter>", lambda event: on_enter(event, button_add, add_img_bright))
button_add.bind("<Leave>", lambda event: on_leave(event, button_add, add_img))

button_sub.bind("<Enter>", lambda event: on_enter(event, button_sub, sub_img_bright))
button_sub.bind("<Leave>", lambda event: on_leave(event, button_sub, sub_img))

button_equal.bind("<Enter>", lambda event: on_enter(event, button_equal, equal_img_bright))
button_equal.bind("<Leave>", lambda event: on_leave(event, button_equal, equal_img))

button_multi.bind("<Enter>", lambda event: on_enter(event, button_multi, multi_img_bright))
button_multi.bind("<Leave>", lambda event: on_leave(event, button_multi, multi_img))

button_div.bind("<Enter>", lambda event: on_enter(event, button_div, div_img_bright))
button_div.bind("<Leave>", lambda event: on_leave(event, button_div, div_img))

button_mod.bind("<Enter>", lambda event: on_enter(event, button_mod, mod_img_bright))
button_mod.bind("<Leave>", lambda event: on_leave(event, button_mod, mod_img))

button_pwr.bind("<Enter>", lambda event: on_enter(event, button_pwr, pwr_img_bright))
button_pwr.bind("<Leave>", lambda event: on_leave(event, button_pwr, pwr_img))

sqrt_button.bind("<Enter>", lambda event: on_enter(event, sqrt_button, sqrt_img_bright))
sqrt_button.bind("<Leave>", lambda event: on_leave(event, sqrt_button, sqrt_img))

button_clear.bind("<Enter>", lambda event: on_enter(event, button_clear, clear_img_bright))
button_clear.bind("<Leave>", lambda event: on_leave(event, button_clear, clear_img))

factorial_button.bind("<Enter>", lambda event: on_enter(event, factorial_button, factorial_img_bright))
factorial_button.bind("<Leave>", lambda event: on_leave(event, factorial_button, factorial_img))





button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)


button_add.grid(row=1, column=3)
button_equal.grid(row=4, column=3)
button_clear.grid(row=1, column=0)
button_sub.grid(row=2, column=3)
button_multi.grid(row=3, column=3)
button_div.grid(row=1, column=2)
button_mod.grid(row=1, column=1)
button_pwr.grid(row=5, column=0)
sqrt_button.grid(row=5, column=2)
factorial_button.grid(row=5, column=3)


#looping the shit out of it
root.mainloop()
