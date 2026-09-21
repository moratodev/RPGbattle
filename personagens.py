from abc import ABC, abstractmethod
from erros import AlvoInvalidoError, PersonagemDerrotadoError, SemFlechasError

# Definindo a classe personagem.
class Personagem(ABC):
    def __init__(self, nome, vida): # Método construtor
        # Atributos da classe
        self.__nome = nome.title().strip()
        self.__vida = vida

    # Métodos da classe
    def obter_nome(self):
        return self.__nome

    def obter_vida(self):
        return self.__vida

    def receber_dano(self, dano):
        if dano <= 0:
            raise ValueError("O dano deve ser maior que zero.")

        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

        print(f"{self.__nome} foi atingido, perdeu {dano} pontos de vida.")

    def esta_vivo(self):
        return self.__vida > 0

    @abstractmethod
    def atacar(self, jogador):
        pass

    def __str__(self):
        return (
            f"Nome: {self.__nome} | "
            f"Vida: {self.__vida} | "
        )


# Criando as classes filhas de PERSONAGEM.
class Mage(Personagem):
    def __init__(self, nome, arma):
        super().__init__(nome, 95)
        self.__arma = arma
        self.__mana = 100 # Novo atributo mago

    def atacar(self, jogador):
        if jogador is self:
            raise AlvoInvalidoError("Você não pode atacar a si mesmo.")

        if not jogador.esta_vivo():
            raise PersonagemDerrotadoError(
                f"O {jogador.obter_nome()} foi derrotado, não é possível atacar!"
            )

        if self.__mana < 8:
            print("Sua mana esgotou!")
        else:
            self.__mana -= 8
            jogador.receber_dano(self.__arma.obter_dano())

    def __str__(self):
        return (
            f"----- Status -----\n"
            f"Nome: {self.obter_nome()} | Classe: Mago\n"
            f"Vida: {self.obter_vida()} | Mana Restante: {self.__mana}\n"
            f"Arma: {self.__arma.obter_nome()} | Dano: {self.__arma.obter_dano()}"
        )


class Kina(Personagem):
    def __init__(self, nome, arma):
        super().__init__(nome, 130)
        self.__arma = arma

    def atacar(self, jogador):
        if jogador is self:
            raise AlvoInvalidoError("Você não pode atacar a si mesmo.")

        if not jogador.esta_vivo():
            raise PersonagemDerrotadoError(
                f"O {jogador.obter_nome()} foi derrotado, não é possível atacar!"
            )

        jogador.receber_dano(self.__arma.obter_dano())

    def __str__(self):
        return (
            f"----- Status -----\n"
            f"Nome: {self.obter_nome()} | Classe: Kina\n"
            f"Vida: {self.obter_vida()}\n"
            f"Arma: {self.__arma.obter_nome()} | Dano: {self.__arma.obter_dano()}"
        )


class Pally(Personagem):
    def __init__(self, nome, arma):
        super().__init__(nome, 110)
        self.__arma = arma

    def atacar(self, jogador):
        if jogador is self:
            raise AlvoInvalidoError("Você não pode atacar a si mesmo.")

        if not jogador.esta_vivo():
            raise PersonagemDerrotadoError(
                f"O {jogador.obter_nome()} foi derrotado, não é possível atacar!"
            )

        try:
            self.__arma.diminuir_flecha()
            jogador.receber_dano(self.__arma.obter_dano())
        except SemFlechasError as e:
            print(e)

    def __str__(self):
        return (
            f"----- Status -----\n"
            f"Nome: {self.obter_nome()} | Classe: Pally\n"
            f"Vida: {self.obter_vida()}\n"
            f"Dano: {self.__arma.obter_dano()} | Flechas restantes: {self.__arma.obter_flechas()}\n"
        )