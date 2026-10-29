import { createContext, useContext } from 'react';
import PropTypes from 'prop-types';
import useLocalStorage from '../hooks/useLocalStorage';

const BookContext = createContext();

export const useBooks = () => useContext(BookContext);

export const BookProvider = ({ children }) => {
  const [books, setBooks] = useLocalStorage('my_books', []);

  const addBook = (book) => setBooks([...books, { ...book, id: Date.now() }]);
  const editBook = (id, updatedBook) => setBooks(books.map(b => b.id === id ? updatedBook : b));
  const deleteBook = (id) => setBooks(books.filter(b => b.id !== id));

  return (
    <BookContext.Provider value={{ books, addBook, editBook, deleteBook }}>
      {children}
    </BookContext.Provider>
  );
};

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
};