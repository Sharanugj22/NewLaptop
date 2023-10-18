# Write a program in Python to check if a number is prime.
# num = int(input("Enter input: "))
# If given number is greater than 1

# for i in range(2, num):
#     # If num is divisible by any number between
#     # 2 and n / 2, it is not prime
#     if (num % i) == 0:
#         print(num, "is not a prime number")
#         break
# else:
#     print(num, "is a prime number")

# Write a program in Python to check if a sequence is a Palindrome.
# input=output
# a=input("Enter input: ")
# b=a[::-1]
#
# if a.upper()==b.upper(): #this ignores cases
#
#     print("{} eqauls {}".format(a,b))
# else:
#     print("{} not eqauls {}".format(a,b))


# count the number capital letters in a string
val="Welcome To Python"
count=0
for char in val:
    if char.isupper():
        print(char, end=" ")
        count += 1

print("total: {}".format(count))


# sorting algorithm
# list=[1,2,5,0,8]
# list.sort()
# print(list)
