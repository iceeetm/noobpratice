class Card:
    def __init__(self, name, kind, cost, hp, attack, defense, intro):
        self.name = name
        self.kind = kind
        self.cost = cost
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.intro = intro

    def __str__(self):
        return f"{self.name}: kind:{self.kind}, cost:{self.cost}, hp:{self.hp}, attack:{self.attack}, defense:{self.defense}, {self.intro}"


cards_info = [
    ("goblin", 'mst', 2, 3, 2, 1, '小型的類人生物。'),
    ("fairy", 'mst', 3, 4, 3, 3, '巴掌大的小妖精背後有翅膀。'),
    ("fireball", 'mag', 3, 0, 3, 0, '初級火球魔法直接攻擊敵人。'),
    ("highheal", 'mag', 8, 6, 0, 2, '高級治癒術回復友軍血量。'),
    ("sword", 'equ', 5, 1, 4, 1, '一般制式長劍。'),
    ("shield", 'equ', 4, 1, 1, 4, '一般制式盾。')
]

cards=[]

for card_info in cards_info:
    card = Card(*card_info)
    cards.append(card)

def display_cards_by_kind(cards, kind):
    found_cards = []
    for card in cards:
        if card.kind == kind:
            found_cards.append(card)
    return found_cards
    

found_cards = display_cards_by_kind(cards, 'mst')

for card in found_cards:
    print(card)