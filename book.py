import flask
import flask_sqlalchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/new-books-collection.db'  # absolute file path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'  # relative file path
db = flask_sqlalchemy.SQLAlchemy(app)


class Book(db.Model):
    """
    A class to represent the details of he review of a book previously read.
    """

    # class attributes
    # ...

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(250), unique=True, nullable=False)
    author = db.Column(db.VARCHAR(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % \
               str(self.id) + ': ' + self.title + ':' \
               + self.author + ':' + str(self.rating)


db.create_all()
