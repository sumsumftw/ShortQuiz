def questions(n1, l1, l2):
    print(l1[n1])
    print(l2[n1])
    n1 += 1
    qNumber = n1
    return qNumber

def user_answer(user_answers,qNumber):
    valid_input = False
    possible_inputs = ["A", "B", "C", "D"]
    while not valid_input:
        choice = input("Which of the following would you like to select?: ").upper()
        if choice in possible_inputs:
            user_answers.append(choice)
            valid_input = True
        else:
            print("That is not an option!")

def check(user_answers,answers):
    totalScore = 0
    for i in range(len(user_answers)):
        if user_answers[i] == answers[i]:
            totalScore += 1
    return totalScore

def percent(total_Score, answers):
    per = total_Score/len(answers)*100
    return per

def letterGrade(per):
    if per == 100:
        grade = "n A+"
    elif per >= 90:
        grade = "n A"
    elif per >= 80:
        grade = " B"
    elif per >= 70:
        grade = " C"
    elif per >= 60:
        grade = " D"
    else:
        grade = " F"
    return grade

