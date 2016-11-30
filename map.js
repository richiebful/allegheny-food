window.onload = function(){
	var foodMap = L.map("main-map", {
		center: [40.4281, -79.6289],
		zoom: 10,
		maxBounds: [[39.724, -80.519],[41.017, -78.657]]
	});
	L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}",
	{
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
		maxZoom: 18,
		minZoom: 8,
		bounds: [[39.724, -80.519],[41.017, -78.657]],
		id: "richiebful.285bkgie",
		accessToken: "pk.eyJ1IjoicmljaGllYmZ1bCIsImEiOiJjaXRocWNhYXYwMnZrMnhudmc2YmczOWZ2In0.-GYJUA4FymhrHdnzznE4RA"
	}).addTo(foodMap);

	var m1 = L.marker([50.0, 20.0]).addTo(foodMap);

	m1.addEventListener("click", function(){
		alert("m1 clicked");
	});
}