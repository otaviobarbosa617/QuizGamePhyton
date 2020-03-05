import requests
import json
import random
import html
from flask import Flask, render_template, request

app = Flask(__name__)

wins = 0
loses = 0

rodada = False

while rodada == False:
    question_num = 1

    r = requests.get("https://opentdb.com/api.php?amount=1&token=b44a0bcf1507babc06d1f664dddecd519bd5d124998c4827eacb9936fca1e48d&category=14&difficulty=easy&type=multiple")
    r.text

    question = json.loads(r.text)

    question_ask = question['results'][0]['question']
    question_cor = question['results'][0]['correct_answer']
    question_not = question['results'][0]['incorrect_answers']
    question_not.append(question_cor)
    random.shuffle(question_not)
    

    print("Question: " + html.unescape(question_ask) + "\n")

    for alternatives in question_not:
        print (str(question_num) + " - " + (html.unescape(alternatives)))
        question_num += 1

   
    answer_user = input("\nWhat's your answer? Type the number! ")
    answer_user = question_not[int(answer_user)-1]
    
    if answer_user == question_cor:
        print("\nCongrats! You've answered right")
        wins += 1
    else:
        print("\nWRONG")
        print("\nThe correct answer is", html.unescape(question_cor))
        loses += 1
    print("\nYou have", str(wins), "wins")
    print("You have", str(loses), "losses")
    print("\nDo you want to keep playing? type Quit to Exit or press Enter to continue ")
    answer_continue = input()
    if answer_continue == "Quit":
        rodada = True

while rodada == True:
    total_wins = wins - loses
    print("You have a total of", total_wins, "points")
    print("See you soon")
    break



    

    



