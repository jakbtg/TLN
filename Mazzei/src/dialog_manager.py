# Dialog manager for the Severus Snape chatbot

import potions_list
import analysis
import nlg
import frame
import random
import math


class DialogManager:
    def __init__(self):
        self.potion = random.choice(potions_list.potions)
        self.frame = frame.Frame(self.potion)
        self.target_ingredients = self.frame.get_target_ingredients()
        self.wrong_answers = 0
        self.question_generator = nlg.NLG("questions")
        self.pos_answer_generator = nlg.NLG("positive answers")
        self.neg_answer_generator = nlg.NLG("negative answers")
        self.memory = []

    # Print the introduction
    def intro(self):
        print(
            f"Professor Snape: Hello, I am Severus Snape, the potions master. I will ask you about the ingredients of the {self.potion.get_name()}."
        )

    # Print memory, frame and wrong answers -- for debugging
    def print_helper(self):
        print(f"\nMemory: {self.memory}")
        print(f"Frame: {self.frame}")
        print(f"Wrong answers: {self.wrong_answers}\n")

    # This method manages the whole chat with the user
    def interview(self):
        self.intro()
        while not self.frame.check_if_complete():
            self.print_helper()
            question, n = self.choose_question()
            self.print_question(question)
            user_answer = input("Student: ")
            self.check_user_answer(user_answer, question, n)
            if self.wrong_answers == 4:
                return self.is_failed()
        return self.is_succeeded()

    # Print the choosen question
    def print_question(self, question):
        print(f"Professor Snape: {question}\n")

    # Choose random question
    def choose_question(self):
        rand = random.randint(0, 100)
        n = 0
        if rand < 30:
            n = 1
            return self.check_not_repeated_question(), n
        else:
            n = 2
            return self.ask_question(), n

    # Check if ingredient of the question is already in the memory
    def check_not_repeated_question(self):
        question = self.question_generator.generate_question()
        checked_question = analysis.Analysis(question)
        if checked_question.check_for_ingredient() in self.memory:
            print("IT WAS IN MEMORY")  # For debugging
            return self.check_not_repeated_question()
        else:
            self.memory.append(checked_question.check_for_ingredient())
            return question

    # Ask a question choosing randomly from a list of questions
    def ask_question(self):
        questions = [
            "Can you tell me an ingredient of the potion?",
            f"Do you know an ingredient of the {self.potion.get_name()}?",
            "Which might be an ingredient of this potion?",
            f"Which ingredient do you think is in the {self.potion.get_name()}?",
            "What do you need to make this potion?",
        ]
        return random.choice(questions)

    # Check if the question contains an ingredient of the target potion
    def check_if_contains_ingredient(self, question):
        checked_question = analysis.Analysis(question)
        ingredient = checked_question.check_for_ingredient()[0]
        if ingredient in self.target_ingredients:
            return True
        else:
            return False

    # Check general user answer
    def check_user_answer(self, user_answer, question, n):
        if n == 1:
            self.user_replies_ingredient(
                user_answer, self.check_if_contains_ingredient(question)
            )
        else:
            self.user_proposes_ingredient(user_answer)

    # Check user answer if it is a reply to a question
    def user_replies_ingredient(self, user_answer, is_target_ingredient):
        analyzed_answer = analysis.Analysis(user_answer)
        is_positive_answer = analyzed_answer.check_positivity()
        if is_target_ingredient:
            # Add target ingredient to frame both if the answer is positive or negative
            # Because even if the user says no, when the Professor replies that the student is wrong,
            # the student will get the piece of information that the ingredient is in the potion and +1 wrong answer
            self.frame.add_ingredient(self.memory[-1])
            if is_positive_answer:
                print(f"Professor Snape: {self.pos_answer_generator.generate_answer()}")
            else:
                self.wrong_answers += 1
                print(f"Professor Snape: {self.neg_answer_generator.generate_answer()}")
        else:
            if is_positive_answer:
                self.wrong_answers += 1
                print(f"Professor Snape: {self.neg_answer_generator.generate_answer()}")
            else:
                print(f"Professor Snape: {self.pos_answer_generator.generate_answer()}")

    # Check user answer if it is a proposal of an ingredient
    def user_proposes_ingredient(self, user_answer):
        checked_answer = analysis.Analysis(user_answer)
        ingredients = checked_answer.check_for_ingredient()
        if len(ingredients) == 0:
            self.wrong_answers += 1
            print(f"Professor Snape: {self.neg_answer_generator.generate_answer()}")
            return
        if self.check_if_already_said(ingredients[0]):
            print(
                "Professor Snape: It is correct, but you already said it, are you dumb?"
            )
            return
        if ingredients[0] in self.target_ingredients:
            self.frame.add_ingredient(ingredients)
            self.memory.append(ingredients)
            print(f"Professor Snape: {self.pos_answer_generator.generate_answer()}")
        else:
            self.wrong_answers += 1
            self.memory.append(ingredients)
            print(f"Professor Snape: {self.neg_answer_generator.generate_answer()}")

    # Check if user already said the ingredient
    def check_if_already_said(self, ingredient):
        if ingredient in self.frame.get_current_ingredients():
            return True
        return False

    # If the user fails
    def is_failed(self):
        print(
            "\t\t You failed the exam and you are wasting my time. Get out of my sight!"
        )

    # Get grade
    def get_grade(self):
        rand = random.choice([2, 3, 3.8, 4.3])
        grade = 31 - (self.wrong_answers * rand)
        return math.floor(grade)

    # Print comment based on grade
    def comment(self):
        comment = ""
        grade = self.get_grade()
        if grade == 31:
            comment = "You definitely appreciate the exact art of potion making, my dear student. You possess the predisposition to become one of the best potion makers in the world.\n\t\t I am very proud of you, your grade is 30 cum laude."
        elif grade >= 27:
            comment = f"My student, indeed you are a great potion maker. Your potential is interesting.\n\t\t You passed the exam with a grade of {grade}."
        elif grade >= 22:
            comment = f"You probably did not pay attention to the class, you still have a lot to learn. But you are not a really bad student.\n\t\t You somehow passed the exam with a grade of {grade}."
        else:
            comment = f"You got {grade}. Only a griffindor would reply to my questions like you did. You did pass the exam, but I don't want to waste my time with you anymore. Go away!"
        return comment

    # If the user succeeds
    def is_succeeded(self):
        print(f"\t\t {self.comment()}")


if __name__ == "__main__":
    dialog_manager = DialogManager()
    dialog_manager.interview()
