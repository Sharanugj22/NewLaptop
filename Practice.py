# # Convert string to list
# str1 = "this is python"
# print(str1.split(" "))
#
# # Convert list to string
# str1 = ['this', 'is', 'python']
# print(" ".join(str1))

# reverse string
# str = "this is python"
# reverse = "python is this"
# ss=str.split()
# d=""
# for i in ss:
#     d=i+" "+d
# print(d)

# Print each word in string in reverse order
# Output: yM emaN si lihkiN
# country_set = "My Name is Nikhil"
# ss = country_set.split()
# print("split", ss)
# ff=""
# dd = []
# #Type 1: with list
# for i in ss:
#     dd.append(i[::-1])
# print(" ".join(dd))
#
# #Type 2: without list
# for i in ss:
#     ff=i[::-1]
#     print(ff, end=" ")


# Input String str = "My Name is Nikhil"
# Print all the words separately one by one in separate line in Java
# Output:
# My
# Name
# is
# Nikhil

# country_set = ("My Name is Nikhil")
# ss=country_set.split((" "))
#
# for i in ss:
#     print(i)

# print value in pyramid.......................
# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# method-1:dd
# n=5
# for i in range(n):
#     # print(" "*(n-i)+" *"*(i+1))
#     print(" "*(i)+" *"*(n-i)) # rever pyramid
#
# #method-2:
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
# --------------
# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n-i):
#         print("*", end=" ")
#     print()
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# Print value in beluw format......................
# Ourput: below
# as
# asl
# aslm
# aslmk
# aslmkd

# a="aslmkd gghg"
# ss=[]
# for i in a:
#     ss.append(i)
#     print("".join(ss))
# ......................................................................
# sort the random numbers and print in reverse/Desc order.....
# a=(1,2,3,9,8,10)
# s=sorted(a)
# print("sorted values: ",s)
# print("Sorted and decrementing: ",a[::-1])

# Print numbers in reverse order............................

# a=(1,2,3,9,8,10)
# r=a[::-1]
# print("Sorted and decrementing: ",r)

# ..........................................................

# Write a code to find Lower cases for the above input......
# EX: Input — I Love Java & Selenium Webdriver
# str = "I Love Java & Selenium Webdriver"
# lower=[]
# for i in str:
#     k=i.islower() #check upper/lower case
#     j=i.isspace() # check for spaces
#     if k==True or j==True:
#         lower.append(i)
# print("Lower cases:","".join(lower))
#

# ..........................................................

# Print every word in reverse order ex: welcome to python to emoclew ot nohtyp.....

# str="welcome to python"
# splt=str.split()
# print(splt)
# for i in splt:
#     # print(i)
#     ss=i[::-1]
#     print(ss, end=" ")


# Print string in reverse order.....................
# Type-1
# srt="abcd"
# srt1=srt[::-1]
# print(srt1)

# Type-2
# srt="abcd"
# for i in reversed(srt):
#     print(i, end="")

# ..................................................

# Print even/odd number.............................
# for i in range(0,10+1):
#     if i%2 ==0:
#         print("even: ", i)
#     else:
#         print("Odd: ", i)
# ..................................................

# Print duplicate values............................
# a=[1,1,2,5,5,8,8]
# dup=[]
# dup1=[]

# for i in a:
#     if i not in dup:
#         dup.append(i)
#     else:
#         dup1.append(i)
# print(dup1)
# ...................................................

# Print duplicate values from two string............................
# s1="Java With Collections"
# s2="Java Selenium"
# a=s1 + " "+ s2
# b=[]
# print("The common letters are:")
# for i in a:
#     if i not in b:
#         str(b.append(i))
# print("".join(b))
