import sqlite3
import random
import choice


db_p = sqlite3.connect('O:\SSSQL\db\players.db')
c = db_p.cursor()
# in_battle = 1
# c.execute("UPDATE players SET in_battle = '1' WHERE id = 2")

c.execute("SELECT MAX(id) FROM players")
res = (c.fetchone())

""""Преобразование списка кортежей в строку, убрали лишкие скобки, запятые и преобразовали в число"""
res = str(res)
symbols_to_remove = "(),"
for symbol in symbols_to_remove:
    res = res.replace(symbol, "")
res = int(res)
"""Рандомим ID игрока"""
result_random = random.choice(range(1,res))
print(result_random)

"""Игрок в бою?"""

print(f'{c.execute({"SELECT in_battle FROM players WHERE id ={result_random}})
result = (c.fetchall())
print(result)


db_p.commit()
db_p.close()
