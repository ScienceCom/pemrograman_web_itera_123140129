import { useMemo } from 'react';

export default function useBookStats(books) {
  return useMemo(() => {
    return {
      total: books.length,
      milik: books.filter(b => b.status === 'milik').length,
      baca: books.filter(b => b.status === 'baca').length,
      beli: books.filter(b => b.status === 'beli').length
    };
  }, [books]);
}