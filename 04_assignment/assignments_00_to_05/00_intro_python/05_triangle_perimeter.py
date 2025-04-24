def main():
    side1 : float = float(input("\033[1;3m What is the length of side 1? \033[0m"))
    side2 : float = float(input("\033[1;3m What is the length of side 2? \033[0m"))
    side3 : float = float(input("\033[1;3m What is the length of side 3? \033[0m"))

    print("The perimeter of the triangle is " + str(side1 + side2 + side3))

if __name__ == '__main__':
    main()