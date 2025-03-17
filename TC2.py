#write print how many repeated charcter in string with count numbers
#
# i = 'vishvishrajraj'
# s = {}
# for a in i:
#     if a in s:
#         s[a] +=1
#     else:
#         s[a] = 1
#
# print(s)

#with using keyword
# i = 'hdhdhsbhsdfbsdbf'
# s = {}
# for a in i:
#     s[a] = s.get(a,0) + 1
#
# print('reapeted charcter:\n',s)

# i = 'jsverymusheasyforthehight'
# p = {}
# for a in i:
#     p.setdefault(a,0)
#     p[a] +=1
# print('repeated string:\n'+str(p))

#revese of string with list and without list and without keyword

# i = 'reveenfnfnfnfnf'
#
# # s = i[::-1]
# # print(s)
# #
# # a.append(i)
# # print(a)
# s = ''
# for a in i:
#     s = a + s
# print(s)

#write code reverce list string

# i =['jdff','gdgdg','dhdhdh','dhdhdhd']
# s = []
#
# for a in i:
#     s = [a] + s
# print(s)

#write code all type of number and string and spcial charcter sapreate it first number second charcter last special

# s = '12jsdbjsfbj33&2dcd&*?!#'
# t = ''
# l = ''
# k=''
# for i in range(len(s)):
#     if s[i]>='a' and s[i]<='z':
#         t=t +s[i]
#     elif s[i]>='0' and s[i]<='9':
#         l=l+s[i]
#     else:
#         k +=s[i]
# print(t,l,k)

# write code count the number of elements in list without using keyword

# l = ['hheh','heheh','hdhdh','klsnn']
# n=0
# for i in l:
#     n+=1
# print(n)

#in string

# l = 'shdhdhdhdhdh'
# n=0
# for i in l:
#     n+=1
# print(n)

#with this code 'a' how many repeated in this string print total
# l = 'shashank'
# n=0
# for i in l:
#     if i=='a':
#         n+=1
# print(n)


# l = 'vishwarajvish'
# k=0
# for i in l:
#     if i == 'i':
#         print('i is ther in the string')
#     else:
#         print('not there')
#         k +=1
# print(k)

#write code to print total string and number using txt file
# with open('h.txt',mode='r') as f:
#     s = 0
#     l = 0
#     for i in f:
#         if i>='a' and i<='z':
#             s += 1
#         elif i>='0' and i<='9':
#             l +=1
#     print(s)
#     print(l)

# f = 'ijklmnopqrstuwxyzi'
# p = ''
# for i in f:
#     if i == 'i':
#         p += i
#     else:
#         print(f.count(i))
#
# print(p.count(i))


#find duplicate values in given list and print list first values and last duplicate values with one list
# P = [1,2,3,4,2,3,4,5,6]
# list = []
# k =[]
#
# for i in P:
#     if i not in list:
#         list.append(i)
#     else:
#         k.append(i)
# print(list+k)

#basic factorial program

# f =1
# u = int(input("enter a number:"))
# if u<0:
#     print("factorial cannot find")
# elif u==0:
#     print('factorial is always 1')
# else:
#     for i in range(1,u+1):
#         f = f * i
#     print(f)

# p = [1,2,3,4,5,6]
# k =[]
# for i in p:
#     for j in p:
#         k = i + j
#     print(k)

# f = 'finally i am learning python'
# l =0
# for i in f:
#     if i == 'a':
#         l  = l + 1
# print(l)

# k = input("enter the string:")
# for i in range(len(k)):
#     k = k[:-1:]
# print(k)

#this code is append dictionary into the txt file...
# import json
# i = {1:'hhh',2:'rrr'}
# with open('h.txt', mode='w')as f:
#     f.write(json.dumps(i))

#reverse of string
# s = 'thefirsttime'
# p = ''
# for i in s:
#     p = i + p
# print(p)


# for i in range(len(l)-1,-1,-1):
#     k = l[i]
#     print(k)


# L = [1,24,44,55]
# P = []
# for i in L:
#     P = [i] + P
# print(P)

# l = [1,2,3,4,5]
# p = []
#
# for a in l:
#     p = [a] + l
# print(p)
#
# l = [1,2,2,3,4]
# p = []
# for i in l:
#     p = [i] + p
# print(p)
# print([i- 1])

# l = 'abcd'
# p = ''
# for i in l:
#     p = i + p
# print(p)

# i = 10
# j = 20
# print((i>j and "i>j" or j>i and "j>i"))


#a1b3c7d9 -->[1,9,49,81]
# s = 'a1b3c7d9'
# d = ''
# l =[]
# for i in s:
#     if i >= 'a' and i<='z':
#        d += i
#     else:
#         l += [int(i)**2]
#         # m +=[l**2]
# print(l)
# print(d)

#write code compare both string and sparate common in both string
# l = 'vishwa raj'
# t = l.split()
# # print(t)
# f = set()
# for i in t[0]:
#    for j in t[1]:
#        if i == j:
#            f.add(j)
# print(f)

# l1 = [1,2,3,4,5,]
# l2=[6,7,8,9,5]
# l3=[22,33,44,5,66]
# l4 = l1.count(5)+l2.count(5)+l3.count(5)
# print(l4)

# l4 = []
# for i in l1:
#     for j in l2:
#         for k in l3:
#              if i == j:
#                  l4.append(j)
#
# print(l4)

#reverse of string
# l = 'qwertyuio'
# p = list(l)
# p1=len(p)
#
# while p1>0:
#     for i in p[p1-1]:
#         p1 = p1 - 1
#     print(l[p1])


# pattern code
# for i in range(0,6):
#     for j in range(i):
#         p  = j + 0
#         print(p,end=' ')
#     print()

# l = '*'
# for i in l:
#    if i =='*':
#         i += l
#    else:
#         print(i)

# for i in range(5):
#     for j in range(i):
#         print('*',end=' ')
#     print()

# list1 = [10, 20, 30, 40, 50]
# l = reversed(list1)
# for i in l:
#     print(i)

# for i in list1[::-1]:
#     print(i)

# k = len(list1) -1
# for i in range(k,-1,-1):
#     print(list1[i])
# for i in range(5):
#     print(i)
# else:
#     print('Done!')

# pattern solove----------------
# l = 5
# i = 0
# n=''
# while l>=i:
#     p = '*'
#     i+=1
#     n+=p
#     print(n)


# for i in range(-10,0):
#     print(i)

# i = 10
# while i<0:
#     print(i)
#
# k = -10
# l = reversed([k])
# for i in l:
#     print(i)
#
# def mu(a,b):
#     i = a * b
#     if i <=1000:
#         return i
#     else:
#        return a + b
#
# l = mu(20,30)
# l1 = mu(40,30)
# print(l,l1)

# def l(a,b):
#     if a > b:
#        print("a is greater then b")
#     else:
#         print('b is lessthen')
#
# d = l(10,9)

# else:
#     print('b is greater ')

# def new(num1):
#     return num1 + num1
#
# for i in [1,2,3]:
#     l = new(i)
#     print(l)

# a = 10 + 11j
# print(a.real)
# print(a.imag)

#slice method [begin:end:step] begin start with 0 \ end will -1 with range \ step skip middle based on your input

# l,j = int(input("enter the numbsers"))
#
# if l>1 and j<1000:
#     i = l * j
#     print(i)
#pythonkeyword questions solving--------------------
# l,j = map(int, input("enter the number").split())
# def w(l,j):
#     p = l * j
#     if p>1000:
#         p = l + j
#         print(p)
#     else:
#         return p
#
# f = w(l,j)
# print(f)
#my method
# p = 0
# for i in range(10):
#     p = i-1
#     print('current number:',i,'previous number:',p,'sum:',p+i)

# previous_num= 0
#
# for i in range(10):
#     sum = previous_num + i
#     print('current number:',i,'previous number:',previous_num,'sum:',sum)
#     previous_num = i
#patter question
# k=6
# for i in range(1,k):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print(' ')

#reverse pattern question

# k = 5
# n = 5
# for i in range(0,k+1):
#     for j in range(n-i,0,-1):
#         print(j,end=' ')
#     print(' ')



# u =int(input("enter the number:"))
# sum = 0
# for i in range(1,u+1):
#     sum = sum + i
# print(sum)

# for i in range(1,11):
#     print(i*2)

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i>500:
#         break
#     elif i>150:
#         continue
#     elif i % 5==0:
#         print(i)

# num = 75869
# counter = 0
# while num!=0:
#     num = num//10
#     counter+=1
# print(counter)

# num = 6
# for i in range(1,num-1):
#     print(i)
#
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print(' ')

#Three type of reverse list--------
# List1 = [10, 20, 30, 40, 50]
# list = reversed(List1)
# for i in list:
#     print(i)

# l = len(List1)-1
# for i in range(l,-1,-1):
#     print(List1[i])

# for i in range(len(List1)-1,-1,-1):
#     print(List1[i])

# import random
#
#
# # class name:
# #     def __int__(self):
# #         print("hi")
# # class hello:
# #     def __init__(self):
# #         print("hello")
# #
# # i = int(input("enter the number"))
# # if i<10:
# #     raise Exception("entered numver",name)
# # elif i<10:
# #     raise hello
# # else:
# #     print("please enter the correct")
#
# #
# # class myclass:
# #     def __init__(self):
# #         self.var = 100
# #         self.var1 = 100
# #         self.var2 = 200
# #     def m1(self):
# #         del self.var2
# #
# # obj = myclass()
# # obj.m1()
# # print(obj.__dict__)
#
#
# l = ["iajnnakooadkjaidadi"]
#
# p = 0
# k = input("enter the word:")
# for i in range(len(l)):
#     if l[i] == 'a' and l[i]=='z':
#         if k in l[i]:
#             p+=1
# print(p)
#
# #enter the input as number and get out as words
#
#
# import inflect
#
# def number_to_word():
#     p = inflect.engine()
#     words = p.number_to_words(user)
#     return words
#
# user = int(input("enter the numbers:"))
# result = number_to_word()
# print(result)


# L = 'ADKLNALKSDNON'
#
# p = {}
#
# for i in L:
#     if i in p:
#         p[i] +=1
#     else:
#         p[i] = 1
# print(p)
# #


# function methons practice
# def calculate_area(radius=3.14):
#     return 3.14 * (radius ** 2)
#
# l = calculate_area()
# print(l)


# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# i = int(input("enter the numbers"))
# print(is_even(i))
#


# def reverse_string(l):
#     return l[::-1]
#
# i = input("enter the string :")
#
# print(reverse_string(i))

# def count_vowels():
#     count=0
#     for h in i:
#         h.split()
#         if h in k:
#             count+=1
#     print(count)
#
# k = ["a","e","o","i","u"]
# i = input("enter the string")
# count_vowels()

# def count_sun(s):
#     cout = 0
#     vowel = ['a','e','i','o','u']
#     for char in s:
#         if char.lower() in vowel:
#             cout+=1
#     return cout
#
#
# n = input("enter the string")
# print(count_sun(n))

#desending order
#
# list = [20,30,10,40,60,50]
#
# for i in range(len(list)):
#     index = i
#     for j in range(i+1,len(list)):
#         if list[index] < list[j]:
#             index = j
#     list[i],list[index] = list[index],list[i]
#
# print(list)

#Asending order
# l = [10,30,40,20,60,50]
#
# for i in range(len(l)):
#     index = i
#     for j in range(i+1,len(l)):
#         if l[index] > l[j]:
#             index = j
#     l[i],l[index] = l[index],l[i]
# print(l)


# l = [9,8,4,2,4,1,3]
#
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:                               #< and > is order
#             l[i],l[j] = l[j],l[i]
#
# print(l)

# r = ["dsae"]
# p = ""
# o = []
# for i in r:
#     for j in i:
#         p = j + p
#     o = [p] + o
#     print(o)
# import tkinter as tk
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# frame = tk.Frame(width="20")
# button.pack()
# r.mainloop()


# reverse the each words in string
# str = 'My Name is Jessa'
#
# p = str.split()
# t = ''
# for i in p:
#     o = i[::-1]
#     t+=o
# print(" ".join(t))


#reverse the values only in dic
# ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
#
# revers = {value : key for key,value in ascii_dict.items()}
# print(revers)


#Display all duplicate items from a list

# sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
#
# l = {}
#
# p = []
#
# for i in sample_list:
#     if i not in l:
#         l[i] = 1
#     else:
#         p.append(i)
# print(p)
#
# d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
#
# l1 = ['A', 'C', 'F']
#
# p = {}
# for i in l1:
#     if i in d1:
#         p[i] = d1[i]
#     else:
#         p[i] = None
# print(p)

#in list which is greatest number
# l = [10,20,30,40,50]
#
# k = l[0]
# for i in l[1:]:
#     if i >k:
#         k = i
# print(k)


#reverse of list

# l = [10,20,30,40,50]
#
# p = len(l)-1
#
# for i in range(p,-1,-1):
#     print(l[i])

# n = int(input("enter the row"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(""*(n-j) ,"*"*j,end="")
#     print()


#print duplicate values in list

# list1 = [10,20,30,30,20,50,50]
#
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#     else:
#         print(i)


# u = input("enter :")
# o = 0
# y = 0
# for i in u:
#     if i>='a' and i<='z':
#         o+=1
#     elif i >= '0' and i <= '9':
#         y+=1
#         # print(i.count("digits:"+i))
#
# print("letters",o)
# print("digits",y)

#
# u = input("enter:")
#
# o = 0
# p = 0
# for i in u:
#     if i == i.upper():
#         o+=1
#     elif i == i.lower():
#         p+=1
# print("upper latter:",o)
# print("lower latter",p)

#
# u= input("enter the password:")
#
# l = ''
# l2 = 0
# if u>='a' and u<='z':
#     o = u.split()
#     if o == u[1]:
#         l+=u
# elif u>='A' and u<='Z':
#     l+=u
# elif u>='0' and u<='9':
#     l+=u
# else:
#     l+=u


#
# p = [1,2,2,3,4,4,5,7]
#
# l = {}
# k = []
# l2 = []
# for i in p:
#     if i not in k:
#         k.append(i)
#     else:
#         l2.append(i)
# print(l2)

#
# import random
#
# dice = 0
#
# while dice >=100:
#     user1= random.randint(1,6)
#     user2 = random.randint(1,6)
#
#     print(user2)


# write program given string , convert in dictionary with key as numbers and string is value


# l = "abcd"
#
# d = {}
# n = 0
# for i in l:
#     n+=1
#     d[n] = i
# print(d)



# sorting list
# l = [10,20,330,40]
#
# for i in range(len(l)):
#     for j in range(0,len(l)-i-1):
#         if l[j] > l[j+1]:
#             l[j] , l[j+1] = l[j+1],l[j]
#
# print(l)


# find middle in the list

# l = [10,30,40,50,60,30,50,60]
#
# midle = int(len(l)/2)
#
# print(l[midle])


# def new(a,b):
#     try :
#         c = a / b
#         print(c)
#     except ZeroDivisionError:
#         print("please provide atleast 1")
# new(10,0)



# k = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
#
#
# for i in range(len(k)):
#     for j in range(i,len(k)):
#         if k[i] > k[j]:
#             k[i] ,k[j] = k[j] , k[i]
# print(k)


# l = "my name is vish"
#
# k = l.capitalize()
# print(k)
# k =l.split()

# for i in k:
#     if i in k[:]:
#         h = i.split(",")

# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class SLL:
#     def __init__(self):
#         self.head = None
#
#     def display(self):
#         temp = self.head
#         if self.head is None:
#             print("empty")
#         else:
#             while temp:
#                 print(temp.data,"-->",end="")
#                 temp = temp.next
#
# l = SLL()
#
# n = node(10)
# l.head = n
# n1 = node(20)
# l.head.next = n1
# n2 = node(30)
# n1.next = n2
# n4 = node(40)
# n2.next = n4
#
# l.display()

#second largest number in list print
#
# def secondlargest(lst):
#     if len(lst)<2:
#         return None
#     first , second = float('-inf'),float('-inf')
#
#     for num in numbers:
#            if num>first:
#             second = first
#             first = num
#         elif first>num>second:
#             second = num
#
#     return second if second != float('-inf') else None
#
# numbers = [10,20,304,40]
#
# print(secondlargest(numbers))


# easy method

# l = [10,20,304,40]
#
# first = 0
# second = 0
# t = 0
# for i in l:
#     if i>first:
#         second = first
#         first = i
#     elif first>i>second:
#         second = i
#
# print(second)


# find prime numbers
#
# start = 1
# end = 10
#
# for i in range(start,end+1):
#     if i >1:
#         for j in range(2,i):
#             if (i%j) == 0:
#                 break
#         else:
#             print(i)


#string palindrome checking

# def palindrome(s):
#     return s == s[::-1]
#
# user = input("enter the string to check:")
# k = palindrome(user)
#
# if k == True:
#     print("its palindrome")
# else:
#     print("not palindrome")


# Write program count number of occurrence string and based on frequency sort
# l = "orange, apple, banana, apple, apple,banana caret,"
#
#
# g = l.split()
# d = {}
#
# for i in g:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i] = 1
#
# a = sorted(d.items(), key =lambda x : x[1])
# print(a)


# descending order

# s = "apple, banana, orange, apple, banana, banana,"

# l = s.split()
# d = {}
# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
#
# f = sorted(d.items(),key=lambda x : x[1],reverse=True)
# print(f)


# add two dictionary to single dict

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# s = {**dict1 , **dict2}
# print(s)

# reverse of string another method
#
# l = "asdfg"
# p=[]
# o = len(l)-1
# while o>=0:
#     p.append(l[o])
#     o = o - 1
# s = "".join(p)
# print(s)


# output aaaabbbcc string * numbers
# l = "a4b3c2"
# k = ""
# p=""
# for i in l:
#     if i>="a" and i<="z":
#         k+=i
#         p = i
#     else:
#         k = k + p * (int(i)-1)
# print(k)


# write program print largest element and index of that.
# u = [1,2,4,7,5,6,8,10]
#
# o = 1
# for i in range(len(u)):
#     if u[i] > u[o]:
#         o = i
# print(o,u[o])


#write a program count the repeates string and print o/p -> a4b3c3d3

# l = "aaaabbbcccddd"
#
#
# s = ""
# c = 1
# for i in range(1,len(l)):
#     if l[i] == l[i - 1]:
#         c += 1
#         if i == len(l)-1:
#             s += l[-1] + str(c)
#     else:
#         s += l[i-1] + str(c)
#         c = 1
#
# print(s)

# write program to a*4->aaaa times like all
# l = "a4g3c2z5"
#
# s = ""
# k = ""
# g = ""
# for i in l:
#     if i >= "0" and i<="9":
#         s += i
#     elif i>='a' and i<="z":
#         k+=i
# for j in range(len(k)):
#     for z in range(j,j+1):
#         g += k[j]*int(s[z])
# print(g)


# write a code print [1,3,4] , [2,2,5,5]same elements remove

# l = [1,2,2,3,4,5,5]
#
# out = [i for i in l if l.count(i) == 2]
# print(out)

# list1 = [5, 20, 15, 20, 25, 50, 20]
#
# output = [i for i in list1 if list1.count(i) == 1]
# print(output)


# prime check
# n = 3
#
# prime = True
#
# if n<=1:
#     prime = False
# else:
#     for i in range(2,n):
#         if n%2 == 0:
#             prime = False
#             break
#
# if prime:
#     print("prime")
# else:
#     print("not prime")

# reverse list

# list1 = [100, 200, 300, 400, 500]
#
# k = []
# l = len(list1)
# for i in list1:
#     while l>0:
#         l = l - 1
#         k.append(list1[l])
# print(k)


# def my_fun(text,ch):
#     k = ""
#     for i in text:
#         if i == " ":
#             i = ch
#         k+=i
#     return k
#
# text = "D t C mpBl ckFrid yS le"
# ch = "a"
#
# print(my_fun(text,ch))



# def my_method(arr):
#     k = []
#     l = 0
#     for i in arr:
#         if arr.count(i) == 1:
#             k.append(i)
#     else:
#         for j in k:
#             if j > l:
#                 l = j
#         print(l)
# arr = [4, 3, 2, 7, 3, 4, 8,9]
# my_method(arr)


#write program to print lowet element in list

# l = [1,3,4,5,6,2]
#
# k = l[0]
#
# for i in l:
#     if i < k:
#         k = i
# print(k)

# count the total 1 in the random string

# import random
#
# k = "".join(random.choice('01') for _ in range(10))
#
# c = 0
# for i in k:
#     if int(i) == 1:
#         c += 1
# print(c)
# print(k)

# anagrams problem-> , if str is same as next str then add in list and sub list

# output:["bat",["cat","act"],["pet","ept","tep"]]
# strs=["bat","cat","act","pet","tep","ept"]
#
# k = []
# d = {}
#
# for i in strs:
#     s = "".join(sorted(i))
#     if s not in d:
#         d[s] = []
#     d[s].append(i)
#
# g = list(d.values())
# print(g)


# reverse the integer without keyword

# s = 1234543
#
# rever = 0
# k =0
# while s != k:
#     digit = s % 10
#     rever = rever * 10 + digit
#     s = s//10
# print(rever)


# reverse the float without keyword
# n = 123.78
#
# int_part = int(n)
# fc_part = str(n).split(".")[1]
#
# revers = 0
# while int_part != 0:
#     digit = int_part % 10
#     revers = revers * 10 + digit
#     int_part = int_part // 10
#
# rev_frac = fc_part[::-1]
# rev_f = int(rev_frac)
# mul = 10**len(rev_frac)
#
# r = revers + rev_f / mul
# print(r)

# print the greatest number in list and print the missing number in list
# n = [3,7,1,9,4]
#
# g = 0
# k = []
# for i in n:
#     if i > g:
#         g = i
# print(g)
# for j in range(min(n) , g + 1):
#     if j not in n:
#         k.append(j)
# print(k)


# Binary numbers divided in parts
#
# binary = "010101010"
#
# l = len(binary)
# part =3
# dived_part = l // part
#
# for i in range(0,l , dived_part):
#     div = binary[i :i+dived_part]
#     print(div)


# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
#
# k = {}
#
# for key , values in users.items():
#     if values == "active":
#         k[key] = values
# print(k)

# write program to print comman elements in lists
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]
#
# k =[]
#
# for i in list_a:
#     if i in list_b:
#         k.append(i)
# print(k)


#

# d = {"a":2 , "b":3, "f" : 4}
#
# d1 = {"a":3,"b":4 , "c" : 3}
#
# r = {}
#
# for key in set(d.keys()).union(d1.keys()):
#     r[key] = d.get(key, 0) + d1.get(key, 0)
# print(r)


# d1 = {"a":2 , "b":4}
# d2 = {"a":3, "b":5}
#
# d = { key : values + values for key,values in set(d1.items()).union(d2.items())}
# print(d)

# def my_func(fun):
# 	def inner_fun():
# 		print("hii")
# 		fun()
# 		print("ihi")
# 	return inner_fun
#
# @my_func
# def simple():
# 	print("hie")
# simple()


# l = [3,4,5,6,78,9]
#
# f = 0
# s = l[0]
# t = l[0]
#
# for i in l:
#     if i > f:
#         t = s
#         s = f
#         f = i
#     elif i > s and i != f:
#         t = s
#         s = i
#     elif i >t and i !=s:
#         t =i
# print(s)
# print(t)


# p = 1
#
# user = int(input("enter the number"))
#
# rev = 0
# a = user
# while user != 0:
#     d = user % 10
#     rev = rev * 10 + d
#     user = user // 10
#
# if a == rev:
#     print("palindrome")
# else:
#     print("not")


# using built in keys
# k = [10,32,46,65,2]
#
# d = k.sort()
#
# user1 = list(map(int,input("enter num").split()))
#
# for i in user1:
#     print(k[-i])

# without built in


# without built in function
# k = [10,20,40,50,6]
#
# for i in range(len(k)):
#     for j in range(len(k)):
#         if k[i] > k[j]:
#             k[i],k[j] = k[j] , k[i]
# print(k)
#
# user_ipt = list(map(int , input("enter the number").split()))
#
# for i in user_ipt:
#     print(k[i-1])


# k = "aaaaabbbbcccdd"
# d = ""
# c = 1
# for i in range(1,len(k)):
#     if k[i] == k[i-1]:
#         c +=1
#     else:
#         d += k[i-1] + str(c)
#         c = 1
# d+= k[-1] + str(c)
# print(d)

# import subprocess
# import re
# from traceback import print_tb
#
# ip = "ipconfig"
#
# d = subprocess.run(ip,stdout= subprocess.PIPE ,stderr=subprocess.PIPE,text = True)
#
# r = r"IPv4 Address[.\s+]+:\s+(\d+\.\d+\.\d+\.\d+)"
#
# g = re.findall(r,str(d))
#
# print(g)


# with open("files.txt" , "r+") as f:
#     n = f.write(str(d))
#     print(n)


# l = [2,4,5,3,6,7,8]
# o = []
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i] > l[j]:
#             l[i],l[j] = l[j],l[i]
# for k in l:
#     if k % 2 == 0:
#         o.append(k)
# print(o)


# dictionary = {'Name': 'Tanu', 'Sex': 'Male', 'Age': 23, 'Height': 5.8, 'Occupation': 'Student'}
#
# k = sorted(dictionary)
# print(dictionary[k])
# for i in k:
#     dictionary[i] = dictionary

# def largest_find(n,k2):
#     n.sort()
#     return n[len(n)-k2]
#
#
# K = list(map(int,input("enter the list").split()))
# k2 = int(input("enter the integer"))
#
# # K.sort()
# # print(K[len(K)-k2])
#
# p = largest_find(K,k2)
# print(p)


import subprocess
import re
from pickletools import read_uint1


# ip = "ipconfig"
#
# d = subprocess.run(ip,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
#
# t = r"IPv4 Address[.\s+]+\:\s+(\d+\.\d+\.\d+\.\d+)"
#
# ex = re.findall(t,str(d))
#
# print(ex)

#two list need to combine and remove dublicates and sort the list
# l = [1,2,4,5]
# l2 = [6,7,9,8,9]
#
# l3 = list(set(l + l2))
#
# for i  in range(len(l3)):
#     for j in range(len(l3)-i-1):
#         if l3[j] > l3[j+1]:
#             l3[j],l3[j+1] = l3[j+1],l3[j]
#
# print(l3)
# def last(n):
#         return n[-1]
#
# def check(tuples):
#     return sorted(tuples,key=last)
# k = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# print(check(k))


# def fabinic(n):
#     if n<=1:
#         return n
#     return fabinic(n-1) + fabinic(n-2)
