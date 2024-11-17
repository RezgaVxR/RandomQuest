"""Projecto de preguntas random"""
import random
import json
import time


def load_questions():
    """Funcion que nos ayuda a cargar nuestra lista"""
    with open("Projectos\questions.json", "r") as f:
        questions = json.load(f)["questions"]
    return questions


def get_random_questions(questions, num_questions):
    """Funcion que obtiene una pregunta al azar"""
    if num_questions > len(questions):
        num_questions = len(questions)

    random_questions = random.sample(questions, num_questions)
    return random_questions


def ask_question(question):
    """Funcion para mostarle la pregunta al usuario y nos proporcione su respuesta"""
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i+1)+".", option)

    number = int(input("Choice the correct answer: "))
    if number < 1 or number > len(question["options"]):
        print("Invalid choice")
        return False

    correct = question["options"][number-1] == question["answer"]
    return correct


questions = load_questions()
total_questions = int(input("Enter the number of questions: "))
random_questions = get_random_questions(questions, total_questions)
correct = 0
start_time = time.time()

for question in random_questions:
    is_correct = ask_question(question)
    if is_correct:
        correct += 1

    print("----------------------------------------")


completed_time = time.time()-start_time
print("Summary")
print("Total Questions: ", total_questions)
print("Correct Answer", correct)
print("Score:", str(round((correct/total_questions)*100, 2))+"%")
print("Time: ", round(completed_time, 2), "seconds")
