class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        choice = input(f"Q.{self.question_number + 1}: {current_q.text} (True/False): ")
        self.keep_score(choice)
        self.question_number += 1

    def keep_score(self, ans):
        current_q = self.question_list[self.question_number]
        if current_q.answer == ans:
            print("That's right! Great Job!")
            self.score += 1
            print(f"Your score is now: {self.score}/{self.question_number}.\n")
        else:
            print("Nope, that's not it. On to the next!")
            print(f"Your score is now: {self.score}/{self.question_number}.\n")
