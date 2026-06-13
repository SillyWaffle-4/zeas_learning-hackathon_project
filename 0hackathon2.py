import tkinter as tk
import pygame
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Button as TkButton
from tkinter.ttk import *
import random
import math
import re

pygame.mixer.init()

pygame.mixer.music.load("music/hackathon_audio.mp3")

pygame.mixer.music.play(-1)

def get_numbers_from_question(q_text):
    return [float(s) if '.' in s else int(s) for s in re.findall(r'\b\d+(?:\.\d+)?\b', q_text)]

def start_game(selected_mode):
    global game_mode, score, lives, question_num, stack_history, overflow_detected, randomized_indices
    game_mode = selected_mode
    score = 0
    lives = 3
    question_num = 0
    stack_history = []
    overflow_detected = False

    play_again_button.place_forget()
    
    randomized_indices = list(range(len(questions)))
    random.shuffle(randomized_indices)
    
    mode_frame.place_forget()
    
    current_idx = randomized_indices[question_num]
    ctx.itemconfig(text1, text=questions[current_idx], fill="black", font=(my_font, 22))
    
    setup_static_layout()

def reset_to_menu():
    global question_num, score, lives, stack_history, overflow_detected, showing_result, drop_mode_active

    pygame.mixer.init()
    pygame.mixer.music.load("music/hackathon_audio.mp3")
    pygame.mixer.music.play(-1)
    
    ctx.delete("shape")
    ctx.delete("stacked_shape")
    ctx.delete("falling_shape")
    ctx.delete("top_bar")
    ctx.itemconfig(text1, text="")

    showing_result = False
    drop_mode_active = False
    overflow_detected = False
    score = 0
    lives = 3
    stack_history = []
    
    # Hide game layout
    play_again_button.place_forget()
    toggle_buttons("normal")
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    
    mode_frame.place(relx=0.5, rely=0.5, anchor="center")

def draw_top_bar():
    ctx.delete("top_bar")
    w_win = root.winfo_screenwidth()
    h_win = root.winfo_screenheight()
    
    ctx.create_text(w_win * 0.15, h_win * 0.06, text=f"SCORE: {score}", 
                    font=(my_font, 18, "bold"), fill="black", tags="top_bar")
    
    hearts = "O " * lives + "X " * (3 - lives)
    ctx.create_text(w_win * 0.5, h_win * 0.06, text=f"LIFE: {hearts}", 
                    font=(my_font, 18, "bold"), fill="red", tags="top_bar")

def draw_shape_generation(cx, cy, size, q_text, nums, tags_value="shape"):
    r = size / 2
    if "rectangle" in q_text:
        w, h = size * 1.4, size * 0.8
        lbl1, lbl2 = "", ""
        if len(nums) >= 2:
            lbl1, lbl2 = str(nums[0]), str(nums[1])
        elif len(nums) == 1:
            lbl1 = str(nums[0])
        ctx.create_rectangle(cx - w/2, cy - h/2, cx + w/2, cy + h/2, fill="#ffcc00", outline="black", width=4, tags=tags_value)
        ctx.create_text(cx, cy + h/2 + 15, text=lbl1, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        ctx.create_text(cx - w/2 - 25, cy, text=lbl2, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        
    elif "square" in q_text:
        lbl = str(nums[0]) if len(nums) > 0 else ""
        ctx.create_rectangle(cx - size/2, cy - size/2, cx + size/2, cy + size/2, fill="#ff9999", outline="black", width=4, tags=tags_value)
        ctx.create_text(cx, cy + size/2 + 15, text=lbl, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        
    elif "triangle" in q_text:
        lbl1, lbl2 = "", ""
        if len(nums) >= 2:
            lbl1, lbl2 = str(nums[0]), str(nums[1])
        elif len(nums) == 1:
            lbl1 = str(nums[0])
        points = [cx, cy - size/2, cx - size/2, cy + size/2, cx + size/2, cy + size/2]
        ctx.create_polygon(points, fill="#99ccff", outline="black", width=4, tags=tags_value)
        ctx.create_line(cx, cy - size/2, cx, cy + size/2, dash=(4, 4), fill="gray", width=2, tags=tags_value)
        ctx.create_text(cx + 25, cy, text=lbl2, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        ctx.create_text(cx, cy + size/2 + 15, text=lbl1, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        
    elif "circle" in q_text:
        lbl = str(nums[0]) if len(nums) > 0 else ""
        ctx.create_oval(cx - r, cy - r, cx + r, cy + r, fill="#b3ffb3", outline="black", width=4, tags=tags_value)
        ctx.create_line(cx, cy, cx + r, cy, fill="black", width=2, tags=tags_value)
        ctx.create_text(cx + r/2, cy - 15, text=lbl, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        
    elif "parallelogram" in q_text:
        lbl1, lbl2 = "", ""
        if len(nums) >= 2:
            lbl1, lbl2 = str(nums[0]), str(nums[1])
        offset = size * 0.4
        points = [cx - size/2 + offset, cy - size/3, cx + size/2 + offset, cy - size/3,
                  cx + size/2 - offset, cy + size/3, cx - size/2 - offset, cy + size/3]
        ctx.create_polygon(points, fill="#e6b3ff", outline="black", width=4, tags=tags_value)
        ctx.create_line(cx - size/2 + offset, cy - size/3, cx - size/2 + offset, cy + size/3, dash=(4,4), fill="gray", width=2, tags=tags_value)
        ctx.create_text(cx - size/2 + offset - 25, cy, text=lbl2, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        ctx.create_text(cx, cy + size/3 + 15, text=lbl1, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        
    elif "trapezoid" in q_text:
        lbl1, lbl2, lbl3 = "", "" if len(nums) < 2 else "", ""
        if len(nums) >= 3:
            lbl1, lbl2, lbl3 = str(nums[0]), str(nums[1]), str(nums[2])
        w_top, w_bot = size * 0.7, size * 1.3
        h = size * 0.7
        points = [cx - w_top/2, cy - h/2, cx + w_top/2, cy - h/2,
                  cx + w_bot/2, cy + h/2, cx - w_bot/2, cy + h/2]
        ctx.create_polygon(points, fill="#ffb3d9", outline="black", width=4, tags=tags_value)
        ctx.create_line(cx - w_top/2, cy - h/2, cx - w_top/2, cy + h/2, dash=(4,4), fill="gray", width=2, tags=tags_value)
        ctx.create_text(cx - w_top/2 - 25, cy, text=lbl3, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        ctx.create_text(cx, cy - h/2 - 15, text=lbl1, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)
        ctx.create_text(cx, cy + h/2 + 15, text=lbl2, font=(my_font, max(int(size*0.12), 10), "bold"), tags=tags_value)

def on_click(num):
    global question_num, score, showing_result, drop_y, current_drop_size, drop_mode_active, current_drop_x, target_drop_y, overflow_detected
    showing_result = True
    
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    
    current_idx = randomized_indices[question_num]
    correct_idx = int(questionanswerset[current_idx])
    
    w_win = root.winfo_screenwidth()
    h_win = root.winfo_screenheight()
    
    if correct_idx == num:
        ctx.itemconfig(text1, text="CORRECT!!!", fill="green", font=(my_font, 35, "bold"))
        score += 100

        pygame.mixer.init()
        pygame.mixer.music.load("music/correct1.mp3")

        pygame.mixer.music.play(-1)

        draw_top_bar()
        
        if game_mode == "Shape Drop Mode":
            drop_mode_active = True
            current_drop_size = min(w_win, h_win) * 0.14
            drop_y = h_win * 0.20
            current_drop_x = w_win / 2
            
            lowest_occupied = h_win - (current_drop_size / 2) - 20
            for shape in stack_history:
                potential_surface = shape['y'] - (shape['size'] / 2) - (current_drop_size / 2)
                if potential_surface < lowest_occupied:
                    lowest_occupied = potential_surface

            target_drop_y = lowest_occupied
            if target_drop_y < h_win * 0.38:
                overflow_detected = True
                
            animate_drop()
        else:
            draw_shape_generation(w_win/2, h_win/2, min(w_win, h_win)*0.35, questions[current_idx].lower(), get_numbers_from_question(questions[current_idx]), "shape")
            root.after(1000, updatey)
    else:
        if correct_idx == 1: correct_ans = button1displays[current_idx]
        elif correct_idx == 2: correct_ans = button2displays[current_idx]
        elif correct_idx == 3: correct_ans = button3displays[current_idx]
        else: correct_ans = button4displays[current_idx]
        handle_wrong_answer(f"INCORRECT!\nCorrect Answer: {correct_ans}")
        pygame.mixer.init()
        pygame.mixer.music.load("music/incorrect1.mp3")

        pygame.mixer.music.play(-1)


def animate_drop():
    global drop_y
    ctx.delete("falling_shape")
    
    current_idx = randomized_indices[question_num]
    q_text = questions[current_idx].lower()
    nums = get_numbers_from_question(questions[current_idx])
    
    draw_shape_generation(current_drop_x, drop_y, current_drop_size, q_text, nums, "falling_shape")
    
    if drop_y < target_drop_y:
        drop_y += 35
        root.after(20, animate_drop)
    else:
        stack_history.append({'q_text': q_text, 'nums': nums, 'x': current_drop_x, 'y': target_drop_y, 'size': current_drop_size})
        ctx.delete("falling_shape")
        redraw_stack()
        root.after(1000, updatey)

def redraw_stack():
    ctx.delete("stacked_shape")
    if game_mode == "Shape Drop Mode" and drop_mode_active:
        for shape in stack_history:
            draw_shape_generation(shape['x'], shape['y'], shape['size'], shape['q_text'], shape['nums'], "stacked_shape")

def handle_wrong_answer(msg_text):
    global lives, showing_result
    showing_result = True
    lives -= 1
    draw_top_bar()
    
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    
    current_idx = randomized_indices[question_num]
    ctx.itemconfig(text1, text=msg_text, fill="red", font=(my_font, 30, "bold"))
    if game_mode != "Shape Drop Mode":
        w_win = root.winfo_screenwidth()
        h_win = root.winfo_screenheight()
        draw_shape_generation(w_win/2, h_win/2, min(w_win, h_win)*0.35, questions[current_idx].lower(), get_numbers_from_question(questions[current_idx]), "shape")
    root.after(2500, updatey)

def show_end_game_button():
    w_win = root.winfo_screenwidth()
    h_win = root.winfo_screenheight()
 
    play_again_button.place(x=w_win/2 - 120, y=h_win * 0.65, width=240, height=60)

def updatey():
    global question_num, showing_result, drop_mode_active
    showing_result = False
    drop_mode_active = False
    question_num += 1
    
    ctx.delete("shape")
    ctx.delete("stacked_shape")
    ctx.delete("falling_shape")

    if overflow_detected:
        ctx.itemconfig(text1, text=f"THE STACK OVERFLOWED! YOU WIN!!! YAY!!!!\nFinal Score: {score}", fill="purple", font=(my_font, 32, "bold"))
        show_end_game_button()

        pygame.mixer.init()
        pygame.mixer.music.load("music/yay.mp3")

        pygame.mixer.music.play(-1)
        return

    if lives <= 0:
        ctx.itemconfig(text1, text=f"GAME OVER!\nYou ran out of lives.\nFinal Score: {score}", fill="red", font=(my_font, 30, "bold"))
        show_end_game_button()

        pygame.mixer.init()
        pygame.mixer.music.load("music/womp.mp3")

        pygame.mixer.music.play(-1)
        return

    if question_num >= len(questions):
        ctx.itemconfig(text1, text=f"VICTORY!\nYou finished all questions.\nFinal Score: {score}", fill="blue", font=(my_font, 30, "bold"))
        show_end_game_button()

        pygame.mixer.init()
        pygame.mixer.music.load("music/yay.mp3")

        pygame.mixer.music.play(-1)
        return

    current_idx = randomized_indices[question_num]
    toggle_buttons("normal")
    ctx.itemconfig(text1, text=questions[current_idx], fill="black", font=(my_font, 22))
    draw_top_bar()
    setup_static_layout()


    pygame.mixer.init()
    pygame.mixer.music.load("music/hackathon_audio.mp3")

    pygame.mixer.music.play(-1)

def toggle_buttons(state_value):
    button1.config(state=state_value)
    button2.config(state=state_value)
    button3.config(state=state_value)
    button4.config(state=state_value)

def setup_static_layout():
    w_win = root.winfo_screenwidth()
    h_win = root.winfo_screenheight()
    
    draw_top_bar()
    redraw_stack()
    ctx.coords(text1, w_win / 2, h_win * 0.12)
    ctx.itemconfig(text1, width=int(w_win * 0.8))
    
    if not randomized_indices:
        return

    current_idx = randomized_indices[question_num] if question_num < len(questions) else 0
    
    if showing_result:
        if game_mode != "Shape Drop Mode":
            draw_shape_generation(w_win/2, h_win/2, min(w_win, h_win)*0.35, questions[current_idx].lower(), get_numbers_from_question(questions[current_idx]), "shape")
    else:
        btn_w = w_win * 0.38
        btn_h = h_win * 0.22
        
        x1 = w_win * 0.10
        x2 = w_win * 0.52
        y1 = h_win * 0.35
        y2 = h_win * 0.63
        
        button1.place(x=x1, y=y1, width=btn_w, height=btn_h)
        button2.place(x=x2, y=y1, width=btn_w, height=btn_h)
        button3.place(x=x1, y=y2, width=btn_w, height=btn_h)
        button4.place(x=x2, y=y2, width=btn_w, height=btn_h)
        
        button1.config(text=button1displays[current_idx])
        button2.config(text=button2displays[current_idx])
        button3.config(text=button3displays[current_idx])
        button4.config(text=button4displays[current_idx])

root = Tk()
my_font = "Segoe UI"

root.attributes('-fullscreen', True)
try:
    root.state('zoomed')
except:
    pass
root.resizable(False, False)
root.title("Math Learner")


showing_result = False
drop_mode_active = False
overflow_detected = False
game_mode = None
score = 0
lives = 3
stack_history = []
randomized_indices = []
drop_y = 0
current_drop_x = 0
current_drop_size = 0
target_drop_y = 0

style = Style()
style.configure("TButton", font=(my_font, 20))

ctx = Canvas(root, bg="lightblue", highlightthickness=0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
ctx.pack(fill="both", expand=True)

mode_frame = Frame(root, padding=20)
mode_frame.place(relx=0.5, rely=0.5, anchor="center")



Label(mode_frame, text="Select Game Mode", font=(my_font, 28, "bold")).pack(pady=20)
Button(mode_frame, text="Classic Quiz Mode", command=lambda: start_game("Classic Quiz")).pack(fill="x", pady=10, ipady=10)
Button(mode_frame, text="Shape Drop Mode", command=lambda: start_game("Shape Drop Mode")).pack(fill="x", pady=10, ipady=10)

questions = [
    "A rectangle has a length of 8 and a width of 5. What is its perimeter?",
    "A square has a side length of 6. What is its area?",
    "A triangle has a base of 10 and a height of 4. What is its area?",
    "A circle has a radius of 7. What is its approximate circumference? (Use pi = 3.14)",
    "A parallelogram has a base of 9 and a height of 6. What is its area?",
    "A square has an area of 49. What is its perimeter?",
    "A rectangle has an area of 40 and a length of 8. What is its width?",
    "A triangle has a base of 6 and a height of 8. What is its area?",
    "A circle has a diameter of 10. What is its approximate area? (Use pi = 3.14)",
    "A trapezoid has bases of 4 and 6, and a height of 5. What is its area?",
    "A rectangle has a length of 12 and a width of 4. What is its area?",
    "A square has a perimeter of 32. What is its area?",
    "A triangle has sides of length 5, 12, and 13. What is its perimeter?",
    "A parallelogram has a base of 7 and a height of 4. What is its area?",
    "A circle has a radius of 3. What is its approximate area? (Use pi = 3.14)",
    "A rectangle has a perimeter of 30 and a width of 5. What is its length?",
    "A trapezoid has bases of 8 and 12, and a height of 4. What is its area?",
    "A square has a side length of 9. What is its perimeter?",
    "A triangle has a base of 14 and a height of 3. What is its area?",
    "A circle has a circumference of 31.4. What is its approximate radius? (Use pi = 3.14)"
]

questionanswerset = [
    "3", "1", "4", "2", "1", "4", "2", "3", "1", "4",
    "2", "3", "1", "4", "2", "3", "1", "4", "2", "3"
]

button1displays = ["40", "36", "40", "21.98", "54", "14", "32", "48", "78.5", "50", "32", "16", "30", "22", "9", "25", "40", "18", "42", "10"]
button2displays = ["13", "24", "14", "43.96", "30", "49", "5", "14", "31.4", "24", "48", "64", "25", "11", "28.26", "20", "96", "36", "21", "2.5"]
button3displays = ["26", "12", "28", "153.86", "15", "21", "12", "24", "100", "15", "16", "64", "60", "14", "18.84", "10", "20", "80", "81", "17"]
button4displays = ["30", "16", "20", "49", "27", "28", "4", "20", "25", "25", "24", "32", "18", "28", "6", "15", "16", "36", "38", "15.7"]

question_num = 0
text1 = ctx.create_text(root.winfo_screenwidth()/2, root.winfo_screenheight()*0.12, text="", fill="black", font=(my_font, 22), justify="center")

button1 = Button(root, command=lambda: on_click(1))
button2 = Button(root, command=lambda: on_click(2))
button3 = Button(root, command=lambda: on_click(3))
button4 = Button(root, command=lambda: on_click(4))

play_again_button = TkButton(root, text="Play Again", font=(my_font, 22, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white", cursor="hand2", command=reset_to_menu)

root.mainloop()