# -*- coding: utf-8 -*-

import jsonapi_requests

api = jsonapi_requests.orm.OrmApi.config({
    'API_ROOT': 'http://api.geokrety.house.kumy.net/v1',
    'VALIDATE_SSL': False,
    'TIMEOUT': 3,
    'APPEND_SLASH': False,
})

# class Person(jsonapi_requests.orm.ApiModel):
#     class Meta:
#         type = 'person'
#         api = api
#
#     name = jsonapi_requests.orm.AttributeField('name')
#     married_to = jsonapi_requests.orm.RelationField('married-to')


class User(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'user'
        api = api
        path = 'users'

    name = jsonapi_requests.orm.AttributeField('name')
    language = jsonapi_requests.orm.AttributeField('language')
    country = jsonapi_requests.orm.AttributeField('country')
    join_datetime = jsonapi_requests.orm.AttributeField('join-datetime')
    email = jsonapi_requests.orm.AttributeField('email')
    latitude = jsonapi_requests.orm.AttributeField('latitude')
    Longitude = jsonapi_requests.orm.AttributeField('longitude')
    daily_mails = jsonapi_requests.orm.AttributeField('daily-mails')
    observation_radius = jsonapi_requests.orm.AttributeField('observation-radius')
    hour = jsonapi_requests.orm.AttributeField('hour')
    secid = jsonapi_requests.orm.AttributeField('secid')
    statpic_id = jsonapi_requests.orm.AttributeField('statpic-id')
    last_update_datetime = jsonapi_requests.orm.AttributeField('last-update-datetime')
    last_mail_datetime = jsonapi_requests.orm.AttributeField('last-mail-datetime')
    last_login_datetime = jsonapi_requests.orm.AttributeField('last-login-datetime')

    news = jsonapi_requests.orm.RelationField('news')
    news_comments = jsonapi_requests.orm.RelationField('news-comments')
    news_subscriptions = jsonapi_requests.orm.RelationField('news-subscriptions')
    geokrety_owned = jsonapi_requests.orm.RelationField('geokrety-owned')
    geokrety_held = jsonapi_requests.orm.RelationField('geokrety-held')
    moves = jsonapi_requests.orm.RelationField('moves')
    moves_comments = jsonapi_requests.orm.RelationField('moves-comments')


class Geokret(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'geokret'
        api = api
        path = 'geokrety'

    name = jsonapi_requests.orm.AttributeField('name')
    description = jsonapi_requests.orm.AttributeField('description')
    tracking_code = jsonapi_requests.orm.AttributeField('tracking-code')
    missing = jsonapi_requests.orm.AttributeField('missing')
    distance = jsonapi_requests.orm.AttributeField('distance')
    archived = jsonapi_requests.orm.AttributeField('archived')
    caches_count = jsonapi_requests.orm.AttributeField('caches-count')
    pictures_count = jsonapi_requests.orm.AttributeField('pictures-count')
    average_rating = jsonapi_requests.orm.AttributeField('average-rating')
    created_on_datetime = jsonapi_requests.orm.AttributeField('created-on-datetime')
    updated_on_datetime = jsonapi_requests.orm.AttributeField('updated-on-datetime')

    owner = jsonapi_requests.orm.RelationField('owner')
    holder = jsonapi_requests.orm.RelationField('holder')
    type_ = jsonapi_requests.orm.RelationField('type')
    moves = jsonapi_requests.orm.RelationField('moves')
    last_position = jsonapi_requests.orm.RelationField('last-position')
    last_move = jsonapi_requests.orm.RelationField('last-move')


class GeokretyType(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'geokrety-type'
        api = api
        path = 'geokrety-types'

    name = jsonapi_requests.orm.AttributeField('name')


class Move(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'move'
        api = api
        path = 'moves'

    comment = jsonapi_requests.orm.AttributeField('comment')
    username = jsonapi_requests.orm.AttributeField('username')
    moved_on_datetime = jsonapi_requests.orm.AttributeField('moved-on-datetime')
    application_name = jsonapi_requests.orm.AttributeField('application-name')
    application_version = jsonapi_requests.orm.AttributeField('application-version')
    pictures_count = jsonapi_requests.orm.AttributeField('pictures-count')
    comments_count = jsonapi_requests.orm.AttributeField('comments-count')
    created_on_datetime = jsonapi_requests.orm.AttributeField('created-on-datetime')
    updated_on_datetime = jsonapi_requests.orm.AttributeField('updated-on-datetime')

    waypoint = jsonapi_requests.orm.AttributeField('waypoint')
    latitude = jsonapi_requests.orm.AttributeField('latitude')
    longitude = jsonapi_requests.orm.AttributeField('longitude')
    altitude = jsonapi_requests.orm.AttributeField('altitude')
    country = jsonapi_requests.orm.AttributeField('country')
    distance = jsonapi_requests.orm.AttributeField('distance')

    author = jsonapi_requests.orm.RelationField('author')
    type_ = jsonapi_requests.orm.RelationField('type')
    geokret = jsonapi_requests.orm.RelationField('geokret')
    comments = jsonapi_requests.orm.RelationField('comments')


class MoveType(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'move-type'
        api = api
        path = 'moves-types'

    name = jsonapi_requests.orm.AttributeField('name')


class MoveComment(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'move-comment'
        api = api
        path = 'moves-comments'

    comment = jsonapi_requests.orm.AttributeField('comment')
    type_ = jsonapi_requests.orm.AttributeField('type')
    created_on_datetime = jsonapi_requests.orm.AttributeField('created-on-datetime')
    updated_on_datetime = jsonapi_requests.orm.AttributeField('updated-on-datetime')

    author = jsonapi_requests.orm.RelationField('author')
    move = jsonapi_requests.orm.RelationField('move')


class News(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'news'
        api = api
        path = 'news'

    title = jsonapi_requests.orm.AttributeField('title')
    content = jsonapi_requests.orm.AttributeField('content')
    username = jsonapi_requests.orm.AttributeField('username')
    comments_count = jsonapi_requests.orm.AttributeField('comments-count')
    created_on_datetime = jsonapi_requests.orm.AttributeField('created-on-datetime')
    last_comment_datetime = jsonapi_requests.orm.AttributeField('last-comment-datetime')

    author = jsonapi_requests.orm.RelationField('author')
    comments = jsonapi_requests.orm.RelationField('comments')
    subscriptions = jsonapi_requests.orm.RelationField('subscriptions')


class NewsComment(jsonapi_requests.orm.ApiModel):
    class Meta:
        type = 'news-comment'
        api = api
        path = 'news-comments'

    comment = jsonapi_requests.orm.AttributeField('comment')
    icon = jsonapi_requests.orm.AttributeField('icon')
    created_on_datetime = jsonapi_requests.orm.AttributeField('created-on-datetime')
    subscribe = jsonapi_requests.orm.AttributeField('subscribe')

    author = jsonapi_requests.orm.RelationField('author')
    news = jsonapi_requests.orm.RelationField('news')
