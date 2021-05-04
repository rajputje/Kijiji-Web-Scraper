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
   * @param {Number} numOfPages Number of pages to link
   * @param {Object} container HTML element that will contain the links
   * */
  function paginate(currentPage, numOfPages, container){
    var ul = container;
    var minPage = Math.max(currentPage - 2, 1);
    var maxPage = minPage + numOfPages;
  
    var prevHref = (currentPage == 1) ? "/" : "/" + (currentPage-1);
    var prevList = makePageItem(prevHref, "Previous", false);
    ul.append(prevList);

    for(var i = minPage; i < maxPage; i++){
      var pageItem = makePageItem("/" + i, i, i == currentPage);
      ul.append(pageItem);
    }

    var nextList = makePageItem("/" + (parseInt(currentPage) + 1), "Next", false);
    ul.append(nextList);
}