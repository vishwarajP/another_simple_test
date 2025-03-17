# python all practise questions here

# str = input('enter the string to print:')
#
# l = len(str)
# for i  in range(0,l-1,2):
#     print(str[i])
# if i%2==0:
#     print(i)

# str = 'pynative'
#
# p = list(str)
# for i in p:
#     if i=='n':
#         print(i)
#
# import keyword
#
# print(keyword.kwlist)

# a=10
# b=0x10
# c=0o10
# d=0b10
# print(a,b,c,d)

# import turtle as tb
#
# for i in range(500):
#     tb.forward(200)
#     tb.color('red')
#     tb.bgcolor('gold')
#     tb.down
#     tb.right(300)
#     tb.color('black')
#     tb.left(200)
#     print(i)
#
#
# str = 'My Name is Jessa'
# l = ''
# for i in str:
#     l = i + l

# print(str[::-1])

# x = str.split()
# for i in x:                easy methond
#     print(i[::-1],end=' ')


# def reverse_word(statement):
#     word = statement.split()
#
#     words = [i[::-1] for i in word]
#
#     result = " ".join(words)
#     return result
#
# str = 'my name is jessa'
# d = reverse_word(str)
# print(d)


# with open('h.txt','r') as r:
#     l = r.read()
#     print(l.replace('\n',' '))

# numbers = [10,20,30,40,50,60,70]
#
# l = len(numbers)
#
# i = 0
#
# while i<l:
#     if numbers[i]>50:
#         del numbers[i]
#         l = l - 1
#     else:
#         i = i + 1
#
# print(numbers)

# with keywors we can reverse dic
# ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

# d = list(ascii_dict.items())
# l = list(reversed(d))
# v = dict(l)
# print(v)

# print({value:key for key, value in ascii_dict.items()})

# pattern = 5
# numbers = 0
#
# for i in range(pattern,0,-1):
#     numbers+=1
#     for j in range(1,i+1):
#         print(numbers,end=' ')
#     print(' ')

# assert
# def divesion(a,b):
#     assert b!=0, " this should be 1 "
#     return a /b
# try :
#     print('its not should be zero')
# except:
#     print('please enter greaterthen one')
# l = divesion(10,0)
# print(l)

# testcase using assert
# def add(a,b):
#     return a + b
#
# def test_add():
#     result = add(2 , 3)
#     assert result == 5,f"expected result 5 but got result{result}"
#
# test_add()

# l = input("enter the input")
# k = l[::-1]
# print(k)
# l1 = ''
# for i in l:
#     l1 = i + l1
# print(l1)
#
# p = len(l)-1
# o = ''
# while p>=0:
#     o = o + l[p]
#     p = p - 1
# print(o)

# print(''.join(reversed(l)))

# numbers = [1, 2, 3, 4, 5, 6, 7]
# l = []
# for i in numbers:
#     l.append(i**2)
# print(l)


# def add(a,b):
#     print("add",a+b)
#
# def product(a,b):
#     print("product",a*b)


# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
#
# l = []
#
# for i in range(len(list1)):
#     for j in range(i,i+1):
#         l.append(list1[i]+list2[j])
# print(l)