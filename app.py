from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.receber_avaliacao('gui', 10)
restaurante_praca.receber_avaliacao('caua', 8)
restaurante_praca.receber_avaliacao('peixada', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()