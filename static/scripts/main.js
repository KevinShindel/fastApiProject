// Create GoogleMap
let map = $("#map")
$(init_map = function() {
    map.googleMap({
        zoom: 15, // Initial zoom level (optional)
        coords: [46.640232, 32.561961],
        type: $("#map_type").val()
    });
    load_data();
})

// Add point pop-up window
function showForm() {
    $("#pop-up").toggle("hidden");
    $(".wrapper").toggle("hidden");
}

// Close button
$("#pop-up button[type=button]").click(function () {
    $("#pop-up").toggle("hidden");
    $(".wrapper").toggle("hidden");
})

// Close pop-up if click on wrapper
$('.wrapper').click(function (){
    $("#pop-up").toggle("hidden");
    $(".wrapper").toggle("hidden");
})

