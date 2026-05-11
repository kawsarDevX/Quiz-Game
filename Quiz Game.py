import random

easy_questions = [
    {"question": "What is 10 / 2 ?",
        "options": ["a) 2", "b) 4", "c) 5"],
        "answer": "c"
    },

    {
        "question": "Which planet do we live on ?",
        "options": ["a) Mars", "b) Earth", "c) Jupiter"],
        "answer": "b"
    },

    {
        "question": "What color is the sky on a clear day ?",
        "options": ["a) Blue", "b) Green", "c) Red"],
        "answer": "a"
    },

    {
        "question": "How many days are there in a week ?",
        "options": ["a) 5", "b) 6", "c) 7"],
        "answer": "c"
    },

    {
        "question": "Which animal says meow ?",
        "options": ["a) Dog", "b) Cat", "c) Cow"],
        "answer": "b"
    },

    {
        "question": "What is the capital of Bangladesh ?",
        "options": ["a) Dhaka", "b) Sylhet", "c) Khulna"],
        "answer": "a"
    },

    {
        "question": "Which number comes after 9 ?",
        "options": ["a) 8", "b) 10", "c) 11"],
        "answer": "b"
    },

    {
        "question": "How many months are in a year ?",
        "options": ["a) 10", "b) 11", "c) 12"],
        "answer": "c"
    },

    {
        "question": "Which animal can fly ?",
        "options": ["a) Bird", "b) Tiger", "c) Elephant"],
        "answer": "a"
    },

    {
        "question": "What is 7 + 2 ?",
        "options": ["a) 8", "b) 9", "c) 10"],
        "answer": "b"
    },

    {
        "question": "Which season is very cold ?",
        "options": ["a) Summer", "b) Winter", "c) Rainy"],
        "answer": "b"
    },

    {
        "question": "What is 12 - 5 ?",
        "options": ["a) 6", "b) 7", "c) 8"],
        "answer": "b"
    },

    {
        "question": "Which shape has 3 sides ?",
        "options": ["a) Square", "b) Triangle", "c) Circle"],
        "answer": "b"
    }
]
medium_questions = [
    {   "question": "Which language is used for web development ?",
        "options": ["a) Python", "b) HTML", "c) C"],
        "answer": "b"
    },

    {
        "question": "How many continents are there ?",
        "options": ["a) 5", "b) 6", "c) 7"],
        "answer": "c"
    },

    {
        "question": "What is 100 / 4 ?",
        "options": ["a) 20", "b) 25", "c) 30"],
        "answer": "b"
    },

    {
        "question": "Which gas do humans breathe in ?",
        "options": ["a) Oxygen", "b) Nitrogen", "c) Carbon"],
        "answer": "a"
    },

    {
        "question": "Which planet is known as the Red Planet ?",
        "options": ["a) Venus", "b) Mars", "c) Saturn"],
        "answer": "b"
    },

    {
        "question": "What is 14 + 19 ?",
        "options": ["a) 31", "b) 32", "c) 33"],
        "answer": "c"
    },

    {
        "question": "Which country invented pizza ?",
        "options": ["a) Italy", "b) France", "c) Spain"],
        "answer": "a"
    },

    {
        "question": "What is 9 * 8 ?",
        "options": ["a) 72", "b) 81", "c) 64"],
        "answer": "a"
    },

    {
        "question": "What does CPU stand for ?",
        "options": ["a) Central Process Unit", "b) Central Processing Unit", "c) Computer Personal Unit"],
        "answer": "b"
    },

    {
        "question": "Which country has the largest population ?",
        "options": ["a) India", "b) China", "c) USA"],
        "answer": "a"
    },

    {
        "question": "How many hours are there in 2 days ?",
        "options": ["a) 24", "b) 36", "c) 48"],
        "answer": "c"
    },

    {
        "question": "What is 50 - 18 ?",
        "options": ["a) 30", "b) 32", "c) 34"],
        "answer": "b"
    },

    {
        "question": "Which device is used to type on a computer ?",
        "options": ["a) Monitor", "b) Keyboard", "c) Mouse"],
        "answer": "b"
    },

    {
        "question": "Which is the fastest land animal ?",
        "options": ["a) Tiger", "b) Lion", "c) Cheetah"],
        "answer": "c"
    }
]
hard_questions = [

    {
        "question": "Who developed the theory of relativity ?",
        "options": ["a) Newton", "b) Einstein", "c) Tesla"],
        "answer": "b"
    },

    {
        "question": "What is the binary of 10 ?",
        "options": ["a) 1010", "b) 1110", "c) 1001"],
        "answer": "a"
    },

    {
        "question": "Which planet has the most moons ?",
        "options": ["a) Earth", "b) Saturn", "c) Mars"],
        "answer": "b"
    },

    {
        "question": "What is 144 / 12 ?",
        "options": ["a) 10", "b) 11", "c) 12"],
        "answer": "c"
    },

    {
        "question": "Which data structure uses FIFO ?",
        "options": ["a) Stack", "b) Queue", "c) Tree"],
        "answer": "b"
    },

    {
        "question": "Who wrote Romeo and Juliet ?",
        "options": ["a) Shakespeare", "b) Dickens", "c) Homer"],
        "answer": "a"
    },

    {
        "question": "Which is the smallest prime number ?",
        "options": ["a) 0", "b) 1", "c) 2"],
        "answer": "c"
    },

    {
        "question": "What is the capital of Canada ?",
        "options": ["a) Toronto", "b) Ottawa", "c) Vancouver"],
        "answer": "b"
    },

    {
        "question": "What is the result of 2^5 ?",
        "options": ["a) 16", "b) 32", "c) 64"],
        "answer": "b"
    },

    {
        "question": "Which programming language is known for AI ?",
        "options": ["a) Python", "b) HTML", "c) CSS"],
        "answer": "a"
    },

    {
        "question": "Which planet is closest to the sun ?",
        "options": ["a) Venus", "b) Mercury", "c) Earth"],
        "answer": "b"
    },

    {
        "question": "What is 17 * 6 ?",
        "options": ["a) 92", "b) 102", "c) 112"],
        "answer": "b"
    },

    {
        "question": "Which organ pumps blood ?",
        "options": ["a) Brain", "b) Heart", "c) Liver"],
        "answer": "b"
    },

    {
        "question": "Which country won the 2022 FIFA World Cup ?",
        "options": ["a) France", "b) Brazil", "c) Argentina"],
        "answer": "c"
    },

    {
        "question": "Which keyword is used to create a function in Python ?",
        "options": ["a) func", "b) define", "c) def"],
        "answer": "c"
    },

    {
        "question": "What is the value of pi approximately ?",
        "options": ["a) 3.14", "b) 2.14", "c) 4.13"],
        "answer": "a"
    },

    {
        "question": "Which company created Python ?",
        "options": ["a) Microsoft", "b) Google", "c) Python Software Foundation"],
        "answer": "c"
    }
]
while True:
    score = 0
    try:
            
        choice = int(input("Game Mode Selection\n 1. Easy\n 2. Medium\n 3. Hard\n (Please select only 1, 2, or 3) : "))
        if choice not in (1,2,3):
            print("Error: Invalid Choice! Please select 1, 2, or 3 only........")
            continue
        if choice == 1:
            selected_questions = easy_questions
            random.shuffle(selected_questions)
        elif choice == 2:
            selected_questions = medium_questions
            random.shuffle(selected_questions)
        elif choice == 3:
            selected_questions = hard_questions
            random.shuffle(selected_questions)
    except:
        print("Error: Invalid Choice! Please select 1, 2, or 3 only........")
        continue
    
    def noob(question):
        global score
        while True:
            print("(question)- ",question["question"],"\n(options)- ",question["options"])
            user = input("Choose:  ").lower()
            
            if user not in ("a", "b", "c"):
                print("Error select a, b, or c only")
                continue
            elif user == question["answer"]:
                print("Currect Answer")
                score += 1
            else:
                print("Wrong Answer")

            break
    
    for q in selected_questions:
        noob(q)

    if score >=10 :
        print("Final Score:", score)
        print("Excellent! 🥳")
    elif 5 <= score <=9:
        print("Final Score:", score)
        print("Good 🥰")
    else:
        print("Final Score:", score)
        print("Try again..😔")
            
    while True:
        again = (input("Do you wanna play again? (y/n): ")).lower()
        if again == "n":
            print("thank you for playing our game")
            exit()
            
        elif again == "y":
            break
            
        else:
            print("you press wrong key")
            continue
            