'''
#Write a program that takes two numbers as input and prints their sum.

while True:
    choice=input("do you want to start?")
    if choice=="no":
        print("you are quiting")
        break
    elif choice=="yes":
         num1=int(input("enter first number"))
         num2 = int(input("enter sec number"))
         sum= num1+num2
         print( "sum is:", sum)
    else:
        print("invalid text")

#Write a python program that checks whether a given number is even or odd.

while True:
    number=int(input("enter a number"))
    if number % 2 == 0:
        print("the number is even")
    elif number==0:
        print("the number is 0!!")
    else:
        print("the number is an odd number")

#Write a python program that calculates the factorial of a given number.

def factorial_recur(num):
    if num==0 or num==1:
        return 1
    elif num<0:
        print("cannot find factorial of negative number")
    else:
        return(num*factorial_recur(num-1))

num=int(input("enter a number"))
result=factorial_recur(num)
print(f"the factorial of {num} is :", result)



#Write a program that asks the user for their name and then prints a greeting message.
name=input("what is your name")
print(f"hello {name}! welcome to python programming")


#Write a program that takes a string input from the user and writes it to a text file.
samplefile=open("D:/python/demo2 text foc.txt",'w')
user_name=input("enter user name")
print("user name is:",user_name, file=samplefile)

#Write a program that reads the content of a text file and prints it to the console.
samplefile=open("D:/python/demo2 text foc.txt",'r')
content=samplefile.read()
print(content)

#Write a python program that takes a string as input and returns its length.
str1=input("Enter a string")
print("the length of the str1 is:", len(str1))

#Write a python program that concatenates two strings and returns the result.
str2="hello mam, I am Jaya,"
str3=" I am trying my best here"
str4=str2+str3
print(str4)

#Write a python program that checks if a substring is present in a given string.
str5="hello! welcome to the pythom and ml learning course"
print("welcome to " in str5)
print("ml learning course" not in str5)

#Write a python program that converts a given string to uppercase.
str5="hello! welcome to the pythom and ml learning course"
print(str5.upper())

#Write a python program that generates the first n numbers in the Fibonacci sequence. ______________________

#Write a python program that calculates the sum of the digits of a given number.
#I gave it a try!
num1=int(input("enter a two digit no."))
if num1<10:
    print("you entered 1 digit number!!")
elif num1==10:
    print("sum is 1")
else:


#Write a program that asks the user for their birth year and calculates their age



#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines
#I gave it a try!
def func1():
    input1 = input("what some lines about yourself")
while input1=='  ':
    input1 = input("what some lines about yourself")
    print("lines about you:", input1)

result=func1()
print(result)


#Write a program that reads data from a CSV file and prints it to the console.
samplefile=open("D:/python/python programming notes/username.csv", 'r')
content=samplefile.read()
print(content)


#Write a program in python that counts the frequency of each character in a string.
str2="hello i am jaya, welcome to python"
print("count of e:", str2.count("e"))

#Write a program in python that converts a given string to title case (first letter of each word capitalized)
str3="the greedy monkey"
print(str3.title())


#Write a python program that checks if two strings are anagrams of each other.


#Write a python program that removes all punctuation from a given string
str4="hello all!"

#Write a python program that takes a list of numbers and returns their sum.



#Write a python program that counts the occurrences of a specific element in a list.
list4=[33.33,4,5,23,56,"hello","wow","wow",4,3,4,3,3,3,3,3,3,4,65]
print(list4.count("wow"))

#Write a python program that returns the minimum and maximum values in a list of numbers
list4=[33.33,4,5,23,56,4,3,4,3,3,3,3,3,3,4,65]
print(max(list4))
print(min(list4))



#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

input2=float(input("enter temperature in celius or fahrenhiet"))
choice=input("Select 'C' for celcius and 'f' fahrenhiet").strip()
while True:
          if choice.upper()== "C" or choice.lower()=="c":
              fahrenheit=input2*9/5+32
              print("the temperature in fahrenheit is:",fahrenheit.__round__())
              break
          elif choice.upper()=="F" or choice.lower()=="f":
               celsius=(input2 - 32)*5/9
               print("the temperature in celcius is:",celsius.__round__())
               break
          else:
              print("invalid option")
              choice = input("Select 'C' for celcius and 'F' fahrenhiet").strip()

#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
num1=int(input("enter first number"))
choice=input("choose mathematical operator")
num2=int(input("enter sec number"))
if choice== '+':
    result=num1+num2
    print("the solution is :",result)
elif choice == "-":
    result = num1 - num2
    print("the solution is :",result)
elif choice == "*":
    result = num1 * num2
    print("the solution is :",result)
elif choice == "/":
    result = num1 / num2
    print("the solution is :",result)

#Write a program that copies the contents of one text file to another.

#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix

string = input("Enter the string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

if string.startswith(prefix):
    print(f"The string '{string}' starts with the prefix '{prefix}'.")
else:
    print(f"The string '{string}' does not start with the prefix '{prefix}'.")

if string.endswith(suffix):
    print(f"The string '{string}' ends with the suffix '{suffix}'.")
else:
    print(f"The string '{string}' does not end with the suffix '{suffix}'.")
'''
#Write a program in python that converts a string into a list of its characters
str6="hello students"
print(list(str6))

















