import MySQLdb


# 连接数据库
def connect_sql():

    conn = MySQLdb.connect(
        host = '127.0.0.1',
        user = 'root',
        passwd = '123',
        db = 'news',
        port = 3306,
        charset = 'utf8'
    )
    #获取数据
    cursor = conn.cursor()  #找到cursor
    cursor.execute('SELECT * FROM `news`ORDER by `id` DESC;')  #执行SQL
    rest = cursor.fetchall()  #拿到结果
    print(rest)
    conn.close()


class all_sql(object):
    def __init__(self):
        self.get_con()

    def get_con(self):
        try:
            self.conn = MySQLdb.connect(
            host='127.0.0.1',
            user='root',
            passwd='123',
            db='news',
            port=3306,
            charset='utf8'
            )
        except MySQLdb.Error as e:
            print(e)

    def close_con(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e :
            print(e)

    def get_one(self):
        # 准备sql
        sql = 'SELECT * FROM `news`ORDER by `id` DESC;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql)
        # 拿到结果
        rest = cursor.fetchall()
        print(rest)
        # 关闭cousor/连接
        cursor.close()
        self.conn.close()

    def add_one(self):
        try:
            sql =  (
               "INSERT INTO `news`(`img_url`) VALUE "
              " ('C:/Users\succful\Desktop\opencvStudy\bili_python操作数据库\news_imge');"
               )
            cursor = self.conn.cursor()
            cursor.execute(sql)
            #提交事务
            self.conn.commit()
            cursor.close()
            self.close_con()
        except:
            print('error')
            self.conn.commit()   #提交正确的
            self.conn.rollback()  #有一条错误就不能提交
def main():
    obj = all_sql()
    # obj.get_one()
    obj.add_one()

if __name__ == '__main__':
    main()






