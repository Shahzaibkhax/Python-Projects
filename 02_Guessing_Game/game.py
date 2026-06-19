import random 

print("============================")
print("Welcome to the guessing game")
print("============================")

secret_number = random.randint (1,100)
print("I have choseen a number form 1 to 100 . Can you guess it ?")

Lives = 7 
guessed_correctly = False

while guessed_correctly == False and Lives > 0 :
    print(f"\n Lives remaining: {Lives}")
    guess = int(input("/n Enter the guess :"))

    if guess < secret_number :
        print("Too Low ! Try a higher number ")
        Lives -= 1 

    elif guess > secret_number :
        print("Too Higher ! Try a low number ")
        Lives-= 1
    
    else :
        print(f"Congatulations ! You guessed the right number{secret_number}.")
        guessed_correctly = True

if Lives == 0:
    print("\nGAME OVER! You ran out of lives.")
    print(f"The secret number was: {secret_number}. Better luck next time!")


