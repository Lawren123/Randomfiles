# --- Define your functions below! ---
def intro():
     print("Hello. I am a bot named Alex")
def process_input(solution):
    farewell = ["goodbye","see you later","farewell","bye"]
    greetings = ["hi", "Hello","Wassup","what's good ", "what's up" ]
    #if solution == "hi"
    if is_valid_input(solution,greetings):
        say_greeting()
    elif is_valid_input(solution,farewell):
        say_farewell()
    else:
        say_default()

def say_greeting():
    print("Hey there!")

def say_default():
    print("That's cool")
def say_farewell():
    print("goodbye")
def is_valid_input(user_input, valid_response):
    for item in valid_response:
        if user_input == item:
            return True
    return False
#leaving code
def leaving():
    print ("Ok see you later friend")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) " )
        answer = answer.lower()
            #print("That's cool") #replace
        process_input(answer)



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
