from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# holds all the question objects
question_bank = []

# looping through the questions
for question in question_data:
    # getting the text and the answer and assigning it to a variable
    question_text = question["text"]
    question_answer = question["answer"]
    # getting the question data and assigning it to a new variable
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].answer)

# getting reference to the quiz question
quiz = QuizBrain(question_bank)

# checking
while quiz.still_has_question():
    # asking the user a new question
    quiz.next_question()

print("CONGRATULATIONS you've completed all of our quiz questions!")
print(f"Your final Score is: {quiz.score}/{quiz.question_number}")
