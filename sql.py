import sqlite3

# def add_question(question):

# conn = sqlite3.connect('API.db')

# c= conn.cursor()
# c.execute("""CREATE TABLE question(number int primary key, content text)""")
# c.execute("""CREATE TABLE choice(number int  references question(number), Optionkey varchar, Optioncontent varchar)""")
# c.execute("""CREATE TABLE answer(number int  references question(number), answer varchar)""")
# # c.execute("""INSERT INTO question(number, Content) VALUES ("1", "Hi") """)
# conn.commit()
# conn.close()

def add_question(question):
    conn = sqlite3.connect("API.db")
    c= conn.cursor()
    sql1 = """ INSERT OR REPLACE INTO question (number,Content) VALUES (?, ?) """
    c.execute(sql1, ( int(question["Number"]),str(question["Content"]) ))
    print("Add success")
    conn.commit()

    data = question["Options"]
    sql2 =""" INSERT INTO choice (number,Optionkey,Optioncontent) VALUES (?, ?, ?) """
    for i in range(len(data)):
        c.execute(sql2, (int(question["Number"]), str(data[i]["OptionKey"]), str(data[i]["OptionContent"])))
        print("Add success")
        conn.commit()
    conn.close()


def answer():
    sql= """ SELECT * FROM answer"""
    conn = sqlite3.connect("API.db")
    data = conn.execute(sql).fetchall()
    conn.close()
    return data