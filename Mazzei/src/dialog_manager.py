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
        self.answer_generator = nlg.NLG("answers")

    def intro(self):
        return f"Hello, I am Severus Snape, the potions master. I will ask you about the ingredients of the {self.potion.get_name()} potion."

    def interview(self):
        while not self.frame.check_if_complete():
            print(self.question_generator.generate_question())
            answer = input()
            checked_answer = analysis.Analysis(answer)
            if checked_answer.number_of_ingredients() == 1:
                self.frame.add_ingredient(checked_answer.check_for_ingredient())
            print(self.answer_generator.generate_answer())
        return (
            f"Congratulations! You have completed the {self.potion.get_name()} potion!"
        )


if __name__ == "__main__":
    dialog_manager = DialogManager()
    print(dialog_manager.intro())
    print(dialog_manager.interview())
