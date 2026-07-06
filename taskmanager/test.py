import json
with open("taskmanager/tasks.json", "r") as file:
        data=json.load(file)
        data["tasks"].append({"title":"1"})

print(data)
        
