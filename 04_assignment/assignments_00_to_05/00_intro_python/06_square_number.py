def main():
    square : float = float(input("\033[1;3m Type a number to see its Square: \033[0m"))
    print(str(square) + " Square is " + str(square ** 2))

if __name__ == '__main__':
    main()