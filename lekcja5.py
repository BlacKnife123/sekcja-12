"""
PLIK - nazwana lokacja, która przechowuje na STAŁE dane na dysku

RAM - pamięć podręczna komputera, gdzie przechowywane są dane TYMCZASOWO


Operacje na plikach
1) otwieranie
2) edycja/ pisanie/ czytanie
3) zamykanie

podstawowwe sposoby na otwieranie plików

r - R ead (czytanie - domyślnie)
w - W rite (pisanie) - jeśli plik istniał to go usunie, jeśli nie to stworzy nowy
a - A ppend (dopisywanie)

rozszerzenie to tylko 'tekst' nadawany po to, aby inne programy rozpoznawały plik w odpowiedni dla tych programów sposób

tell - mówi, gdzie skończyliśmy ostatnia operacje na pliku
seek - szuka (zmienia) - na miejsce wskazane przez nas
"""

with open("test.txt","r",encoding="UTF-8") as file:
    print(file.readline())
    print(file.tell())
    print(file.readline())
    print(file.tell())
    file.seek(0)
    print(file.tell())
    print(file.readline())
    print(file.tell())

