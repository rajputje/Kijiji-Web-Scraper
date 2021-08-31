let minPriceChk = document.querySelector("#min_price_chk");
let maxPriceChk = document.querySelector("#max_price_chk");

let minPriceInput = document.querySelector("#min_price");
let maxPriceInput = document.querySelector("#max_price");

minPriceChk.addEventListener("click", minPriceClicked);
maxPriceChk.addEventListener("click", maxPriceClicked);

window.addEventListener("load", onWindowLoad);

function onWindowLoad(e){
    minPriceChk.checked = minPriceChk.value == "True";
    maxPriceChk.checked = maxPriceChk.value == "True";
    minPriceClicked();
    maxPriceClicked();
}

function minPriceClicked(e){
    if(minPriceChk.checked){
        minPriceInput.readOnly = false;
        minPriceChk.value = true;
    }
    else{
        minPriceInput.readOnly = true;
        minPriceChk.value = false;
    }
}

function maxPriceClicked(e){
    if(maxPriceChk.checked){
        maxPriceInput.readOnly = false;
        maxPriceChk.value = true;
    }
    else{
        maxPriceInput.readOnly = true;
        maxPriceChk.value = false;
    }
}