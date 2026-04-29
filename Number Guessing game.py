import random as rand

secret_number = rand.randint(1,100)
succeed = False
user_tries = 0

while True:
    # User Input
    user_input = int(input('Enter the secret number: '))
    if user_input < 1 or user_input > 100: # Check User Stay on Number range
        print('Out of bonds! Stay between 1 and 100')
        continue

    user_tries += 1 # Increment 1 each time the User Get it Wrong
    # Check user Input 
    if user_input == secret_number :
        print ('Congratulation You guessed the Secret Number!!!')
        break
    elif user_input > secret_number :
        print('Hey almost there the Number is Lower!') # Print Hint
    elif user_input < secret_number :
        print('Hey almost there the Number is Higher!') # Print Hint
    else :
        print ('Wrong Try again!!!')
    if user_tries == 3 : 
        print ('Nice try!!! You exceeded your Tries The Answer Was :',secret_number)
        break
    


