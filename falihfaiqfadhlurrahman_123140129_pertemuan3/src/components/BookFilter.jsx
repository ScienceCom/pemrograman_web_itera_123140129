import PropTypes from 'prop-types';

export default function BookFilter({ searchTerm, setSearchTerm, filterStatus, setFilterStatus }) {
  return (
    <div className="book-filter">
      <input 
        type="text" 
        placeholder="Cari judul atau penulis..." 
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <select value={filterStatus} onChange={(e) => setFilterStatus(e.target.value)}>
        <option value="all">Semua Status</option>
        <option value="beli">Ingin Dibeli</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="milik">Sudah Dimiliki</option>
      </select>
    </div>
  );
}

BookFilter.propTypes = {
  searchTerm: PropTypes.string.isRequired,
  setSearchTerm: PropTypes.func.isRequired,
  filterStatus: PropTypes.string.isRequired,
  setFilterStatus: PropTypes.func.isRequired
};