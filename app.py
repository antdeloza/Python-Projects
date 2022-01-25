from tkinter import *
import parser

root = Tk() # tkinter instance to be able of use it
root.title("My Calculator") # app title

display = Entry(root) #Input text
display.grid(row=1, columnspan=6,sticky=W+E) # Input text properties


i =  0
#Function to get the numbers on screen
def get_numbers(n):
    global i 
    display.insert(i, n)
    i+=1

#function to get the operators
def get_operation(operator):
    global i 
    operator_length = len(operator) #get the operator length  
    display.insert(i, operator)
    i+=operator_length

#function to clear the display
def clear_display():
    display.delete(0, END)

#function to clear characters one by one
def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0,display_new_state)
    else:
        clear_display()
        display.insert(0,'Error')

#function to convert the strings into math expressions and then evaluate it.
def calculate():
    display_state = display.get()
    try:
        math_exppresion = parser.expr(display_state).compile()
        result = eval(math_exppresion)
        clear_display()
        display.insert(0,result)
    except expression as identifier:
        clear_display()
        display.insert(0,'Error')
        

#Numeric Buttons 1-3
Button(root, text="1", command=lambda:get_numbers(1)).grid(row=2, column=0,sticky=W+E)
Button(root, text="2", command=lambda:get_numbers(2)).grid(row=2, column=1,sticky=W+E)
Button(root, text="3", command=lambda:get_numbers(3)).grid(row=2, column=2,sticky=W+E)

#Numeric Buttons 4-6

Button(root, text="4", command=lambda:get_numbers(4)).grid(row=3, column=0,sticky=W+E)
Button(root, text="5", command=lambda:get_numbers(5)).grid(row=3, column=1,sticky=W+E)
Button(root, text="6", command=lambda:get_numbers(6)).grid(row=3, column=2,sticky=W+E)

#Numeric Buttons 7-9

Button(root, text="7", command=lambda:get_numbers(7)).grid(row=4, column=0,sticky=W+E)
Button(root, text="8", command=lambda:get_numbers(8)).grid(row=4, column=1,sticky=W+E)
Button(root, text="9", command=lambda:get_numbers(9)).grid(row=4, column=2,sticky=W+E)


#Auxiliary Buttons
Button(root, text="AC", command=lambda:clear_display()).grid(row=5, column=0,sticky=W+E)
Button(root, text="0", command=lambda:get_numbers(0)).grid(row=5, column=1,sticky=W+E)
Button(root, text="%", command=lambda:get_operation("%")).grid(row=5, column=2,sticky=W+E)


#Operation Buttons
Button(root, text="+", command=lambda:get_operation("+")).grid(row=2, column=3,sticky=W+E)
Button(root, text="-", command=lambda:get_operation("-")).grid(row=3, column=3,sticky=W+E)
Button(root, text="x", command=lambda:get_operation("*")).grid(row=4, column=3,sticky=W+E)
Button(root, text="/", command=lambda:get_operation("/")).grid(row=5, column=3,sticky=W+E)


#Deleting Button
Button(root, text="🠔",command=lambda:undo()).grid(row=2, column=4,sticky=W+E, columnspan=2)

#Exponential Buttons
Button(root, text="^n", command=lambda:get_operation("**")).grid(row=3, column=4,sticky=W+E)
Button(root, text="^2", command=lambda:get_operation("**2")).grid(row=3, column=5,sticky=W+E)


#Grouping Buttons
Button(root, text="(", command=lambda:get_operation("(")).grid(row=4, column=4,sticky=W+E)
Button(root, text=")", command=lambda:get_operation(")")).grid(row=4, column=5,sticky=W+E)

#Equal Button
Button(root, text="=", command=lambda:calculate()).grid(row=5, column=4,sticky=W+E,columnspan=2)




#App Start
root.mainloop()
