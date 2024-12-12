var toggle_header = document.getElementById("toggle_header");
var header = document.querySelector("header");

toggle_header.onclick = changeClass;

function changeClass()
{
    header.classList.toggle("red");
    header.classList.toggle("green");
};