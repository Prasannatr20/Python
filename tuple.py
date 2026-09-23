# tup = (2,1,3,1)
# print(tup)
# print(type(tup))
# tup1 = (1,)
# print(tup1)
# print(type(tup1))
# print(tup.count(1))
# print(tup.index(1))

# Practise

# movie1 = input("Enter your movie name: ")
# movie2 = input("Enter your movie name: ")
# movie3 = input("Enter your movie name: ")
# list = [movie1, movie2, movie3]
# movies = [input("Enter movie: "), input("Enter movie: "), input("Enter movie: ")]
# print(movies)

#Palindrome

# list = [1,2,2,1,8]
# list2 = list.copy()
# list2.reverse()
# if(list==list2):
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#Count

# grades = ("c","a", "d", "b", "a", "b", "a", "c", "a")
# print(grades.count("a"))

#List sort

# grades = ["c","a", "d", "b", "a", "b", "a", "c", "a"]

# grades.sort()
# print(grades)

#Practise

player = ["Arun", "warrior", "sword", "shield"]
mission = ("Dragon Cave", "DRAGON", 5)
message = "the warrior entered the dragon cave. the dragon is waiting inside."
count=0

if("sword" in player):
    print("Sword available")
    count+=1
else:
    print("Not available")
    count-=1
if("shield" in player):
    print("Sword available")
    count+=1
else:
    print("Not available")
    count-=1
if("Dragon Cave" in mission):
    print("The mission name is dragon cave")
    count+=1
else:
    print("Other mission")
    count-=1
if(mission[1].endswith("GON")):
    print("Ends with GON")
    count+=1
else:
    print("Not available")
    count-=1
if(message.find("warrior")!=-1):
    print("Warrior is available")
    count+=1
else:
    print("Warrior is not available")
    count-=1
message = message.replace("dragon" , "monster")
message = message.capitalize()
print("Message length: ", len(message))
if(count>4):
    print("Ready for battle")
else:
    print("Not ready")

print(message)