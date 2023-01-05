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
        self.question_generator = nlg.NLG("questions")
        self.pos_answer_generator = nlg.NLG("positive answers")
        self.neg_answer_generator = nlg.NLG("negative answers")
        self.memory = []

    def intro(self):
        return f"Hello, I am Severus Snape, the potions master. I will ask you about the ingredients of the {self.potion.get_name()} potion."

    def interview(self):
        while not self.frame.check_if_complete():
            # for i in range(4):
            question = self.check_not_repeated_question()
            print(question)
            print(f"Memory: {self.memory}")
            print(f"Frame: {self.frame}")
            user_answer = input()
            # checked_answer = analysis.Analysis(user_answer)
            # if checked_answer.number_of_ingredients() == 1:
            #     self.frame.add_ingredient(checked_answer.check_for_ingredient())
            # print(self.pos_answer_generator.generate_answer())
            if self.check_user_answer(user_answer):
                print(self.pos_answer_generator.generate_answer())
                self.frame.add_ingredient(self.memory[-1])
            else:
                print(self.neg_answer_generator.generate_answer())
                self.frame.add_wrong_ingredient()
        return (
            f"Congratulations! You have completed the {self.potion.get_name()} potion!"
        )

    # Check if ingredient of the question is already in the memory
    def check_not_repeated_question(self):
        question = self.question_generator.generate_question()
        checked_question = analysis.Analysis(question)
        if checked_question.check_for_ingredient() in self.memory:
            self.check_not_repeated_question()
        else:
            self.memory.append(checked_question.check_for_ingredient())
            return question

    # Check if the user answer is correct
    def check_user_answer(self, answer):
        current = self.memory[-1]
        tmp = self.frame.get_wrong_ingredients()
        self.frame.add_ingredient(current)
        if tmp == self.frame.get_wrong_ingredients():
            # Means that the proposed ingredient is in the potion
            if answer == "yes":
                return True
            else:
                return False
        else:
            # Means that the proposed ingredient is not in the potion
            if answer == "no":
                return True
            else:
                return False


if __name__ == "__main__":
    dialog_manager = DialogManager()
    print(dialog_manager.intro())
    print(dialog_manager.interview())
