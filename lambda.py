import json
import psycopg2

def lambda_handler(event, context):
    conn = psycopg2.connect(
        dbname='',
        host='',
        port='',
        user='',
        password=''
    )

    cur = conn.cursor()
    query = 'SELECT * FROM public.shoes'
    cur.execute(query)
    print(cur.fetchone())
    cur.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
