class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        return "Очень интересный вопрос! Не знаю."


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        return f"{someone.name}, {question}\n" + someone.answer_question(question) + "\n"


class Curator(Human):
    def answer_question(self, question):
        if question == "мне грустненько, что делать?":
            return f"Держись, всё получится. Хочешь видео с котиками?"
        else:
            return super().answer_question(question)


class Mentor(Human):
    def answer_question(self, question):
        if question == "мне грустненько, что делать?":
            return "Отдохни и возвращайся с вопросами по теории."
        else:
            return super().answer_question(question)


class CodeReviewer(Human):
    def answer_question(self, question):
        if question == "что не так с моим проектом?":
            return "О, вопрос про проект, это я люблю."
        else:
            return super().answer_question(question)


student = Student("Тимофей")
curator = Curator("Марина")
mentor = Mentor("Ира")
reviewer = CodeReviewer("Евгений")
friend = Human("Виталя")

print(student.ask_question(curator, 'мне грустненько, что делать?'))
print(student.ask_question(mentor, 'мне грустненько, что делать?'))
print(student.ask_question(reviewer, 'когда каникулы?'))
print(student.ask_question(reviewer, 'что не так с моим проектом?'))
print(student.ask_question(friend, 'как устроиться на работу питонистом?'))
print(student.ask_question(mentor, 'как устроиться работать питонистом?'))
