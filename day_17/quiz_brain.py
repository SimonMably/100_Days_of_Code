class QuizBrain:
    """Class that cycles through questions of the quiz. If user gets a
    question correct, provides user with next question."""

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """
        Retrieves next question from question_list, depending on
        question_list. Displays question to user and takes user input.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text}"
                            f" (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """
        Checks list of questions to see if there are any remaining
        questions. Returns True or False. Quiz continues if True, quiz ends
        if False."""
        # From Udemy course solution (it makes more sense than my solution
        # below)
        return self.question_number < len(self.question_list)
        '''# A less simplified variation of the the above code
        if self.question_number < len(self.question_list):
            return True
        else:
            return False'''
        '''# My solution
        if self.question_number < 12:
            return True
        else:
            return False'''

    # correct_answer = current_question.answer (from next_question())
    def check_answer(self, user_answer, correct_answer):
        """Checks if users answer is correct or wrong. If correct, adds 1
        point to users score."""
        if user_answer.lower() == correct_answer.lower():
            print("You are correct!!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


