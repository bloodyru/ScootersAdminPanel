var mymap = L.map('mapid').setView([48.470987, 135.092935], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYmxvb2R5cnUiLCJhIjoiY2txYnpjMnoxMDNyODJ1cDliaGlsOGdlNCJ9.lmO1vBnXQzD21BQBAwhJhQ'
}).addTo(mymap);

window.addEventListener("load", startup, false);

function watchColorPicker(event) {
document.getElementById('id_ColorZone').value=document.getElementById('id_hex_color').value
drowpolygon(poly)
}

function startup() {
  colorWell = document.querySelector("#id_hex_color");
  colorWell.addEventListener("input", watchColorPicker, false);
  colorWell.addEventListener("change", watchColorPicker, false);
  colorWell.select();

}

var polygonfieldstring = document.getElementById('id_GPSPoints').value;
var colorzone = document.getElementById('id_ColorZone').value;
document.getElementById('id_hex_color').value=document.getElementById('id_ColorZone').value
var tomassive = polygonfieldstring.split(",");
var gpsmassive = [];
for(var k=0;k<tomassive.length;){
    var latLong = tomassive[k].split();
    gpsmassive.push([parseFloat(tomassive[k]), parseFloat(tomassive[k+1]) ]);
    k=k+2
}



var polygon = L.polygon(
    gpsmassive,{color: document.getElementById('id_hex_color').value}
).addTo(mymap);

var poly = [];
var polygonForDb = [];

var newpolygon
function drowpolygon(poly) {
    if (poly.length>3){
        mymap.removeLayer(newpolygon)
       }
    newpolygon = L.polygon( poly,{color: document.getElementById('id_hex_color').value}).addTo(mymap);
}
function onMapClick(e) {
    polygonForDb.push(e.latlng.lat);
    polygonForDb.push(e.latlng.lng);
    poly.push([e.latlng.lat, e.latlng.lng]);
    document.getElementById('id_GPSPoints').value = polygonForDb;
    drowpolygon(poly)

}

mymap.on('click', onMapClick);






