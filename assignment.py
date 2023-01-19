## Assignment Part-1
#Q1. Why do we call Python as a general purpose and high-level programming language?

#ans- Due to versatility along with its beginner freendleness has made it one of the most used
     #programming languase along with it also convert high level code to low level code i.e 
     #(compiter-- interpreter)

Q2. Why is Python called a dynamically typed language?

# ans-- it called dynamically because the python interpreter does type checking only as code 
         # run, and the type of variable is allowed to change over its lifetime

# Q3. List some pros and cons of Python programming language?

# ans-- PROS are (flexible , embeddable , we can allowed to change variable over its lifetime.)
       # CONS are (high memory consumption , slower than other languages speed , 
       # also have runtime error due to[dynamical typing feature])

# Q4. In what all domains can we use Python?

# ans -- the domin are (Data science , machine learning , A.I ,Web development , Networking )

# Q5. What are variable and how can we declare them?

# ans -- variable is a name given to specific memory location 
#  we declare variable name should start with alphabet 
# we can use underscore(-) as a part of variable
#  we can't use any special character or symbol
 
# Q6. How can we take an input from the user in Python?

# ans -- we can use input () function 
name = input()
age = input()
location = ()
print("user name = ",name)
print("user age = ",age)   # we need to give input
print("user location = ",location)

# Q7. What is the default datatype of the value that has been taken as an input using input() function?

# ans -- default data type return are a string..

# Q8. What is type casting?

# ans -- type casting convert one data to another 

# Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

# ans -- i don't know answer ??

# Q10. What are keywords?

# ans -- keywords are used to define the syntex of the coading
#     e.g. break , for ,if , lamda 

# Q11. Can we use keywords as a variable? Support your answer with reason.

# ans -- no we cannot use keyward as a vareable name they are used to define syntex
#        strc. of python language 

# Q12. What is indentation? What's the use of indentaion in Python?

# ans --it refer to spaces at the beginning of code line , the use are it indicate a block of code

# Q13. How can we throw some output in Python?

# ans --  we use proper syntex and than give print statement. 

# Q14. What are operators in Python?

# ans --   operator is a character or characters that determine the action that is to be performed
# e.g. numerical operators , assignment operator , camparision operator (the value that operator act
# on are called opperand)

# Q15. What is difference between / and // operators?

# ans --/ for float division // for integer division 

# Q16. Write a code that gives following as an output.
# iNeuroniNeuroniNeuroniNeuron

# ans 
multiply_numeric_str = "iNeuron"*4
print("Multiply numeric str = ", multiply_numeric_str)

# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

#ans 
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# Q18. What are boolean operator?

# ans --  Boolean type is one of Python's built-in data types. It's used to represent the truth
#  value of an expression ( it is true or false)

#Q19. What will the output of the following?

1 or 0

0 and 0

True and False and True

1 or 0 or 0

# ans --
# (or) for it return true if one statement are true 
# (and) for it return true if both the statement are true 

m = 1
n = o 

print("m>0 and n<1", m>0 and n<1)
print("m>1 or n<1", m>1 or n<1)
print("not (m>1 or n<1) Result",not(m>0 and n<1)

# Q20. What are conditional statements in Python?

# ans -- it is the name suggested itself it is use to handle condition in our program
# e.g - [if-else]

# Q21. What is use of 'if', 'elif' and 'else' keywords?

# ans -- it is used in python for desicision making

# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". 
# If age is < 18 display "I can't vote".

# ans --

# Q23. Write a code that displays the sum of all the even numbers from the given list.
#        numbers = [12, 75, 150, 180, 145, 525, 50]

# ans -- 
int_list = [12, 75, 150, 180, 145, 525, 50]
for num in int_list:
   if num%2 == 0:
        print("Even number in the list = ",num)


# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

# ans --
num1 = 10
num2 = 20
num3 = 5



if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)

# Q25. Write a program to display only those numbers from a list that satisfy the following conditions
#  numbers = [12, 75, 150, 180, 145, 525, 50]

- the number must be divisible by five

# ans--
int_list = [12, 75, 150, 180, 145, 525, 50]
for num in int_list:
   # print("Current element of the list = ",num)
   if num%5 == 0:
        print("Divisible by five in the list = ",num)

-# If the number is greater than 150, then skip it and move to the next number

# ans --
a = [12, 75, 150, 180, 145, 525, 50]
b = []
for i in a:
    if i > 150:
        if i > 500:
            break
        continue
if i % 5 == 0:
        b.append(i)
print(b)


-#If the number is greater than 500, then stop the loop

# ans --
a = [12, 75, 150, 180, 145, 525, 50]
b = []
for i in a:
    if i > 500:
        if i > 500:
            break
