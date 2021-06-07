import random
import time
responses = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего",
"Хорошие перспективы", "Знаки говорят - да", "Пока не ясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсазать",
 "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

## Following function asks user question, then returns random results from responses
def answerQuery():
    question = input("Задай свой вопрос: ")
    print(random.choice(responses))
    print("\n")
answerQuery()

## Following asks user if they would like to play again, and loops until user is finished
secondQuestion = (input("Ещё вопросы есть? Д/Н: "))
while secondQuestion == str("Д"):
    answerQuery()
    secondQuestion = (input("Ещё впросы? Д/Н: "))
else:
    print(input("Press any key to exit"))
    