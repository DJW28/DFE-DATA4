# # print(10*2
# # )

# # print(10/2)

# # print(10//4)
# # print(10/4)
# # print(10%4)

# # print(10 * (5 + 2))

# # numone = int(input("Please enter a number"))
# # numtwo = int(input("Please enter a number"))
# # print(numone + numtwo)

# # print("Hello World")


# # firstname = input("Please enter First Name")
# # lastname = input("Please enter Last Name")
# # print("Hello" +" "+ firstname +" "+ lastname)


# number1 = input("enter whole number:")
# number2 = input("enter decimal number:")

# integernum = int(number1)
# floatnum = float(number2)
# roundnum = int(round(floatnum))
# print(number1)
# print(number2)
# print(roundnum)

# textvar1 = "ilikepies"

# textvar2 = textvar1.isalpha() 
# print(textvar2)


# pet
# name = "Dog"
# age = 3
# bark = True
# tweet=  False


# print("My pet it called", name, ", He is", age, "years old.")
# print("Statement:", name, "barks.", bark)
# print("Statement:", name, "tweets.", tweet)


# shoppinglist= ["Meat", "Veggies", "Cake", "Beer for the weekend."]

# print(shoppinglist)

# shoppinglist.append("Parsnips")

# print(shoppinglist)

# coolcows=["Winnie the Moo", "Moolan","Milkshake", "Mooana"]
# coolsheep=["Baaaart", "Baaarnaby"]
# coolpigs=["Chris p. Bacon", "Hamlet", "Hogwarts"]

# coolanimals = [coolcows, coolpigs, coolsheep]
# for loopvar in coolanimals:
#     for subloopvar in loopvar:
#         print(subloopvar)

# print(coolanimals[0][2])

# books={"Book 1 yo":"That guy", "The Book":"Other guy", "Nah":"John Yah"}

# print(books["Nah"])
# print(books["Book 1 yo"])
# print(books["The Book"])

# var1 = "ilikepies"
# # var1 = 3
# var2 = 6

# if var1 < var2:
#     print(var1, "is less than", var2)
# else:
#         print(var1, "is not less than ", var2)

# if var1 >= var2:
#     print(var1, "is greater than or equal to", var2)
# else:
#         print(var1, "is not greater than ", var2)        

# print("this is the rest of the program")

# if var1.isdigit() or not (var2 > 3 amd var2 < 10):
#     print("the answer was True")
# else:
#     print("the answer was False")


# Mark = int(input("Please enter mark:"))
# Distinction = 85
# Pass = 65
# Fail = 64
# if Mark >= Distinction:
#     print("Distinction")
# elif Mark >= Pass:
#     print("Pass")
# else:
#     print("Fail")

# if Mark >= Distinction:
#     print("Distinction")

# if Mark >= Pass:
#         print("Pass")

# if Mark <= Fail:
#     print("fail")

                                        #pyhton work book


# integer = int(input("Enter number:"))
# if(integer%2==0):
#     print("Even")
# else:
#     print("Odd")


    #for loop
 
# coolcows = ("Winnie the Moo", "Moolan", "Milkshake", "Mooana")

# for loopvar in coolcows:
#     print(loopvar)
#     if loopvar =="Moolan":
#         break           #<----stops
#     print(loopvar)

# for loopvar in coolcows:
#     if loopvar =="Moolan":
#         continue            #<----skips 
#     print(loopvar)

# coolcows = "Winnie the Moo"


# for loopvar in range(5,56,5):
#     print(loopvar, coolcows)

    #while loop

# Score = 500
    
# while Score > 100:
#     Score = int(input("Please enter score:"))
#     if Score > 100:
#         print("Not a valid score, try again")

# if Score >=85:
#     print("Distinction")
# elif Score >=65:
#     print("Pass")
# else:
#     print("Fail")




# friends =[]
# count = 0
# while count <5:
#     name =input("What is your name")
#     friends.append(name)    
#     count += 1

# for friend in friends:
#      print(friend, "is awesome")   
   
#     # result.append(x)
# print(name, "is awesome")
    # if name == "":
    #     continue


# print(name
# while count <5:
#     print(name, "is awesome!")
#     count += 1

# for i in range(10,21,2):
#     print(i)

# name = list(map(str, input("Enter 5 names: ").split()))

# name1 = input("enter your name:")
# name2 = input("enter your name:")
# name3 = input("enter your name:")
# name4 = input("enter your name:")
# name5 = input("enter your name:")

# for loopvar in name:
#     print(loopvar, "is awesome")


# def cal_average(num):
#     senval=0
#     num = input("Enter value:")
#     for t in int[num]:
#         senval = senval + t
#     avg = senval / len int[num]
#     return avg

# print("The average is", cal_average([]))
# avg = ()
# value = []

# while avg >=0:
#     numberlist = list(map(int, input("Enter value")))
#     value.append(numberlist)
#     avg +=1
#     average = sum(numberlist)/len(numberlist)
#     for average in value:
#         print("the Average is" , round(average,2))
    # def cal_average():
    # average = sum(numberlist)/len(numberlist)
    # return average
#     for loopvar in numberlist:
#         print(numberlist)
# if loopvar == 0:
#     continue

# print("The Average is", (average))

# reverse word inputted

    # word = input("insert word: ")
    # revword = word[::-1]
    # print(revword)


# ------------------------function exercise-----------------------------

# def add_calc(number1, number2):
#     answer = number1 + number2
#     return answer

# number1 = input("Enter a number")
# number2 = input("Enter a number")

# added_number = (int),add_calc
# print(added_number)

#----------------------------Functions------------------------------------------

# def calcgraderesult(int_hwscore, int_asscore, int_exmscore):
#     result= (int(int_hwscore) + int(int_asscore) + int(int_exmscore)) / 175*100
#     if int(result) >= 85:
#             gradescore = "A"
#     elif int(result) >= 70:
#             gradescore = "B"
#     elif int(result) >= 60:
#             gradescore = "C"
#     elif int(result) >= 50:
#             gradescore = "D"
#     elif int(result) >= 45:
#             gradescore = "E"
#     else:
#             gradescore = "F"
#     return result, gradescore



# studentname = input("Enter student name: ")
# int_hwscore = input("Enter" + studentname + "'s homework score: ")
# int_asscore = input("Enter" + studentname + "'s assessment score: ")
# int_exmscore = input("Enter"+ studentname + "'s exam score: ")

# graderesult = calcgraderesult(int_hwscore, int_asscore, int_exmscore)
# print(studentname + " achieved Grade " + graderesult[1] + " (" + str(round(graderesult[0],2)) +").")

# for temploopvar in [1,1]:




# from _typeshed import SupportsNoArgReadline
# from types import MappingProxyType


# item_list = ["burger","hotdog", "bun", "ketchup", "cheese"]
# n=0

# while n<5:
#     for i in item_list:
#         print(item_list[i])


# print(item_list[5])


# classes

# class Student:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


    
# John = Student("John", "21", "2")
# Jane = Student("Jane", "22", "1")



# print(getattr(John, "age", "set"))

    #self.claset = claset

    # John = Student("John", "21")
    # Jane = Student("Jane", "22")
    # Marq = Student("Marq","22","3")
    # Var = Student("Var","23","4")
    # Tar = Student("Tar","17","1")
    # Van = Student("Van","21","1")
    # Lumen = Student("Lumen","20","2")
    # Cumin = Student("Cumin","19","2")
    # Daw = Student("Daw","20","3")
    # Arn = Student("Arn","24","4")

    # s1 = Student
    # print(s1.name)
    
    #print(getattr("John", "age"))


#Student = {

#}


#    studentname = input("Enter student name: ")
# int_hwscore = input("Enter" + studentname + "'s homework score: ")
# int_asscore = input("Enter" + studentname + "'s assessment score: ")
# int_exmscore = input("Enter"+ studentname + "'s exam score: ")

myfile = open('README.md')
chars = myfile.readlines()
myfile.close()

chars.insert(2,"I like flies\n")
chars.append("\nCheese is pretty good to eat\n")
print(chars)
output = "".join(chars)

myfile = open('README.md', mode='w')
myfile.write(output)
myfile.close()




# teams = ["NO","BRO","Hoopshafjord","hahahaha","nowwayFC"]

# with open("teams.txt", "w") as file:
#     for i in teams:
#         newline = str(i)
#         file.write(newline + "\n")

# with open("teams.txt", "r") as file:
#     print(file.read())
#     print(file.read())