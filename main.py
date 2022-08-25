import pymysql
import settings

db = pymysql.connect(host=settings.DB_HOST,
                    user=settings.DB_USER_NAME,
                    password=settings.DB_PASSWORD,
                    database=settings.DB_DATABASE_NAME,
                    port=settings.DB_PORT,
                    charset='utf8mb4')

cursor = db.cursor(pymysql.cursors.DictCursor)

cursor.execute("select region_2depth_code from address_info where region_1depth_code = 11;")
cursor.fetchall()