favourite_game_style = input("What's your favourite game style")
favourite_game_series = input("What's your favourite game series")
favourite_game = input("What's your favourite game")
if favourite_game_style == "RPG":
    if favourite_game_series == "Eldar Scrolls":
        if favourite_game == "Oblivion":
            print("Noice")
        elif favourite_game == "Skyrim":
            print("Not cool broski")
        elif  favourite_game == "Morrowind":
            print("Haha old person")
elif favourite_game_style == "FPS":
    if favourite_game_series == "Halo series":
        if favourite_game == "Halo 1":
            print("Classic")
        elif favourite_game == "Halo 2":
            print("duel wield needlers op")
        elif favourite_game == "Halo 3":
            print("deffo the best")
        elif favourite_game == "Halo Wars":
            print("Go die")
    elif favourite_game_series == "COD":
        print("lol noob")
    else:
        print("What other FPS games are there?")
elif favourite_game_style == "MOBA":
    if favourite_game == "LOL":
        print("Yay, add me")
    elif favourite_game == "Dota 2":
        print("Go home Russian scum")
else:
    print("Enter an acutual valid game please")
    
