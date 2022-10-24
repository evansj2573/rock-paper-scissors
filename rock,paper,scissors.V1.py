
def choice_checker(question):

    valid = False
    while not valid:


        responce = input(question)

        if responce == "r" or responce == "rock":
            return responce





user_choice = choice_checker("choose rock / paper / "
                             "scissors (r/p/s) : ")
