import sqlite3
import numpy
import struct
import os
#global var
#数据库文件绝句路径
DB_FILE_PATH = '/home/gubo/WorkSPace/WorkSpace/maskdetect/dataBaseFace/FaceDatabase.db'
#表名称
TABLE_NAME = ''
#是否打印sql
SHOW_SQL = True
def close_all(conn, cu):
    '''关闭数据库游标对象和数据库连接对象'''
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()
def get_conn(path):
    '''获取到数据库的连接对象，参数为数据库文件的绝对路径
    如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
    路径下的数据库文件的连接对象；否则，返回内存中的数据接
    连接对象'''
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print('硬盘上面:[{}]'.format(path))
        return conn
    else:
        conn = None
        print('内存上面:[:memory:]')
        return sqlite3.connect(':memory:')

def get_cursor(conn):
    '''该方法是获取数据库的游标对象，参数为数据库的连接对象
    如果数据库的连接对象不为None，则返回数据库连接对象所创
    建的游标对象；否则返回一个游标对象，该对象是内存中数据
    库连接对象所创建的游标对象'''
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()

def update(conn, sql):
    '''更新数据'''
    if sql is not None and sql != '':
        # if data is not None:
        cu = get_cursor(conn)
        #     for d in data:
        #         if SHOW_SQL:
        #             print('执行sql:[{}],参数:[{}]'.format(sql, d))
        cu.execute(sql)
        conn.commit()
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))
conn = sqlite3.connect('/home/gubo/WorkSPace/WorkSpace/maskdetect/dataBaseFace/FaceDatabase.db')
cur = conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)"
cur.execute(sql)
cur.execute("select name from sqlite_master where type='table' order by name")
# cur.execute("select *")

print(cur.fetchall())
#
# cur.execute("select id from t_FacialFeature")
# print (cur.fetchall())
# cur.execute("PRAGMA table_info(t_FacialFeature)")
# print (cur.fetchall())
#
# def GetTables(db_file = 'FaceDatabase.db'):
#     try:
#         conn = sqlite3.connect(db_file)
#         cur = conn.cursor()
#         cur.execute("select name from sqlite_master where type='table'")
#         print (cur.fetchall())
#     except sqlite3.Error as e:
#             print (e)
# GetTables()
cur.execute("select id from t_FacialFeature ")

abc = cur.fetchall()
des = cur.description
# print("表头:", ",".join([item[0] for item in des]))
# print(abc)
cur.execute("select feature from t_FacialFeature where id = 8")

features = cur.fetchall()[0]
for feature in features:
    # feature = 'data_a' + str(feature)
    # feature = open(feature, 'rb')
    # print(len(feature))
    feature = struct.unpack('f'*256, feature)
    print(feature)

# data_raw = struct.unpack('%df' % 256, feature)
# print(data_raw)

    #
    # import base64
    # f = open('/home/gubo/WorkSPace/WorkSpace/maskdetect/fp32.bin', 'rb')
    # # print(f)
    # base = '3xEUPJevij1QD+e9nsnuvJnXGz5dFz08+4srPnXU3r1aKow8nJkDPttXB75CMw++4jtuveCuUrqTEqq9EsihvYFcDLlYY5M9gT19PZuJq71+8wq9c16XvERIBL6eSOk70IsUvUGKjj2ougg9w1dcvH2JRb3Wyqa8bkZtPWHytryXrx2919miO0JXo70wC989XbpWvVoBjr0YGVo7hJGdPT2KUL0O1is9HjURPVbfG71G6Cq+aLjHPD9rg7zi34y7shRivXGqgDzC85K9RcGLPa4GFz3HjJG9zr2eOkN+Mb0HzYU9yok3PNLznD1cnqG98HLUPDOb0rwTeQa9Mie4vcpSsLxMr6A8jJM9PbIms7zlHkw9Ej9DPFSbZr1Y8OM8IVmQPHPmV7ylJAO+Xrw+vYqg/7sjjTm9j4sOPA/0kLy0gOs9ltR9Pfk7Ab00pTi8uD5bvS3gnD1i7xw9pgKxOmeuSL0DOi68/is/O6VpPb3Mfhw8Na0fveWamL1901+9hr5jvM1lzT3/MYU9nZJYPWf9Qzv0BI69kEZnOg5gND0qMNa9gTKROsDGID0LVYc94zqHPf6qlLtd7yc9ginjvdlTlz2clwC9cJjvvQmAzrxZu1c9kHU0PZi5xT3qiH69f3jNu1pRM72EwDG8msGRPWgdQL1PDLM9Jv8zvd4BrbyvK7Q8PxCNvTuHjr04Jca9LM3avOg/OD3Zago9xjRNvONFc70hoze+j4WWPV2LJr2d7HU9bp7VPdp0jr2QbTg9qx17PZN66j1ajXc8K/CUvXIdNr1JBDQ9eNZyPf4zBTtFy5s9mPpYvbwdSTxOwcQ8ILocPU1zzD11Tek9dr+UvIt/hb2X3ha9IZSPvS399Lwxoww9dBaFPZU8ETwqmCO9Ggcevf7E6z1/64g9N9dYvVRZYbxwmme9wKmyPbVZLb2Dp/K9pf+IPd0+5z2TKBy99kKLPWQ8Xr3yxq29GXNyvSanPj3h7DQ9f7FjPHMMnzzyT8S8xSEeveWAwrzH+nu9x2bTPCc3Lr1pMD6+GY4ivHDjGj2j2GA8IOejvXfNfj0+kIc9/66Fuws/d7x+YXQ9MzADvSYdRD2ufAy9dgtLvRt8FT7GjsK8Ss8rPSsiBb2F3WI9DSoUPbMh/j11VAs+giATPJ7dfz39Zaa9D1t1u7Y6hzstLlA9gb4bvchgRL1lmm+9TbNFvbZnl7wqvLM9bY1FPSieBL1/7I69zVsHveHsBL1Dm109jSimvOOnzbyFy4M8G3mdvXeKuzzJ8ca9ixtQPZaXgbzxFIW9mEPuuTsAqjwHrQe9kgTlvTIslb31cuq7JO69u0zKFT063IG7IrLvu2UmEDzFftU8prWnvQ=='
    # feature = base64.b64decode(base)
    # print(len(feature))
    # # print(feature)
    # print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
    # # data_raw = struct.unpack('%df' % 256, f.read(4*256))
    # data_raw = struct.unpack('%df' % 256, feature)
    # fp2 = []
    # for fp123 in data_raw:
    #     fp2.append(fp123)
    # # data_raw.tofile("fp32.bin")
    # fp2 = numpy.mat(fp2)
    # fp2.astype(numpy.float32).tofile("fp3.bin")
    # print(data_raw)
    # f.close()
    # bytes = struct.pack( ('%df' % len(data_raw)), *data_raw)
    # # print(bytes)
    # print('===================================================')
# data_raw = struct.unpack('%df' % 256, bytes)
# # print(data_raw)
# fp2 = []
# for fp123 in data_raw:
#     fp2.append(fp123)
# # data_raw.tofile("fp32.bin")
# fp2 = numpy.mat(fp2)
# fp2.astype(numpy.float32).tofile("fp2.bin")
def update_test():
    '''更新数据...'''
    print('更新数据...')
    data = bytes
    md5 = 'ee5e380951bca85170af3b1ab5984a27'
    update_sql = "UPDATE t_FacialFeature SET feature = x'%s' WHERE ID = 1 ;" % (data.hex())
    update_sql1 = "UPDATE t_FacialFeature SET md5 = '%s' WHERE ID = 1 ;" % md5

    conn = get_conn(DB_FILE_PATH)
    update(conn, update_sql)
    conn = get_conn(DB_FILE_PATH)
    update(conn, update_sql1)
# update_test()