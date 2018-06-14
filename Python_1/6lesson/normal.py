# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health=150, damage=20, armor=2):
        self.name = name.lower()
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, who_defend):
        who_defend.health -= (self.damage / who_defend.armor)

    def _calc_armor(self, who_calc):
        print(self.damage / who_calc.armor)


class Player(Person):
    def __init__(self, name, health=150, damage=20, armor=2):
        super().__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health=150, damage=20, armor=1):
        super().__init__(name, health, damage, armor)


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    # первым атаковать будет тот, кто бой инициировал. Его имя должно быть первым в классе Game
        while player.health and enemy.health >= 0:
            player.attack(enemy)
            enemy.attack(player)
        if player.health > 0:
            print(player.name + ',поздравляем, вы победил!')
        else:
            print(player.name + 'очень жаль, но вы проиграли, попробуйте после того как увеличите урон')


telwen = Player('Telwen')
npc = Enemy('BadGuy')
x = Game(telwen, npc)
