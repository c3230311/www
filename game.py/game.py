class Player:
    def __init__(self, name, health, mana, strength, agility):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.skills = {}

    def add_skill(self, skill_name, skill_power):
        self.skills[skill_name] = skill_power

    def update_health(self, amount):
        self.health += amount

    def update_mana(self, amount):
        self.mana += amount

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print("Skills:")
        for skill, power in self.skills.items():
            print(f"  {skill}: {power}")

# プレイヤーの作成とステータスの表示
player = Player("Hero", 100, 50, 20, 15)
player.add_skill("Fireball", 30)
player.add_skill("Heal", 20)
player.update_health(-10)
player.update_mana(-5)
player.display_status()
