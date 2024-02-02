import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
    label_check["text"] = ""
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    print(reps)

    work_time = WORK_MIN #* 60
    short_break = SHORT_BREAK_MIN #* 60
    long_break = LONG_BREAK_MIN #* 60

    if reps == 8:
        count_down(long_break)
        label_1.config(text="break!", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break)
        label_1.config(text="break!", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_time)
        label_1.config(text="Work!", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    checkmark = "✓"
    minutes = int(count/60)
    seconds = int(count % 60)

    minutes_text = f"{minutes}" if minutes > 9 else f"0{minutes}"
    seconds_text = f"{seconds}" if seconds > 9 else f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes_text}:{seconds_text}")

    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count  -1)
    else:
        start_timer()
        if reps % 2 == 0:
            label_check["text"] += checkmark
        
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pymodoro")
window.config(padx=100, pady=50,bg=YELLOW)

label_1 = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)    
label_1.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

label_check = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
label_check.grid(column=1, row=3)

window.mainloop()