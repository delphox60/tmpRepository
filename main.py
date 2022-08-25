import pymysql
import settings

region_12depth_code_list = []
region_123depth_code_list = []

db = pymysql.connect(host=settings.DB_HOST,
                    user=settings.DB_USER_NAME,
                    password=settings.DB_PASSWORD,
                    database=settings.DB_DATABASE_NAME,
                    port=settings.DB_PORT,
                    charset='utf8mb4')

cursor = db.cursor(pymysql.cursors.DictCursor)

cursor.execute("select region_2depth_code from address_info where region_1depth_code = 11;")

region_2depth_code_list = cursor.fetchall()
for i in region_2depth_code_list:
    
    if (i["region_2depth_code"] == None):
        break
    
    region_12depth_code_list.append("11" + str(i["region_2depth_code"]))
    


