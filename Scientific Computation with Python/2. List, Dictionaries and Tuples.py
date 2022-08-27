print("-----------------------------------\nLists\n-----------------------------------")
#Lists
"""
Lists is a collection of related values (Can be any data type) surrounded by Square Brackets. For example
"""
print("")
exampleList = [5, 4, True, 2.01, 1, "This is a string!"] #This is how you create an List! An array would use {}
print("Print the content of a List!")
print("This is inside exampleList: ", exampleList)

print("\nUsing a For Loop to iterate through each element!")
for i in exampleList: #We can use a FOR LOOP to iterate through each elements.
    print(i)

print("\nThe size of exampleList (using len()) is: ", len(exampleList)) #Returns the size of a List

"""
You can access elements in a list using its index. Modifying them is also possible
"""
print("\nAccessing elements in a List (Index 5")
print(exampleList)
print("\nIndex 5 stores: " + exampleList[5]) #Accesing an element

"""
Lists are Mutable, meaning that we can change an element on a list. Strings are example of immutable where you can't change a character in it. You require to make a whole new string
"""
exampleList[5] = "Now it's this string!" #Modifying an element
print("Modifying Index 5\nIndex 5 stores: ", exampleList[5])

"""
The range() function creates an list from 0 to n-1 (Incremental) which we used for FOR LOOPS
"""
exampleList2 = [x for x in range(4)] #This is list comprehension
print("Ways to use FOR Loops\nExample 1:")
for number in exampleList2:
    print(number)
print("Example 2:")
for i in range(len(exampleList2)): #This is an Index Loop where range() returns a list of numbers from 0 to n-1
    print(exampleList2[i])

"""
You can use the concatenating operator (+) to append a list to another list! Much like for strings
"""
a = [1,2,3]
b = [4,5,6]
c = a + b
print("Concatenating Lists a and b: ", c)

"""
You can also get a specific section of a List using listName[Index1:Index2]
"""
print("First 2 elements of List C: ",c[:2]) #We want all numbers up to, and not including, index 2
print("Get the 2 elements starting from index 3 of List C: ", c[2:4]) #Include elements from Index 2 and to, but not including, Index 4
print("Last elements of List C from index 4: ", c[4:])

"""
Other List Methods: https://docs.python.org/3/tutorial/datastructures.html
"""

exampleList3 = list() #This is how we create an empty list
exampleList3.append(3)
exampleList3.append("Hello")
exampleList3.append(True)
print("\nDeclaring an empty list and adding to it: ", exampleList3)

"""
There are many useful methods for Lists, which we can help with a lot of things. These methods takes in a List of purely just numbers:
    min - gets the smallest
    max - gets the biggest
    sum - gets the sum of all the numbers in the list
"""

"""
Let's say that we want to go through a string. We can use the split() method to break the string into pieces and produce a list of strings.
"""
stringExample = "This is a test!"
stringList = stringExample.split() #This splits each word whereever there is a space (Which is the default delimiter)
print("\nString: ", stringExample, "\nSplitting a String and printing it:", stringList) #Now we can iterate through each element
"""
The delimiter tells the program how we want to split the word. It means that anything after a delimiter character is what we want to store in the List.
Say that the delimiter is ';' then the follow string ('1;2     ;3;;;4') will be split to: [1, 2     , 3, 4]7
    If there is no character after a delimiter then it is not included
"""
print("\n\n")
print("-----------------------------------\nDictionaries\n-----------------------------------")
#Dictionaries
"""
Dictionaries is a data type where we store values in a sort of 'key-value- pair -> They're like HashMaps in Java
"""

