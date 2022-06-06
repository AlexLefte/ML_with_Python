from Film import Film


# Definirea clasei Animatie, mostenind clasa Film
class Animatie(Film):
    def __init__(self, titlu: str, durata: float, limba_dublare: str):
        super().__init__(titlu, durata)
        self.limba_dublare = limba_dublare

    # Definirea metodei de returnare a limbii in care se realizeaza dublarea
    def get_limba(self):
        return self.limba_dublare
