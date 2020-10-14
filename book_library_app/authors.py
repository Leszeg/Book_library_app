from book_library_app import app, db
from flask import jsonify, request
from book_library_app.models import Author, AuthorSchema, author_schema
from webargs.flaskparser import use_args


# dekorator route - informuje że funkcja ma zostać wywołana w momencie wejścia pod podanu adres url
# Dekorator app.route rejestruje daną funkcjonalność dla danej regóły URL
@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    author_schema = AuthorSchema(many=True)
    return jsonify({
        'success': True,
        'data': author_schema.dump(authors),
        'number_of_records': len(authors)
    })


@app.route('/api/v1/authors/<int:author_id>', methods=['GET'])
def get_author(author_id: int):
    author = Author.query.get_or_404(author_id, description=f"Author with id {author_id} not found")

    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    })


@app.route('/api/v1/authors', methods=['POST'])
@use_args(author_schema)
def create_author(args: dict):
    author = Author(**args)
    db.session.add(author)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    }), 201


@app.route('/api/v1/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Author with id {author_id} has been updated'
    })


@app.route('/api/v1/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Author with id {author_id} has been deleted'
    })
