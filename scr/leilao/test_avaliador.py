from unittest import TestCase

from scr.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

# Padroes de Nomenclaturas utilizados em testes:
#       test_quando_add_em_ordem_crescente_deve_retornar_menor_e_maior_valor_de_um_lance
    def test_deve_retornar_menor_e_maior_valor_de_um_lance_quando_add_em_ordem_crescente(self):

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

    def test_deve_retornar_menor_e_maior_valor_de_um_lance_quando_add_em_ordem_decrescente(self):

        gui = Usuario('Gui')
        ana = Usuario('Ana')

        lance_da_ana = Lance(ana, 10.0)
        lance_do_gui = Lance(gui, 156.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_da_ana)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 10.0
        maior_valor_esperado = 156.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
