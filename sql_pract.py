import pymysql
import pymysql.cursors
from pprint import pprint as print

conn = pymysql.connect(
    database="world",
    user="nvasiuta",
    password="244805859",
    host='10.100.33.60',
    cursorclass=pymysql.cursors.DictCursor
)


cursor=conn.cursor()

cursor.execute("SELECT `Name`,`HeadOfState` FROM `country` ")

result = cursor.fetchall()

print(result[0]["HeadOfState"])


for x in result:
    print(x['HeadOfState'])








