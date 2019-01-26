# -*- coding: utf-8 -*-

from flask import Flask, abort, render_template

import jsonapi_requests
from jsonapi_requests.request_factory import ApiInternalServerError

from .api import Geokret, Move, MoveComment, News, NewsComment, User

app = Flask(__name__)


@app.before_request
def before_request():
    # When you import jinja2 macros, they get cached which is annoying for local
    # development, so wipe the cache every request.
    if app.debug:
        app.jinja_env.cache = {}


@app.route("/users")
def users_collection():
    users = User.get_list()
    return render_template('users.html', users=users)


@app.route("/users/<user_id>")
def user(user_id):
    user = User.from_id(user_id)
    try:
        User.exists(user_id)
    except AssertionError:
        abort(404)
    return render_template('user.html', user=user)


@app.route("/geokrety")
def geokrety_collection():
    geokrety = Geokret.get_list()
    return render_template('geokrety.html', geokrety=geokrety)


@app.route("/geokrety/<geokret_id>")
def geokret(geokret_id):
    geokret = Geokret.from_id(geokret_id)
    try:
        Geokret.exists(geokret_id)
    except AssertionError:
        abort(404)
    return render_template('geokret.html', geokret=geokret)


@app.route("/moves")
def moves_collection():
    moves = Move.get_list()
    return render_template('moves.html', moves=moves)


@app.route("/moves/<move_id>")
def move(move_id):
    move = Move.from_id(move_id)
    try:
        Move.exists(move_id)
    except AssertionError:
        abort(404)
    return render_template('move.html', move=move)


@app.route("/news")
def news_collection():
    news = News.get_list()
    return render_template('newss.html', newss=news)


@app.route("/news/<news_id>")
def news(news_id):
    news = News.from_id(news_id)
    try:
        News.exists(news_id)
    except AssertionError:
        abort(404)
    return render_template('news.html', news=news)


@app.route("/news-comments")
def news_comments_collection():
    comments = NewsComment.get_list()
    return render_template('news-comments.html', comments=comments)


@app.route("/news-comments/<comment_id>")
def news_comment(comment_id):
    comment = NewsComment.from_id(comment_id)
    try:
        NewsComment.exists(comment_id)
    except AssertionError:
        abort(404)
    return render_template('news-comment.html', comment=comment)


@app.route("/moves-comments")
def moves_comments_collection():
    comments = MoveComment.get_list()
    return render_template('moves-comments.html', comments=comments)


@app.route("/moves-comments/<comment_id>")
def move_comment(comment_id):
    comment = MoveComment.from_id(comment_id)
    try:
        MoveComment.exists(comment_id)
    except AssertionError:
        abort(404)
    return render_template('move-comment.html', comment=comment)


if __name__ == "__main__":
    app.run()
