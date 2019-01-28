#Create a task list. A user is presented with the text below.
# Let them select an option to list all of their tasks,
# add a task to their list,
# delete a task, or quit the program.
# Make each option a different function in your program.



userTasks = []


def prob1():

    askUser = ""
    while askUser != "0":

        print("Congrats your're running Chelsea's Task List!")
        askUser = input("What would you like to do next? (1)List all tasks. (2) Add task to list. (3) Delete a task (0)Quit the program")

        if askUser == "2":
            print(addTask(askUser))
        elif askUser == "1":
            return (listTasks(askUser))
        elif askUser == "3":
            print(deleteTask(askUser))
        elif askUser == "0":
            print(getOut(askUser))
            print("Goodbye!")
        else:
            print("Error! That is not a selected option")




def addTask(askUser1):

    askUser1 = input("What would you like to add")
    userTasks.append(askUser1)
    return userTasks


def deleteTask(askUser):
    askUser = input("What would you like to delete?")
    userTasks.remove(askUser)
    return userTasks


def listTasks(askUser):
    for eachEl in userTasks:
        print(eachEl)

def getOut(x):
    return userTasks





prob1()

