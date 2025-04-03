from flask import Flask, render_template
from models import Artist, Album, Song, Movie, Book, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///preferences.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/songs')
def songs():
    songs_list = Song.query.join(Album).join(Artist).all()
    return render_template('songs.html', songs=songs_list)


@app.route('/movies')
def movies():
    movies_list = Movie.query.order_by(Movie.year.desc()).all()
    return render_template('movies.html', movies=movies_list)


@app.route('/books')
def books():
    books_list = Book.query.order_by(Book.year).all()
    return render_template('books.html', books=books_list)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Добавляем данные только если таблицы пустые
        if not Artist.query.first():
            artist1 = Artist(name='YT')
            artist2 = Artist(name='Nas')
            db.session.add_all([artist1, artist2])

            album1 = Album(title='OI!', year='2025', artist=artist1)
            album2 = Album(title='Illmatic', year='1994', artist=artist2)
            db.session.add_all([album1, album2])

            song1 = Song(title='Girls Trip', length='2:16', track_number=1, album=album1)
            song2 = Song(title='Memory Lane', length='4:05', track_number=6, album=album2)
            db.session.add_all([song1, song2])

            movie1 = Movie(title='Большой куш', year='2000', director='Гай Ричи', genre='Криминал, Комедия, Боевик')
            movie2 = Movie(title='Карты, деньги, два ствола', year='1998', director='Гай Ричи',
                           genre='Боевик, Комедия, Криминал')
            db.session.add_all([movie1, movie2])

            book1 = Book(title='1984', author='George Orwell', year='1949', genre='Антиутопия')
            book2 = Book(title='Хоббит', author='J.R.R. Tolkien', year='1937', genre='Фэнтези')
            db.session.add_all([book1, book2])

            db.session.commit()

    app.run(debug=True)