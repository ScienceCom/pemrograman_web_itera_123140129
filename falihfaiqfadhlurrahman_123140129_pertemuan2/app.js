// 1. CLASS: Model Data menggunakan ES6 Class
class TaskItem {
    constructor(id, title, category) {
        this.id = id;
        this.title = title;
        this.category = category;
        this.completed = false; // State awal
    }
}

// 2. CLASS: Arsitektur Utama Aplikasi
class DashboardApp {
    constructor() {
        // Deklarasi variabel dengan let & const secara tepat
        const savedData = localStorage.getItem('dashboard_tasks');
        this.tasks = savedData ? JSON.parse(savedData) : [];
        
        // DOM Elements
        this.form = document.getElementById('task-form');
        this.titleInput = document.getElementById('task-title');
        this.categoryInput = document.getElementById('task-category');
        this.taskList = document.getElementById('task-list');
        this.weatherInfo = document.getElementById('weather-info');
        this.weatherIcon = document.getElementById('weather-icon');

        // Inisialisasi Aplikasi
        this.bindEvents();
        this.render();
        this.fetchWeather();
    }

    // 3. ARROW FUNCTION 1: Event Binder dengan Event Delegation
    bindEvents = () => {
        // Submit form
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.addTask(this.titleInput.value.trim(), this.categoryInput.value);
        });

        // Event delegation untuk tombol di dalam task-list
        this.taskList.addEventListener('click', (e) => {
            const btn = e.target.closest('button');
            if (!btn) return;

            const id = Number(btn.dataset.id);
            if (btn.classList.contains('btn-toggle')) this.toggleTask(id);
            if (btn.classList.contains('btn-edit')) this.editTask(id);
            if (btn.classList.contains('btn-delete')) this.deleteTask(id);
        });
    }

    // 4. ASYNC/AWAIT & DESTRUCTURING (Memanggil Cuaca area ITERA/Bandar Lampung)
    fetchWeather = async () => {
        try {
            // Fetch dari Open-Meteo
            const response = await fetch('https://api.open-meteo.com/v1/forecast?latitude=-5.36&longitude=105.31&current_weather=true');
            const data = await response.json();
            
            // Destructuring bersarang (nested destructuring)
            const { current_weather: { temperature, windspeed } } = data;
            
            // Template Literals
            this.weatherIcon.textContent = '';
            this.weatherInfo.textContent = `${temperature}°C | Angin: ${windspeed} km/h`;
        } catch (error) {
            this.weatherIcon.textContent = '';
            this.weatherInfo.textContent = 'Gagal memuat cuaca.';
        }
    }

    // 5. ARROW FUNCTION 2 & SPREAD OPERATOR (Tambah Tugas)
    addTask = (title, category) => {
        if (!title) return;
        const newTask = new TaskItem(Date.now(), title, category);
        
        // Immutability: Menggunakan Spread Operator alih-alih .push()
        this.tasks = [...this.tasks, newTask];
        
        this.saveAndRender();
        this.form.reset();
    }

    // FITUR EDIT (Spread Operator & Destructuring Array)
    editTask = (id) => {
        // Mencari tugas yang ada
        const taskToEdit = this.tasks.find(t => t.id === id);
        if(!taskToEdit) return;

        const newTitle = prompt("Edit judul tugas:", taskToEdit.title);
        
        if (newTitle !== null && newTitle.trim() !== '') {
            // Immutability: Update menggunakan .map() dan Spread Operator Object
            this.tasks = this.tasks.map(task => 
                task.id === id ? { ...task, title: newTitle.trim() } : task
            );
            this.saveAndRender();
        }
    }

    // FITUR TOGGLE SELESAI
    toggleTask = (id) => {
        this.tasks = this.tasks.map(task => 
            task.id === id ? { ...task, completed: !task.completed } : task
        );
        this.saveAndRender();
    }

    // FITUR HAPUS
    deleteTask = (id) => {
        if(confirm("Yakin ingin menghapus agenda ini?")) {
            this.tasks = this.tasks.filter(task => task.id !== id);
            this.saveAndRender();
        }
    }

    // HELPER: Simpan ke LocalStorage dan Render Ulang
    saveAndRender = () => {
        localStorage.setItem('dashboard_tasks', JSON.stringify(this.tasks));
        this.render();
    }

    // 6. ARROW FUNCTION 3 & TEMPLATE LITERALS (Render UI)
    render = () => {
        if (this.tasks.length === 0) {
            this.taskList.innerHTML = `<p style="text-align:center; color:#64748b;">Belum ada agenda.</p>`;
            return;
        }

        const html = this.tasks.map(task => {
            // Destructuring Object saat merender
            const { id, title, category, completed } = task;
            
            return `
                <div class="task-card ${completed ? 'done' : ''}">
                    <div class="task-info">
                        <span class="task-title">${title}</span>
                        <span class="task-badge">${category}</span>
                    </div>
                    <div class="task-actions">
                        <button class="btn-icon btn-toggle" data-id="${id}" title="Tandai Selesai">✔</button>
                        <button class="btn-icon btn-edit" data-id="${id}" title="Edit">✏️</button>
                        <button class="btn-icon btn-delete" data-id="${id}" title="Hapus">🗑️</button>
                    </div>
                </div>
            `;
        }).join('');

        this.taskList.innerHTML = html;
    }
}

// Inisialisasi Aplikasi (Instansiasi Class)
document.addEventListener('DOMContentLoaded', () => {
    new DashboardApp();
});