def main():
    filename = input("")
    with open(filename) as file:
        print(file.read())

if __name__ == "__main__":
    main()