import customtkinter as ctk
import cal
from PIL import Image

# 1. ALWAYS use ctk.CTk() when building with CustomTkinter
window = ctk.CTk() 
window.title("Task manager")
window.geometry("1200x800")
window.configure(fg_color="#F5F5F7")

# --- PHASE 2: LAYOUT ---

# SIDEBAR FIRST: This allows it to span the absolute full height (top to bottom)
sidebar = ctk.CTkFrame(
    window, 
    fg_color="#FFFFFF", 
    width=220, 
    border_color="green", 
    border_width=2
)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# --- SIDEBAR BUTTONS ---

# 1. Dashboard Button Setup
mytasksicon = ctk.CTkImage(
    light_image=Image.open("icon/task-management.png"),
    size=(20, 20)
)

mytasks = ctk.CTkButton(
    sidebar,
    text="   Dashboard", # Added 3 spaces for uniform alignment
    image=mytasksicon,
    compound="left",
    anchor="w",
    fg_color="transparent",
    text_color="#1C1C1E",
    corner_radius=12 # Rounded, but not overly distorted pill shape
)
# Big top margin to clear the ceiling, tight bottom margin
mytasks.pack(fill="x", padx=10, pady=(20, 2)) 

# 2. Planner Button Setup
calendericon = ctk.CTkImage(
    light_image=Image.open("icon/calendar.png"),
    size=(20, 20)
)

calender = ctk.CTkButton(
    sidebar,
    text="   Planner", # Added 3 spaces to perfectly match Dashboard's alignment
    image=calendericon,
    compound="left",
    anchor="w",
    fg_color="transparent",
    text_color="#1C1C1E",
    corner_radius=12,
     command=lambda: cal.open_calendar(window) # Matches Dashboard's bubble shape
        
)
# Balanced vertical margin so it sits neatly under Dashboard
calender.pack(fill="x", padx=10, pady=2) 
#creating pop uup calender



#archive button setup
archiveicon=ctk.CTkImage(light_image=Image.open("icon/archive.png"),
                         size=(20,20))
archive=ctk.CTkButton(sidebar,
                      text="archive",
                      image=archiveicon,
                      compound="left",
                      anchor="w",
                      fg_color="transparent",
                      text_color="#1C1C1E",
                      corner_radius=12
                      )
archive.pack(fill="x",padx=10, pady=2)

#settin button setup
settingicon=ctk.CTkImage(light_image=Image.open("icon/settings.png"),
                         size=(20,20))
setting=ctk.CTkButton(sidebar,
                      text="settings",
                      image=settingicon,
                      compound="left",
                      anchor="w",
                      fg_color="transparent",
                      text_color="#1C1C1E",
                      corner_radius=12
                      )
setting.pack(side="bottom",fill="x",padx=10, pady=(10,30))




# HEADER SECOND: Now it fills the remaining top width next to the sidebar
header = ctk.CTkFrame(
    window, 
    fg_color="#FFFFFF", 
    height=70, 
    border_color="green", 
    border_width=2
)
header.pack(side="top", fill="x")
header.pack_propagate(False)

#seach bar 
searchimage=ctk.CTkImage(light_image=Image.open("icon/search.png"),
                         size=(20,20))
searchlabel=ctk.CTkLabel(header,text=None,image=searchimage,compound="left",corner_radius=12,fg_color="transparent",anchor="w")
searchlabel.pack(side="left",padx=15)

search = ctk.CTkEntry(
    header,
    width=300,
    height=38,
    corner_radius=18,
    placeholder_text="Search tasks...",
    border_width=0,
    fg_color="#F3F4F6"
)
search.pack(
    side="left",
    padx=20,
    pady=16
)


# CONTENT CANVAS: Fills up the remaining space perfectly
content = ctk.CTkFrame(
    window, 
    fg_color="#FFFFFF", 
    corner_radius=16, 
    border_color="red", 
    border_width=2
)
content.pack(side="left", fill="both", expand=True, padx=20, pady=20)


window.mainloop()