# ⚔️ Batalha RPG - Sistema de Turnos em Python

Um jogo clássico de batalha RPG por turnos executado no terminal, desenvolvido inteiramente em Python. Este projeto foi criado para aplicar conceitos avançados de **Programação Orientada a Objetos (POO)**, como herança, abstração, encapsulamento e tratamento de exceções personalizadas.

## 🎮 Funcionalidades

* **Três Classes Únicas:**
  * 🛡️ **Kina (Guerreiro):** Maior quantidade de vida, focado em ataques diretos com espada.
  * 🏹 **Pally (Arqueiro):** Ataques à distância com arco. Possui um sistema integrado de contagem e esgotamento de flechas.
  * 🔮 **Mage (Mago):** Usa magia através de um cajado. Possui um sistema de "Mana" que é consumida a cada ataque.
* **Inteligência Básica do Inimigo:** O sistema gera um adversário com uma classe aleatória (diferente da do jogador) para garantir batalhas dinâmicas.
* **Sistema de Exceções Customizadas:** Regras de negócio protegidas por erros personalizados (ex: tentar atacar sem flechas, atacar um alvo já derrotado ou atacar a si mesmo).

## 📂 Estrutura do Projeto

O código foi construído de forma modular para facilitar a leitura e manutenção:

* `main.py`: Arquivo principal responsável pelo loop do jogo, interação com o utilizador e gestão dos turnos.
* `personagens.py`: Contém a classe base abstrata `Personagem` e as classes filhas com os seus métodos específicos de ataque.
* `armas.py`: Define os equipamentos usados pelas classes (`Espada`, `Arco`, `Cajado`), gerindo atributos como dano e munição.
* `erros.py`: Módulo dedicado às classes de erro personalizadas (`PersonagemDerrotadoError`, `AlvoInvalidoError`, `SemFlechasError`).

## 🚀 Como Executar o Jogo

1. Certifica-te de que tens o [Python 3](https://www.python.org/) instalado no teu computador.
2. Faz o clone deste repositório ou descarrega os ficheiros.
3. Abre o terminal (ou Prompt de Comando), navega até à pasta do projeto e executa:

```bash
python main.py
