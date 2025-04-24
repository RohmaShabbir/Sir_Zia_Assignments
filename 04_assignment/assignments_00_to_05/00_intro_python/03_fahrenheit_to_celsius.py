def main():
    # Prompt the user for input
    fahrenheit = float(input("Enter a temeratur in Fahrenheit: "))

    # convert farenheit to celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Output the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# Python file to call the main() function.
if __name__ == '__main__':
    main()