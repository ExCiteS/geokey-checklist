var marker;
var map;

function initMap() {

  var mylat = parseFloat(document.getElementsByName('checklistLat')[0].value);
  var mylng = parseFloat(document.getElementsByName('checklistLng')[0].value);

  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: mylat, lng: mylng},
    zoom: 12
  });

  var myLatLng = new google.maps.LatLng(mylat, mylng);
  placeMarker(myLatLng);

  google.maps.event.addListener(map, 'click', function(event) {
    placeMarker(event.latLng);
  });

}

function placeMarker(location) {
    if (marker) {
        marker.setPosition(location);
    } else {
       marker = new google.maps.Marker({
            position: location,
            map: map
        });
    }
    document.getElementsByName('checklistLat')[0].value = location.lat();
    document.getElementsByName('checklistLng')[0].value = location.lng();
}
