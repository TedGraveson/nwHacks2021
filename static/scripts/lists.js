let listBtn = document.getElementById("list-btn");
let listItem = document.getElementById("list-item");
let list = document.getElementById("list");
listSub = document.getElementById("submit-list");
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
listSub.addEventListener("click", function() {
    postList(list);
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

function postList() {
    $.post( "/getList/",
    {    
        items : JSON.stringify(listArray),
        timeEnd  : date.value,
        address : address.value,
        date : date.value,
        tip : tip.value,
        first : firstName.innerHTML,
        last : lastName.innerHTML
    },
    function() {
        listArray = [];
        listItem.value = null;
        list.innerHTML = "";
        console.log("Sent");
        
    });
};

