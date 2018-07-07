from flask import Blueprint, jsonify

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    print(page)
    return jsonify({})


@simple_page.route('/')
def next():
    return jsonify({})
