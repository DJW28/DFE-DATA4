
# import pdb     
# pdb.set_trace()

class Student:
    
    def __init__(self,name,age,claset,hwscore,asscore,exmscore):
        self.name = name
        self.age = age
        self.set = claset
        self.hwscore = hwscore
        self.asscore = asscore
        self.exmscore = exmscore

    def average(self):
        
        return(self.hwscore + self.asscore + self.exmscore) /3
        
        # name = input()
        # self.hwscore = input("Enter" + self.name + "'s homework score: ")
        # self.asscore = input("Enter" + self.name + "'s assessment score: ")
        # self.exmscore = input("Enter"+ self.name + "'s exam score: ")
        # return(hwscore + asscore + exmscore)/3
    
John = Student("John", 21, 2,10,20,55)
#John.average(10,25,int(input(" Enter Exam score: ")))
avg = John.average()

# Jane = Student("Jane", 22, 1)

# Marq = Student("Marq",22,3)
# Var = Student("Var",23,4)
# Tar = Student("Tar",17,1)
# Van = Student("Van",21,1)
# Lumen = Student("Lumen",20,2)
# Cumin = Student("Cumin",19,2)
# Daw = Student("Daw",20,3)
# Arn = Student("Arn",24,4)



#print(John.name) , " achieved an average score of " ,  (f"{John.average}")
print(John.name, " achieved an average score of ", avg)





# class budget:

#     balance = 0

#     def deposit (self,moneyin):
#         pass
#     def withdraw(self,moneyout):
#         pass


# food = budget()

# food.deposit()
# food.withdraw()

# clothes = budget()
# hosue = budget()