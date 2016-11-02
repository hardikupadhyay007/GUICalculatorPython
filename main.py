from tkinter import *
from functools import partial
from enum import Enum

class Operators(Enum):
    plus = 1
    minus = 2
    times = 3
    divide = 4

class Calculator:
    def __init__(self, master):
        self.intNum = 0
        self.num1 = None
        self.num2 = None
        self.operator = None
        
        frame = Frame(master)
        frame.grid()

        #Displays text to show what the user is inputing and the result
        self.var = StringVar()
        label = Label(frame, height = 1, width = 13, textvariable = self.var, relief=RAISED)
        label.grid(columnspan=10)

        #Create Buttons for the numbers of the calculator
        calcNum = 0
        for x in range(0, 4):
            for y in range(0, 3):
                self.buttonNum = Button(frame, text = calcNum, command=partial(self.appendNum, calcNum))
                if calcNum == 9:
                    self.buttonNum.grid(row = x +1, column = 1)
                    break
                else:
                    self.buttonNum.grid(row = x + 1, column = y)
                    calcNum += 1

        #Creates Buttons for the operators of the calculator
        for x in range(0, 4):
            if x == 0:
                y = Operators.plus
                z = "+"
            elif x == 1:
                y = Operators.minus
                z = "-"
            elif x == 2:
                y = Operators.times
                z = "*"
            elif x == 3:
                y = Operators.divide
                z = "/"
            self.buttonOp = Button(frame, text = z,command=partial(self.opr, y))
            if x == 3:
                self.buttonOp.grid(row = 6, column = 1)
            else:
                self.buttonOp.grid(row = 5, column = x, pady = 10)
            

        self.buttonEnter = Button(frame, text = "E", command=self.enter)
        self.buttonEnter.grid(pady = 10)

    def opr(self, y):
        self.operator = y
        z = ""
        if y == Operators.plus:
            z = "+"
        elif y == Operators.minus:
            z = "-"
        elif y == Operators.times:
            z = "*"
        elif y == Operators.divide:
            z = "/"
        self.var.set(z)
        if self.num1 is None:
            self.num1 = self.intNum
        self.intNum = 0

    def enter(self):
        if self.num1 is None:
            raise ValueError ("No number has been entered")
        
        if self.num2 is None:
            self.num2 = self.intNum
            
        if self.operator is None:
            raise ValueError ("An operator is needed")
        elif self.operator is not None:
            result = 0
            if self.operator == Operators.plus:
                result = self.num1 + self.num2
            elif self.operator == Operators.minus:
                result = self.num1 - self.num2
            elif self.operator == Operators.times:
                result = self.num1 * self.num2
            elif self.operator == Operators.divide:
                if self.num2 == 0:
                    raise ValueError ("Can't divide by 0!")
                result = self.num1 / self.num2
            #This following code allows the user to reuse the answer for further calculations
            self.num1 = result
            self.num2 = None
            self.var.set(result)

    def appendNum(self, x):
        #Adds numbers first as a string and then converts answer to int
        #Allows user to input e.g 1;2;0;9 which forms to 1209
        self.intNum = int(str(self.intNum) + str(x))
        #Displays number
        self.var.set(self.intNum)
        

root = Tk()

app = Calculator(root)

root.mainloop()
root.destroy()
