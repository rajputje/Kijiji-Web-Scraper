var autocompleteLocation;
function initAutoComplete(){
    console.log("initAutoComplete");
    autocompleteLocation = new google.maps.places.Autocomplete(
        document.getElementById('location'),
        {
            componentRestrictions: {'country' : 'CA'},
            fields: ['name']
        }
    );

    //autocompleteLocation.addListener('place_changed', onPlaceChanged);
}

/*
function onPlaceChanged(){
    console.log("on place changed");
    var place = autocompleteLocation.getPlace();

    if(!place.geomoetry){
        //User did not select a prediction

    }
    else{

    }
}
*/