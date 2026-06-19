import random 

print("============================")
print("Welcome to the guessing game")
print("============================")

secret_number = random.randint (1,100)
print("I have choseen a number form 1 to 100 . Can you guess it ?")

guessed_correctly = False

while guessed_correctly == False : 
    guess = int(input("/n Enter the guess :"))

    if guess < secret_number :
        print("Too Low ! Try a higher number ")

    elif guess > secret_number :
        print("Too Higher ! Try a low number ")
    
    else :
        print(f"Congatulations ! You guessed the right number{secret_number}.")
        guessed_correctly = True



