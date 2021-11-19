# import pdb     
# pdb.set_trace()
#=================

# EXERCISE  34----Even or Odd

# def numchecker(number):
#     if number %2 == 0:
#         print(" The Number is even ")
#     else:
#         print(" The Number is odd ")


# number = int(input(" Enter Number "))

# numchecker(number)

# number = int(input(" Enter Number "))

# import dw_functions
# dw_functions.numchecker(number)


# EXERCISE 35 ----------- Dog Years


# humanage = int(input(" Enter age "))


# def calcdogage(humanage):
#     i = humanage
#     if humanage == 2:
#         print(" You are ",i*5.25, " in dog years ") 
#     if humanage == 1:
#         print(" You are ",i*5.25, " in dog years")
    
#     if humanage >= 3:
#         # i = humanage *4
#         print("you are",i*4," in dog years " )
#     elif humanage <=0:
#         print(" Invalid entry, Please try again ")
    

# calcdogage(humanage)


#EXERCISE 36 ================= Vow or Con

# vowels = ["a","e","i","o","u"]

# letter = str(input(" Enter Letter "))

# def alphchecker(letter):
#     if letter in vowels:
#         print(letter,"is a Vowel")
#     elif letter == "y":
#         print(letter,"is sometimes a Vowel")
#     else:
#         print(letter,"is a Consonant")


# alphchecker(letter)

# ============ EXERCISE 37 ============ Name Shape
    # "monogon" : "circle",
    # "bigon" : "line",
    # "triangle" : "isocoles",
    # "quadrilateral" : "sqaure"

# numofsides = input()

# sides = numofsides 
# shapename = { "3" : "isosceles",
# "4" : "sqaure",
# "5" : "pentagon",
# "6" : "hexagon",
# "7" : "heptagon",
# "8" : "octagon",
# "9" : "nonagon",
# "10" : "decagon"    
# }

# #print(shapename.items())








# # shapes = (monogon01,bigon2,triangle3,quadrilateral4,pentagon5,hexagon6,heptagon7,octagon8,nonagon9,decagon10)

# error = "Invalid number of sides, Please Try again"
# sides = str(input("Enter how many sides:"))

# def whatshape(sides):
    
#     if sides not in shapename:
#         print("error") 
#     elif sides in shapename:
#         return shapename.get(sides)

    
# print(shapename.get(sides))

    # shapes = (monogon01,bigon2,triangle3,quadrilateral4,pentagon5,hexagon6,heptagon7,octagon8,nonagon9,decagon10)




# # print("Invalid number of sides, Please Try again")


# <3 or >10
# print("Invalid number of sides, Please try again")


#===========Exercise 40============
tside1 = int(input("Enter 1st side length: "))
tside2 = int(input("Enter 2nd side length: "))
tside3 = int(input("Enter 3rd side length: "))
Scalene = "Your Triangle is a Scalene triangle"
Isosceles = "Your Triangle is an Isosceles triangle"
Equilateral = "Your Triangle is an Equilateral triangle"

def tricalc(tside1,tside2,tside3):
    if tside1 == tside2 and tside1 or tside2 != tside3:
        return(Isosceles)
    if tside1 == tside2 and tside1 == tside3 and tside2 == tside3:
        return(Equilateral)
    if tside1 != tside2 and tside1 != tside3 and tside2 != tside3:
        return(Scalene)



tricalc.
