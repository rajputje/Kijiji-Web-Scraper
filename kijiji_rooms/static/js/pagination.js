/**
 * Returns a list item that links to a page number.
 * @param {string} href Link to navigate to when this item is clicked
 * @param {*} text Text to be displayed on this item
 * @param {boolean} isActive Is this the current page?
 * @returns 
 */
function makePageItem(href, text, isActive){
    var li = document.createElement("li");
    li.className = "page-item";
    if(isActive) 
      li.className += " active";
    var a = document.createElement("a");
    a.className = "page-link";
    a.href = href;
    a.text = text;
    li.append(a);
    return li;
  }

  /**
   * Appends page links to container. Page number cannot be below 1.
   * @param {Number} currentPage Current page number
   * @param {Object} searchVars Variables for filtering search results 
   * @param {Number} numOfPages Number of pages to link
   * @param {Object} container HTML element that will contain the links
   * */
  function paginate(currentPage, searchVars, numOfPages, container){
    var ul = container;
    var minPage = Math.max(currentPage - 2, 1);
    var maxPage = minPage + numOfPages;
    searchVars = JSON.parse(searchVars);

    //"Previous" Button
    var prevHref = (currentPage == 1) ? getUrl(1, searchVars) : getUrl(currentPage-1, searchVars);
    var prevList = makePageItem(prevHref, "Previous", false);
    ul.append(prevList);

    //Rest of the numbered buttons (eg. 1,2,3,4,...)
    for(var i = minPage; i < maxPage; i++){
      var pageItem = makePageItem(getUrl(i, searchVars), i, i == currentPage);
      ul.append(pageItem);
    }

    //"Next" button
    var nextList = makePageItem(getUrl(parseInt(currentPage)+1, searchVars), "Next", false);
    ul.append(nextList);
}

function getUrl(pageNum, searchVars){
  href = "/" + pageNum + "?location=" + searchVars.location + "&distance=" + searchVars.distance + "&min_price=" + searchVars.minPrice
            + "&max_price=" + searchVars.maxPrice;
  if(searchVars.minPriceEnabled)
    href += "&min_price_chk=" + searchVars.minPriceEnabled;
  if(searchVars.maxPriceEnabled)
    href += "&max_price_chk=" + searchVars.maxPriceEnabled;
  return href;
}