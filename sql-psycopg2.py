import psycopg2


# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the Artist table
# cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the Name column from the Artist table
# cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select only "Queen" from the Artist table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 - select only by artist_id #51 from the Artist table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# Query 5 - select only the albums with artist_id #51 from the Album table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# Query 6 - select all tracks where the composer is Queen from the Track table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch a single result
# results = cursor.fetchone()

#close the connection
connection.close()

# print results
for result in results:
    print(result)