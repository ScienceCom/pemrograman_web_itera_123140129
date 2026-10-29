import { useBooks } from '../context/BookContext';
import useBookStats from '../hooks/useBookStats'; 
export default function Stats() {
  const { books } = useBooks();
  const stats = useBookStats(books);

  return (
    <div style={{ padding: '20px' }}>
      <h2>Statistik Perpustakaan Pribadi</h2>
      <ul>
        <li>Total Buku: <strong>{stats.total}</strong></li>
        <li>Sudah Dimiliki: <strong>{stats.milik}</strong></li>
        <li>Sedang Dibaca: <strong>{stats.baca}</strong></li>
        <li>Ingin Dibeli: <strong>{stats.beli}</strong></li>
      </ul>
    </div>
  );
}