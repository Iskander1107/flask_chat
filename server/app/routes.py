# -*- coding: utf-8 -*- 
from app import app
import flask

coins = 0
""
@app.route('/index')
def index():
    return flask.render_template('index.html', coins=coins)


@app.route('/add', methods=['POST', 'GET'])
def add_coin():
    global coins
    coins += 1
    return flask.redirect('/index')


@app.route('/get_coins_number')
def get_coins_number():
    return str(coins)