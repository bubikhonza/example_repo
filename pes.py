from enum import Enum

class PsiRasa(Enum):
    RETRIEVER = "Retriever"
    BULDOCEK = "Buldocek"
    DALMATIN = "Dalmatin"

class DatabazePsu:
    def __init__(self):
        self.psi = []

    def zapis_psa(self, pes: Pes) -> None:
        self.psi.append(pes)

    def dej_mi_posledniho_psa(self) -> Pes:
        return self.psi[-1]

class Pes:
    def __init__(self,
                 jmeno: str,
                 rasa: PsiRasa,
                 barva: str,
                 vek: int):
        self.jmeno = jmeno
        self.rasa = rasa
        self.barva = barva
        self.vek = vek
        self.cele_jmeno = self.jmeno + str(self.rasa)
        self.id = 12312312
        self.srst = "kratkosrsty"

    def stekej(self):
        if self.rasa == PsiRasa.RETRIEVER:
            print(f"hafhaf, Ja jsem {self.jmeno}")
        elif self.rasa == PsiRasa.BULDOCEK:
            print(f"chrochro, Ja jsem {self.jmeno}")
        else:
            print(f"haf, tady {self.jmeno}")

    def mavej_ocasem(self):
        print(f"Mavam ocasem!!!! ({self.jmeno})")

    def pozdrav(self):
        self.stekej()
        self.mavej_ocasem()