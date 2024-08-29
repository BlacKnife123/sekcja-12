def readFile(plik):
    try:
        with open(plik,"r",encoding="UTF-8") as file:
            for line in file:
                print (line)

    except FileNotFoundError:
        print("Plik nie istnieje")

plik = input("Jak nazywa się plik który otworzyć: ")

readFile(plik)

