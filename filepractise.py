# with open("practise.txt", "a+") as f:
#     f.write("Hi everyone\nwe are learning file I/O using Java.\n")
#     f.write("I like programming in Java")


# with open("practise.txt", "r") as f:
#     data = f.read()
#     new_data = data.replace("Java", "Python")
# with open("practise.txt", "w") as f:
#    f.write(new_data)

# with open("practise.txt", "r") as f:
#     data = f.read()
#     if data.find("learning")!=-1:
#         print("Found")
#     else:
#         print("Not found")


# def check_for_line():
#     data = True
#     count=1
#     with open("practise.txt", "r") as f:
#         word="hg"
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(count)
#                 return
#             count+=1
#     return -1

# print(check_for_line())




def even():
    list =[]
    current =""
    with open("numbers.txt", "r") as f:
        data = f.read()
        data = tuple(data)
        for i in range(len(data)):
            if data[i] ==',':
                
                list.append(data[i-1])
    print(list)
        # count=0
        # for i in list:
        #     if list[i]%2==0:
        #         count+=1
        # print(count)

even()