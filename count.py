f = open('pokemon_list.txt', 'r')
charcnt = {}

# namelist = f.readlines()
namelist = [x.strip() for x in f.readlines()]
f.close()

# print(namelist)
# print(set("ゴニョニョ"))
# exit(1)
for name in namelist:
    if not len(name) == 5:
        continue
    splitname = list(name)
    print(splitname)
    for char in splitname:
        if char in charcnt:
            charcnt[char]+= 1
        else:
            charcnt[char] = 1
# print(charcnt)
# print(name)

pokemonscore = {}
for name in namelist:
    if not len(name) == 5:
        continue
    pokemonscore[name] = 0
    for char in set(name):
        pokemonscore[name] += charcnt[char]
# print(pokemonscore)
def func(x):
    return -x[1]
# for name, score in sorted(pokemonscore.items(),key=lambda x:-x[1]):
for name, score in sorted(pokemonscore.items(),key=func):
    print(name,score)
for char in "ジーランス":
    print(char,charcnt[char])
for char in "ソーナンス":
    print(char,charcnt[char])


# sorted([(ソーナンス, 1100000000),(ドククラゲ,3)])
