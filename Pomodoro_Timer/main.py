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
TEXT="✔"
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    head.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN *60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN *60

    if reps%8==0:
        count_down(long_break_sec)
        head.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        head.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        head.config(text="Work",fg=GREEN)
        

# ---------------------------- COUNTDOWN ------------------------------- # 

def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min==0:
        count_min="00"    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000, count_down,count - 1)
    else:
        start_timer()  
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✔"
        if reps%2==0:
            check_mark.config(text=mark)  


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW,highlightthickness=0)

head=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
head.grid(row=1,column=2)

canvas=Canvas(width=200,height=224,bg=YELLOW)
tomato_img=PhotoImage(file=r"tomato.png")
canvas.create_image(102,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(row=2,column=2)

start_button=Button(text="start",highlightthickness=0,command=start_timer)
start_button.grid(row=3,column=1)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=3,column=3)
check_mark=Label(fg=GREEN)
check_mark.grid(row=4,column=2)
window.mainloop()