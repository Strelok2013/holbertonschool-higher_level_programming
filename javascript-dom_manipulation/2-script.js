var header = document.querySelector("header");
var red_header = document.getElementById("red_header");

red_header.onclick = function addredclass()
{
    header.classList.add("red");
};