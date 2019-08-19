# import web
# urls = (
#     '/', 'index'
# )
# app = web.application(urls, globals())
# render = web.template.render('templates/')
# db = web.database(dbn='mysql', host='127.0.0.1', port=3308, db='test', user='root', pw='123')
# class index:
#     def GET(self):
#         email = db.select('tb_tmp1')
#         return render.index('价格')
# if __name__ == "__main__":
#     app.run()

import web
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())
class hello:
    def GET(self, name):
        if not name:
            name = 'World'
            return 'Hello, ' + name + '!'
if __name__ == "__main__":
    app.run()
