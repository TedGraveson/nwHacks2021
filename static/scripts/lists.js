let listBtn = document.getElementById("list-btn");
let listItem = document.getElementById("list-item");
let list = document.getElementById("list");
let listSub = document.getElementById("submit-list");
let listArray = [];
let date = document.getElementById("date-time");
let address = document.getElementById("address");
let tip = document.getElementById("tip");
let firstName = document.getElementById("firstName");
let lastName = document.getElementById("lastName");


listBtn.addEventListener("click", function() {addListItem(listItem.value)});
listItem.addEventListener("keyup", function(event) {
    if(event.key == "Enter") {
        listBtn.click();
    }
});


//Stops enter from hitting form
$(document).ready(function() {
    $(window).keydown(function(event){
      if(event.keyCode == 13) {
        event.preventDefault();
        return false;
      }
    });
  });

function addListItem(item) {
    if (item !== "") {
        let node = document.createElement("LI");
        let textNode = document.createTextNode(item);
        node.appendChild(textNode);
        node.classList = "list-group-item"
        list.appendChild(node)
        listArray.push(item)
        listItem.value = null;
    }
};




$(listSub).click(function(e) {
    console.log("yo")
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: document.url,
        data: JSON.stringify({
            "items" : listArray,
            "timeEnd"  : date.value,
            "address" : address.value,
            "date" : date.value,
            "tip" : tip.value
        }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data){
            window.location.replace(`${response.data}`);},
        failure: function(errMsg) {
            alert(errMsg);
        }
    })
    });

