import sqlite3

connection = sqlite3.connect("roster.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

roster_data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]
cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', roster_data)

cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')

cursor.execute('SELECT Name, Age FROM Roster WHERE Species = "Bajoran"')
bajorans = cursor.fetchall()
print("Bajoran Characters:")
for row in bajorans:
    print(row)

cursor.execute('DELETE FROM Roster WHERE Age > 100')

cursor.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')
rank_updates = [
    ('Captain', 'Benjamin Sisko'),
    ('Lieutenant', 'Ezri Dax'),
    ('Major', 'Kira Nerys')
]
for rank, name in rank_updates:
    cursor.execute(f'UPDATE Roster SET Rank = ? WHERE Name = ?', (rank, name))

cursor.execute('SELECT * FROM Roster ORDER BY Age DESC')
sorted_roster = cursor.fetchall()
print("Roster Sorted by Age: ")
for row in sorted_roster:
    print(row)

connection.commit()
connection.close()