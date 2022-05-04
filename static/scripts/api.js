let load_data = function () {
    $.get('http://127.0.0.1:8000/points/').
    then(function (data) {
        Array.from(data).forEach((item)=> map.addMarker(item))
    }, function (error) {
        console.error(error)
    });
}

$("#form").submit(function (e) {
    e.preventDefault();

    let data =  $(e.target).serialize();
    // TODO: need to refactor coords from string to array
    $.post("http://127.0.0.1:8000/points/", data);
  });

// TODO: Create method for delete markers
$(this).click(function (e){
    let id = e.target // Find marker id;
    map.removeMarker();
})