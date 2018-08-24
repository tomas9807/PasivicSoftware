day = '30'
month = '5'
offset = -1 if day=='15' else 0
quin = int(month * 2) + int(offset)
print(day,month,quin)