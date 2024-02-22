import psycopg2
import pandas


if __name__ == '__main__':
    # Connect to your postgres DB

    # substitute with your own data
    conn = psycopg2.connect("dbname=DB_NAME user=YOUR_NAME password=YOUR_PASS host=localhost")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute('SELECT * From "YOUR_TABLE_NAME"')

    records = cur.fetchall()
    print(records)
    data = pandas.DataFrame(records)
    print(data)
