hwList = {
    "math" : "monday",
    "english" : "tuesday",
    "chemistry" : "friday"
}

key = input("enter a subject to check when your homework is due: ")
for i in hwList.keys():
    if key == i:
        print("your homework is due on " + hwList[key])
    else:
        print("you have no homework for this class")