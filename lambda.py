import json
import psycopg2

#dbname:defined when create workgroup
#host:in workgroup general information
#port:default
#user:defined when create workgroup
#password:defined when create workgroup


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
