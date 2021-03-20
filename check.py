#import string as s # an object is created with name "string" 
import math # as object is created with name "math" 
from string import *
from math import pi
# module --- a file in python
# package --- group of modules
# libraries/frameworks --- group of packages
ascii_lowercase
ascii_uppercase
import MyPackage # mp
# print(MyPackage.one.One(5))
# print(MyPackage.two.Two(6 , 4))
# print(MyPackage.three.Three(55))
print(MyPackage.One(90) , MyPackage.Two(55,45) , MyPackage.Three(160))
r = 90
pi * r * r
print(__name__) # name of module for interpretor

if __name__ == '__main__':
    print("Hello, Woerld")