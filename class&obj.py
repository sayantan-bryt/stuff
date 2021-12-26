class Enemy:
    life = 3

    def attack(self):
        print("ouch!")
        self.life -=1

    def checkLife(self):
        if self.life <= 0:
            print("I lost")
        else:
            print(str(self.life) + " Life left")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()

enemy1.checkLife()
enemy2.checkLife()