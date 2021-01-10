let listBtn = document.getElementById("list-btn");
let listItem = document.getElementById("list-item");
let list = document.getElementById("list")
listSub = document.getElementById("submit-list")
let listArray = [];

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
        list : JSON.stringify(listArray)
    },
    function() {
        console.log(JSON.stringify(listArray));
        
    });
};