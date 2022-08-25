from urllib import request
import pymysql
import settings
import requests

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
    region_12depth_code = "11" + str(i["region_2depth_code"])
    if len(region_12depth_code) == 5:
        region_12depth_code_list.append(region_12depth_code)
    
region_12depth_code_list = list(set(region_12depth_code_list))

for i in region_12depth_code_list:
    cursor.execute("select region_3depth_code from address_info where region_1depth_code = 11 and region_2depth_code = \"%s\";" % i[2:])
    tmp_list = cursor.fetchall()
    for three_dc in tmp_list:
        
        region_123depth_code = i + str(three_dc["region_3depth_code"])
        if len(region_123depth_code) == 8:
            region_123depth_code_list.append(region_123depth_code)

# print(len(region_123depth_code_list))

for code in region_12depth_code_list:
    info = requests.get("http://fullbang.kr:8080/product/%s/marketPrice?capacity=0&date=2022-08-15&parkingAvailability=false&placeType=MOTEL" % code).text[1:-1].split(",")
    info.append("address_code:" + code)
    print(info)
    print("")

for code in region_123depth_code_list:
    info = requests.get("http://fullbang.kr:8080/product/%s/marketPrice?capacity=0&date=2022-08-15&parkingAvailability=false&placeType=MOTEL" % code).text[1:-1].split(",")
    info.append("address_code:" + code)
    print(info)
    print("")
