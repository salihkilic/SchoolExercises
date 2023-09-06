# Things to do, chapter 16
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch16.html#idm45794973069144

import csv
import sqlite3
import redis
import sqlalchemy as sa
from sqlalchemy.orm import Session, DeclarativeBase


# 16.1 Save the following text lines to a file called books.csv (notice that if the fields are separated by commas,
# you need to surround a field with quotes if it contains a comma):
print("\n------ 16.1 ------")
print(f"Check Files/books.csv for contents")


# 16.2 Use the csv module and its DictReader method to read books.csv to the variable books. Print the values in
# books. Did DictReader handle the quotes and commas in the second book’s title?
print("\n------ 16.2 ------")
with open("Files/books.csv", 'rt') as reader:
    csv_data = csv.DictReader(reader)
    books = [row for row in csv_data]
    print("Books:")
    for x in books:
        print(x)


# 16.3 Create a CSV file called books2.csv by using these lines:
print("\n------ 16.3 ------")
print(f"Check Files/books2.csv for contents")


# 16.4 Use the sqlite3 module to create a SQLite database called books.db and a table called books with these fields:
# title (text), author (text), and year (integer).
print("\n------ 16.4 ------")
conn = sqlite3.connect("Files/books.db")
curs = conn.cursor()

# The book does not tell you this, but adding the IF NOT EXISTS makes sure you don't get an exception when you run
# this more than once.
curs.execute('''CREATE TABLE IF NOT EXISTS books
            (title TEXT PRIMARY KEY,
            author TEXT,
            year INT)''')
print("Database created. Check Files/books.db")


# 16.5 Read books2.csv and insert its data into the book table.
print("\n------ 16.5 ------")
with (open("Files/books2.csv", 'rt') as reader):
    csv_data = csv.DictReader(reader)
    books2 = [row for row in csv_data]

for book in books2:
    print(f"Adding {book['title']} to the DB")
    ins = 'INSERT OR IGNORE INTO books VALUES(?, ?, ?)'
    curs.execute(ins, ([book['title'], book['author'], book['year']]))
print("Books are added to NoSql DB, we check in the next exercise if it worked")

# Again, the book does not tell you this, but if you don't commit your changes, your entries will not actually be
# pushed to the database. You won't be able to do 16.8 otherwise.
conn.commit()


# 16.6 Select and print the title column from the book table in alphabetical order.
print("\n------ 16.6 ------")
curs.execute('''SELECT * FROM books ORDER BY title''')
rows = curs.fetchall()

print("The titles in alphabetical order: \n")
for item in rows:
    print(f"{item[0]}")


# 16.7 Select and print all columns from the book table in order of publication.
print("\n------ 16.7 ------")
curs.execute('''SELECT * FROM books ORDER BY year''')
rows = curs.fetchall()

print("The titles in order of publication: \n")
for item in rows:
    print(f"{item[2]}")

# Make sure to close the connection so SQLalchemy is able to connect when we're done with SQLite
curs.close()
conn.close()


# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. As
# in 16.6, select and print the title column from the book table in alphabetical order.
print("\n------ 16.8 ------")

# Create the session
engine = sa.create_engine('sqlite:///Files/books.db')
session = Session(engine)
print(f"We created the following session: {session}\n")


# Create a book object that reflects the book schema on the DB. To do this, we need to inherit from DeclarativeBase.
# I do not understand why, but we can't inherit directly from it, so we declare it ourselves.
class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'books'
    title = sa.Column(sa.Text, primary_key=True)
    author = sa.Column(sa.String)
    year = sa.Column(sa.Integer)

    def __repr__(self):
        return f"TEST {self.title} {self.author} {self.year}"


# Define what we want to select from DB
stmt = sa.select(Book).order_by(Book.title)
# Retrieve the books from the DB through our session
retrieved_books = session.scalars(stmt)
# Print out the book titles in the order we received them
for book in retrieved_books:
    print(book.title)


# 16.9 Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis
# hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.
print("\n------ 16.9 ------")

# Download redis server here: https://redis.io/download
# If you are on windows, check this link: https://redis.io/docs/getting-started/installation/install-redis-on-windows/
# Pip install Redis for python as well

conn = redis.Redis()
conn.hset("test", mapping={"count": "1", "name": "Fester Bestertester"})
print("Set the data on Redis")

redis_data = conn.hmget("test", ['count', 'name'])
print(f"Retrieved the following data from Redis: {redis_data}")


# 16.10 Increment the count field of test and print it.
print("\n------ 16.10 ------")
# We could easily set the count to two directly, but let's get the count, increment it and then send it back.
count = conn.hget("test", "count")
print(f"Current count: {count}")
inc_count = int(count) + 1
# Send the new incremented count back to redis
conn.hset("test", "count", str(inc_count))
# Check if we did what we set out to do
count = conn.hget("test", "count")
print(f"Count on redis ({count}) is incremented: {int(count) == inc_count}")
