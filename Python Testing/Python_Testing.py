import time
number = 0
iteration = 0
def numbers():
    number = input("What is your number?\n")
    number = int(number)
    print("Starting...")
    for x in range(iteration, number):
        time.sleep(1)
        print(number)
    time.sleep(1)
def main():
    print("Hello!")
    numbers()
main()