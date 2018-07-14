# Author: Allen Anker
# Created by Allen Anker on 14/07/2018


from flask import jsonify, Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook


web = Blueprint('web', __name__)


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :q: search key word
    :page: how many results
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)


@web.route('/hello')
def hello():
    return 'Hello'