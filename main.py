from flask import render_template, request, redirect, url_for
import book


@book.app.route('/')
def home():
    print(request)
    print(request.args)
    print(request.args.get)
    print(request.args.get('some name attribute'))
    all_books = book.db.session.query(book.Book).all()
    return render_template(template_name_or_list='./index.html', all_books=all_books)


@book.app.route("/add", methods=['GET', 'POST', ])
def add():
    if request.method == 'POST':
        new_book_instance = book.Book(
            # id=1,
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating'],
        )
        book.db.session.add(new_book_instance)
        book.db.session.commit()
        return redirect(location='/add')
    return render_template(template_name_or_list='./add.html')


@book.app.route('/edit', methods=['GET', 'POST', ])
def edit():
    if request.method == 'POST':
        book_to_update_id = request.form['the-book-id']
        book_to_update = book.Book.query.get(book_to_update_id)
        book_to_update.rating = request.form['rating']
        book.db.session.commit()
        return redirect(url_for('home'))
    book_to_display_id = request.args.get('book_id')
    book_to_display = book.Book.query.get(book_to_display_id)
    return render_template('./rating.html', book=book_to_display)


@book.app.route('/delete')
def delete():
    book_to_delete_id = request.args.get('book_id')
    book_to_delete = book.Book.query.get(book_to_delete_id)
    book.db.session.delete(book_to_delete)
    book.db.session.commit()
    return redirect(url_for(endpoint='home'))


if __name__ == "__main__":
    # app.run(debug=True)
    book.app.run(debug=True)
