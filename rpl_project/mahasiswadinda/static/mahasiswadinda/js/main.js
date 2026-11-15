console.log('Halo dari main.js');

document.addEventListener('DOMContentLoaded', function () {
    const tombol = document.getElementById('btn-mulai');

    if (tombol) {
        tombol.addEventListener('click', function (event) {
            event.preventDefault(); // cegah link "#" melompat ke atas halaman
            alert('Selamat belajar!');
        });
    }
});