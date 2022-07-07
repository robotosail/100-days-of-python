# creating a class that controls the question number
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        # getting the question list from the user and assigning it to a variable
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Retrieves items from the question list"""
        # getting the question and question number from the question list and then asking the user the question
        current_question = self.question_list[self.question_number]
        # incrementing the question number after each answered question
        self.question_number += 1
        # turning the user answer into title case so it matches the format
        user_answer = input(
            f"Question {self.question_number}: {current_question.text} (True/False): ").title()
        # sending the data over to the check answer function
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        """Returns true if there are still quiz questions left"""
        # checks if the question number is still less than the length of the question list
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Checks if the user answer matches the correct answer """
        # returns true if the answers matches and false if it doesn't
        if user_answer == correct_answer:
            self.score += 1
            print("Correct")
        else:
            print("Wrong")
            # shows correct answer
            print(f"The correct answer is {correct_answer}")
        # showing the user their score
        print(f"Current Score: {self.score}/{self.question_number}")
        # prints a new line
        print("\n")
