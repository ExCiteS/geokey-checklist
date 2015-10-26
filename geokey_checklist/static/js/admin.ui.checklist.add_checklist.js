var marker;
var map;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 47.6097, lng: -122.3331},
    zoom: 8
  });

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      map.setCenter(pos);
    }, function() {
      handleLocationError(true);
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false);
  }

  google.maps.event.addListener(map, 'click', function(event) {
    placeMarker(event.latLng);
  });

}

function handleLocationError(browserHasGeolocation) {
  if(browserHasGeolocation) {
    alert('Error: The GeoLocation service failed.');
  }
  else {
    alert('Error: Your browser doesn\'t support geoLocation.');
  }
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

    //alert(location.lat() + ", " + location.lng());
    document.getElementsByName('checklistLat')[0].value = location.lat();
    document.getElementsByName('checklistLng')[0].value = location.lng();
}
