import PropTypes from 'prop-types';
import { useBooks } from '../context/BookContext';

export default function BookList({ books }) {
  const { deleteBook } = useBooks();

  if (books.length === 0) return <p>Tidak ada buku yang sesuai.</p>;

  return (
    <div className="book-list">
      {books.map(book => (
        <div key={book.id} className="book-card" style={{ border: '1px solid #ccc', padding: '10px', marginBottom: '10px' }}>
          <div>
            <h4>{book.title}</h4>
            <p>Oleh: {book.author}</p>
            <span className={`badge ${book.status}`}>Status: {book.status}</span>
          </div>
          <button style={{ marginTop: '10px', cursor: 'pointer' }} onClick={() => deleteBook(book.id)}>Hapus</button>
        </div>
      ))}
    </div>
  );
}

BookList.propTypes = {
  books: PropTypes.array.isRequired
};