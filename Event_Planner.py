import os
import pyaudio
import datetime as d
import time
import json
import threading

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
        return f"Your {Title} Event was added successfully🤩"
    
    except Exception as e:
        return f"Something Went Wrong : {e}"

def View_Events():
    Events =Load_Event()
    if not Events:
        print("the Events List is Empty\nTime to get Planning🌴✈️")
        return 
    
    print("\n📅 Upcoming Events:")
    for event in Events:
        time=d.datetime.fromisoformat(Events[event])
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"{event} : {formatted_time}")
    print("These are all your Events ,Enjoy your Events🌃")

def Update_Event(Title,choice):  
    Events =Load_Event()
    if not Events:
        return "the Events List is Empty\nTime to get Planning🌴✈️"
    if Title not in Events:
        return f"{Title} is not present in event list🤔"
    if choice==1:
        date_time = d.datetime.strptime(input("Enter date and time in format YYYY MM DD HH MM SS: "),"%Y %m %d %H %M %S")
        Events[Title]=date_time.isoformat()
        Save_Event(Events)
        return f"{Title} has been updated succesfully😊"
    else:
        del Events[Title]
        Save_Event(Events)
        return f"{Title} has been deleted successfully🗑️"


def Reminder():
    '''this is to remind the user that the events are near'''

    while True:
        Event =Load_Event()
        curr_time = d.datetime.now()
        for event, event_time in Event.items():
            formatted_time = d.datetime.fromisoformat(event_time)
            remaining_time = (formatted_time - curr_time).total_seconds()
            if 0 <= remaining_time <= 600:
                print(f"\nIt is time for {event} at {formatted_time.strftime('%Y-%m-%d %H:%M:%S')}\nGet Ready🥳  (press ctrl+s to stop)")
        time.sleep(10)

def main():
    reference = True
    reminder_thread = threading.Thread(target=Reminder, daemon=True)
    reminder_thread.start()  
    while reference:
        print("what do you Want to do:\n1.Add An Event \n2.Update an Event \n3.View all upcoming Event \n4.exit ")
        choice =int(input("enter your Choice: "))
        match choice:
            case 1:
                Title=input("Enter the name of the Event: ").capitalize()
                date_time=d.datetime.strptime(input("Enter date and time in format YYYY MM DD HH MM SS: "),"%Y %m %d %H %M %S")
                message= Add_Event(Title,date_time)
                print(message+"\n")
            case 2:
                Title=input("Enter the name of the Event you want to update: ").capitalize()
                print("1.Change Time\n2.Delete Event")
                choice=int(input("enter Your Choice: "))
                while True:
                    if choice==1 or choice==2:
                        break
                    else:
                        print("enter valid Choice😑")
                        choice=int(input("enter Your Choice: "))
                message =Update_Event(Title,choice)
                print(message+"\n")
            case 3:
                View_Events()
            case 4:
                reference = False
            case _:
                print("please choose a valid choice!!!")
    print("Thanks For Using Our Event Organiser")

if __name__ == "__main__":
    main()