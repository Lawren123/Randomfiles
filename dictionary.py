#Dictionary startercode
#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
readMe = f.read()
f.close()
while True:
    print("Can your password survive a dictionary attack?")

    #Take input from the keyboard, storing in the variable test_password
    #NOTE - You will have to use .strip() to strip whitespace
    #and newlines from the file and passwords
    test_password = input("Type in a trial password: ").lower()

    #Write logic to see if the password is in the dictionary file below here:


    if test_password in readMe:
        print("Oh no! It's to weak. Try again!")
    else :
        print("Awsome! Your password isn't in the dictionary.")
