from ShortQuizModules import (questions,
                              user_answer,
                              check,
                              percent,
                              letterGrade
                              )

questionsNanswers = ["What is highschool did Sumit first attend?",
                     "What was Sumit's best mile time?",
                     "How many cousins does Sumit Have?",
                     "What is 2 + 2?",
                     "What is the square root of 169?",
                     "What game does Edo like to play the most?"
]

answer_choices = ["A. Van Nuys B. Reseda C. Birmingham D. Cleveland",
                  "A. Between 5 and 6 mins B. Under 5 mins C. Between 6 and 7 mins D. Over 7 mins",
                  "A. 14 B. 8 C. 19 D. 17",
                  "A. 1  B. 2 C. 4 D. 6",
                  "A. 12 B. 19 C. 69 D. 13 ",
                  "A. League of legends B. Pokemon C. Valorant D. Rocket League"
]

answers = ["B",
           "A",
           "C",
           "C",
           "D",
           "A"
]

user_answers = []
qNumber = 0

flag = False

while not flag:
    if qNumber == len(answers):
        break
    else:
        qNumber = questions(n1=qNumber,l1=questionsNanswers,l2=answer_choices)
        user_answer(user_answers,qNumber)
        print("-------------------------------------------------------------------------------")

totalScore = check(user_answers,answers)
per = percent(totalScore,answers)
grade = letterGrade(per)
print(f"You got {totalScore} of {len(answers)}."
      f"\n You got {per:.2f}% which is a{grade}.")