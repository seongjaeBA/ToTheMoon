'use strict';
$(document).ready(function() {
    // [ basic maps ]
    var basic;
    basic = new GMaps({
        el: '#basic-map',
        lat: 37.497981,
        lng: 127.027542,
        scrollwheel: false
    });
    // [ Gmaps ]
    var map;
    map = new GMaps({
        el: '#markers-map',
        lat: 37.497981,
        lng: 127.027542,
        scrollwheel: false
    });
    // [ Add-marker map ]
    map.addMarker({
        lat: 37.497981,
        lng: 127.027542,
        title: 'Marker with InfoWindow',
        infoWindow: {
            content: '<p><Phoenicoded></Phoenicoded> <br/> Buy Now at <a href="">Themeforest</a></p>'
        }
    });
    // [ Gmap-overlay ]
    var mapOverlay;
    mapOverlay = new GMaps({
        el: '#mapOverlay',
        lat: 37.497981,
        lng: 127.027542,
        scrollwheel: false
    });
    mapOverlay.drawOverlay({
        lat: 37.497981,
        lng: 127.027542,
        content: '<div class="overlay">여기가 어디?</div>'
    });

    // [ Geomap ]
    var mapGeo = new GMaps({
        div: '#mapGeo',
        lat: 37.497981,
        lng: 127.027542,
    });
    // [ Geocoding form ]
    $('#geocoding_form').submit(function(e) {
        e.preventDefault();
        GMaps.geocode({
            address: $('#address').val().trim(),
            callback: function(results, status) {
                if (status == 'OK') {
                    var latlng = results[0].geometry.location;
                    mapGeo.setCenter(latlng.lat(), latlng.lng());
                    mapGeo.addMarker({
                        lat: latlng.lat(),
                        lng: latlng.lng()
                    });
                }
            }
        });
    });

    // 강남 대로 앞 찍었는데 지하로 들어갔네 하악
    var panorama;
    panorama = GMaps.createPanorama({
        el: '#mapStreet',
        lat: 37.497981,
        lng: 127.027542,
    });

    // map type 조절 확인해봐야함.
    var mapT;
    mapT = new GMaps({
        div: '#mapTypes',
        lat: 37.497981,
        lng: 127.027542,
        mapTypeControlOptions: {
            mapTypeIds: ["hybrid", "roadmap", "satellite", "terrain", "osm"]
        }
    });
    mapT.addMapType("osm", {
        getTileUrl: function(coord, zoom) {
            return "https://a.tile.openstreetmap.org/" + zoom + "/" + coord.x + "/" + coord.y + ".png";
        },
        tileSize: new google.maps.Size(256, 256),
        name: "OpenStreetMap",
        maxZoom: 18
    });
    mapT.setMapTypeId("osm");
    var georssmap = new google.maps.Map(document.getElementById('georssmap'), {
        zoom: 4,
        center: {
            lat: 37.497981,
            lng: 127.027542,
        }
    });

    // 데이터 ip location marker
    var georssLayer = new google.maps.KmlLayer({
        url: 'http://api.flickr.com/services/feeds/geo/?g=322338@N20&lang=en-us&format=feed-georss'
    });
    georssLayer.setMap(georssmap);
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: {
            lat: 37.497981,
            lng: 127.027542,
        }
    });


    // marker clustering
    var labels = '가나다라마바사아자차';
    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });
    var markerCluster = new MarkerClusterer(map, markers, {
        imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
    });
});
var locations = [{
    lat: 37.497981,
    lng: 127.027542,
}, {
    lat: 36.336120,
    lng: 127.394750,
}, {
    lat: 35.182090, 
    lng: 129.051166,
}, {
    lat: 35.147991,
    lng: 126.827312,
}, {
    lat: 37.466103, 
    lng: 126.702494,
}
]
