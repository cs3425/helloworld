import random

def helloworld(name=None, aday=None, temp=None):
    """
    return hello world, or hello {name}
    """

    # print greeting
    if not name:
        print("hello world")
    else:
        print("hello {}".format(name))
        
    #what should your hairstyle be on a given day
    if aday == 1:
        print("Wear princess leia buns on that day!")
    elif (aday%2) == 0:
        print("Don't wear pigtails on that day")
    else:
        print("Wear pigtails on that day!") 
        
    #what should you eat today
    if temp > 50:
        options = ["sushi","grilled cheese","mac n cheese","salad","enchiladas"]
        foodopt = random.randint(0,4)
        print("You should eat", options[foodopt])
    else:
        print("You should probably just hibernate.")  