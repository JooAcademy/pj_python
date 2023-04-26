FOODS = [(0, 13), (14, 16), (8, 7), (12, 4), (2, 1), (6, 14), (9, 10), (13, 18), (3, 19), (13,5)]
pos = (14, 16)
print(FOODS)


def add_food():
    if pos in FOODS:
        continue
    FOODS.append(pos)

i = FOODS.index(pos)
del FOODS[i]
add_food()

       
print(i)
print(FOODS)
