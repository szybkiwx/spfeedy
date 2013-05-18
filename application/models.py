from application import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(), index = True, unique = True)
    password = db.Column(db.String(256), index = True)
    salt = db.Column(db.String(16))
       
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname) 
 
    def __repr__(self):
        return '<User %r>' % (self.username)


class Category(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), index = True, unique = True)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    #parent = db.relationship('Category', backref = db.backref('categories', lazy='dynamic'))
    parent = db.relationship('Category', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref = db.backref('categories', lazy='dynamic'))

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), index = True)
    url = db.Column(db.String(), index = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref = db.backref('subscriptions', lazy='dynamic'))


class Feed(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), index = True)
    link = db.Column(db.String(), index = True)
    description = db.Column(db.String(), index = True)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'))
    subscription = db.relationship('Subscription', backref = db.backref('feeds', lazy='dynamic'))
