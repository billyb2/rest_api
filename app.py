from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

db.create_all()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.name} - {self.description}"

def book_to_object(book):
    return {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}


@app.route("/")
def index():
    return "Hello"

@app.route("/books")
def get_books():
    books = Book.query.all()

    output = list(map(book_to_object, books))
    return {"books": output}

@app.route("/books/id")
def get_book(id):
    return book_to_object(book)

@app.route("/books", methods=["POST"])
def add_book():
    book = Book(book_name = request.json["book_name"], author = request.json["author"], publisher = request.json["publisher"])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id}

@app.route("/books", methods=["DELETE"])
def add_book():
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}

    db.session.delete(book)
    db.sesion.commit()

    return {"message": "yay"}
