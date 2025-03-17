# c = "kjfnskjfnsjdf"

# d= {}
#
# for i in c:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


#this is branch test

# def square(x):
#     return x **2
#
# number = [1,2,3,4,5]
#
# result = list(map(square,number))
# print(result)
#
# new = list(result)
# print(new)
# import re
# import tkinter
# from threading import *
#
# import random
# import time
#
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
#
# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#
# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)


# p = []
#
# o = ""
# with open("h.txt" ,"r")as f:
#     l = f.read()
#     u = l.split()
#     print(" ".join(u))

# import re
# emails = [
#     "Send an email to user@example.com",
#     "Contact me at john.doe@example.com",
#     "Email us at support@example.com",
#     "Invalid email: not_an_email",
#     "Another valid email: alice_123@example.com"
# ]
#
# pattern = r"\b[A-Za-z0-9+_%-.]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}\b"
#
# match = re.findall(pattern,"".join(emails))
#
# for mail in match:
#     print(mail)


# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#
# k = len(sample_list)
#
# o = int(k/3)
#
#
# start = 0
#
# end = o
#
# for i in range(3):
#     index = slice(start,end)
#
#     h = sample_list[index]
#     print(h)
#
#     j = list(reversed(h))
#     print("reverse",j)
#
#     start = end
#
#     end += start


# import json
#
# class PersonalInfo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def showInfo(self):
#         print("Developer name is " + self.name, "Age is ", self.age)
#
# dev = PersonalInfo("John", 36)
# developer_Dict = {
#     PersonalInfo: dev,
#     "salary": 9000,
#     "skills": ["Python", "Machine Learning", "Web Development"],
#     "email": "jane.doe@pynative.com"
# }
# print("Writing JSON data into file by skipping non-basic types")
# with open("developer.json", "w") as write_file:
#     json.dump(developer_Dict, write_file, skipkeys=True)
# print("Done")


# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
#
# j = {}
#
# cout = 0
#
# for i in sample_list:
#     if i >=1:
#         cout+=1
# print(cout)

# exmple of decorator
# def check(function):
#    def member(arg1,agr2):
#        new_arg = arg1.capitalize()
#        new_arg1 = agr2.capitalize()
#
#        new_strig = function(new_arg,new_arg1)
#
#        return new_strig
#    return member
#
# @check
# def another_check(name,name1):
#     return 'Hello ' + name + " worl " + name1 + "!"
# print(another_check("sis","yeeh"))


# l = [10,20,30,40,50]

# for i in l[::-1]:
#     print(i)

# p = len(l)-1
#
# for j in range(p,-1,-1):
#     print(l[j])


# r = []
#
# for i in l:
#     r = [i] + l
# print(r)

# k = input()
#
# j = k.split()
# s = set()
# r = []
# for i in j:
#     s.add(i)
#     r = s
#
# o = " ".join(sorted(list(r)))
# print(o)


# l = [10,20,30,10]
#
# u = []
# y = []
# for i in l:
#     if i not in u:
#         u.append(i)
#     else:
#         y.append(i)
# print(y)


# user = input("enter the worlds:")
#
# u = 0
# l = 0
#
# for i in user:
#     if i >= 'A' and i <="Z":
#         u+=1
#     elif i >= "a" and i<="z":
#         l+=1
#
# print("upper case:",u)
# print("lower case:",l)

# import yaml
#
# with open("resource.yml","r") as f:
#     prime = yaml.safe_load(f)
#     print(prime)


# remove dublicate values in list
# l = [10,20,30,40,20,40]
#
# k = []
# p = []
# for i in l:
#     if i not in k:
#         k.append(i)
#     else:
#         p.append(i)
# print


# n = 5
#
# for i in range(1,n+1):
#     print(""*(n-1),(str(i)+"")*(2*i-1))


# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
#
# u = {i for i in first_set if i in second_set}
# h = {j for j in first_set if j not in second_set}
#
# print(u)
# print(h)

# k = []
# d = dict(k)
# j = []
# for i in first_set:
#     if i in second_set:
#         k.append(i)
#     elif i not in second_set:
#         j.append(i)
#
# print(d)
# print(j)


# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#
# class sll:
#     def __init__(self):
#         self.head = None
#
#
#     def display(self):
#         temp = self.head
#         if self.head is None:
#             print("empty")
#         while temp:
#             print(temp.data,"-->",end="")
#             temp = temp.next
#
# l = sll()
# n1 = node(10)
# l.head = n1
# n2 = node(20)
# l.head.next = n2
# n3 = node(30)
# n2.next = n3
# l.display()


# string = "asdfghj"
#
# k =""
#
# j = ""
#
# h= ""
# d = len(string)
# for i in range(d):
#     if i == 0:
#         k+=string[i]
#     elif i == len(string)-1:
#         j += string[i]
#     else:
#         h+= string[i]
#
# print(k)
# print(j)
# print(h)


# p=11
# o = 6
# for i in range(1,o+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for k in range(1,o+1):
#     for h in range(1,o-k):
#         print("*",end=" ")
#     print()

#
# list1 = [5, 30, 15, 20]
#
# l = []
# first = 0
# second = 0
#
# four = 0
# five = 0
#
# for i in range(len(list1)):
#     if i>=0 and i<=2:
#         second = first
#         first = i
#     elif i >2 and i < 4:
#         five = four
#         four = i
#
# l.append(list1[first]+list1[second])
# l.append(list1[four]+list1[five])
# print(l)


# l = [10,20,30,10,50,60]
#
# h = []
#
# a = int(len(l) / 2)
#
#
# for i in range(1,int(len(l)-1)):
#     k = l[i-1] + l[-i]
#     h.append(k)
# print(h)


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

# import re
# with open("anirban.txt" , "r") as f:
#     s = f.read()
#     k = r"ERROR"
#     c = re.findall(k,s)
# print(c)
# import re
#
# def my_method():
#     with open("files.txt" , "r") as f:
#         s = f.read()
#         a = r"\d"
#         f = re.findall(a,s)
#         print(f)
#
# my_method()


# def my_decorator(func):
#     def wrapper():
#         print("sometime is before")
#         func()
#         print("sometime")
#     return wrapper()
#
# @my_decorator
# def say_hello():
#     print("hello")
#
# say_hello()


# class my:
#     def __init__(self,name ,age):
#         self.name = name
#         self.age = age
#
# class student(my):
#     def __init__(self,name,age,year):
#         super().__init__(name,age)
#         self.grade = year
#
#     def g(self):
#         print("my name and age" , self.name,self.age,self.grade)
#
# s = student("vish",24,2021)
# s.g()
# print(s)

#
# class my:
#     def __iter__(self,):
#         self.s = 1
#         return self
#
#     def __next__(self):
#         if self.s <=20:
#             x = self.s
#             self.s += 1
#             return x
#         else:
#             raise StopIteration
# s = my()
# k = iter(s)
#
# for i in k:
#     print(i)


# f = 1
# user = int(input("enter"))
# if f<1:
#     print("atleast one")
# else:
#     for i in range(1,user):
#         f = f*i
#         print(f)


# def my(s1,s2):
#     l = int(len(s1)/2)
#     x = s1[:l:]
#     a = x + s2
#     b = a+ s1[l:]
#     print(b)
#
# my("Ault","Kelly")


# l1 = [10,20,3,3,9,8,10,20]
# l2 = [2,3,4,5,6,7,8]
#
# p = []
# q = []
# o = []
# for i in l1:
#     if i not in p:
#         p.append(i)
#     else:
#         q.append(i)
# print(q)
#
# for j in l2:
#     if j not in q:
#         q.append(j)
#     else:
#         o.append(j)
# print(o)


# name = [1,2,3,2,3,4,5]
# s = int(len(name) / 2)
# h = []
# for i in  range(1,int(len(name)-2)):
#     k = name[i - 1] + name[-i]
#     h.append(k)
# print(h)


# f = 1
# user = int(input("enter"))
# if user<=1:
#     print("no")
# else:
#     for i in range(1,user+1):
#         f = f*i
#         print(f)


# import string
# str1 = '/*Jon is @developer & musician!!'
#
# l = "#"
#
# for i in string.punctuation:
#     str1 = str1.replace(i,l)
#
# print(str1)


# import re
# str_ = "Current Frequency:5 GHz (Channel 60)"
# d = r'[Channel]\ \d+'
# s = re.findall(d,str_)
#
# print(s)
#
# l = "aaaabbbsssmmm"
#
# k = ""
# c = 1
#
# for i in range(1,len(l)):
#     if l[i] == l[i-1]:
#         c += 1
#     else:
#         k += l[i-1] + str(c)
#         c = 1
# k += l[-1] + str(c)
# print(k)


# l = "PYnative"
#
# for i in range(len(l)):
#     if i %2 == 0:
#         print(l[i])
#
# print(type(dir()))


# l = [1,3,4,5,6,2]
#
# k = l[0]
#
# for i in l:
#     if i < k:
#         k = i
# print(k)
#
#
# def my_company(fun):
#     def my_name(*args,**kwargs):
#         print("welcome to company")
#         result = fun(*args,**kwargs)
#         print("happy joining")
#         return result
#     return my_name
#
# @my_company
# def simple_method():
#     k = "vish"
#     print(k.upper())
# simple_method()

#
# def genrator(n):
#     cout = 1
#     while cout <= n:
#         yield cout
#         cout+=1
#
# j = genrator(5)
#
# print(next(j))
# print(next(j))


# class calucatore:
#     def add(self,a,b):
#         self.a = a
#         self.b = b
#         return self.a + self.b
#
#     def check(self,c,d):
#         self.c = c
#         self.d = d
#         return self.c + self.d
#
#
# n1 = int(input("enter a"))
# n2 = int(input("enrer b"))
# n3 = int(input("enter a"))
# n4 = int(input("enrer b"))
# k = calucatore()
#
# if k.add(n1,n2) == k.check(n3,n4):
#     print("pass")
# else:
#     print("fail")

# import json
#
# person = { " name " : "vish",
# "language" : "Kannada",
# "age" : 25}
#
# with open("h.txt" , "r") as f:
#     k = json.load(f)
# print(k)


# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
#
# list3 = []
#
# for i in zip(list1,list2):
#     list3 += i
# print(list3)
#
# l = [i + j for i , j  in zip(list1,list2)]
# print(l)


# import random
#
# k = "".join(random.choice("01") for _ in range(10))
#
# c = 0
#
# for i in k:
#     if int(i) == 1:
#         c+=1
# print(c)
# print(k)


# list1 = ["Bengaluru", "Hyderabad", "Mumbai", "Chennai", "Chennai"]
#
# l = []
# k = []
# for i in list1:
#     if i not in l:
#         l.append(i)
#     else:
#         k.append(i)
# print(l)

# a,b = [str(i) for i in input("enter the two string").split()]
#
# print(a + b)

# overide the in inherent class with init
# class shape:
#     def __init__(self,length):
#         self.length = length
#
# class square(shape):
#     def __init__(self,length):
#         shape.__init__(self,length)
#
#     def my_methon(self):
#         return self.length
#
# k = square(5)
#
# print(k.my_methon())

# n = [3,7,1,9,4]
#
# g = n[0]
# h = n[0]
# k = []
# for i in n:
#     if i > g:
#         g = i
#     if i < h:
#         h = i
# print(h) #min number
# print(g) #max number
# for j in range(h, g+1):
#     if j not in n:
#         k.append(j)
# print(k) #missing num

# l = [1,2,3,4]
# k = list(map(lambda x : x**2,l))
#
# print(k)


# li2=[1,2,3,4]
# li3=['a','b','c','d']


# s = dict(zip(li2,li3))

# print(s)
# li1=[1,3,4,2,4,2,4,2,6,7,8,4,2,5,2,4,5,3,6,6,7]


# o = list(set(li1))
# print(o)
# l = []

# for i in li1:
#     if i not in l:
#         l.append(i)

# print(l)

# s1="silent"

# s2="listen"


# if sorted(s1) == sorted(s2):
#     print("anoragm")
# else:
#     print("not")


# l1 = [1,4,3,5,8,10]
# l2 = [2,7,-1,9,20,-10,-2,1]
# l1.extend(l2)
#
# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if l1[i] < l1[j]:
#             l1[i],l1[j] = l1[j],l1[i]
# print(l1)


# user = int(input("enter the number"))
#
# sum = 0
# d = len(str(user))
# a = user
# while user != 0:
#     r = user % 10
#     sum = sum + r ** d
#     user = user // 10
#
# if a == sum:
#     print("amstrong number")
# else:
#     print("not")



#
# num = int(input("enter the number"))
#
# l = len(str(num))
# print(l)
# sum = 0
# a = num
# while num != 0:
#     d= num % 10
#     sum = sum + d ** l
#     num = num // 10
# if a == sum:
#     print("ams")
# else:
#     print("not")


import re
import subprocess

ip= "ipconfig"

pattern = "IPv4 Address[.\s+]+"
d = subprocess.run(ip , stdout=subprocess.PIPE , stderr= subprocess.PIPE , text=True)
print(d)
g = re.findall(pattern,str(d))
print(g)
