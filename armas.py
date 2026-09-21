from erros import SemFlechasError

# Definindo a classe arma.
class Arma:
    def __init__(self, nome, dano): # Método construtor
        # Atributos da classe arma.
        self.__nome = nome.title().strip()
        self.__dano = dano

    # Métodos arma
    def obter_nome(self):
        return self.__nome

    def obter_dano(self):
        return self.__dano


# Criando as classes filhas de ARMA
class Arco(Arma):
    def __init__(self, nome, dano):
        super().__init__(nome, dano)
        self.__flecha = 15

    # Métodos arco
    def obter_flechas(self):
        return self.__flecha

    def diminuir_flecha(self):
        if self.__flecha <= 0:
            self.__flecha = 0
            raise SemFlechasError("Suas flechas esgotaram.")
        else:
            self.__flecha -= 1


class Espada(Arma):
    def __init__(self, nome, dano):
        super().__init__(nome, dano)


class Cajado(Arma):
    def __init__(self, nome, dano):
        super().__init__(nome, dano)