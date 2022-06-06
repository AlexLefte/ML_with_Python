# Imortarea claselor necesare in modulul curent
from Cinematograf import Cinematograf
from Drama import Drama
from Animatie import Animatie


# Functie ce afiseaza lista completa de comenzi
def lista_comenzi():
    print("Lista posibilelor comenzi este: ")
    print("1. adauga_drama <titlu> <durata> <varsta>")
    print("2. adauga_animatie <titlu> <durata> <limba_dublare>")
    print("3. afisare (pentru afisarea tuturor filmelor")
    print("4. afisare_animatii")
    print("5. alege_film (alege film aleatoriu)")
    print("6. salveaza_filme <nume_fisier>")
    print("7. exit (iesire din aplicatie)")
    return


# Functie de citire a listei de filme, dintr-un fisier de tip text
# in care a fost realizata o salvare anterioara (implicit 'lista_filme.txt')
def get_list():
    # Initializare lista goala
    movies_list = []
    # Deschiderea fisierului 'lista_filme.txt', in mode read-text
    try:
        with open(file='lista_filme.txt', mode='rt') as new_file:
            lines = new_file.readlines()  # Citire linii prezente in fisier
            divs = []                     # Lista de diviziuni create din lista 'lines'

            # Split lista de linii in diviziuni egale ca dimensiune (cate 5 linii)
            for i in range(0, len(lines), 5):
                divs.append(lines[i:i + 5])         # Adaugarea unei noi diviziuni in lista diviziunilor
            for div in divs:                        # Parcurgerea listei de diviziuni
                for i, line in enumerate(div):      # Parcurgerea fiecarei linii apartinand unei diviziuni
                    line = line.split()             # Transformarea liniei in lista de cuvinte
                    if i % 5 == 0:                  # IF linia 0 => salvare nume
                        nume = " ".join(line[2:])
                    elif i % 5 == 1:                # ELIF linia 1 => salvare durata
                        durata = float(line[1])
                    elif i % 5 == 2:                # ELIF linia 2 => salvare gen
                        gen = line[1]
                    elif i % 5 == 3:                # ELIF linia 3 => salvare varsta_minima/limba_dublare
                        optional = line[-1]
                if gen == 'Drama':                  # IF genul e drama => adauga obiect din clasa Drama
                    movies_list.append(Drama(nume, durata, int(optional)))
                elif gen == 'Animatie':             # ELIF genul e animatie => adauga obiect din clasa Animatie
                    movies_list.append(Animatie(nume, durata, optional))
        return movies_list                          # Returneaza o lista de filme existenta in fisierul text
    except FileNotFoundError:  # Daca fisierul nu a fost deja creat/gasit, se va intoarce o lista goala
        return []

# Functie ce preia comanda utilizatorlui de la tastatura
def get_input() -> list:
    # Preluarea inputului si crearea unei liste continand elementele comenzii
    comanda = input("\nIntroduceti comanda: ").split()
    # Returnarea comenzii sub formatul unei liste
    return comanda


# Functie ce identifica tipul comenzii si ulterior apeleaza functia corespunzatoare
def alege_comanda(cmd: list, cinema: Cinematograf):
    try:
        # Verificam daca a fost introdusa o comanda valida
        if cmd[0] not in ['adauga_drama', 'adauga_animatie', 'afisare', 'afisare_animatii', 'alege_film',
                          'salveaza_filme', 'exit']:
            raise ValueError
    except ValueError:
        # Daca a fost introdusa o comanda invalida se afiseaza un mesaj informativ si se solicita
        # o noua comanda
        print("Comanda invalida!")
        return

    # Verificarea si identificarea comenzii introduse de utilizator
    if cmd[0] == "adauga_drama":
        try:
            # Este testata durata filmului
            if (float(cmd[-2]) > 180 or float(cmd[-2]) < 0) != 0:
                raise ValueError
        except ValueError:
            # Daca durata nu este incadrata in intervalul [0, 180], este afisat un mesaj informativ
            print("Durata filmelor trebuie sa fie de cel putin 0, respectiv"
                  " cel mult 180 de minute! Filmul nu a fost adaugat.")
            return
        except Exception:
            # Mesaj de eroare in cazul in care durata nu poate fi convertita catre float
            print("Nu ati introdus o durata corespunzatoare (float)!")
            return
        # Apelarea functiei adauga_drama
        adauga_drama(cmd[1:], cinema)

    elif cmd[0] == "adauga_animatie":
        try:
            # Este testata durata filmului
            if (float(cmd[-2]) > 180 or float(cmd[-2]) < 0) != 0:
                raise Exception
        except ValueError:
            # Daca durata nu este incadrata in intervalul [0, 180], este afisat un mesaj informativ
            print("Durata filmelor trebuie sa fie de cel putin 0, respectiv"
                  " cel mult 180 de minute! Filmul nu a fost adaugat.")
        except Exception:
            # Mesaj de eroare in cazul in care durata nu poate fi convertita catre float
            print("Nu ati introdus o durata corespunzatoare (float)!")
            return
        adauga_animatie(cmd[1:], cinema)

    elif cmd[0] == "afisare":
        afisare(cinema)

    elif cmd[0] == "afisare_animatii":
        afisare_animatii(cinema)

    elif cmd[0] == "alege_film":
        alege_film(cinema)

    elif cmd[0] == "salveaza_filme":
        salveaza_filme(cmd[1], cinema)

    elif cmd[0] == "exit":
        print("Va multumim! La revedere!")
        quit()
    return


# Functie pentru adaugarea unei drame
def adauga_drama(cmd: list, cinema: Cinematograf):
    # Apelarea metodei de adaugare_film in lista cinematografului
    cinema.adaugare_film(Drama(' '.join(cmd[:-2]), cmd[-2], cmd[-1]))
    return


# Functie pentru adaugarea unei animatii
def adauga_animatie(cmd: list, cinema: Cinematograf):
    # Apelarea metodei de adaugare_film in lista cinematografului
    cinema.adaugare_film(Animatie(' '.join(cmd[:-2]), cmd[-2], cmd[-1]))
    return


# Functie pentru afisarea filmelor salvate in lista cinematografului
def afisare(cinema):
    # Apelarea metodei de afisare a filmelor din cadrul listei cinematografului
    cinema.afisare_filme()
    return


# Functie pentru afisarea animatiilor salvate in lista cinematografului
def afisare_animatii(cinema):
    # Apelarea metodei de afisare a filmelor din cadrul listei cinematografului
    cinema.afisare_animatii()
    return


# Functie pentru alegerea unui film aleator din lista
def alege_film(cinema):
    cinema.alegere_film_aleator()
    return


# Functie pentru salveara filmelor intr-un fisier de tip .txt
def salveaza_filme(nume_fisier, cinema):
    cinema.salvare_filme(nume_fisier)
    return
