var update_header = document.getElementById("update_header");
var header = document.querySelector("header");

update_header.onclick = changeText;

function changeText()
{
    header.textContent = "New Header!!!"
};