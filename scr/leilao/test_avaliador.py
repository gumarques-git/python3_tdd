from unittest import TestCase

from scr.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_avalia(self):

        gui = Usuario('Gui')
        ana = Usuario('Ana')

        lance_da_ana = Lance(ana, 10.0)
        lance_do_gui = Lance(gui, 156.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_da_ana)
        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 10.0
        maior_valor_esperado = 156.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
