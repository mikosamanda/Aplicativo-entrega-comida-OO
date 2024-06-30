from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_praca.receber_avaliacao("Gui", 10)
restaurante_praca.receber_avaliacao("Any", 7)
restaurante_praca.receber_avaliacao("Ju", 9)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()

