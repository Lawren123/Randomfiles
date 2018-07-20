//My Variales!
var ourLoc;
var view;
var map;

//  We should initalize our variables!
function init() {
	// Initalize things here
	ourLoc = ol.proj.fromLonLat([-84.3869,33.7739]);

	view = new ol.View({
		center: ourLoc,
		zoom: 20 // Students can play around with the starting zoom.
	});

	map = new ol.Map({
		target: 'map', // The "Target" is our <div> name.
		layers: [
		  new ol.layer.Tile({
		    source: new ol.source.OSM() // Explain: this is a required variable.
		  })
		],
		loadTilesWhileAnimating: true,
		view: view
	});

}

function panHome(){
  view.animate({
    center:ourLoc,
    Duration: 2000 //2000 milliseconds = 2 seconds
  });
}

function panToLocation(){
  var countryName = document.getElementById("country-name").value;
  var lon = 0.0;
  var lat = 0.0;
  if(countryName===""){
    alert("You didn't enter a country name!")
  }
  // Finf variables from rest Countries API
  var query = "https://restcountries.eu/rest/v2/name/"+ countryName;
  query = query.replace(/ /g, "20%")
  alert(query);

  var countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, false);
  countryRequest.send();

  alert("Ready State"+ countryRequest.readyState);
  alert("Status"+ countryRequest.status);
  alert("Respone" + counrtyRequest.responeText);

  var location = ol.proj.fromLon([lon,lat]);

  view.animate({
    center: location,
    duration: 2000
  });
}
window.onload = init;
