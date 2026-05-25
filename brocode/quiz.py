questions =("What Day is it?:",
            "What month is it?:",
            "What did you eat today?:",
            "How do you feel today?:",
            "Are you tired?")
options = (("A. Sunday", "B. Monday", "C. Friday", "D. Saturday"),
           ("A. May", "B. Feb", "C. July", "D. Aug"),
           ("A. Chips", "B. Sandwich", "C. Popcorn", "D. nothing"),
           ("A. Happy", "B. Sad", "C. Ok", "D. Meh"),
           ("A. Yes", "B. No", "C. Maybe", "D. Kinda"))
answers = ("C", "A", "C", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("---------------------")
print("       RESULTS       ")
print("---------------------")

for answer in answers:
    print(answer, end=" ")
print()

for guess in guesses:
    print(guess, end=" ")
print()

score = score/len(questions) * 100
print(f"Your score is: {score}%")