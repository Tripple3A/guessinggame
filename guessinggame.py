'''In Bagels, a deductive logic game, you
must guess a secret three-digit number
based on clues. The game offers one of
the following hints in response to your guess:
“Pico” when your guess has a correct digit in the
wrong place, “Fermi” when your guess has a correct
digit in the correct place, and “Bagels” if your guess
has no correct digits. You have 10 tries to guess the
secret number.'''
#establish the correct guess
#has to run until you get it right
#while loop only runs ten time
#it breaks only when you get correct answer or no of tries ends
#let the program say the correct guess when it ends
CORRECT_NUMBER = '275'
number_of_tries = 1

while number_of_tries <= 10:
    number = input("Please enter a three-digit number: ")
    
    #incase the number entered is exactly correct
    if number == CORRECT_NUMBER:
        print(f"Correct guess! The secret code is {number}")
        break
    else:
        
        for letter in number:
            if letter in CORRECT_NUMBER:
                if number.index(letter) == CORRECT_NUMBER.index(letter):
                    print(f"Fermi!! Letter {letter} is in the right place")
                else:
                    print(f"Pico!!Letter {letter} is in the wrong place")
                
            else:
                print(f"Bagels!!The letter {letter} is not part of the three-secret digit")
                
    number_of_tries+=1
    
                
print("Unfortunately the number of tries are up!")
print(f"The correct secret-code was {CORRECT_NUMBER}")
    
        
        
    

    
        