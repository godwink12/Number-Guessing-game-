import random as rand

secret_number = rand.randint(1,100)
succeed = False
user_tries = 3

while True:
    # User Input
    user_input = input('Enter the secret number: ')

    # Check user Input 
    if user_input == secret_number :
        print ('Congratulation You guessed the Secret Number')
        succeed = True


