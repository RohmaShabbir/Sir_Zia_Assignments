SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("\033[1;3mPlease type an adjective and press enter.\033[0m ")
    noun: str = input("\033[1;3mPlease type a noun and press enter.\033[0m ")
    verb: str = input("\033[1;3mPlease type a verb and press enter.\033[0m ")

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

