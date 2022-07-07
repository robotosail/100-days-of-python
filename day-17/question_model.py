# store data from a list so it can be used as an object instead of an array
class Question:
    # creating a new initizaliztion
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer
