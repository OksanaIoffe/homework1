
# Класс для представления вопроса
class Question:
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

# Класс для представления теста
class Quiz:
    def __init__(self, name, questions=None):
        self.name = name
        self.questions = questions or []

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        score = 0
        for question in self.questions:
            print(question.text)
            user_answer = input("Введите ваш ответ: ")
            if question.check_answer(user_answer):
                score += 1

        print("Вы ответили на", score, "вопросов из:", len(self.questions))

# Класс для представления администратора
class Administrator:
    def __init__(self):
        self.quizzes = []

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def search_result(self, quiz_name):
        for quiz in self.quizzes:
            if quiz.name == quiz_name:
                return quiz

# Пример использования
quiz1 = Quiz("История")
quiz1.add_question(Question("В каком году произошла Русская революция?", "1917"))
quiz1.add_question(Question("Кто был самым первым президентом США?", "Джордж Вашингтон"))

quiz2 = Quiz("Математика")
quiz2.add_question(Question("Сколько будет 2 + 2?", "4"))
quiz2.add_question(Question("Какой символ используется для обозначения умножения?", "*"))
quiz2.add_question(Question("Как называется угол величиной 90 градусов?", "Прямой"))


admin = Administrator()
admin.add_quiz(quiz1)
admin.add_quiz(quiz2)

quiz_name = input("Введите название теста для поиска результата: ")
found_quiz = admin.search_result(quiz_name)
if found_quiz:
    found_quiz.run()
else:
    print("Тест с таким названием не найден.")
