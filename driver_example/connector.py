import logging

import psycopg2

DB_HOST = ''
DB_NAME = ''
DB_USERNAME = ''
DB_PASSWORD = ''
DB_PORT = ''

connection = None
try:
    connection = psycopg2.connect(host=DB_HOST,
                                  database=DB_NAME,
                                  user=DB_USERNAME,
                                  password=DB_PASSWORD,
                                  port=DB_PORT)

except (Exception, psycopg2.Error) as e:
    logging.error('Error Occurred during connection to Database: %s' % e)
# finally:
#     if connection:
#         connection.close()
#         logging.info('Connection Closed.')
