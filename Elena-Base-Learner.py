from tkinter import (
    Tk,
    Canvas,
    Label,
    Entry,
    Button,
    PhotoImage,
    LEFT,
    RIGHT,
    HORIZONTAL,
    VERTICAL,
)
import pygame
from os import path
from tkinter import Button
from PIL import Image, ImageTk
from tkinter import *
from PIL import Image, ImageTk
import pygame

root = Tk()
root.title("Number System Quiz")
root.geometry("1800x900")
root.configure(bg="tan")

pygame.mixer.init()
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play(-1)

score = 0
got_wrong = False


def question1():
    global got_wrong

    got_wrong = False

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question2)

    def wrong():
        global got_wrong
        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 1", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(root, text="What is Binary?", font=("Arial", 40), bg="tan").place(
        x=100, y=200
    )

    Button(
        root,
        text="Base 2 number system that uses 0 and 1",
        command=correct,
        font=("", 20),
    ).place(x=40, y=350, width=675, height=100)

    Button(
        root,
        text="Base 2 number system that uses 1 and 2",
        command=wrong,
        font=("", 20),
    ).place(x=725, y=350, width=675, height=100)

    Button(
        root,
        text="Base 3 number system that uses 0,1,2",
        command=wrong,
        font=("", 20),
    ).place(x=40, y=500, width=675, height=100)

    Button(
        root,
        text="Base 3 number system that uses 1,2,3",
        command=wrong,
        font=("", 20),
    ).place(x=725, y=500, width=675, height=100)


def question2():
    global score, got_wrong

    for widget in root.winfo_children():
        widget.destroy()

    got_wrong = False

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question3)

    def wrong():
        global got_wrong

        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 2", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(
        root, text="How many digits does Binary use?", font=("Arial", 40), bg="tan"
    ).place(x=100, y=200)

    Button(root, text="2", command=correct, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )

    Button(root, text="8", command=wrong, font=("", 20)).place(
        x=725, y=350, width=675, height=100
    )

    Button(root, text="3", command=wrong, font=("", 20)).place(
        x=40, y=500, width=675, height=100
    )

    Button(root, text="10", command=wrong, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def question3():
    global score, got_wrong

    for widget in root.winfo_children():
        widget.destroy()

    got_wrong = False

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question4)

    def wrong():
        global got_wrong

        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 3", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(
        root, text="How many bits are in one byte?", font=("Arial", 40), bg="tan"
    ).place(x=100, y=200)

    Button(root, text="8", command=correct, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )
    Button(root, text="4", command=wrong, font=("", 20)).place(
        x=725, y=350, width=675, height=100
    )
    Button(root, text="2", command=wrong, font=("", 20)).place(
        x=40, y=500, width=675, height=100
    )
    Button(root, text="16", command=wrong, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def question4():
    global score, got_wrong

    for widget in root.winfo_children():
        widget.destroy()

    got_wrong = False

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question5)

    def wrong():
        global got_wrong

        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 4", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(
        root, text="Which digit is NOT used in Binary?", font=("Arial", 40), bg="tan"
    ).place(x=100, y=200)

    Button(root, text="0", command=wrong, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )
    Button(root, text="1", command=wrong, font=("", 20)).place(
        x=725, y=350, width=675, height=100
    )
    Button(root, text="2", command=correct, font=("", 20)).place(
        x=40, y=500, width=675, height=100
    )
    Button(root, text="Both 0 and 1", command=wrong, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def question5():
    global score, got_wrong

    for widget in root.winfo_children():
        widget.destroy()

    got_wrong = False

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question6)

    def wrong():
        global got_wrong

        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 5", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(
        root,
        text="Computers primarily use Binary because it has:",
        font=("Arial", 40),
        bg="tan",
    ).place(x=50, y=200)

    Button(root, text="Two states (ON/OFF)", command=correct, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )

    Button(root, text="Eight digits", command=wrong, font=("", 20)).place(
        x=725, y=350, width=675, height=100
    )

    Button(root, text="Ten symbols", command=wrong, font=("", 20)).place(
        x=40, y=500, width=675, height=100
    )

    Button(root, text="Sixteen symbols", command=wrong, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def question6():
    global score, got_wrong

    for widget in root.winfo_children():
        widget.destroy()

    got_wrong = False

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question7)

    def wrong():
        global got_wrong

        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 6", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(
        root, text="A binary character is called a...", font=("Arial", 40), bg="tan"
    ).place(x=50, y=200)

    Button(root, text="Character", command=wrong, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )

    Button(root, text="Digit", command=wrong, font=("", 20)).place(
        x=725, y=350, width=675, height=100
    )

    Button(root, text="Symbol", command=wrong, font=("", 20)).place(
        x=40, y=500, width=675, height=100
    )

    Button(root, text="Bit", command=correct, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def question7():
    global score, got_wrong

    for widget in root.winfo_children():
        widget.destroy()

    got_wrong = False

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question8)

    def wrong():
        global got_wrong

        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 7", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(root, text="What is Binarys main use?", font=("Arial", 40), bg="tan").place(
        x=50, y=200
    )

    Button(root, text="Fixing computers", command=wrong, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )

    Button(
        root, text="Making a car and repairing it", command=wrong, font=("", 20)
    ).place(x=725, y=350, width=675, height=100)

    Button(
        root, text="Writing and publishing books.", command=wrong, font=("", 20)
    ).place(x=40, y=500, width=675, height=100)

    Button(root, text="Store and process data", command=correct, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def question8():
    global score, got_wrong

    for widget in root.winfo_children():
        widget.destroy()

    got_wrong = False

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question9)

    def wrong():
        global got_wrong

        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 8", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(
        root, text="Binary is the foundation of:", font=("Arial", 40), bg="tan"
    ).place(x=50, y=200)

    Button(root, text="Computers", command=wrong, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )

    Button(root, text="Computer systems", command=correct, font=("", 20)).place(
        x=725, y=350, width=675, height=100
    )

    Button(root, text="Writing", command=wrong, font=("", 20)).place(
        x=40, y=500, width=675, height=100
    )

    Button(root, text="Databases", command=wrong, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def question9():
    global score, got_wrong

    for widget in root.winfo_children():
        widget.destroy()

    got_wrong = False

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question10)

    def wrong():
        global got_wrong

        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 9", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(
        root,
        text="Which device commonly uses Binary internally?",
        font=("Arial", 40),
        bg="tan",
    ).place(x=50, y=200)

    Button(root, text="Printer", command=wrong, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )

    Button(root, text="Car ", command=wrong, font=("", 20)).place(
        x=725, y=350, width=675, height=100
    )

    Button(root, text="Computer", command=correct, font=("", 20)).place(
        x=40, y=500, width=675, height=100
    )

    Button(root, text="Databases", command=wrong, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def question10():
    global score, got_wrong

    for widget in root.winfo_children():
        widget.destroy()

    got_wrong = False

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)

    def correct():
        global score

        if not got_wrong:
            score += 1

        result.config(text="Correct!", fg="green")
        root.after(1000, question11)

    def wrong():
        global got_wrong

        got_wrong = True
        result.config(text="Incorrect!", fg="red")

    Label(root, text="Question 10", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(
        root,
        text="What is the highest digit that can appear in Binary?",
        font=("Arial", 35),
        bg="tan",
    ).place(x=50, y=200)

    Button(root, text="0", command=wrong, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )

    Button(root, text="3 ", command=wrong, font=("", 20)).place(
        x=725, y=350, width=675, height=100
    )

    Button(root, text="2", command=wrong, font=("", 20)).place(
        x=40, y=500, width=675, height=100
    )

    Button(root, text="1", command=correct, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def show_final_score():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="tan")

    Label(root, text="Quiz Complete!", font=("Arial", 50), fg="green", bg="tan").place(
        x=500, y=250
    )

    Label(root, text=f"Final Score: {score}/11", font=("Arial", 40), bg="tan").place(
        x=550, y=400
    )
    img = Image.open("Party-removebg-preview (1).png")
    img = img.resize((300, 300))

    photo = ImageTk.PhotoImage(img)

    picture = Label(root, image=photo, bg="tan")
    picture.image = photo   # Keep a reference!
    picture.place(x=650, y=500)

def question11():
    for widget in root.winfo_children():
        widget.destroy()
    global got_wrong

    got_wrong = False

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="tan")

    Label(root, text=f"Score: {score}", font=("Arial", 20), bg="tan").place(x=20, y=20)

    result = Label(root, text="", font=("Arial", 30), bg="tan")
    result.place(x=650, y=650)


def correct():
    global score

    if not got_wrong:
        score += 1

    root.configure(bg="tan")

    Label(root, text="Extra Question?", font=("Arial", 40), bg="tan").place(
        x=550, y=150
    )


def extra_question():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="tan")

    result = Label(root, text="", font=("Arial", 40), bg="tan")
    result.place(x=400, y=650)

    def correct():
        global score
        score += 1
        result.config(text="Correct!", fg="green")
        root.after(1000, show_final_score)

    def wrong():
        result.config(text="Incorrect!", fg="red")
        root.after(1000, show_final_score)

    Label(root, text="Bonus Question", font=("Arial", 30), bg="tan").place(x=650, y=100)

    Label(root, text="What does CPU stand for?", font=("Arial", 40), bg="tan").place(
        x=250, y=200
    )

    Button(root, text="Central Processing Unit", command=correct, font=("", 20)).place(
        x=40, y=350, width=675, height=100
    )

    Button(root, text="Computer Power Unit", command=wrong, font=("", 20)).place(
        x=725, y=350, width=675, height=100
    )

    Button(root, text="Central Program Utility", command=wrong, font=("", 20)).place(
        x=40, y=500, width=675, height=100
    )

    Button(root, text="Control Processing Utility", command=wrong, font=("", 20)).place(
        x=725, y=500, width=675, height=100
    )


def question11():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="tan")

    Label(root, text="Extra Question?", font=("Arial", 40), bg="tan").place(
        x=550, y=150
    )

    Label(
        root,
        text="Would you like to answer one extra question?",
        font=("Arial", 25),
        bg="tan",
    ).place(x=350, y=250)

    def yes():
        extra_question()

    def no():
        show_final_score()

        Label(
            root, text="Quiz Completed!", font=("Arial", 50), fg="green", bg="tan"
        ).place(x=500, y=350)

    Button(root, text="Yes", command=yes, font=("Arial", 20)).place(
        x=500, y=450, width=200, height=100
    )

    Button(root, text="No", command=no, font=("Arial", 20)).place(
        x=800, y=450, width=200, height=100
    )


def yes():
    extra_question()


def no():
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Quiz Completed!", font=("Arial", 50), fg="green", bg="tan").place(
        x=500, y=350
    )


Button(root, text="Yes", command=yes, font=("Arial", 20)).place(
    x=500, y=450, width=200, height=100
)

Button(root, text="No", command=no, font=("Arial", 20)).place(
    x=800, y=450, width=200, height=100
)


Button(root, text="Yes", command=yes, font=("Arial", 20)).place(
    x=500, y=450, width=200, height=100
)

Button(root, text="No", command=no, font=("Arial", 20)).place(
    x=800, y=450, width=200, height=100
)


ctx = Canvas(root, width=1800, height=900, bg="tan")
ctx.pack()

img = Image.open("table.png")
img = img.resize((325, 400))

photo = ImageTk.PhotoImage(img)

ctx.create_image(1600, 250, image=photo)

ctx.image = photo
text = ctx.create_text(100, 100, text="BINARY", fill="black", font=("", 40))
ctx.pack()
text = ctx.create_text(650, 100, text="OCTAL", fill="black", font=("", 40))
ctx.pack()
text = ctx.create_text(1100, 100, text="HEXADECIMAL", fill="black", font=("", 40))
ctx.pack()


def click():
    print("Button clicked!")


my_button = Button(
    root, text="Click to start Binary!", command=question1, font=("", 13)
)
my_button.pack()
my_button.place(x=25, y=150, width=175, height=75)

my_button = Button(root, text="Click to start Octal!", command=click, font=("", 13))
my_button.pack()
my_button.place(x=600, y=150, width=150, height=75)

my_button = Button(
    root, text="Click to start Hexadecimal!", command=click, font=("", 13)
)
my_button.pack()
my_button.place(x=1100, y=150, width=200, height=75)

text = ctx.create_text(100, 300, text="Binary to Octal", fill="black", font=("", 15))
ctx.pack()
text = ctx.create_text(
    100, 320, text="Binary to Hexadecimal", fill="black", font=("", 15)
)
ctx.pack()
text = ctx.create_text(100, 340, text="Binary to Decimal", fill="black", font=("", 15))
ctx.pack()

text = ctx.create_text(650, 300, text="Octal to Binary", fill="black", font=("", 15))
ctx.pack()
text = ctx.create_text(
    650, 320, text="Octal to Hexadecimal", fill="black", font=("", 15)
)
ctx.pack()
text = ctx.create_text(650, 340, text="Octal to Tens", fill="black", font=("", 15))
ctx.pack()

text = ctx.create_text(
    1100, 300, text="Hexadecimal to Binary", fill="black", font=("", 15)
)
ctx.pack()
text = ctx.create_text(
    1100, 320, text="Hexadecimal to Octal", fill="black", font=("", 15)
)
ctx.pack()
text = ctx.create_text(
    1100, 340, text="Hexadecimal to Tens", fill="black", font=("", 15)
)
ctx.pack()

my_button = Button(root, text="Click to start!", command=click, font=("", 16))
my_button.pack()
my_button.place(x=25, y=375, width=150, height=75)
my_button = Button(root, text="Click to start!", command=click, font=("", 16))
my_button.pack()
my_button.place(x=625, y=375, width=150, height=75)
my_button = Button(root, text="Click to start!", command=click, font=("", 16))
my_button.pack()
my_button.place(x=1100, y=375, width=150, height=75)

text = ctx.create_text(100, 500, text="Binary + Octal", fill="black", font=("", 15))
ctx.pack()
text = ctx.create_text(
    100, 520, text="Binary + Hexadecimal", fill="black", font=("", 15)
)
ctx.pack()
text = ctx.create_text(100, 540, text="Binary + Decimal", fill="black", font=("", 15))
ctx.pack()
text = ctx.create_text(100, 560, text="Binary + Binary", fill="black", font=("", 15))
ctx.pack()

text = ctx.create_text(
    650, 500, text="Octal + Hexadecimal", fill="black", font=("", 15)
)
ctx.pack()
text = ctx.create_text(650, 520, text="Octal + Decimal", fill="black", font=("", 15))
ctx.pack()
text = ctx.create_text(650, 540, text="Octal + Octal", fill="black", font=("", 15))
ctx.pack()
text = ctx.create_text(650, 560, text="Octal + Binary", fill="black", font=("", 15))
ctx.pack()

text = ctx.create_text(
    1100, 500, text="Hexadecimal +  Hexadecimal", fill="black", font=("", 15)
)
ctx.pack()
text = ctx.create_text(
    1100, 520, text="Hexadecimal + Decimal", fill="black", font=("", 15)
)
ctx.pack()
text = ctx.create_text(
    1100, 540, text="Hexadecimal + Octal", fill="black", font=("", 15)
)
ctx.pack()
text = ctx.create_text(
    1100, 560, text="Hexadecimal + Binary", fill="black", font=("", 15)
)
ctx.pack()


my_button = Button(root, text="Click to start!", command=click, font=("", 16))
my_button.pack()
my_button.place(x=25, y=575, width=150, height=75)
my_button = Button(root, text="Click to start!", command=click, font=("", 16))
my_button.pack()
my_button.place(x=565, y=575, width=150, height=75)
my_button = Button(root, text="Click to start!", command=click, font=("", 16))
my_button.pack()
my_button.place(x=1050, y=575, width=150, height=75)
root.title("Line Example")


ctx.pack()
ctx.create_line(0, 688, 1800, 688, fill="black", width=3)

text = ctx.create_text(700, 775, text="Tutorial", fill="black", font=("", 40))
ctx.pack()
tutorial_button = Button(root, text="Start Tutorial", command=click)

tutorial_button = Button(root, text="Start Tutorial", command=click, font=("Arial", 20))


tutorial_button.place(x=950, y=725, width=250, height=75)


root.mainloop()
