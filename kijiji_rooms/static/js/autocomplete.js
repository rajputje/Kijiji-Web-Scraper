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
}