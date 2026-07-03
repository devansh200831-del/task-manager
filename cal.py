import customtkinter as ctk
popup=None
def open_calendar(parent):
     global popup
     if popup is not None:
         return
     else:
        popup = ctk.CTkToplevel(parent)
        popup.title("Planner")
        popup.geometry("350x400")
        popup.configure(fg_color="#FFFFFF")
        popup.resizable(False, False)
        popup.focus()
        def close():
         global popup
         popup.destroy()
         popup=None

        back_button = ctk.CTkButton(popup,text="←",command=close)
        back_button.pack(padx=10, pady=10)
                                  
                                 
                            
                               
   


   