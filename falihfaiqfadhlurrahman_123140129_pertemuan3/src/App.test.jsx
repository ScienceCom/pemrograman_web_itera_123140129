import { render, screen, fireEvent, renderHook } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';

// Import komponen menggunakan struktur folder yang diratakan (flattened)
import BookForm from './components/BookForm';
import BookFilter from './components/BookFilter';
import useBookStats from './hooks/useBookStats';

describe('Aplikasi Manajemen Buku Pribadi', () => {
  
  // Test 1: Render BookForm dengan benar
  it('1. Render form input dengan benar', () => {
    render(<BookForm onSubmit={vi.fn()} />);
    expect(screen.getByPlaceholderText(/Judul Buku/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Nama Penulis/i)).toBeInTheDocument();
  });

  // Test 2: Validasi input kosong (Error Handling)
  it('2. Menampilkan pesan error jika disubmit kosong', () => {
    render(<BookForm onSubmit={vi.fn()} />);
    
    const submitButton = screen.getByRole('button', { name: /Tambah Buku/i });
    fireEvent.click(submitButton);
    
    expect(screen.getByTestId('error-msg')).toBeInTheDocument();
    expect(screen.getByText(/wajib diisi/i)).toBeInTheDocument();
  });

  // Test 3: Fungsi onSubmit dipanggil jika data valid
  it('3. Memanggil onSubmit dengan data valid', () => {
    const mockSubmit = vi.fn();
    render(<BookForm onSubmit={mockSubmit} />);
    
    const titleInput = screen.getByPlaceholderText(/Judul Buku/i);
    const authorInput = screen.getByPlaceholderText(/Nama Penulis/i);
    const submitButton = screen.getByRole('button', { name: /Tambah Buku/i });

    fireEvent.change(titleInput, { target: { value: 'Pemrograman React' } });
    fireEvent.change(authorInput, { target: { value: 'Falih' } });
    fireEvent.click(submitButton);
    
    expect(mockSubmit).toHaveBeenCalledTimes(1);
    expect(mockSubmit).toHaveBeenCalledWith(expect.objectContaining({ 
      title: 'Pemrograman React', 
      author: 'Falih' 
    }));
  });

  // Test 4: Komponen Filter merender input & select dengan benar
  it('4. Render BookFilter dan opsinya', () => {
    render(
      <BookFilter 
        searchTerm="" 
        setSearchTerm={vi.fn()} 
        filterStatus="all" 
        setFilterStatus={vi.fn()} 
      />
    );
    expect(screen.getByPlaceholderText(/Cari judul atau penulis/i)).toBeInTheDocument();
    expect(screen.getByRole('combobox')).toBeInTheDocument();
  });

  // Test 5: Custom Hook perhitungan statistik berjalan benar
  it('5. Custom Hook useBookStats menghitung statistik dengan benar', () => {
    const mockBooks = [
      { id: 1, status: 'milik' },
      { id: 2, status: 'baca' },
      { id: 3, status: 'milik' },
      { id: 4, status: 'beli' },
    ];
    
    const { result } = renderHook(() => useBookStats(mockBooks));
    
    expect(result.current.total).toBe(4);
    expect(result.current.milik).toBe(2);
    expect(result.current.baca).toBe(1);
    expect(result.current.beli).toBe(1);
  });
});