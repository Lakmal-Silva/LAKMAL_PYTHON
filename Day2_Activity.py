class Family:

    def __init__(self,x):

        self.x=x+5
        print(self.Child_1()+self.Child_2())
       

    def Child_1(self):
        return self.x+100
    

    def Child_2(self):
        return self.x*100
     


Family(100)
