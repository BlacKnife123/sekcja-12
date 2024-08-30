def readFile(plik, slowo):
    try:
        with open(plik,"r",encoding="UTF-8") as file:
            for line in file:
                wordCount = line.count(slowo)

            print(f"Słowo {slowo} w pliku {plik} wystąpilo: {wordCount}")

    except FileNotFoundError:
        print("Plik nie istnieje")

    except PermissionError:
        print("Nie masz dostępu do odczytania pliku")

plik = input("Jak nazywa się plik który otworzyć: ")
slowo = input("Jakie słowo chcesz sprawdzić: ")

readFile(plik,slowo)


