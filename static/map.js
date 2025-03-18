function initMap() {
    var map = L.map('map').setView([48.8566, 2.3522], 12);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    var concession1 = L.marker([48.8566, 2.3522]).addTo(map)
        .bindPopup("Concession 1");

    var concession2 = L.marker([48.8666, 2.3322]).addTo(map)
        .bindPopup("Concession 2");
}

document.addEventListener("DOMContentLoaded", function () {
    initMap();
});

