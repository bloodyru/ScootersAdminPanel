var mymap = L.map('mapid').setView([48.470987, 135.092935], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYmxvb2R5cnUiLCJhIjoiY2txYnpjMnoxMDNyODJ1cDliaGlsOGdlNCJ9.lmO1vBnXQzD21BQBAwhJhQ'
}).addTo(mymap);

var polygonfieldstring = document.getElementById('id_GPSPoints').value;
var colorzone = document.getElementById('id_ColorZone').value;
console.log(colorzone);
var tomassive = polygonfieldstring.split(",");
var gpsmassive = [];
for(var k=0;k<tomassive.length;){
    var latLong = tomassive[k].split();
    gpsmassive.push([parseFloat(tomassive[k]), parseFloat(tomassive[k+1]) ]);
    k=k+2
}

var polygon = L.polygon(
    gpsmassive,{color: colorzone}
).addTo(mymap);

var polygonForDb = [];
function onMapClick(e) {
    polygonForDb.push(e.latlng.lat);
    polygonForDb.push(e.latlng.lng);

    document.getElementById('id_GPSPoints').value = polygonForDb;
}

mymap.on('click', onMapClick);
