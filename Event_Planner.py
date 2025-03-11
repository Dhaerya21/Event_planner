import os
import datetime
import time
import json

File_path = "Events.json"

def Load_Event():
    if os.path.exists(File_path):
        with open(File_path,"r") as file:
            try:
                return json.load(file)
            except Exception:
                return {}
    return {}

def Save_Event(Events):
    with open(File_path,"w") as file:
        json.dump(Events,file,indent=4)

def Add_Event(Title,date_time):
    try:
        Events=Load_Event()
        Events[Title]=date_time.isoformat()
        Save_Event(Events)
        return f"Your {Title} Event was added successfully"
    
    except Exception as e:
        return f"Something Went Wrong : {e}"

def View_Events():
    pass

def Update_Event():  
    pass

def Reminder():
    pass

def main():
    event = {"title" :"date & time"}
    reference = True
    while reference:
        print("what do you Want to do:\n1.Add An Event \n2.Update an Event \n3.View all upcoming Event \n4.exit ")
        choice =int(input("enter your Choice: "))
        match choice:
            case 1:
                Title=input("Enter the name of the Event: ").capitalize()
                date_time=datetime.datetime.strptime(input("Enter date and time in format YYYY MM DD HH MM SS: "),"%Y %m %d %H %M %S")
                message= Add_Event(Title,date_time)
                print(message)
            case 2:
                Update_Event()
            case 3:
                View_Events()
            case 4:
                reference = False
            case _:
                print("please choose a valid choice!!!")
    print("Thanks For Using Our Event Organiser")

if __name__ == "__main__":
    main()