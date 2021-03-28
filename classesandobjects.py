# # Classes ---- blueprint of objects
# # objects --- variables from userdefined types
# # int x;

# # struct Example {
# #     int x,y,z; # 6B
# #     float a,b; # 8B
# #     char arr[20]; # 20B
# # }


# # class Example { # set of variables(attributes) and functions(methods)
# #     #access modifiers ---- private, public
# #     private:
# #     int x,y,z;
# #     public float a,b,c;
# #     static int count = 1; // this variable will now be given a shared location, doesnt need an object to access them,
# #     char arr[100];
# #     #functions
# #     public:
# #     def takeInput():
# #         #print(x,y,z,a,b,c,arr);
# #         x = input("Enter x:  ")
# #         count += 1
# #     def func2():
# #         x * y * z * a
# # }
# # Example E , F, J , K, L; # 118B
# # E.takeInput(), F.takeInput(), J.
# # E.func2()
# # F.func2()
# # int x,y;

# #
# class Person:
#     '''Documentation String, optional, describe about your class'''
#     s1 = 100 # All Static as well as public
#     s2 = 200
#     s3 = 300
#     def __init__(self , a,b,c): # here, we will create ObjectAttributes
#         self.a = a
#         self.b = b
#         self.c = c

#     def one(self):  # first arg will be fixed in any class function --- i.e, object it self
#         print(self.a, self.b, self.c)

#     def show(self):
#         print(self.a*self.b*self.c)

#     def __del__(self):
#         print("Attribute Destroyed!")


# P = Person(12,13,14)  # calling the default, constructor function of the class, unless you override the default constructor
# Q = Person(20,3.4,5.6)
# R = Person(90,80,70)
# #print(Person.i)
# print(Person.__doc__)
# #Person.i = 900
# #print(P.i, Q.i, R.i)
# #print(P.a , Q.b, R.c)
# # print(P.i)
# # P.show() # we dont have to pass self arg here, that automatically passed
# # R.show(), R.show()
# #P.a = 'Changed'
# #print(Q.a, R.a, P.a)
# P.one()
# Q.one()
# R.one()
# P.show()
# Q.show()
# R.show()

# del P

class Point:
    __points_count = 0 # ClassAttribute - Static , private with __
    def __init__(self,x,y): # Constructor --- ObjectAttributes
        self.__x_coordinate = x
        self.y_coordinate = y
        Point.__points_count += 1
    
    def show(self):
        print(self.__x_coordinate)

P1 = Point(23,-19) # __init__
P2 = Point(12,-8)
P3 = Point(-11,-22)
P2.show()
#print(P1.__x_coordinate , P2.y_coordinate)
#print(Point.__points_count)
# To access a private attribute
print(P1._Point__x_coordinate)