def show_welcome_message():
    print("==================")
    print("Welcome To Gamertag Program")
    print("==================")
    print("Press Any key To Continue")
    input()


def process_gamertag_input():
    print("Enter Your Gamertag (3-16 Characters, or type 'exit'):")
    gamertag = input().strip()

    if gamertag.lower() == "exit":
        print("Exiting program...")
        return False


    if len(gamertag) < 3:
        print("Gamertag Must Be At Least 3 Characters Long")
    elif len(gamertag) > 16:
        print("Gamertag Must Be At Most 16 Characters Long")
    else:
        print("Your Gamertag Is: " + gamertag)

    return True


def run_program():
    show_welcome_message()

    is_running = True
    while is_running:
        is_running = process_gamertag_input()


if __name__ == "__main__":
    run_program()
