# Dialog manager for the Severus Snape chatbot

import potions_list
import analysis
import nlg
import frame
import random


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
        return f"Hello, I am Severus Snape, the potions master. I will ask you about the ingredients of the {self.potion.get_name()}."

    def interview(self):
        while not self.frame.check_if_complete():
            question = self.check_not_repeated_question()
            print(question)
            print(f"Memory: {self.memory}")
            print(f"Frame: {self.frame}")
            user_answer = input()
            self.check_user_answer(
                user_answer, self.check_if_contains_ingredient(question)
            )
        return f"Congratulations! You have completed the {self.potion.get_name()}!"

    # Check if ingredient of the question is already in the memory
    def check_not_repeated_question(self):
        question = self.question_generator.generate_question()
        if question is None:
            print("IT WAS NONE")
            return self.check_not_repeated_question()
        checked_question = analysis.Analysis(question)
        if checked_question.check_for_ingredient() in self.memory:
            self.check_not_repeated_question()
        else:
            self.memory.append(checked_question.check_for_ingredient())
            return question

    # Check if the question contains an ingredient of the target potion
    def check_if_contains_ingredient(self, question):
        checked_question = analysis.Analysis(question)
        ingredient = checked_question.check_for_ingredient()[0]
        if ingredient in self.target_ingredients:
            return True
        else:
            return False

    # Check user answer
    def check_user_answer(self, user_answer, is_target_ingredient):
        if is_target_ingredient:
            if user_answer == "yes":
                self.frame.add_ingredient(self.memory[-1])
                print(self.pos_answer_generator.generate_answer())
            elif user_answer == "no":
                self.wrong_answers += 1
                print(self.neg_answer_generator.generate_answer())
        else:
            if user_answer == "yes":
                self.wrong_answers += 1
                print(self.neg_answer_generator.generate_answer())
            elif user_answer == "no":
                print(self.pos_answer_generator.generate_answer())


if __name__ == "__main__":
    dialog_manager = DialogManager()
    print(dialog_manager.intro())
    print(dialog_manager.interview())
