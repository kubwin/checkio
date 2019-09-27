class Person:                                                                         
    def __init__(self, age: object) -> object:
        self.age = age                                                                
                                                                                      
    def amIOld(self):                                                                 
        if self.age<0:                                                                
            print('Age is not valid, setting age to 0')                               
            self.age=0                                                                
    def yearPasses(self):                                                             
        self.age+= 1                                                                  


a= Person(1)
a.yearPasses()
print(a.age)

