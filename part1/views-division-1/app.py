# У вас есть приложение с использованием REST X, 
# где все views находятся в одном файле. 
# 
# Необходимо сделать рефакторинг архитектуры приложения.
# Структура приложения должна быть следующего вида:
# 
# views-division-1
# ├── ./app.py   - Основной фаил, здесь инициализируется приложение
# ├── ./test.py  - Здесь наши тесты, запустите их как проверите приложение
# └── ./views
#     └── ./views/books.py - вынесите в этот файл class based views
#
# Требования к выполнению задания:
# - Создавайте необходимые файлы и папки в корне папки "views-division-1".
# - В файле app.py не должно быть лишних переменных
# - Приложение должно запускаться. 
# - Запрос на эндпоинт должен возвращать корректный код.
# - Название файла должно совпадать с названием неймспейса.
#
# Менять значения, возвращаемые view-функциями, 
# а также url-адреаса в данном задании не требуется.
# в данной задаче мы также опускаем логику работы с сущностями в БД.

from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
app.url_map.strict_slashes = False

api = Api(app)
book_ns = api.namespace('books')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        return [], 200

    def post(self):
        return "", 201


@book_ns.route('/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        return bid, 200


# Вы можете протестировать свое приложение самостоятельно.
# Проверьте получаете ли вы соответсвующие коды
# в ответах на запрос по адресу
#  GET http://localhost:10001/books/  - returns [] code 200
#  POST http://localhost:10001/books/ - returns "" code 201
#  GET http://localhost:10001/books/1 - returns bid (Int), code 200

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
