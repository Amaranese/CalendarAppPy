
import datatime

scheduleFile = "schedule.txt"



print("")
print("Allison's Calendar App".upper())
print("")
print("1. View Todays Tasks")
print("2. Add New Task")
print("")


user = input("Please choose option 1 or 2: ")
print("")


now = datetime.datetime.now()


todaysDate = now.strftime("%d-%m-%Y")

if(user == "1"):
    f = open(scheduleFile, "r")
    MYSCHEDULE = f.read().split("\n")
    print("")
    print("****Today's Tasks****".upper())
    print("")
    print("Todays date is " + str(todaysDate))
    print("")
    print("To Do:".upper())
    success = False
    
    
    for line in range(0, len(MYSCHEDULE)):
        currentLine = MYSCHEDULE[line]
        taskDate = currentLine.split(",")[0]
        if(taskDate == todaysDate):
            success = True
            print("")
            print(currentLine.split(",")[1].capitalize() + (" - ") + ("This task is " + currentLine.split(",")[2]))
            print("")
            break
            if(success == True):
                break
                

    if(success == False):
        print("")
        print("You have no tasks due today")
        print("")  
        user = input("Would you like to add a task? Type 1(No) or 2(Yes): ")
        print("")   
        if user != "2":
            print("See you next time!")
     
                    
    f.close()
                


if(user == "2"):
    date = input("Input task due date (dd-mm-yyyy): ")
    task = input("Advise the task: ")
    category = input("Urgent or not urgent: ")
         
    a = open(scheduleFile, "a")
    a.write("\n" + date + "," + task + "," + category)
    a.close()
    print("")
    print("Task added to calendar".upper())

    
    if(date == todaysDate):
        f = open(scheduleFile, "r")
        MYSCHEDULE = f.read().split("\n")
        print("")
        print("****Today's Tasks****".upper())
        print("")
        print("Todays date is " + str(todaysDate))
        print("")
        print("To Do:".upper())


        for line in range(0, len(MYSCHEDULE)):
            currentLine = MYSCHEDULE[line]
            taskDate = currentLine.split(",")[0]
            if(taskDate == todaysDate):
                print("")
                print(currentLine.split(",")[1] + (" - ") + ("This task is " + currentLine.split(",")[2]))
                print("")
                f.close()