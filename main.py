print("==================")
print("Welcome To Gamertag Program")
print("==================")
print("Press Any key To Continue")
input()

bool = True
while bool:
    print("Enter Your Gamertag")
    gamertag = input()
    if len(gamertag) < 3:
        print("Gamertag Must Be At Least 3 Characters Long")
    elif len(gamertag) > 16:
        print("Gamertag Must Be At Most 16 Characters Long")
    else:
        print("Your Gamertag Is: " + gamertag)
        bool = False
