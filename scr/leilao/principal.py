from builtins import print

from scr.leilao.dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario('Gui')
ana = Usuario('Ana')

lance_da_ana = Lance(ana, 10.0)
lance_do_gui = Lance(gui, 156.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_da_ana)
leilao.lances.append(lance_do_gui)

for lance in leilao.lances:
    print(f'Usuario {lance.usuario.nome} deu um lance de R${lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'Menor lance = {avaliador.menor_lance} e Maior lance = {avaliador.maior_lance}')