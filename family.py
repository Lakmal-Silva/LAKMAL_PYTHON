class Family:

    def __init__(self, familyname,x):

        self.name=familyname
        self.x=x

    def Ismail(self):
        print("Answer is "+str(self.x*5))


Family("Ziam",10).Ismail()