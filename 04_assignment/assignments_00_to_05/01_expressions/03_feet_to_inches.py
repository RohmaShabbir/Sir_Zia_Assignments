INCHES_IN_FOOT: int = 12  # coversion factor. There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: ")) # Get the numberof feet, make sure to cast it to a float!
    inches: float = feet * INCHES_IN_FOOT # Perform the conversion
    print(f"This is {inches} inches!")
    

if __name__ == "__main__":
    main()