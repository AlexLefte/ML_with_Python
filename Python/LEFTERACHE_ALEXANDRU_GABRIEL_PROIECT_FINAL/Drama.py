from Film import Film


# Definirea clasei Drama, mostenint clasa Film
class Drama(Film):
    def __init__(self, titlu: str, durata: float, varsta_minima: int):
        super().__init__(titlu, durata)
        self.varsta_minima = varsta_minima
