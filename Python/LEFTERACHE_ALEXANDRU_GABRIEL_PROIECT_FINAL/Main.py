# Importarea modulelor/claselor neesare in cadrul modulului curent
from Cinematograf import Cinematograf as Cinema
import Functii_aplicatie as Func


if __name__ == "__main__":

    # Obtinerea listei de filme salvata intr-o executie anterioara in fisierul
    # "lista_filme.txt" (considerat implicit, deja existent in cadrul proiectului)
    cinema_list = Func.get_list()

    # Crearea unei instante de tip Cinematograf
    cinema = Cinema(cinema_list)
    print("\nBine ati venit!")

    # Afisarea listei de comenzi valabile
    Func.lista_comenzi()

    # Crearea unei bucle pentru preluarea comenzilor utilizatorului. Intreruperea acesteia poate fi
    # realizata prin introducerea comenzii 'exit'
    while True:
        # Preluarea comenzii de la tastatura
        comanda = Func.get_input()

        # Identificarea si executarea comenzii
        Func.alege_comanda(comanda, cinema)
