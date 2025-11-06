import sys

# sys._getframe().f_code.co_name can be used to print the name of the current function

def whileLoop_return():
    print("In function", sys._getframe().f_code.co_name)
    while True:
        return
    print("End of function", sys._getframe().f_code.co_name)
        # This doesn't print because the function has already returned in the while loop

def whileLoop_break():
    print("In function", sys._getframe().f_code.co_name)
    while True:
        break
    print("End of function", sys._getframe().f_code.co_name)

def whileLoop_continue():
    print("In function", sys._getframe().f_code.co_name)
    while True:
        continue
        # This while loop will never end
    print("End of function", sys._getframe().f_code.co_name)
        # this line does not print because the while loop before never ends

whileLoop_return()
whileLoop_break()
whileLoop_continue()
