from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase('hiking_trip.sqlite')

db.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id integer primary key autoincrement,
        name text, 
        age integer
        )
        ''')
# db.print_tables(verbose=True)

# db.execute('INSERT INTO user (name, age) VALUES ("Miki", 17)')


# user_names = db.execute('SELECT * FROM user')
# print(user_names)
# db.pretty_print('SELECT * from user WHERE id > 5')

#spremeni
# db.execute('UPDATE user SET age=43 WHERE id=5')
# db.pretty_print('SELECT * from user')

#izbriši
# db.execute('DELETE FROM user WHERE id=3')
# db.pretty_print('SELECT * from user')

#spremeni tabelo
# db.execute('ALTER TABLE user ADD email text')
# db.pretty_print('SELECT * from user')

#izbrisi tabelo
#db.execute('DROP TABLE user')