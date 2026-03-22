from pes import Pes, PsiRasa
from panicek import Panicek

pes1 = Pes(jmeno = "Ales", rasa = PsiRasa.BULDOCEK, barva = "Cerna", vek=11)
pes2 = Pes("Peny", PsiRasa.RETRIEVER, "Zlata", 6)
pes3 = Pes("Carl", "Dalmatin", "Bila", 10)

panicek1 = Panicek(jmeno="Honza", psi=[pes1, pes2])
panicek2 = Panicek(jmeno="Karel", psi=[pes3])
#
# panicek1.dej_povel_pozdravu_psum()
# panicek2.dej_povel_pozdravu_psum()

panicek1.dej_povel_pozdravu_psum()
pes4 = Pes("Josef", "Dalmatin", "Bila", 10)
panicek1.pridej_psa(pes4)

panicek1.dej_povel_pozdravu_psum()
print("konec")

