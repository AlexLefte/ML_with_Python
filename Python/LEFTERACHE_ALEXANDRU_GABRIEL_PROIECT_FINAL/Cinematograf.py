# Librarie necesara in implementarea metodei afisare_film_aleator()
import random


# Crearea clasei Cinematograf, cu atributele/metodele sale specifice
class Cinematograf:
    # Constructorul unui obiect (instante) din clasa Cinematograf
    def __init__(self, cinema_list=None):
        # Daca nu lista oferita ca argument nu este goala => lista_filme = cinema_list
        if cinema_list is not None:
            self.lista_filme = cinema_list
        # Altfel initializare lista de filme goala
        else:
            self.lista_filme = []
        return

    def adaugare_film(self, film):
        self.lista_filme.append(film)   # Adaugarea elementului apartinand clasei `film` in lista de filme
        # a cinematografului
        return

    def afisare_filme(self):
        # Afisarea unui mesaj de informare in cazul in care lista de filme este goala la momentul curent
        if len(self.lista_filme) == 0:
            print("Nu a fost adaugat niciun film pana in acest moment.")
            return
        for film in self.lista_filme:
            # Afisarea atributelor
            print("Nume film: ", film.titlu)
            print("Durata: ", film.durata, "min")
            print("Gen: ", film.__class__.__name__)
            # Afisarea atributelor particulare (varsta_minima/dublaj), in functie de genul filmului
            if film.__class__.__name__ == "Drama":
                print("Varsta minima: ", film.varsta_minima, "\n")
            elif film.__class__.__name__ == "Animatie":
                print("Dublaj: ", film.limba_dublare, "\n")
        return

    def afisare_animatii(self):
        count = 0  # Contor utilizat pentru a verifica daca exista animatii in lista de filme a cinematografului
        for film in self.lista_filme:
            if film.__class__.__name__ == "Animatie":
                count = 1
                # Afisarea atributelor filmului
                print("Nume animatie: ", film.titlu)
                print("Durata: ", film.durata, "min")
                print("Limba in care se face dublarea: ", film.limba_dublare, "\n")
        # Daca nu a fost gasita nicio animatie, se afiseaza un mesaj informativ
        if count == 0:
            print("Nu a fost introdusa nicio animatie pana in acest moment!")
        return

    def alegere_film_aleator(self):
        # Daca nu exista niciun film in lista cinematografului, se afiseaza un mesaj informativ
        if len(self.lista_filme) == 0:
            print("Nu a fost adaugat niciun film pana in acest moment.")
            return
        # Se extrage un film aleator, utilizand metoda `sample()`, din modulul `random`
        film_random = random.sample(self.lista_filme, 1)[0]
        # Afisarea atributelor corespunzatoare
        print("Nume animatie: ", film_random.titlu)
        print("Durata ", film_random.durata, "min")
        print("Gen: ", film_random.__class__.__name__)
        if film_random.__class__.__name__ == 'Drama':
            print("Varsta minima: ", film_random.varsta_minima)
        elif film_random.__class__.__name__ == 'Animatie':
            print("Dublaj: ", film_random.limba_dublare)
        return

    def salvare_filme(self, nume_fisier):
        # Daca lista filmelor este goala la momentul curent => afisare mesaj informativ
        if len(self.lista_filme) == 0:
            print("Atentie! Nu a fost adaugat niciun film pana in acest moment.")
            return

        # Adaugarea extensiei '.txt'
        nume_fisier += '.txt'

        # Deschiderea unui fisier in modul write-text, avand numele dorit de catre utilizator.
        # Aici se va suprascrie si salva lista filmelor adaugate anterior
        with open(file=nume_fisier, mode="wt") as new_file:
            for film in self.lista_filme:
                # Scrierea atributelor comune
                new_file.write("Nume film: " + film.titlu + "\n" + "Durata: " + film.durata + "\n" +
                               "Gen: " + film.__class__.__name__ + "\n")
                # Scrierea atributelor particulare genului
                if film.__class__.__name__ == 'Drama':
                    new_file.write("Varsta minima: " + film.varsta_minima + '\n\n')
                elif film.__class__.__name__ == 'Animatie':
                    new_file.write("Dublaj: " + film.limba_dublare + '\n\n')
        return
