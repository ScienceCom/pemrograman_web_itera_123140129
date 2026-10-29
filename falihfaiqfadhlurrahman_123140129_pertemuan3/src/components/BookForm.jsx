import { useState } from 'react';
import PropTypes from 'prop-types';

export default function BookForm({ onSubmit, initialData }) {
  const [formData, setFormData] = useState(initialData || { title: '', author: '', status: 'beli' });
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.title.trim() || !formData.author.trim()) {
      setError('Judul dan Penulis wajib diisi!');
      return;
    }
    setError('');
    onSubmit(formData);
    if (!initialData) setFormData({ title: '', author: '', status: 'beli' }); // Reset if adding new
  };

  return (
    <form className="book-form" onSubmit={handleSubmit} data-testid="book-form">
      <h3>{initialData ? 'Edit Buku' : 'Tambah Buku Baru'}</h3>
      {error && <div className="error-msg" data-testid="error-msg">{error}</div>}
      
      <input 
        type="text" 
        placeholder="Judul Buku" 
        value={formData.title} 
        onChange={(e) => setFormData({...formData, title: e.target.value})} 
      />
      <input 
        type="text" 
        placeholder="Nama Penulis" 
        value={formData.author} 
        onChange={(e) => setFormData({...formData, author: e.target.value})} 
      />
      <select 
        value={formData.status} 
        onChange={(e) => setFormData({...formData, status: e.target.value})}>
        <option value="beli">Ingin Dibeli</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="milik">Sudah Dimiliki</option>
      </select>
      
      <button type="submit">{initialData ? 'Simpan Perubahan' : 'Tambah Buku'}</button>
    </form>
  );
}

BookForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  initialData: PropTypes.object
};