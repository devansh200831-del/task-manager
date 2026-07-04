import customtkinter as ctk
import calendar
from datetime import datetime as dt
popup=None
def open_calendar(parent):
     global popup
     if popup is not None:
         return
     else:
        popup = ctk.CTkToplevel(parent)
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
        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

        for column, day in enumerate(days):
             label = ctk.CTkLabel(
             calendar_frame,
             text=day,
             width=35,
             corner_radius=12,
             border_color="blue",
             border_width=1
             
                 )

             label.grid(row=0, column=column, padx=5, pady=5)
        listweek=calendar.monthcalendar(dt.now().year,dt.now().month)

        for week in range(len(listweek)):
                 for day,date in enumerate(listweek[week]):
                     if date!=0:
                         datelabel=ctk.CTkLabel(calendar_frame,text=str(date),width=35,height=35,corner_radius=18)
            
                         datelabel.grid(row=1+week ,column=day,padx=5,pady=5)
                     else:
                         datelabel=ctk.CTkLabel(calendar_frame,text="",width=35,height=35,corner_radius=18)
            
                         datelabel.grid(row=1+week ,column=day,padx=5,pady=5)

        #moving cal
       
                       
     

     
        def close():
         global popup
         popup.destroy()
         popup=None
         
        popup.protocol("WM_DELETE_WINDOW", close)

        back_button = ctk.CTkButton(popup,text="←",command=close)
        back_button.pack(side="bottom",padx=10, pady=10)
        move=ctk.CTkLabel(popup,fg_color="Blue",corner_radius=28,text="")
        move.pack(side="bottom",fill="both",expand=True)                
        



      
                                  


                                 
                            
                               
   


   