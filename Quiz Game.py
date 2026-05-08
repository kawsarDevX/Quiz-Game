questions = [

    {
        "question": "What is 5 + 5 ?",
        "options": ["a) 8", "b) 10", "c) 12"],
        "answer": "b"
    },

    {
        "question": "What is 9 - 4 ?",
        "options": ["a) 5", "b) 3", "c) 7"],
        "answer": "a"
    },

    {
        "question": "What is 3 * 3 ?",
        "options": ["a) 6", "b) 9", "c) 12"],
        "answer": "b"
    },

    {
        "question": "What is 10 / 2 ?",
        "options": ["a) 2", "b) 4", "c) 5"],
        "answer": "c"
    },

    {
        "question": "Which planet do we live on ?",
        "options": ["a) Mars", "b) Earth", "c) Jupiter"],
        "answer": "b"
    }

]

while True:

    choice = int(input("Game Mode Selection\n 1. Easy\n 2. Medium\n 3. Hard\n (Please select only 1, 2, or 3) : "))
    if choice not in (1,2,3):
        print("Error: Invalid Choice! Please select 1, 2, or 3 only........")
        continue
    if choice == 1:
        num1 = questions[0]
        num2 = questions[1]

    elif choice == 2:
        num3 = questions[2]
        num4 = questions[3]

    elif choice == 3:
        num5 = questions[4]
    
    def noob(num1):
        while True:
            print("(question)- ",num1["question"],num1["options"])
            user = input("Choose: ").lower()
            if user not in ("a", "b", "c"):
                print("Error select a, b, or c only")
                continue
            elif user == num1["answer"]:
                print("Currect Answer")
            else:
                print("Wrong Answer")

            break
            
        
    
    if choice == 1:
        noob(num1)
    if choice == 1:
        noob(num2)
    
    if choice == 2:
        noob(num3)
    if choice == 2:
        noob(num4)
    
    if choice == 3:
        noob(num5)

    again = (input("Do you wanna play again? (y/n): ")).lower()
    if again == "n":
        print("thank you for playing our game")
        break
    elif again == "y":
        continue
        
    else:
        print("you press wrong key")
        break
        