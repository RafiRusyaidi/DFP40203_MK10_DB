import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_mk10'
)


def print_hi():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT namapelajar FROM pelajar')
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0])

def main():
    mycursor = mydb.cursor()
    sql = "INSERT INTO pelajar (idpelajar, namapelajar) VALUES (%s, %s)"
    id = int(input("Enter your student ID : "))
    nama = (input("Enter your Name : "))
    val = (id, nama)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


if __name__ == '__main__':
    main()
