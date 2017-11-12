from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.atom import AtomFeed
from flask import request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import datetime
from flask import make_response
import gnupg

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../development/test.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/articles', methods=['PUT'])
def addArticle():
    form = AddArticleForm(request.form)
    if form.validate():
        article = Article(content=form.content.data, summary=form.summary.data, title=form.title.data, updated=datetime.datetime.now(), published=datetime.datetime.now())
        if article.verify():
            db.session.add(article)
            db.session.commit()
            return make_response('Added article successfully', 201)
        else:
            return make_response('Signature not found or incorrect (currently only on pgp.mit.edu)', 400)
    else:
        return make_response('Missing arguments or invalid length', 400)

@app.route('/recent.atom')
def recent_feed():
    feed = AtomFeed('Recent Articles',
                    feed_url=request.url, url=request.url_root)
    articles = Article.query.order_by(Article.updated.desc()).all()
    for article in articles:
        feed.add(str(article.title), str(article.content),
                 content_type='html',
                 author=str(article.username),
                 #url=make_external(article.url),
                 url=article.id,
                 summary=article.summary,
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
    username = db.Column(db.Unicode)

    def verify(self):
        gpg = gnupg.GPG(gnupghome='/tmp')
        gpg.encoding = 'utf-8'
        verified = gpg.verify(self.content)
        #import pdb;pdb.set_trace()
        keyid = verified.key_id
        import_result = gpg.recv_keys('http://pgp.mit.edu', keyid)
        verified = gpg.verify(self.content)
        valid = verified.valid
        self.username = verified.username
        return valid

    def __repr__(self):
        return '<Article %r>' % self.title

class AddArticleForm(Form):
    content = StringField('content', [validators.DataRequired()])
    title = StringField('title', [validators.DataRequired()])
    summary = StringField('summary', [validators.DataRequired()])
