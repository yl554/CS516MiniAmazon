from flask import current_app as app
from flask_login import current_user

from .product import Product


class Review:
    def __init__(self, display_name, pid, uid, rating, title, body):
        self.display_name = display_name
        self.pid = pid
        self.uid = uid
        self.rating = rating
        self.title = title
        self.body = body
    
    @staticmethod
    def get_reviews_with_pid(pid):
        rows = app.db.execute('''
        SELECT display_name, pid, uid, rating, title, body
        FROM Reviews 
        WHERE pid=:pid
        ''',
        pid=pid)
        return [Review(*row) for row in rows]
