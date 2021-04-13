from tkinter import *
import random
from tkinter import messagebox

top = Tk()
top.title("Guessify")  #title of window
top.geometry("230x350")     #size of window
top.resizable(0, 0)         #disable maximize option
top.configure(bg="#66ccff") #background color for window

num = random.randint(0, 9) #generate random number
mylist = []
mytry = IntVar()
# a container to store the number
guess = 0
# a place where strord number will show
interger = IntVar()

# a function to get number from clicked button
def number(num):
     # access global variable
     global guess, mytry
     guess = str(num)
     interger.set(guess)
     
# a submit function
def submit():
     global guess, num, mylist
     guess = int(guess)
     if guess == num:
          messagebox.showinfo("result", "your guess is right!")
          mylist.append(guess)
          mytry.set(mylist)
          lenght = len(mylist)
          score = str(110 - (lenght * 10))+"%"
          a = messagebox.showinfo("score", score)
          if a == 'ok':
               top.destroy()
     elif guess < num:
          messagebox.showinfo("result", "wrong, Hint: "+ "guess is to small")
          mylist.append(guess)
          mytry.set(mylist)
     elif guess > num:
          messagebox.showinfo("result", "wrong, Hint: "+ "guess is to large")
          mylist.append(guess)
          mytry.set(mylist)
     else :
          messagebox.showerror("result", "error")

# display guessed number
M1 = Message(top, textvariable=interger, fg="navyblue")
M1.grid(row=7, column=3, pady=5)
# previous guesses
mytry.set("no try yet!") 
M2 = Message(top, textvariable=mytry)
M2.grid(row=10, column=1, columnspan=5, padx=4)

L1 = Label(top, text="click and start guessing...", fg="blue")
L1.grid(row=0, column=1, columnspan=5, pady=7, padx=15)

L2 = Label(top, text="your guessed number (0 is default)", fg="navyblue")
L2.grid(row=6, column=1, columnspan=10, pady=7, padx=15)

L3 = Label(top, text="your previous guesses!")
L3.grid(row=9, column=1, columnspan=5, pady=4)

B2 = Button(top, text="2", command=lambda: number(2), font=3, width=3, border=3, bg="orange", fg="white")
B1 = Button(top, text="1", command=lambda: number(1), font=3, width=3, border=3, bg="orange", fg="white")
B3 = Button(top, text="3", command=lambda: number(3), font=3, width=3, border=3, bg="orange", fg="white")
B4 = Button(top, text="4", command=lambda: number(4), font=3, width=3, border=3, bg="orange", fg="white")
B5 = Button(top, text="5", command=lambda: number(5), font=3, width=3, border=3, bg="orange", fg="white")
B6 = Button(top, text="6", command=lambda: number(6), font=3, width=3, border=3, bg="orange", fg="white")
B7 = Button(top, text="7", command=lambda: number(7), font=3, width=3, border=3, bg="orange", fg="white")
B8 = Button(top, text="8", command=lambda: number(8), font=3, width=3, border=3, bg="orange", fg="white")
B9 = Button(top, text="9", command=lambda: number(9), font=3, width=3, border=3, bg="orange", fg="white")
B0 = Button(top, text="0", command=lambda: number(0), font=3, width=3, border=3, bg="orange", fg="white")
Bs = Button(top, text="submit", command=submit, width=10, border=3, bg="green", fg="white")

# Packing button's
B1.grid(row= 2, column=1)
B2.grid(row= 2, column=2)
B3.grid(row= 2, column=3)
B4.grid(row= 2, column=4)
B5.grid(row= 2, column=5)
B6.grid(row= 3, column=1)
B7.grid(row= 3, column=2)
B8.grid(row= 3, column=3)
B9.grid(row= 3, column=4)
B0.grid(row= 3, column=5)
Bs.grid(row= 8, column=1, columnspan=5, pady=4)
top.mainloop()