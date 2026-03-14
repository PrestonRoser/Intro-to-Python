import db_handling

def main():
    con = db_handling.db_handler()

    command(con)

def input_player_data():
        player_name = input("What is the player's name?\n")
        player_age = input("What is their age?\n")
        player_score = input("What is their overall score?\n")

        return player_name, player_age, player_score

def command(con):
    action = input("What action would you like to take? 'i'=insert, 'r'=read, 's'=search, or 'q'=quit.\n")

    if action == 'q':
        return
    elif action == 'i':
        name, age, score = input_player_data()
        db_handling.insert_data(con, name, age, score)
    elif action == 'r':
        print(db_handling.read_name(con))
    elif action == 's':
        filter = input("Are you searching for players by name, age, or score?\n").lower() # need to be method ?

        search_factor = None
        if filter == 'name':
            search_factor = input("What is the name you are searching for?\n").lower()
        elif filter == 'age':
            search_factor = input("What is the age you are searching for?\n")
        elif filter == 'score':
            search_factor = input("What is the score you are searching for?\n")
        else:
            print(f"Unknown input '{filter}' recieved, please try again.")

        if search_factor != None:
            result = db_handling.get_user_by_filter_factor(con, filter, search_factor)

            if result == None:
                print(f"We were unable to find any players by the factor '{search_factor}'.")
            else:
                print(result)
    else:
        print(f"Command '{action}' not found. Please try again using 'i'=insert, 'r'=read, 's'=search, or 'q'=quit.\n")

    return command(con)


if __name__ == "__main__":
    main()
