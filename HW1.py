from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase('Chinook_Sqlite.sqlite')
# db.print_tables(verbose=True)

# 1.1)
artist_name = db.execute('SELECT Name FROM Artist')
print(artist_name)

# 1.2)
db.pretty_print('Select Name FROM Artist')

# 2.1)
billing_germany = db.execute('''
    SELECT * 
    FROM Invoice 
    WHERE BillingCountry = "Germany"
    ''')
print(billing_germany)

# 2.2)
db.pretty_print('SELECT * FROM Invoice WHERE BillingCountry = "Germany"')

# 3)
album_number = db.execute('SELECT COUNT(*) FROM Album')
print(album_number[0][0])

# 4)
customers_france = db.execute('''
    SELECT COUNT(*) 
    FROM Customer 
    WHERE Country = "France"
    ''')
print(customers_france[0][0])
