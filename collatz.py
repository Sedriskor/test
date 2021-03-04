def collatz(number): #collatz sequence funtion
    if number % 2 == 0:
        number = number // 2
        print(number)

    else:
        number = 3 * number + 1
        print(number)

    return number


def user_enter():
    while True:
        try:  
            number = int(input('Pls enter a number: '))

        except ValueError:
            print('Pls enter a number not a str !!')
            continue

        return number


number = user_enter()
while True:  #main program loop
    number = collatz(number)  
    if number == 1:
        break



