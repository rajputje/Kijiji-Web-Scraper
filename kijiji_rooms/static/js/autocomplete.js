var autocompleteLocation;
function initAutoComplete(){
    autocompleteLocation = new google.maps.places.Autocomplete(
        document.getElementById('location'),
        {
            componentRestrictions: {'country' : 'CA'},
            fields: ['name']
        }
    );
}