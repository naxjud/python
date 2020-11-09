
car_started = False
print("####Car Game####")

while True:
    command = input("> ").lower()

    if command == "start":
        if car_started:
            print("Car already started")
        else:
            car_started = True
            print("Car started")
    elif command == "stop":
        if not car_started:
            print("Car already stopped")
        else:
            car_started = False
            print("Car stopped")
    elif command == "quit":
        print("Car Game ended")
        break
    elif command == "help":
        print("""
    start - for Starting
    stop  - for stopping
    quit  - to end the game
    help  - to get help
        """)
    else:
        print("""
    I don't understand this command!
    Type help to see all available commands 
        """)
