document.addEventListener('DOMContentLoaded', function () {

    console.log('js')
    // Django admin alanlarının ID'leri genelde 'id_alanadi' şeklindedir
    const durumField = document.querySelector('#id_durum');
    const nedenSatiri = document.querySelector('.field-pasif_nedeni'); // Satırın tamamını gizler

    function showHideNeden() {
        if (durumField.value === 'Pasif') {
            nedenSatiri.style.display = 'block';
        } else {
            nedenSatiri.style.display = 'none';
        }
    }

    if (durumField && nedenSatiri) {
        // Sayfa yüklendiğinde mevcut duruma göre göster/gizle
        showHideNeden();
        // Seçim her değiştiğinde çalıştır
        durumField.addEventListener('change', showHideNeden);
    }
});