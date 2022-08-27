"""
Files are stored in the Secondary Memory of a Computer, we may want Python to read from them!
    - Text Files can be thought as a sequence of lines

In order to read the contents of a file, we need to tell python which file we want to work with and what we are going to do with it.
    1. We use open() to return a 'file handle' which is a variable that can be used to perform operations on it
        - for example: `handle = open(filename, mode)`
            - handle - variable name and allows us to interact with the file (sort of like a bridge)
            - filename - name of the file
            - mode - tells pythong if we want to 'r'ead or 'w'rite. This is optional!
"""

fhandle = open('./files/mbox.txt')
print(fhandle) # This won't really print out the entire text file, only details about the handle
print()

"""
The `newline` character is a special character to tell python that there needs to be a new line.
For example: 
Hello\nthis\n\nis\ncool will print out:
    Hello
    this
    
    is
    cool

\n is treated as a single character so H\nY will be 3 characters long

You may not see it in the textfile but EVERY line ends with a newline character which allows python (and everyone) know where the line ends

"""

#Printing the contents of a textfile and number of line:
file = open('./files/mbox.txt')
count = 0
print("Using definite iteration to print the textfile")
for line in file: # We are treating the textfile as a sequence of strings where each line is a string so this loop goes through each line and prints it out
    line = line.rstrip()#Print will ALWAYS add \n to the end of each line so you may see gaps. So we do this to elimite any whitespaces
    print(line)
    count = count + 1
print("\n\nLine Count: ", count)
file.close()




"""
You can also read the ENTIRE textfile into a single string (Includes newlines as well) using read()
"""
file = open('./files/mbox.txt')
print("\n\nUsing read() to print the textfile")
readfile = file.read() #Creates a single string of the entire textfile
print(readfile) #readfile should be: 'hello\nthis\nis\n\na\ntest\nfor\nfile\nreading'
file.close()

"""
You can also search through a file for a specific things using if statements in the for loop
"""
print("\n\nLooking for line starting with 'test'")
file = open('./files/mbox.txt')
for line in file:
    line = line.rstrip()
    if line.startswith('test'):
        print(line)
file.close()

print("\n\nLooking for line starting with 'test' using 'continue' keyword")
#The keyword 'continue' works similar to 'break' in loops. Instead of stopping the entire loop, it goes to the next item!
file = open('./files/mbox.txt')
for line in file:
    line = line.rstrip()
    if not line.startswith('test'):
        continue
    print(line)
file.close()

print("\n\nLooking for lines that contains 'ignore this' in the line")
file = open('./files/mbox.txt')
for line in file:
    line = line.rstrip()
    if not 'ignore this' in line: #If the line does not contain 'ignore this' we move to the next
        continue
    print(line)
file.close()

"""
Sometimes, you may also ask the user to enter the name of a file! Remember you can get good and bad file names.
The code below allows the code to do something if the user enters an invalid file
"""
fname = input("Enter the name of the file here: ")
try:
    fhand = open(fname) #Opens a file handler for the file they want to access but if they enter an invalid file then an error will occur hence the try-execpt statement
except:
    print("Unable to open ", fname)
    quit() #Ends the entire code - optional


