import random as r
secret_age = r.randint(1, 10)
flag = False


def game_func(guessed_age, secret):
    if guessed_age < secret:
        return 'Too Low'
    elif guessed_age > secret:
        return 'Too High'
    else:
        return 'CORRECT!'


for i in range(1, 6):
    print("Take a guess. You have " + str(6-i) + " guesses left!")
    guess = input()
    if game_func(int(guess), secret_age) == 'CORRECT!':
        print("YOU WON THE GAME!")
        flag = True
        break
if not flag:
    print("YOU LOSE THE GAME!")
