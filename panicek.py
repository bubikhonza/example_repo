from pes import Pes

class Panicek:
    def __init__(self, jmeno: str, psi: list):
        self.jmeno = jmeno
        self.psi = psi

    def dej_povel_pozdravu_psum(self):
        print(f"Davam povel vsem psum!!! ({self.jmeno})")
        for pes in self.psi:
            pes.pozdrav()

    def pridej_psa(self, pes: Pes):
        self.psi.append(pes)
