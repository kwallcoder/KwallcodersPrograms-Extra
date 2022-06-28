count_Right = 0
count_Wrong = 0
streak = 0
hold_Streak = 0
best_Streak = 0
def quiz_Question(asked_Question, answer):
    global count_Right
    global streak
    global count_Wrong
    global hold_Streak
    global best_Streak
    Question = input(asked_Question)
    if Question == answer:
        count_Right += 1
        streak += 1
            
        if count_Right == 1 and streak == 1:
            print("Good Job!")
        elif count_Right == 2 and streak == 1:
            print("Great! Thats your second one correct")
        elif count_Right == 2 and streak == 2:
            print("Great! You're on a streak of two!")
        elif count_Right == 3 and streak == 1:
            print("Great! Thats your third one correct")
        elif count_Right == 3 and streak == 2:
            print("Great! You're on a streak of two!")
        elif count_Right == 3 and streak == 3:
            print("Great! You're on a streak of three!")
    else:
        streak = 0
        count_Wrong += 1
        if count_Wrong == 1:
            print("Wrong!")
        elif count_Wrong == 2:
            print("Horrible! Thats your second one wrong!")
        elif count_Wrong == 3:
            print("Wow... they were right, you are bad! Thats your third one wrong.")
    print("")
    if hold_Streak < streak:
          hold_Streak = streak
          best_Streak = streak

asked_Question = "How many subscribers does Kwallcoder have?"
answer = "144"
quiz_Question(asked_Question, answer)

asked_Question = "Is Kwallcoder a gaming channel?"
answer = "Yes"
quiz_Question(asked_Question, answer)

asked_Question = "Is Kwallcoder a bad gaming channel?"
answer = "No"
quiz_Question(asked_Question, answer)

print("You got",count_Right,"questions correct,",count_Wrong,"questions wrong, and your best streak was", best_Streak,".") 
