from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Database model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)


# Create the database and insert dummy data if the table is empty
with app.app_context():
    db.create_all()  # Create tables if not exist
    if Book.query.count() == 0:  # Only insert if table is empty
        dummy_books = [
            Book(title="1984", author="George Orwell"),
            Book(title="Brave New World", author="Aldous Huxley"),
            Book(title="The Catcher in the Rye", author="J.D. Salinger"),
        ]
        db.session.bulk_save_objects(dummy_books)
        db.session.commit()


# Get all books
@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify(
        [{"id": book.id, "title": book.title, "author": book.author} for book in books]
    )


# Get book by ID
@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get(id)
    if book:
        return jsonify({"id": book.id, "title": book.title, "author": book.author})
    else:
        return jsonify({"error": "Book not found"}), 404


# Create new book
@app.route("/books", methods=["POST"])
def create_book():
    data = request.json
    new_book = Book(title=data["title"], author=data["author"])
    db.session.add(new_book)
    db.session.commit()
    return (
        jsonify(
            {"id": new_book.id, "title": new_book.title, "author": new_book.author}
        ),
        201,
    )


# Update existing book
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = Book.query.get(id)
    if book:
        data = request.json
        book.title = data["title"]
        book.author = data["author"]
        db.session.commit()
        return jsonify({"id": book.id, "title": book.title, "author": book.author})
    else:
        return jsonify({"error": "Book not found"}), 404


# Delete book by ID
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": f"Book with ID {id} deleted"}), 200
    else:
        return jsonify({"error": f"Book with ID {id} not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
