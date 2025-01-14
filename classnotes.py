"""
import datetime

def datetime_and_count():

    firstname= "koda"
    print("\ngood job \n")
    print(datetime.datetime.now(), "\n")
    print("and? \n")


    for x in range(0,100):
        print("\n", x, "\n")
    print("\n", datetime.datetime.now(), "\n")

"""

'''
def fun1():
    a = 1
def fun2():
    a = 2
    fun1()
    return a
a = 0 
print(fun2())
'''

def fullname(w1,w2):
  return w1 + ' ' + w2

f=fullname(w2='faith',w1='charity')
print(f)
