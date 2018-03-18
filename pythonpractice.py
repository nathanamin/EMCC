#Welcome to the simple python syntax tutorial for emcc

#First, let's run a simple print statement
#Here, "Hello World" is the string we are printing, which we envelop in quotation marks
print "Hello World"


#This is how you assign values to variables
changing = 3
print (changing)

changing = 9
print (changing)

different = 12
print (different)
print (changing)

red = 5
blue = 10
print (red, blue)

yellow = red
print (yellow, red, blue)

red = blue
print (yellow, red, blue)


#Here, we will learn to define functions
def add(x, y=5):
    """Return x plus y, optional"""
    return x + y
add(4)
add(8,3)


#Arrays! Matrices!
myList=[1,2,3,4,5,6]
print (myList)
print (len(myList))
#You can do this to .csv, .txt, or any data file you import

#Speaking of which... here is how you import data
#First, install pandas library (should probably also install numpy)

import pandas as pd
filename = 'Downloads/Video_Games_Sales_as_at_22_Dec_2016.csv'
data = pd.read_csv(filename)
data.head()


#For loops!

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# Prints out 0,1,2,3,4

#Here's a while statement for you
count = 0
while count < 5:
    print(count)
    count += 1
                # This is the same as count = count + 1



#Want to know how many components are in your string/array? Easy!
print (len("Hello, world!"))
