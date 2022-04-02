# libraries needs to be imported 

import turtle 
import matplotlib.pyplot as pl  # to generate graph 
import csv  # to store scores in excel file 
import os.path 
from random import choice 
import random 
import operator 
import time
 
file_name = "scores.csv" 
file_exist = os.path.isfile(file_name)           # to check if file already exists 
if file_exist == False:                          # if file does not exist then it creates new csv file and inserts a title in it 
    fh = open(file_name, "a") 
    fh.writelines(["Points Achived" + "\n"]) 
    fh.close() 
 
 
def max_avg(file_name): 
    fh = open(file_name, "r") 
    csv_reader = list(csv.reader(fh))               # extracts data from the csv file 
    data_points = [float(csv_reader[i][0]) for i in range(len(csv_reader)) if i >= 1] # list comprehention to make a list of all the scores of user from previous games 
    fh.close() 
    max_score = max(data_points)        # gets the maximum scores from all games user played 
    avg_score = round(sum(data_points) / len(data_points), 2) # gets the average scores from all games user played 
    print("your maximum score is : ", max_score) 
    print("your average score is : ", avg_score) 
    print() 
    print("Your Current score is : ", points) 
    print() 
    if max_score == data_points[-1]: # checks if the latest games's score is the highest or not
        lst = [data_points[i] for i in range(0, len(data_points) - 1)] 
        if max_score in lst: 
            print("Well Done !!!!") 
            print("Your current score is in level with your personal high score") 
        else: 
            print("Well Done !!!!") 
            print("You Have Created A New High Score ") 
    else: 
        print("Keep Trying !!!!") 
        print("You Can Beat Your Best Score ") 
 
 
def graph_scores(file_name):                # gets data from csv and plots a graph 
    fh = open(file_name, "r") 
    csv_reader = list(csv.reader(fh)) 
    y = [float(csv_reader[i][0]) for i in range(len(csv_reader)) if i >= 1] 
    x = [int(i) for i in range(1, len(y) + 1)] 
    fh.close() 
    pl.plot(x, y, "r.", linewidth=4, linestyle="-", markeredgecolor="b") 
    pl.ylabel("Points --> ") 
    pl.xlabel("Number of games played -->") 
    pl.title("Scores in games played") 
    pl.show() 
 
 
def show_points():                  # shows how many points the user earned currently 
    global points 
    print(f"Your current score is {points}") 
 
 
def word_game():            # asks user to make a word from random set o letters 
    global points 
    answers_dict = { 
        'eac': 'ace', 'ngki': 'king', 'uqnee': 'queen', 'acjk': 'jack', 'dofo': 'food', 'orgilal': 'gorilla', 
        'berrub': 'rubber', 'cnplie': 'pencil', 'bkdoraey': 'keyboard', 'sumoe': 'mouse', 'rohes': 'horse', 
        'kisrcte': 'sticker' 
    } 
    card = choice(list(answers_dict.items())) 
    question = card[0] 
    answer = card[1] 
    print("Rearrange these jumbled letters {} to form a meaningful word  ".format(question))
    user_answer = input("Enter Your Answer :") 
    print()
 
    if user_answer == answer:                   # checks is answer is correct and if yes then awards 1 point
        print("Your answer is correct!!!") 
        print("You earn 1 point") 
        print()
        print("Please Go Back To Turtle Module To Continue Playing!!!!")
        print()
        points += 1 
    else: 
        print("Your Answer Is Wrong")           # if answer is wrong then displays the correct answer
        print("Correct Answer Is :",answer)
        print()
        print("Please Go Back To Turtle Module To Continue Playing!!!!")
        print()
    show_points() 
 
 
def math_quiz():            # generates a random maths questions 
    global points 
    first_number = random.randint(1, 100) 
    sec_number = random.randint(1, 100) 
    ope = ["+", "-", "*", "/"] 
    random_operator = random.randint(0, 3) 
    comp_ans = 0 
    if random_operator == 0: 
        comp_ans = operator.add(first_number, sec_number) 
    elif random_operator == 1: 
        comp_ans = operator.sub(first_number, sec_number) 
    elif random_operator == 2: 
        comp_ans = operator.mul(first_number, sec_number) 
    elif random_operator == 3: 
        comp_ans = operator.truediv(first_number, sec_number) 
 
    comp_ans = round(comp_ans, 2) 
    print("Solve this maths problem and give your answer by rounding it to 2 digits :") 
 
    print("Solve : {} {} {} = ".format(first_number, ope[random_operator], sec_number)) 
    c = float(input("Enter your answer here: ")) 
    if comp_ans == c: 
        print()
        print("Your answer is correct!!!") 
        print()
        print("You earn 1 point") 
        print()
        print("Please Go Back To Turtle Module To Continue Playing!!!!")
        print()
        points += 1 
    else: 
        print()
        print("oops your answer is wrong") 
        print("the correct answer is", comp_ans) 
        print("Please Go Back To Turtle Module To Continue Playing!!!!")
        print()
    show_points() 
 
 
def eat_apple():  # checks if the user came near any apple  
    if (player.distance(food1) < 30) : # triggers maths or english game if came near black apple and ends the game if came near red apple
        word_game()                         #black
        x1 = random.randint(-bound, bound) 
        y1 = random.randint(-bound, bound) 
        food1.goto(x1,y1) 
    elif (player.distance(food2) < 30): 
        word_game()                         #black
        x2 = random.randint(-bound, bound) 
        y2 = random.randint(-bound, bound) 
        food2.goto(x2, y2)
    elif (player.distance(food3) < 30): 
        math_quiz()                         #black
        x3 = random.randint(-bound, bound) 
        y3 = random.randint(-bound, bound) 
        food3.goto(x3, y3)
    elif (player.distance(food4) < 30): 
        math_quiz()                         #black
        x4 = random.randint(-bound, bound) 
        y4 = random.randint(-bound, bound) 
        food4.goto(x4, y4)
    elif (player.distance(food5) < 30) or (player.distance(food6) < 30) or (player.distance(food7) < 30) or (player.distance(food8) < 30): 
        print("The Game Has Ended") #red
        turtle.color('black')
        style = ('Arial', 30, 'italic')
        turtle.write('Game Is Over !!!', font=style, align='center')
        turtle.hideturtle()
        time.sleep(1)
        a = turtle.Screen().bye()
 
    
# did not create a running game loop, but i based the logic for everytime an update is keyed in aka when the user 
# press the arrow keys, it checks before executing the appropriate command 
def move_up():  # helps turtle move up and checks if came near apple
    if player.ycor() < bound: # checks if within boundary, if yes, move
        player.setheading(90) 
        player.forward(10) 
    else: # else turn opposite 
        player.setheading(270) 
    eat_apple()  # after moving, check if turtle has eaten apple 
 
 
def move_right(): # helps turtle move up and checks if came near apple
    if player.xcor() < bound:  # checks if within boundary, if yes, move 
        player.setheading(0) 
        player.forward(10) 
    else:  # else turn opposite 
        player.setheading(180) 
    eat_apple()  # after moving, check if turtle has eaten apple 
 
 
def move_left(): # helps turtle move up and checks if came near apple
    if player.xcor() > -bound: # checks if within boundary, if yes, move
        player.setheading(180) 
        player.forward(10) 
    else: # else turn opposite 
        player.setheading(0) 
    eat_apple() # after moving, check if turtle has eaten apple 
 
 
def move_down(): # helps turtle move up and checks if came near apple
    if player.ycor() > -bound: # checks if within boundary, if yes, move
        player.setheading(270) 
        player.forward(10) 
    else: # else turn opposite 
        player.setheading(90) 
    eat_apple() # after moving, check if turtle has eaten apple 
 
 
def data(points): 
    """To put scores of user in excel file""" 
    point = str(points) 
    fh = open(file_name, "a") 
    fh.writelines([point + "\n"]) 
    fh.close() # after moving, check if turtle has eaten apple 

    


print()
print()
print()
print()
print("                               ___-------___           ")
print("                           _-~~             ~~-__      ") 
print("                         _/ \                 /  \_    ") 
print("     /^\__/^\          _/   \                /     \_  ")
print("   /|  O|| O|        _/      \______________/        \_ ")
print("  | |___||__|      _/        /              \          \_ ")
print("  |          \   _/         /                \           \_ ")
print("  |   (_______) /__________/                  \____________\_ ")
print("  |         /  ||          \                  /              \__       _ ")
print("   \_        \^\\           \                /                  \     // ") 
print("     \_        ||    _-_     \______________/        _-_      //\____//  ")
print("       \_      ||--------------------------------------------||_____//    ")
print("         \-----||====/      |======================|         |/~~~~~/      ")
print("         |_____/  _/       /                       \_        \_           ")
print("                 (_(______/                          \_______|_)           ")
print()

# initialize points = 0 

time.sleep(3)
print()
print("HOW TO PLAY THIS GAME :")
print("1. Try To Eat Black Apples And Answer Randomly Generated Mathematics Or English Questions To Earn 1 Points ")
print("2. STAY AWAY FROM THE RED POISONOUS APPLE ")
print("3. PLEASE GO TO THE TURTLE MODULE TO PLAY THE GAME !!!!")
print()
print()
print("-"*80)
print()
time.sleep(6)

points = 0 
dimensions = 600  # create screen with dimensions 
screen = turtle.Screen() 
screen.listen() 
screen.setup(width=(dimensions + 40), height=(dimensions + 40))  # +40 is jus so we can see the turtle 
bound = dimensions / 2  # define boundaries for calculation 
screen.bgcolor("blue")

# creating the turtles for food and player 
food1 = turtle.Turtle() 
food1.speed(0) 
food1.shape("circle") 
food1.color("Black") 
food1.penup() 
food1.shapesize(0.50, 0.50) 
x1 = random.randint(-bound, bound)  # randomise coordinates but keeping within boundaries 
y1 = random.randint(-bound, bound) 
food1.goto(x1, y1) 


food2 = turtle.Turtle() 
food2.speed(0) 
food2.shape("circle") 
food2.color("Black") 
food2.penup() 
food2.shapesize(0.50, 0.50) 
x2 = random.randint(-bound, bound) 
y2 = random.randint(-bound, bound) 
food2.goto(x2, y2) 


food3 = turtle.Turtle() 
food3.speed(0) 
food3.shape("circle") 
food3.color("Black") 
food3.penup() 
food3.shapesize(0.50, 0.50) 
x3 = random.randint(-bound, bound)  # randomise coordinates but keeping within boundaries 
y3 = random.randint(-bound, bound) 
food3.goto(x3, y3) 


food4 = turtle.Turtle() 
food4.speed(0) 
food4.shape("circle") 
food4.color("Black") 
food4.penup() 
food4.shapesize(0.50, 0.50) 
x4 = random.randint(-bound, bound)  # randomise coordinates but keeping within boundaries 
y4 = random.randint(-bound, bound) 
food4.goto(x4, y4) 


food5 = turtle.Turtle() 
food5.speed(0) 
food5.shape("circle") 
food5.color("Red") 
food5.penup() 
food5.shapesize(0.50, 0.50) 
x5 = random.randint(-bound, bound) 
y5 = random.randint(-bound, bound) 
food5.goto(x5, y5) 


food6 = turtle.Turtle() 
food6.speed(0) 
food6.shape("circle") 
food6.color("Red") 
food6.penup() 
food6.shapesize(0.50, 0.50) 
x6 = random.randint(-bound, bound) 
y6 = random.randint(-bound, bound) 
food6.goto(x6, y6) 


food7 = turtle.Turtle() 
food7.speed(0) 
food7.shape("circle") 
food7.color("Red") 
food7.penup() 
food7.shapesize(0.50, 0.50) 
x7 = random.randint(-bound, bound) 
y7 = random.randint(-bound, bound) 
food7.goto(x7, y7) 


food8 = turtle.Turtle() 
food8.speed(0) 
food8.shape("circle") 
food8.color("Red") 
food8.penup() 
food8.shapesize(0.50, 0.50) 
x8 = random.randint(-bound, bound) 
y8 = random.randint(-bound, bound) 
food8.goto(x8, y8) 

 
player = turtle.Turtle() 
player.shape("turtle") 
player.shapesize(1) 
player.color("green") 
player.penup() 
 

turtle.onkeypress(fun=move_up, key="Up") # activates the arrow keys to control turtle 
turtle.onkeypress(fun=move_right, key="Right") 
turtle.onkeypress(fun=move_down, key="Down") 
turtle.onkeypress(fun=move_left, key="Left") 


screen.exitonclick()
data(points)                        #enters the points earned to csv file


print()
print("You have earned",points,"points !!!")
print()
c= True 
while c==True:                      # asks user if he/she want to see statistics like average and maximum score etc
    stats= input("""Would you like to see the stats from previous games? 
Enter Y for yes and N for no : """)
    print()
    
    if stats.upper()=="Y":
        print("-"*45)
        max_avg(file_name)
        graph_scores(file_name)
        c=False
        print("Good Bye see you again later !!!")
        print("-"*45)
        
    elif stats.upper()=="N":        # to exit the game 
        print("Good Bye see you again later !!!")
        c=False 
    else:                           #if user types wrong input then it askes the same quetion again
        print()
        print("You entered a wrong response")
        c=True 
 
