// Deklarasi Variabel & State Keranjang
let cart = JSON.parse(localStorage.getItem('miniPosCart')) || [];

// === 1. MANIPULASI DOM & RENDER ===
const cartBody = document.getElementById('cart-body');
const totalBelanjaEl = document.getElementById('total-belanja');
const diskonEl = document.getElementById('diskon');
const totalAkhirEl = document.getElementById('total-akhir');
const formBarang = document.getElementById('form-barang');

// Fungsi Format Rupiah
const formatRupiah = (angka) => {
    return 'Rp ' + angka.toLocaleString('id-ID');
};

// Fungsi Render Keranjang
function renderCart() {
    cartBody.innerHTML = '';
    
    // Transformasi Data (Map)
    cart.forEach((item, index) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${index + 1}</td>
            <td>${item.nama}</td>
            <td>${formatRupiah(item.harga)}</td>
            <td>${item.qty}</td>
            <td>${formatRupiah(item.subtotal)}</td>
            <td><button class="btn-danger-sm" onclick="hapusItem(${index})">Hapus</button></td>
        `;
        cartBody.appendChild(tr);
    });

    kalkulasiTotal();
    simpanKeLocalStorage();
}

// === 2. KALKULATOR OTOMATIS & ARRAY REDUCE ===
function kalkulasiTotal() {
    // Menggunakan Reduce untuk menjumlahkan subtotal
    const totalBelanja = cart.reduce((total, item) => total + item.subtotal, 0);
    
    // Logika Diskon: > Rp 50.000 dapat diskon 10%
    let diskon = 0;
    if (totalBelanja >= 50000) {
        diskon = totalBelanja * 0.10;
    }
    
    const totalAkhir = totalBelanja - diskon;

    // Update antarmuka
    totalBelanjaEl.textContent = formatRupiah(totalBelanja);
    diskonEl.textContent = formatRupiah(diskon);
    totalAkhirEl.textContent = formatRupiah(totalAkhir);

    // Menyimpan total akhir sementara untuk fitur pembayaran
    totalAkhirEl.dataset.value = totalAkhir; 
}

// === 3. VALIDASI INPUT FORM ===
formBarang.addEventListener('submit', function(e) {
    e.preventDefault(); // Mencegah reload halaman
    
    const namaInput = document.getElementById('namaBarang');
    const hargaInput = document.getElementById('hargaSatuan');
    const qtyInput = document.getElementById('qty');
    
    let isValid = true;

    // Validasi Nama (Min 3 karakter)
    if (namaInput.value.trim().length < 3) {
        document.getElementById('error-nama').textContent = 'Nama barang minimal 3 karakter!';
        isValid = false;
    } else {
        document.getElementById('error-nama').textContent = '';
    }

    // Validasi Harga (Min Rp 500)
    const hargaVal = parseInt(hargaInput.value);
    if (isNaN(hargaVal) || hargaVal < 500) {
        document.getElementById('error-harga').textContent = 'Harga minimal Rp 500!';
        isValid = false;
    } else {
        document.getElementById('error-harga').textContent = '';
    }

    // Validasi Qty (Min 1)
    const qtyVal = parseInt(qtyInput.value);
    if (isNaN(qtyVal) || qtyVal < 1) {
        document.getElementById('error-qty').textContent = 'Jumlah minimal 1!';
        isValid = false;
    } else {
        document.getElementById('error-qty').textContent = '';
    }

    // Jika valid, masukkan ke array
    if (isValid) {
        const newItem = {
            nama: namaInput.value.trim(),
            harga: hargaVal,
            qty: qtyVal,
            subtotal: hargaVal * qtyVal
        };
        cart.push(newItem);
        renderCart();
        formBarang.reset(); // Kosongkan form
    }
});

// === 4. MANAJEMEN LIST & LOCALSTORAGE ===
function hapusItem(index) {
    cart.splice(index, 1); // Hapus 1 elemen pada index tertentu
    renderCart();
}

function simpanKeLocalStorage() {
    localStorage.setItem('miniPosCart', JSON.stringify(cart));
}

// Tombol Reset Transaksi Baru
document.getElementById('btn-reset').addEventListener('click', () => {
    if(confirm('Apakah Anda yakin ingin mereset transaksi ini?')) {
        cart = [];
        document.getElementById('uangBayar').value = '';
        document.getElementById('hasil-kembalian').textContent = '';
        renderCart();
    }
});

// === 5. KALKULATOR PEMBAYARAN ===
document.getElementById('btn-bayar').addEventListener('click', () => {
    const uangBayar = parseInt(document.getElementById('uangBayar').value);
    const totalAkhir = parseInt(totalAkhirEl.dataset.value) || 0;
    const hasilKembalianEl = document.getElementById('hasil-kembalian');

    if (isNaN(uangBayar)) {
        hasilKembalianEl.textContent = 'Masukkan nominal uang yang valid!';
        hasilKembalianEl.style.color = 'red';
        return;
    }

    if (uangBayar < totalAkhir) {
        hasilKembalianEl.textContent = 'Uang bayar tidak mencukupi!';
        hasilKembalianEl.style.color = 'red';
    } else {
        const kembalian = uangBayar - totalAkhir;
        hasilKembalianEl.textContent = `Uang Kembalian: ${formatRupiah(kembalian)}`;
        hasilKembalianEl.style.color = 'green';
    }
});

// === 6. IMPLEMENTASI FETCH API ASINKRON ===
// Fetch API untuk mengambil kalimat pengumuman promo/toko palsu
async function fetchStoreAnnouncement() {
    const announcementEl = document.getElementById('store-announcement');
    try {
        // Menggunakan JSONPlaceholder sebagai dummy API untuk memenuhi syarat Fetch API
        const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
        const data = await response.json();
        announcementEl.textContent = "Promo Hari Ini: Diskon 10% untuk belanja di atas Rp 50.000!";
    } catch (error) {
        announcementEl.textContent = "Selamat datang di Kantin Kampus!";
        console.error("Gagal mengambil data:", error);
    }
}

// Inisialisasi awal saat halaman dimuat
fetchStoreAnnouncement();
renderCart();