
# Flask Books API

This is a simple REST API built using Flask that performs CRUD operations on a book collection. The API supports listing, adding, updating, and deleting books stored in an SQLite database. The project also demonstrates how to Dockerize the Flask app.

## Features

- Retrieve all books
- Retrieve a book by ID
- Add a new book
- Update an existing book
- Delete a book by ID
- Dummy data is automatically added to the database if it's empty when the app is first started

## Requirements

- Python 3.x
- Flask
- SQLAlchemy
- Docker (optional for containerization)

## Routes

The following API routes are available:

1. **GET /books**  
   Retrieve a list of all books.
   
   Example:
   ```bash
   curl -X GET http://localhost:5000/books
   ```

2. **GET /books/{id}**  
   Retrieve details of a single book by its ID.
   
   Example:
   ```bash
   curl -X GET http://localhost:5000/books/1
   ```

3. **POST /books**  
   Add a new book to the collection. The body should contain the book title and author in JSON format.
   
   Example:
   ```bash
   curl -X POST http://localhost:5000/books         -H "Content-Type: application/json"         -d '{"title": "To Kill a Mockingbird", "author": "Harper Lee"}'
   ```

4. **PUT /books/{id}**  
   Update an existing book's details by its ID. The body should contain the updated title and author in JSON format.
   
   Example:
   ```bash
   curl -X PUT http://localhost:5000/books/1         -H "Content-Type: application/json"         -d '{"title": "Nineteen Eighty-Four", "author": "George Orwell"}'
   ```

5. **DELETE /books/{id}**  
   Delete a book from the collection by its ID.
   
   Example:
   ```bash
   curl -X DELETE http://localhost:5000/books/1
   ```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/flask-books-api.git
cd flask-books-api
```

### 2. Install Dependencies

Create a Python virtual environment and install the required Python packages:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**OR** manually install the required packages:

```bash
pip install flask flask-sqlalchemy
```

### 3. Run the Application

You can run the Flask app locally:

```bash
python app.py
```

The server will start at `http://localhost:5000/`.

### 4. Access the API

You can now access the API using `curl` or any API testing tool (like Postman). Try the following:

- Get all books: `curl -X GET http://localhost:5000/books`
- Add a book: `curl -X POST http://localhost:5000/books -H "Content-Type: application/json" -d '{"title": "Moby Dick", "author": "Herman Melville"}'`

## Docker Setup

You can run the application inside a Docker container if you prefer containerization.

### 1. Build the Docker Image

Make sure you are in the project directory, then build the Docker image:

```bash
docker buildx build --platform linux/arm64 -t flask-books-api --load .
```

### 2. Run the Docker Container

Run the container and expose the Flask app on port 5000:

```bash
docker run -p 5000:5000 flask-books-api
```

You can now access the API at `http://localhost:5000/`.

## Dummy Data

The app will automatically insert the following dummy books into the SQLite database if the database is empty:

1. *1984* by George Orwell
2. *Brave New World* by Aldous Huxley
3. *The Catcher in the Rye* by J.D. Salinger

## License

This project is open-source and available under the [MIT License](LICENSE).
