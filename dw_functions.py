# ------------------------Basic IF function's to match input --------------------------

# ------input display even if true odd if not

def numchecker(number):
    if number %2 == 0:
        print( number, "is even ")
    else:
        print( number, "is odd ")

#------dog years calc from input
def calcdogage(humanage):
    i = humanage
    if humanage == 2:
        print(" You are ",i*5.25, " in dog years ") 
    if humanage == 1:
        print(" You are ",i*5.25, " in dog years")
    
    if humanage >= 3:
        # i = humanage *4
        print("you are",i*4," in dog years " )
    elif humanage <=0:
        print(" Invalid entry, Please try again ")

#------list checked against input
def alphchecker(letter):
    if letter in vowels:
        print(letter,"is a Vowel")
    elif letter == "y":
        print(letter,"is sometimes a Vowel")
    else:
        print(letter,"is a Consonant")

