import sqlite3

def create_table_passwords():
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS passwords(password text, website text, weak text, note text)")
    connect.commit()
    connect.close()


def insert_values(password, website, weak, note):
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO passwords VALUES(?, ?, ?, ?)", (password, website, weak, note))
    connect.commit()
    connect.close()

def show_all_values():
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM passwords")
    passwords = [{"password": row[0], "website":  row[1], "weak": row[2], "note": row[3]} for row in cursor.fetchall()]
    connect.close()
    return passwords

def delete_value(password, website, weak, note):
    connect  = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM passwords WHERE password=? AND website=? AND weak=? AND note=?", (password, website, weak, note))
    connect.commit()
    connect.close()

def update_value(password, website, weak, note, password2, website2, weak2, note2):
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE passwords SET password=?, website=?, weak=?, note=? WHERE password=? AND website=? AND weak=? AND note=?",
                   (password,website,weak,note,password2,website2,weak2,note2))
    connect.commit()
    connect.close()


def search_value(password=False, website=False, weak=False, note=False):
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()

    if password:
        cursor.execute("SELECT * FROM passwords WHERE password=?", (password,))
    elif website:
        cursor.execute("SELECT * FROM passwords WHERE website=?", (website,))
    elif weak:
        cursor.execute("SELECT * FROM passwords WHERE weak=?", (weak,))
    elif note:
        cursor.execute("SELECT * FROM passwords WHERE note=?", (note,))

    passwords = [{"password": row[0], "website": row[1], "weak": row[2], "note": row[3]} for row in cursor.fetchall()]
    connect.close()
    return passwords



