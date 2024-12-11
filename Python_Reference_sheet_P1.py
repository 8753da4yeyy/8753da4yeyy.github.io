#
#
# Allen Navas
# Reference Sheet P1.
# 07/30/2024
#
"""
The purpose of this reference sheet is to re-educate myself and to educate others of how to properly use data types, functions, and classes as well
as other things Python allows the user to do.
"""

# - Pound are used to make single line comments 

""" - Triple quotations are used to also make comments, but to comment out more than one line and end with another triple quotation.
""" 

# Data types
"""
# int - int(integer) is used for single digit variables
Example:
x = 10
y = 20
z = 30

# float - is used for decimal numbers 
Example:
x = 10.0
y = 20.0
z = 30.0

# str - str (String) is used for obtaining words.
Example:
x = "Ten"
y = "Twenty"
z = "Thirty"
"""

# Using print()
"""
print() will be used a lot as it is essential for any of the work to be outputed for the user to see in their works. it is used by simply typing.

print(x) <-- 'x' representing a variable. So if x is 10,  it will output 10 on the screen.
print("Hello World!") <-- This will output Hello, World! to the user.
"""

# Assigning variables
"""
Similar to what was done above, assigning data to a variable is as follows:

x = 10 <-- Assigns the variable 'x' with the digit 10. Declaring this varibale under the 'int' data type.
y = 10.0 <-- Assigns the variable 'y' with the decimal number 10.0. Declaring this variable under the 'float' data type.
z = "ten" <-- Assigns the varibale 'z' with the string word ten. Declaring this variable under the str data type.

"""

# Assigning variables with user inputs
"""
Python allows users to input their own data simply by using the function 'input()'. 
Example:

x = input();

You can also direct the user to type whatever is needed by adding a message prompt in parenthese.
Example:
"""
x = input("Please enter a number: ")

"""
There is a problem with the input function above. The problem being is without desinating a data type, the input function defaults to a string.
The statement above would have caused an error in the compiler because you would have asked the user to assign an integer to a string.
To avoid these errors you must add the data type before adding the input function. 
Example:
"""
x = int(input("Please enter a number: "))

"""
Now the input function should work because the int(input()) will now recognize the user input as a integer. Here are some of the other forms of these data-input functions below.

int(input()) - Obtain user inputs as an int casting
float(int()) - Obtain user inputs as a decimal number with float casting
str(input()) or input() - Obtain user inputs as a string with the string casting
"""

# Loops and Conditional Statements
"""
Before talking about loops, I wanted to make clear of these conditional operators. These operators help either loops or condition statements determine what the output will be.

Conditional Operators:
'<' - Less than
'<=' - Less than or equal to
'>' - Greater than
'>=' - Greater than or equal to
'==' - Equal to
'!=" - Not equal to

Loops are a function that will continuously repeat until a specific condition is met OR is called to end the loop. These loops are:

for():
while():

Note that in front of these loops contain a colon. The colon is used to tell the compiler that anthing after it is part of the loop.
Example:
"""

for x in range(10):
    print(x)
"""
The final output of this loop will show the numbers '0,1,2,3,4,5,6,7,8,9' because since x is equal 0 the loop will print x 10 times then add 1 to x.

Noticed the range() function? The range() function is used as a measurement condition for the loop to continue. The range() function can also be manipulated by adding a starting point
to the loop as shown below.
Example:
"""
for x in range(1, 10):
    print(x)
"""
Now, output will be, "1,2,3,4,5,6,7,8,9" because we told the range to start at 1. Skipping 0, but we still end the loop at 9 because x will end once it equals 10. 
So if we want our output to end at 10. We need to change the 10 to 11, but still start at '1'.
Example:
"""
for x in range(1, 11):
    print(x)
"""
Finally, the loop will output what we were asking for, "1,2,3,4,5,6,7,8,9,10". Loops can be helpful with obtaining data from the user or a file which will be demostrated later on.

While(): loops are used as a way to continue a loop until the condition is met. Once the condition is met, it will break the loop. The difference this time is while loops have a
greater chance of being looped infinitely because the condition DOES NOT UPDATE. Here is one example of a infinite loop.
Example:

while x < 1:
    print(x)
    
I would not recommend putting this in a IDE because all it will output is a unless string of '0'. We CAN however 'break' this loop by doing the following.
Example:
"""
while x < 1:
    print(x)
    break
"""
The 'break' operator ENDS the loop no matter if the condition is met or ends the program. It is useful for testing and if you want the user to continue onto the next loop. There is another operator
for 'continuing'
Example:

while x < 1:
    print(x)
    continue
 
 The 'continue' operator will allow the loop to proceed even though this will again cause an infinite loop. There are ways to make this work, but before that lets move to if statements.
 
 if-else statements are conditional statements that can be represented as true or false. Lets say x = 0.
 Example:
 """
 x = 0
 if x == 0:
    print("X is 0")
 else:
    print("X is not 0")
"""
From the given example, the output will be 'X is 0' because we know the variable x was assigned 0. if-else statements can be used in mountuous way, we even change the condition statement
by using what know as 'elif'. "elif" adds another condition to the existing if-else condition.
Example:
"""
if x == 0:
    print("X is 0")
elif x < 1:
    print("X is 0")
"""
See what I mean? Not only did the first condition check is x is equal to 0, NOW with elif it checks if x is not greater than 1. Still giving the same output 'X is 0'.
Let's go crazy, with if-else statements we can use 'if', 'elif', and 'else' all at the same time.
Example:
"""
if x == 0:
    print("X is 0")
elif x < 1:
    print("X is 0")
else:
    print("X is not 0")
"""
Remember the loops we used before? We can actually use all if-else statements in those loops and even those loops within themselves. 
"""

# Nested Loops
"""
Nested loops are loops within loops. There is no limit to how many loops we can use within themselves, just make sure not to lose track of what you are tring to achieve.
Here's an example of nested loops. Lets use while and for together.
Example:
"""
while x < 1:
    for x in range(10):
        print(x)
    x += 1 # This addition will end the while loop.
"""
What we have is a nested loop. The loop will start with the while loop, since x is less than 1. The loop continues to the for loop. Similar what we previously used in the for loop.
We have the loop print x 10 times, then after it does, it goes to the next line of the while loop with is x = x + 1, makes x to 1 which ends the while loop because x is equal to 1 now, not less than.

Here is another nested loop, using for loops only.
Example:
"""
for x in range(1, 11):
    for y in range(1, 11):
        print(x)
        print(y)
"""
As you see by now based on what the for loop is doing. It will print both x and y 10 times starting from '1' to '10'.

In these loops we can use if statements to add a layer of control in these loops. Rather than having it ONLY be automatated. 
Example:
"""
while x < 1:
    for x in range(1):
        if y == x:
            y = y + 1
            print("y is now 1")
        else:
            print("y is less than equal to X")
        x += 1
"""
What's happening here is the loop starts by checking the condition which is true, then it goes to the for loop which will loop ONCE it transitions to the next line which is the if statements.
Since y and x are both '0', the if statment will use the first branch result. That being it will add '1' to y, then prints "y is now 1". After words, tracking back into the for loop to add '1' to x effectivly ending the while loop.
"""

# Using loops for valid inputs
"""
Loops can be used to ask a user for information and you can use 'sentinals' to ensure the user has entered the correct requirement. 
'Sentinals' are used similar to conditions, the difference being is unless the user does or does not type a specific letter, word, or number. The loop will end.
Example:
"""
userinput = input("Enter a letter: ")
while userinput != "q":
    print("You have typed: " + userinput)
    userinput = input("Enter a another letter: ")
"""
In the example above, first the user will be asked to input a letter. Then the loop begins by checking the 'sentinal', as long as the user DOES NOT input 'q' the loop will continue. 

This concludes Part 1 of my Reference sheet.
"""