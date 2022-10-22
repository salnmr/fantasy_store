import random

loot_table = {"bush": {'Bronze bar': {"quantity": 1, "price": 25}, 'Bread': {"quantity": 1, "price": 10}, 'lint': {"quantity": 10, "price": 1},'broken tool': {"quantity": 5, "price": 30}},
              "old_house": {'Pile of Silver bars': {"quantity": 3, "price": 50}, 'Wand of Kal\' Dread': {"quantity": 1, "price": 100}, 'Scroll of Protection': {"quantity": 1, "price": 150}},
              "smoking_cave": {'Pile of Gold bars': {"quantity": 10, "price": 100}, 'Orb of Driscul': {"quantity": 1, "price": 300}, 'Ye Olden\' Sword of Super Utter Calamity': {"quantity": 1, "price": 750}}}

print(loot_table)
a = random.choice(list(loot_table["bush"].items()))
print(a)
print("--------------------------------------------------------------------------------")
loot_table['bush'].pop(a)
