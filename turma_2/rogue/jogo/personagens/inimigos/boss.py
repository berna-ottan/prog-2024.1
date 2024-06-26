import random

from .inimigo import Inimigo

class Boss(Inimigo):
    def __init__(self):
        self.forca = random.randint(15, 30)
        self.vida = random.randint(50, 130)
        self.defesa = random.randint(1, 6)
        self.nome = "Boss"

    def defender(self, dano):
        dano -= self.defesa
        if dano > 0:
            self.vida -= dano
