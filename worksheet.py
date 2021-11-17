import pdb     
pdb.set_trace()
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


shapename = {
    "3" : "isocoles",
    "4" : "sqaure",
    "5" : "pentagon",
    "6" : "hexagon",
    "7" : "heptagon",
    "8" : "octagon",
    "9" : "nonagon",
    "10" : "decagon"    
}



# shapes = (monogon01,bigon2,triangle3,quadrilateral4,pentagon5,hexagon6,heptagon7,octagon8,nonagon9,decagon10)


sides = int(input("Enter how many sides"))

def whatshape(sides):
    if sides is x in shapename:
        return shapename.get(sides)
    elif sides is < = 3 or 10:

    


    





print(shapename.get(sides))

# <3 or >10
# print("Invalid number of sides, Please try again")

