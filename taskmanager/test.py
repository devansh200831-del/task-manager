import customtkinter as ctk
import calendar
from datetime import datetime as dt
from datetime import date
popup=None
current=date(dt.now().year,dt.now().month,dt.now().day)

def close():
    global popup
    if popup is not None:
        popup.destroy()
        popup=None
def prev():
    global current
    if current.month==1:
        current=date(current.year-1,12,1)
    else:
        current=date(current.year,current.month-1,1)    
def next():
    global current
    if current.month==12:
        current=date(current.year+1,1,1)
    else:
        current=date(current.year,current.month+1,1)    
def drawcal(parent):
    global current,popup
    for widget in parent.winfo_children(): widget.destroy()
    days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    for column, day in enumerate(days):
        label = ctk.CTkLabel(
             parent,
             text=day,
             width=35,
             corner_radius=12,
             border_color="blue",
             border_width=1
             
                 )
        label.grid(row=0, column=column, padx=5, pady=5)
# CALENDER WURK________________________________________________________________________________________________
             
    listweek=calendar.monthcalendar(current.year,current.month)

        

    for week in range(len(listweek)):
         for day,date in enumerate(listweek[week]):
              if date!=0:
                datelabel=ctk.CTkLabel(parent,text=str(date),width=35,height=35,corner_radius=18)
                datelabel.grid(row=1+week ,column=day,padx=5,pady=5)
              else:
                datelabel=ctk.CTkLabel(parent,text="",width=35,height=35,corner_radius=18)
                datelabel.grid(row=1+week ,column=day,padx=5,pady=5)  
    back_button = ctk.CTkButton(popup,text="←",command=close)
    back_button.pack(side="bottom",padx=10, pady=10)
    move=ctk.CTkFrame(popup,fg_color="transparent",corner_radius=28)
    move.pack( side="bottom",fill="x",padx=10,pady=10)    
    previous=ctk.CTkButton(move, text="←",width=40,text_color="blue",command=prev)
    previous.pack(side="left") 
    nextbt=ctk.CTkButton(move, text="→",width=40,text_color="blue",command=next)
    nextbt.pack(side="right") 
    dateforcal=ctk.CTkButton(move,text=dt.now().strftime("%B %Y"),text_color="blue")
    dateforcal.pack()             
def open_calendar(parent):
    global popup
    if popup is not None:
        return
    else:
        popup = ctk.CTkToplevel(parent)
        popup.protocol("WM_DELETE_WINDOW", close)
        popup.title("Planner")
        popup.geometry("420x400")
        popup.configure(fg_color="#FFFFFF")
        popup.resizable(False, False)
        popup.focus()
        calendar_frame = ctk.CTkFrame(
                popup,
                fg_color="transparent"
                      )
        calendar_frame.pack(pady=20)
        back_button = ctk.CTkButton(popup,text="←",command=close)
        back_button.pack(side="bottom",padx=10, pady=10)
        move=ctk.CTkFrame(popup,fg_color="transparent",corner_radius=28)
        move.pack( side="bottom",fill="x",padx=10,pady=10)    
        previous=ctk.CTkButton(move, text="←",width=40,text_color="blue",command=prev)
        previous.pack(side="left") 
        nextbt=ctk.CTkButton(move, text="→",width=40,text_color="blue",command=next)
        nextbt.pack(side="right") 
        dateforcal=ctk.CTkButton(move,text=dt.now().strftime("%B %Y"),text_color="blue")
        dateforcal.pack() 
        drawcal(calendar_frame)


