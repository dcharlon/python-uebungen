import random
import sys

def main():
    level = level_generator()
    problems = []
    solutions = []
    number_of_problems = 10
    generated_problems = 0
    while True:
        x = generate_integer(level)
        y = generate_integer(level)
        problems.append(f"{x} + {y} = ")
        solutions.append(x + y)
        generated_problems += 1
        if generated_problems == number_of_problems:
            break

    done_problems = 0
    score = 0
    attempts_at_problem = 0
    while True:
        if done_problems == number_of_problems:
            sys.exit(f"Your score is {score} out of {number_of_problems} ")
        try:
            attempted_calculation = int(input(problems[done_problems]))
            if attempted_calculation == solutions[done_problems]:
                done_problems += 1
                score += 1
                attempts_at_problem = 0
            else:
                print ("EEE")
                attempts_at_problem += 1
        except ValueError:
            print("EEE")
            attempts_at_problem += 1
        if attempts_at_problem == 3:
            print(f"{problems[done_problems]}{solutions[done_problems]}")
            done_problems += 1
            attempts_at_problem = 0
        
            

def level_generator():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
            else: 
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

main()