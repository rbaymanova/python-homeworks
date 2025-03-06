import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
''')

books_data = [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
]
cursor.executemany('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)', books_data)

cursor.execute('''
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
''')

cursor.execute('SELECT Title, Author FROM Books WHERE Genre = "Dystopian"')
dystopian_books = cursor.fetchall()
print("Dystopian Books:")
for row in dystopian_books:
    print(row)

cursor.execute('DELETE FROM Books WHERE Year_Published < 1950')

cursor.execute('ALTER TABLE Books ADD COLUMN Rating REAL')
rating_updates = [
    (4.8, 'To Kill a Mockingbird'),
    (4.7, '1984'),
    (4.5, 'The Great Gatsby')
]
for rating, title in rating_updates:
    cursor.execute(f'UPDATE Books SET Rating = ? WHERE Title = ?', (rating, title))

cursor.execute('SELECT * FROM Books ORDER BY Year_Published ASC')
sorted_books = cursor.fetchall()
print("Books Sorted by Year_Published: ")
for row in sorted_books:
    print(row)

conn.commit()
conn.close()