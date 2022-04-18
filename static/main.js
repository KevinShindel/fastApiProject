
$(init_map = function() {
    let map = $("#map")
    map.googleMap({
        zoom: 15, // Initial zoom level (optional)
        coords: [46.640232, 32.561961],
        type: $("#map_type").val()
    });

    map.addMarker({
        coords: [46.638174, 32.560896], // GPS coords
        title: 'Два БТРа (Внимание один украден у ВСУ!), Один Краз',
        text:  [46.638174, 32.560896],
    })
    map.addMarker({
        coords: [46.638070, 32.563879], // GPS coords
        title: 'Один Патрульный',
        text:  [46.638070, 32.563879]
    })

    map.addMarker({
        coords: [46.638129, 32.560506], // GPS coords
        title: 'Два Патрульных',
        text:  [46.638070, 32.563879]
    })

    map.addMarker({
        coords: [46.637900, 32.562779], // GPS coords
        title: 'Два Краза',
        text:  [46.637900, 32.562779],
    })
    map.addMarker({
        coords: [46.638652, 32.460717], // GPS coords
        title: 'Блок Пост',
        text:  [46.638652, 32.460717]
    })

    map.addMarker({
        coords: [46.627455, 32.568748], // GPS coords
        title: 'БТР',
        text:  [46.627455, 32.568748]
    })

    map.addMarker({
        coords: [46.6279062814802, 32.5654971625523], // GPS coords
        title: 'Здание захвачено ( приблизительно 50 орков ) есть Кразы',
        text:  [46.6279062814802, 32.5654971625523]
    })

    map.addMarker({
        coords: [46.631793, 32.433660], // GPS coords
        title: 'Блок Пост',
        text:  [46.631793, 32.433660]
    })

    map.addMarker({
        coords: [46.655912, 32.605082], // GPS coords
        title: 'Блок Пост (1 БТР и 1 Тигр)',
        text:  [46.655912, 32.605082]
    })

    map.addMarker({
        coords: [46.655841, 32.584444], // GPS coords
        title: 'Блок Пост (1 БТР и 1 Тигр)',
        text:  [46.655841, 32.584444]
    })

    map.addMarker({
        coords: [46.663306, 32.596297], // GPS coords
        title: 'Блок Пост (1 БТР и 1 Тигр)',
        text:  [46.663306, 32.596297]
    })

    map.addMarker({
        coords: [46.67979966779393, 32.57422316016725], // GPS coords
        title: 'Блок Пост',
        text:  [46.67979966779393, 32.57422316016725]
    })

    map.addMarker({
        coords: [46.656770, 32.607721], // GPS coords
        title: 'Блок Пост',
        text:  [46.656770, 32.607721]
    })

    map.addMarker({
        coords: [46.64055381083328, 32.61595754555059], // GPS coords
        title: 'Здание окупировано, есть вероятность наличии пехоты внутри. Тажке постоянно наличие патрулей вокруг.' +
            'Три Краза и пару Тигров',
        text:  [46.64055381083328, 32.61595754555059]
    })

})