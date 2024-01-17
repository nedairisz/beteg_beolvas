import feladatok

lista=feladatok.beolvas()
"""
szamlalo=feladatok.idosebb(lista)
print(f"{szamlalo} db 50 évnél idősebb beteg van.")
"""
szamlalo2=feladatok.demencia(lista)

li_index=feladatok.legidosebb(lista)
print(f"A legidősebb beteg kora:{lista[li_index].kor} neme:{lista[li_index].nem} betegségei:{lista[li_index].betegsegek}")

"""
n_atlag=feladatok.atlag_n(lista)
f_atlag=feladatok.atlag_f(lista)
if n_atlag>f_atlag:
    print(f"A nők átlagéletkora {n_atlag} magasabb mint a férfiaké {f_atlag}")
else:
    print(f"A férfiak átlagéletkora {f_atlag} magasabb mint a nőké {n_atlag}")"""