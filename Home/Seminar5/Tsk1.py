# 1) Сделать игру морской бой
field_of_battle=[]
for i in range(4):
    for j in range(4):
        field_of_battle.append('0')
for i in range(len(field_of_battle)):
    for j in range(len(field_of_battle[j])):
        print(field_of_battle[i][j],end=' ')
print()
