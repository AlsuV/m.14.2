import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# ----
# Заполните её 10 записями:
# for i in range(11):
#     if i != 0:
#         cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"newuser{i}", f"ex@gmail.com{i}", f"{i}0", "1000"))

# ----
# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser2"))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser4"))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser6"))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser8"))
# cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "newuser10"))

# ----
# Удалите каждую 3ую запись в таблице начиная с 1ой:
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser1",))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser4",))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser7",))
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser10",))

# ----
# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
# cursor.execute("SELECT username, age FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(user)
#

# ----
# module_14_2
# 1. Удалите из базы данных not_telegram.db запись с id = 6.
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser6",))

# ----
# 2. Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
i = cursor.fetchone()[0]
# print(i) /// = 5

# ---
# 3.Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
j = cursor.fetchone()[0]
# print(j) /// = 4000

# ----
# Вывести в консоль средний баланс всех пользователя.
# cursor.execute("SELECT AVG(balance) FROM Users")
# avg_balance = cursor.fetchone()[0]
# print(avg_balance) # /// = 800

print(j/i)

connection.commit()
connection.close()