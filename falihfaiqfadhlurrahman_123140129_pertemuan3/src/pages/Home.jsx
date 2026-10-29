import { useState } from 'react';
import { useBooks } from '../context/BookContext';
import BookForm from '../components/BookForm';
import BookFilter from '../components/BookFilter';
import BookList from '../components/BookList';

export default function Home() {
  const { books, addBook } = useBooks();
  const [searchTerm, setSearchTerm] = useState('');
  const [filterStatus, setFilterStatus] = useState('all');

  const filteredBooks = books.filter(book => {
    const matchSearch = book.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
                        book.author.toLowerCase().includes(searchTerm.toLowerCase());
    const matchStatus = filterStatus === 'all' || book.status === filterStatus;
    return matchSearch && matchStatus;
  });

  return (
    <div style={{ padding: '20px' }}>
      <h2>Manajemen Buku Saya</h2>
      <BookForm onSubmit={addBook} />
      <hr style={{ margin: '20px 0' }} />
      <h3>Daftar Buku</h3>
      <BookFilter 
        searchTerm={searchTerm} setSearchTerm={setSearchTerm}
        filterStatus={filterStatus} setFilterStatus={setFilterStatus}
      />
      <br />
      <BookList books={filteredBooks} />
    </div>
  );
}