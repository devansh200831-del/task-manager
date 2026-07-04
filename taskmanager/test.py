import customtkinter as ctk
import calendar
from datetime import datetime as dt
import datetime
listweek=calendar.monthcalendar(dt.now().year,dt.now().month)

for week in range(len(listweek)):
    for day,date in enumerate(listweek[week]):
        if date!=0:
            datelabel=ctk.CTkLabel(popup,text=str(date),width=35,height=35,corner_radius=18)
            
            datelabel.grid(row=1+week ,column=day,padx=5,pady=5)
        else:
            datelabel=ctk.CTkLabel(popup,text="",width=35,height=35)
            
            datelabel.grid(row=1+week ,column=day,padx=5,pady=5)

