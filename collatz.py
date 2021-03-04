def collatz(number):
    if number % 2 == 0:
        number = number//2
    else:
        number = 3*number + 1
    return number


number = int(input('Plas enter a number: '))

while True:
    number = collatz(number)
    print(number)
    if number ==1:
        break

