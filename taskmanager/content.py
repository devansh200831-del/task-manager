import customtkinter as ctk
import json
task_title=None

taskpopup=None



    
    



def taskclose():
    global taskpopup
    if taskpopup is not None:
        taskpopup.destroy()
        taskpopup=None
def save_task():
    global task_title
    title = task_title.get().strip()
   

    if not title:
        taskclose() 
        return
    with open("taskmanager/tasks.json", "r") as file:
        data=json.load(file)
        data["tasks"].append({"title":title})
    
    with open("taskmanager/tasks.json", "w") as file:
        json.dump(data, file, indent=4)    
    taskclose()       
   
           
  
def addtaskwin(parent):
    global taskpopup,task_title
    if taskpopup is not None:
        return
    else:
        taskpopup = ctk.CTkToplevel(parent)
        taskpopup.protocol("WM_DELETE_WINDOW", taskclose)
        taskpopup.title("Planner")
        taskpopup.geometry("420x500")
        taskpopup.configure(fg_color="#FFFFFF")
        taskpopup.resizable(False, False)
        taskpopup.focus()
        title = ctk.CTkLabel(
               taskpopup,
               text="Add Task",
               font=("Arial", 22, "bold")
                    )
        title.pack(pady=(20, 10))
        task_title = ctk.CTkEntry(
                      taskpopup,
                      width=320,
                      height=40,
                      placeholder_text="Enter task title...",
                       corner_radius=12
                             )
        task_title.pack(pady=(10, 20), padx=20)
        save_button = ctk.CTkButton(taskpopup,text="Save", command=save_task)
        save_button.pack(pady=10)