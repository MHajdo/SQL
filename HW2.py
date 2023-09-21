from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase('Chinook_Sqlite.sqlite')

#db.pretty_print('''
#SELECT Artist.Name, Album.Title
#    FROM Artist
#    JOIN Album
#    ON Artist.ArtistId = Album.ArtistId
#    WHERE Artist.ArtistId = 8
#''')

#db.pretty_print('''
#SELECT Playlist.Name, PlaylistTrack.TrackId, Track.Name AS TrackName
#    FROM Playlist
#    JOIN PlaylistTrack
#    ON Playlist.PlaylistId = PlaylistTrack.PlaylistId
#    JOIN Track
#    ON PlaylistTrack.TrackId = Track.TrackId
#    WHERE Playlist.PlaylistId = 1
#''')

#db.pretty_print('''
#SELECT BillingCountry, SUM(TOTAL) FROM Invoice GROUP BY BillingCountry
#''')

# HOMEWORK 2.1

# 1.1 - MOST EXPENSIVE)
db.pretty_print('''
SELECT MAX(Invoice.Total), * FROM Invoice
''')

# 1.2 - CHEAPEST)
db.pretty_print('''
SELECT MIN(Invoice.Total), * FROM Invoice
''')

# 2 - WHICH CITY HAD MOST ORDERS)
db.pretty_print('''
SELECT Invoice.BillingCity, COUNT(*) AS Invoice_num
FROM Invoice
GROUP BY Invoice.BillingCity
ORDER BY Invoice_num DESC
''')

# 3 - HOW MANY TRACKS HAVE MEDIATYPE: Protected AAC audio file)
db.pretty_print('''
SELECT MediaType.Name, COUNT(*)
FROM Track
JOIN MediaType
ON Track.MediaTypeId = MediaType.MediaTypeId
WHERE MediaType.Name = "Protected AAC audio file"
''')

# 4 - WHAT ARTIST HAS THE MOST ALBUMS)
db.pretty_print('''
SELECT Artist.Name, COUNT(*) AS Albums
FROM Artist
JOIN Album
ON Album.ArtistId = Artist.ArtistId
GROUP BY Album.ArtistId
ORDER BY Albums DESC
''')

# 5 - WHAT GENRE HAS THE MOST TRACKS)
db.pretty_print('''
SELECT Genre.Name, COUNT(*) AS Track_num
FROM Genre
JOIN Track
ON Genre.GenreId = Track.GenreId
GROUP BY Track.GenreId
ORDER BY Track_num DESC
''')

# 6 - WHICH CUSTOMER SPENT THE MOST MONEY)
db.pretty_print('''
SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Money_spent
FROM Customer
JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Invoice.CustomerId
ORDER BY Money_spent DESC
Limit 1
''')

# 7 - WHAT SONGS WERE BOUGHT WITH EACH OTHER)
db.pretty_print('''
SELECT Track.Name, Invoice.InvoiceId
FROM Invoice
JOIN InvoiceLine
ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track
ON Track.TrackId = InvoiceLine.TrackId
''')