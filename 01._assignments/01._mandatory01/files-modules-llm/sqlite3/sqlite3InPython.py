import sqlite3
# Creating zoo db
con = sqlite3.connect("zoo.db")
cursor = con.cursor()

# Creating animal table for zoo DB
cursor.execute("CREATE TABLE IF NOT EXISTS animal (type VARCHAR(50), name VARCHAR(50), day_of_birth DATE)")

# Verify the new table has been created by querying the sqlite_master table built-in to SQLite
result = cursor.execute("SELECT name FROM sqlite_master")
print(result.fetchone())

# Inserting three animals for zoo db
cursor.execute("""
    INSERT INTO animal VALUES
        ('zebra', 'Allan', '2020-12-12'),
        ('duck', 'Donald', '2020-12-14'),
        ('alien', 'ET', '2020-1-1')
""")

# INSERT statement implicitly opens a transaction, 
# which needs to be committed before changes are saved in the database.
# Call con.commit() on the connection object to commit the transaction
con.commit()

#Reading from the zoo DB and printing animals
res = con.execute("SELECT * FROM animal")
print(res.fetchall())

