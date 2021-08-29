from tkinter import *
import math
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

# TIMER RESET
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    header.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# TIMER MECHANISM
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        header.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        header.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        header.config(text="Work", fg=GREEN)


# COUNTDOWN MECHANISM
def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)

# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, bg=YELLOW)

canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(117, 100, image=photo)
timer_text = canvas.create_text(90, 120, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

header = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
header.grid(column=2, row=0)

sub_text="Pick a task, Do it for 25 minutes, Take a small Break,\n" \
         "Repeat this 4 times, Take a longer break."
sub = Label(text=sub_text, font=(FONT_NAME, 10, "bold"), fg=RED, bg=YELLOW)
sub.grid(column=2, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer, fg="black", highlightthickness=0)
start_button.grid(column=2, row=3, padx=50, sticky=W)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer, fg="black", highlightthickness=0)
reset_button.grid(column=2, row=3, padx=50, sticky=E)

check_marks = Label(text="", font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=4)

window.mainloop()