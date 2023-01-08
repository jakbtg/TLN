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

    def intro(self):
        return print(
            f"Hello, I am Severus Snape, the potions master. I will ask you about the ingredients of the {self.potion.get_name()}."
        )

    def interview(self):
        self.intro()
        while not self.frame.check_if_complete():
            print(f"Memory: {self.memory}")
            print(f"Frame: {self.frame}")
            print(f"Wrong answers: {self.wrong_answers}\n")
            question, n = self.choose_question()
            print(question + "\n")
            user_answer = input()
            self.check_user_answer(user_answer, question, n)
            if self.wrong_answers == 3:
                return self.is_failed()
            print("\n")
        return self.is_succeeded()

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
        # if question is None:
        #     print("IT WAS NONE")
        #     return self.check_not_repeated_question()
        checked_question = analysis.Analysis(question)
        if checked_question.check_for_ingredient() in self.memory:
            print("IT WAS IN MEMORY")
            return self.check_not_repeated_question()
        else:
            self.memory.append(checked_question.check_for_ingredient())
            return question

    # Ask a question choosing randomly from a list of questions
    def ask_question(self):
        questions = [
            "Can you tell me an ingredient of the potion?",
            "Do you know an ingredient of the potion?",
            "Can you name an ingredient of the potion?",
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
            if is_positive_answer:
                self.frame.add_ingredient(self.memory[-1])
                print(self.pos_answer_generator.generate_answer())
            else:
                self.wrong_answers += 1
                print(self.neg_answer_generator.generate_answer())
        else:
            if is_positive_answer:
                self.wrong_answers += 1
                print(self.neg_answer_generator.generate_answer())
            else:
                print(self.pos_answer_generator.generate_answer())

    # Check user answer if it is a proposal of an ingredient
    def user_proposes_ingredient(self, user_answer):
        checked_answer = analysis.Analysis(user_answer)
        ingredients = checked_answer.check_for_ingredient()
        if len(ingredients) == 0:
            self.wrong_answers += 1
            print(self.neg_answer_generator.generate_answer())
            return
        if self.check_if_already_said(ingredients[0]):
            print("It is correct, but you already said it, are you dumb?")
            return
        if ingredients[0] in self.target_ingredients:
            self.frame.add_ingredient(ingredients)
            self.memory.append(ingredients)
            print(self.pos_answer_generator.generate_answer())
        else:
            self.wrong_answers += 1
            self.memory.append(ingredients)
            print(self.neg_answer_generator.generate_answer())

    # Check if user already said the ingredient
    def check_if_already_said(self, ingredient):
        if ingredient in self.frame.get_current_ingredients():
            return True
        return False

    # If the user fails
    def is_failed(self):
        return print("You dumb student! You failed!")

    # Get grade
    def get_grade(self):
        rand = random.choice([1, 1.5, 2, 2.5, 3])
        grade = 31 - (self.wrong_answers * rand)
        print(f"Rand is {rand}, wrong answers are {self.wrong_answers}")
        return math.floor(grade)

    # If the user succeeds
    def is_succeeded(self):
        return print(
            f"Congrats! You have completed the {self.potion.get_name()}! Your grade is {self.get_grade()}."
        )


if __name__ == "__main__":
    dialog_manager = DialogManager()
    dialog_manager.interview()
