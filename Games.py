
import random
from tkinter import *

attempts = 5

random_number = random.randint(0, 999)

root = Tk()
root.geometry('500x500')
root.title("GUESS THE NUMBER GAME")
label_0 = Label(root, text="Number guessing game", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Enter number", width=20, font=("bold", 10))
label_1.place(x=80, y=150)
entry_1 = Entry(root)
entry_1.place(x=240, y=150)


def printAttempts(_attempts):
    attempt_string = "Attempt left: " + str(_attempts)
    label_attempt = Label(root,
                          text=attempt_string,
                          width=20,
                          font=("bold", 20))
    label_attempt.place(x=90, y=100)


printAttempts(5)


def printMessage(msg):
    _message = Label(root, text=msg, width=50, font=("bold", 10))
    _message.place(x=80, y=200)




def onSubmit():
    global attempts
    
    print('attempts', attempts)
    guessed_number = entry_1.get()
    guessed_number = int(guessed_number)

    if attempts != 0:
        print('the guess', guessed_number)
        print('the random', random_number)
        if (guessed_number == random_number):
            printMessage("Horray you just got it Right!")
            attempts = 0
            print(attempts)
        else:
            print('removing one attempt')
            attempts = attempts - 1
            printMessage("You got it wrong :")
            if (guessed_number > random_number):
                printMessage("Your guess number is greater than lucky number")
                print('too high', attempts)
            else:
                printMessage("Your guess number is less than lucky number")
                print('too low', attempts)
            if (attempts == 0):
                printMessage("No attempts left, try again later")
                print('run out', attempts)
        printAttempts(attempts)        

Button(root, text='Submit', width=20, bg='blue', fg='white', font=('bold',10),
       command=onSubmit).place(x=180, y=380)

root.mainloop()