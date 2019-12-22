# # class Animals: # in a single file there can be more than one classes

# #     x=10 # can define only for this class

# #     def dog(): # objects are inside the class
# #         print("it barks")

# #     def donkey():
# #         print("")

# #     def monkey():
# #         print("")

# # print(Animals.x)

# # print(Animals.dog())

# class  Family:

#     # inbuilt intial function - executes automatically
#     def __init__(self, familyname): # initiation function (eg farther of family)/ inbuilt function
#         self.name=familyname+" Kumara" # more user defined variables can be set inside __init__(self,x,y,..)

#       # user defined function  
#     def myFunction(self):
#         print("I am inside")



# print(Family("Nissanka").name) # passing the value to the 
# # class named "family" and here only calling the faimily

# Family("Nissanka").myFunction()

class Family:

    def __init__(self,familyname):
        self.name=familyname

    def Ismail(self,x):
        print("i am Ismail" +self.name)
        print("Answer is",x*5)

    def Ishhaq(self):
        print("I am Ishhaq"+self.name)

Family(" Ziam").Ismail(10)