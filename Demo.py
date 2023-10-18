a=[1.1, 2.2, 2.6, 3.8, 'b', [3.1, 3.7, 1.2, 4.6], 'b']
# my_list2 = ['A', 'B', 'C', 'D', 'E', 'F']
# print(a.pop())
# print(a.pop(4))
# a.remove(1.1)
# print(a)
# del a[2][0]
# print(a)



# def pyfunc(r):
#     for x in range(r):
#
#         print(' '*(r-x-1)+'*'*(2*x+1))
# pyfunc(9)
#
# n=5
# for i in range(n):
# #method-1:dd
#     print(" "*(n-i)+"*"*(2*i+1))

# Fibonacci Series:----
# d=int(input('Enter number: '))
# num = '10jhjhj'
# n1, n2 = 0, 1
# n3=0
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(0, d+1):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#
#     print(n3, end=" ")
#
# print()

# if d in n4:
#     print("is a Fibonacci number",d, end=" ")
# else:
#     print(d," is not a Fibonacci number")

# print Even number EXX:: 0,2,4,6,8....
# odd=[]
# even=[]
# for num in range(0, 10 + 1):
#     # checking condition
#     if num % 2 == 0:
#         print("Even numbers are:", num)
#
#     else:
#         print("Odd numbers are:", num)

a=['d',1.1 , 2.1 ,3.1]
print(a)
ss=set(a)
print("Set: ", ss)
a.append(3.4)
print("Append 3.4: ",a)
a.extend([4.5,6.3,6.8])
print("Extend [4.5,6.3,6.8]: ",a)
a.insert(2,3.8)
print("Insert 2,3.8: ",a)

#
#
# from Tools.scripts.mkreal import join
# thislist = [100, 50, 65, 82, 23]
# thislist.reverse()
# print(thislist)
# thislist.sort(reverse = True)
#
# print(thislist)
#
#
#

# dds='dsutngthgtu'
# print(dds[::-1]) #1st type
# #for char in reversed(dds): #2nd type
# #	print(char)             #2nd type
#
#
#
# ee=[1,1,2,3,5,5,6]
# ss=[]
# fg=[]
#
# for i in ee:
#     if i not in ss:
#         ss.append(i)
#     else:
#         fg.append(i)
#
# print(fg)
# #
#
# dd=["sdfs","dasda"]
# ff=[1,5,6,8,9]
# dd.extend(ff)
# print(dd)
# #covert string
# a='ASDF'
# print(a.lower())
#
# #Remove number using pop or Remove
# my_list = [1, 2, 3, 4, 5]
# print(my_list.pop(2)) # remove using pop index value Ex: removed "3" from index 2
# my_list.remove(2) # remove using value not index number Ex: removed "2"
# print(my_list)
#
# #Print in reverse order.......................

# a = [1, 2, 3, 2, 1, 5]
# b = a[::-1]
# print("Reversed: ", b)
# b.sort()
# print("Sorted:", b)

# from pywinauto.application import Application
# from pywinauto.keyboard import send_keys
# from subprocess import Popen
#
# app = Application().start("Skype.exe")
# time.sleep(2)
