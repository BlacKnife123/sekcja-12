"""
podstawowwe sposoby na otwieranie plików

r - R ead (czytanie - domyślnie)
w - W rite (pisanie) - jeśli plik istniał to go usunie, jeśli nie to stworzy nowy
a - A ppend (dopisywanie)

mnogie tryby otwierania plików:

r+ - do czytania i pisania


w+ - do pisania i czytania
różni się tym że usunie instniejcego pliku lub stworzy plik gdy go nie nie było


a+ - "wieczny tryb" dopisywania jest zawsze na końcu jeśli plik nie istniał - stworzy go
"""

with open("test.txt","a+",encoding="UTF-8") as file:
    file.write("Test")
    file.seek
    print(file.tell())
