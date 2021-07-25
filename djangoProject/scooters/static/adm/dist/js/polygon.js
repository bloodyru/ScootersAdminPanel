


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
console.log(polygonfieldstring)
var mass = polygonfieldstring.split(",");
var ans = [];
for(var k=0;k<mass.length;){
    var latLong = mass[k].split();
    ans.push([ parseFloat(mass[k]), parseFloat(mass[k+1]) ]);
    k=k+2
}
console.log(ans)

var polygon = L.polygon([
    ans
]).addTo(mymap);
var polyForDb = [];
function onMapClick(e) {
    polyForDb.push(e.latlng.lat);
    polyForDb.push(e.latlng.lng);

    document.getElementById('id_GPSPoints').value = polyForDb;
}

mymap.on('click', onMapClick);
