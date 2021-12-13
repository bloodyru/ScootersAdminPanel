//добавляем прослушивание события загрузки станицы и запускаем функцию  startup
window.addEventListener("load", startup, false);
//массив с именами  типов зон и и их содержимым
var NamesTypeOfZoneAndParkingAndRide  = JSON.parse(document.getElementById('massiv').textContent);

for (i in NamesTypeOfZoneAndParkingAndRide){
  CanYouParkingOnThisArea = NamesTypeOfZoneAndParkingAndRide[i][4]
  if (CanYouParkingOnThisArea ==true){
    CheckParking= document.getElementById('CanYouParkingOnThisArea'+NamesTypeOfZoneAndParkingAndRide[i][1])
    CheckParking.checked = "checked"
  }
  if (NamesTypeOfZoneAndParkingAndRide[i][3] ==true){
    CheckScooter= document.getElementById('CanYouScooterOnThisArea'+NamesTypeOfZoneAndParkingAndRide[i][1])
    CheckScooter.checked = "checked"
  }
  i=i+1
}


function watchColorPicker(event) {
  for (i in NamesTypeOfZoneAndParkingAndRide) {
  document.getElementById(NamesTypeOfZoneAndParkingAndRide[i][1]+'id_ColorZone').value=document.getElementById(NamesTypeOfZoneAndParkingAndRide[i][1]+'id_hex_color').value
  }
}

function startup() {

  for (i in NamesTypeOfZoneAndParkingAndRide) {
    document.getElementById(NamesTypeOfZoneAndParkingAndRide[i][1]+'id_hex_color').value=NamesTypeOfZoneAndParkingAndRide[i][2]
    document.getElementById(NamesTypeOfZoneAndParkingAndRide[i][1]+'id_ColorZone').value=NamesTypeOfZoneAndParkingAndRide[i][2]
    document.getElementById(NamesTypeOfZoneAndParkingAndRide[i][1]+'MaxSpeed').value=NamesTypeOfZoneAndParkingAndRide[i][5]
    document.getElementById(NamesTypeOfZoneAndParkingAndRide[i][1]+'Description').value=NamesTypeOfZoneAndParkingAndRide[i][6]
    colorWell = document.getElementById(NamesTypeOfZoneAndParkingAndRide[i][1]+"id_hex_color");
    colorWell.addEventListener("input", watchColorPicker, false);
    colorWell.addEventListener("change", watchColorPicker, false);
    colorWell.select();
  }
}

function openZone(ZoneName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(ZoneName).style.display = "block";
    elmnt.style.backgroundColor = color;

}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();