import random   #import module random from standard library | zaimportuj modułu random z biblioteki standardowej

guesses_taken = 0 #assign 0 to variable| przypisz wartość 0 do zmiennej

print('Hello! What is your name?') #output string | wyświetl napis
myName = input() #assign value from keybord to variable | przypisz wartość z klawiatury do zmiennej

number = random.randint(1, 20) #assign to variable integer value randomly generated between 1 to 19 |
                               # przypisz do zmiennej wartość całkowitą losowo wygenerowaną z przedziału od 1 od 19
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #output 2 strings and 1 string typ variable concatenated together|
                                                                           #wyświetl 2 napisy i 1 zmienną typu "łańcuch znaków", które połączono ze sobą

while guesses_taken < 6: #repeat until variable is smaller than 6| powtórz dopóki zmienna jest mniejsza niż 6
    print('Take a guess.') #output string | wyswietl napis
    guess = input() #assign value from keybord to variable | przypisz wartość z klawiatury do zmiennej
    guess = int(guess) #change type of variable to integer type | zmień typ zmiennej na typ liczby całkowitej

    guesses_taken += 1 #increment value of variable by 1 | zwiększ wartość zmiennej o 1

    if guess < number: # check if first variable is smaller than second variable | sprawdż czy pierwsza zmienna jest mniejsza od drugiej zmiennej
        print('Your guess is too low.') #output string | wyswietl napis

    if guess > number: # check if first variable is greater than second variable | sprawdż czy pierwsza zmienna jest większa od drugiej zmiennej
        print('Your guess is too high.') #output string | wyswietl napis

    if guess == number: #  check if first variable is equal to second variable | sprawdż czy pierwsza zmienna jest równa drugiej zmiennej
        break # stop the loop and pass to the first line outside the loop | przerwij pętle i przejðż do pierwszej lini poza pętlą

if guess == number:# check if first variable is equal to second variable | sprawdż czy pierwsza zmienna jest równa drugiej zmiennej
    guesses_taken = str(guesses_taken) #change type of variable to string type | zmień typ zmiennej na typ "łańcuch znaków"
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #output 3 strings and 2 string typ variables concatenated together|
                                                                                              #wyświetl 3 napisy i 2 zmienne typu "łańcuch znaków", które połączono ze sobą

if guess != number: # check if first variable is different from second variable | sprawdż czy pierwsza zmienna jest różna od drugiej zmiennej
    number = str(number) #change type of variable to string type | zmień typ zmiennej na typ "łańcuch znaków"
    print('Nope. The number I was thinking of was ' + number) #output 1 string and 1 string typ variable concatenated together|
                                                              #wyświetl 1 napis i 1 zmienną typu "łańcuch znaków", które połączono ze sobą
