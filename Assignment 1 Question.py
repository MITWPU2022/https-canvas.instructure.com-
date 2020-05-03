#!/usr/bin/env python
# coding: utf-8
# Session 1
 Assignment 1 Question
Session 1: Assignment 1
Table of Contents
1. Introduction
2. Problem Statement
3. Output
1. Introduction
This assignment will help you to consolidate the concepts learnt in the session.
2. Problem Statement
Task 1:
1.
Install Jupyter notebook and run the first program and share the screenshot of the output.
LINK
2.
Write a program which will find all such numbers which are divisible by 7 but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line.
3.
Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name.
4.
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r
3
Task 2:
1.
Write a program which accepts a sequence of comma-separated numbers from console and
generate a list.
2.
Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
3.
Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: AcadGild
Output: dilGdacA
4.
Write a Python Program to print the given string in the format specified in the sample output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
Sample Output:
WE, THE PEOPLE OF INDIA,
having solemnly resolved to constitute India into a SOVEREIGN, !
SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
and to secure to all its citizens
NOTE: The solution shared through Github should contain the source code used  and
the screenshot of the output.
3. Output
N/A
# # ------------------------------------------Task 1:---------------------------------------------

# # Task 1-Q1.Install Jupyter notebook and run the first program and share the screenshot of the output.

# In[1]:


#Task 1 Q1 output
#Link :- https://github.com/diemscse/https-canvas.instructure.com-/blob/master/Screenshot%20(178).png


# # Task 1-Q2.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[2]:


#output of Q2 (solution approach 1)
for n in range(2000,3201,1):
    if n%7==0 and n%5==0:
        print(n,end=', ')


# In[3]:


#output of Q2 (solution approach 2)

nl=[]
for x in range(2000,3201,1):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


# # Task 1 Q3. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
# 

# In[4]:


#output of Q3 (solution approach 1)

getFirstName=input("Enter your name: ")
getLastName=input("Enter uour last name: ")
print(getLastName,getFirstName,sep=' ')


# In[5]:


#output of Q3 (solution approach 2)

getFirstName=input("Enter your name: ")
getLastName=input("Enter uour last name: ")
print(getFirstName[::-1],getLastName[::-1],sep=' ')


# # Task 1 Q.4 Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r3

# In[6]:


#output of Q4 (solution approach 1)
import math
print(4/3*math.pi*6**3)


# In[7]:


#output of Q4 (solution approach 2)
print(((4/3)*3.1415926535897931)*6**3)


# # ------------------------------------------Task 2:---------------------------------------------

# # Task 2 Q1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list

# In[8]:


#output of Q1 (solution approach 1)
print(list(input().split(",")))

#Task 2 Q2 Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
# In[9]:


#output of Q1 (solution approach 1)
for i in range(5):
    for j in range(i):
        print('* ',end='')
    print('\n')
for j in range(5,0,-1):
    for i in range(j,0,-1):
        print('* ',end='')
    print('\n')


# # Task 2- 3. Write a Python program to reverse a word after accepting the input from the user.  Sample Output:  Input word: AcadGild Output: dilGdacA

# In[12]:


#output of Q3 (solution approach 1)
print('Output:',input("Input word: ")[::-1])


# # Task 2- 4.Write a Python Program to print the given string in the format specified in the sample output.WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens Sample Output: WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, ! SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens
# 

# In[13]:


#output of Q4 (solution approach 1)
print("WE, THE PEOPLE OF INDIA,")
print("\t having solemnly resolved to constitute India into a SOVEREIGN, !")
print ("\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC")
print ("\t\t  and to secure to all its citizens")

