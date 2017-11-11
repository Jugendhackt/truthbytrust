from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.atom import AtomFeed
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../development/test.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/recent.atom')
def recent_feed():
    feed = AtomFeed('Recent Articles',
                    feed_url=request.url, url=request.url_root)
    articles = Article.query.order_by(Article.updated.desc()).all()
    for article in articles:
        feed.add(str(article.title), str(article.content),
                 content_type='html',
                 author="noch nicht implementiert",
                 #url=make_external(article.url),
                 url="nochnichtimplementiert",
                 updated=article.updated,
                 published=article.published)
    return feed.get_response()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Unicode, nullable=False)
    title = db.Column(db.Unicode, nullable=False)
    summary = db.Column(db.Unicode, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    published = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.title
