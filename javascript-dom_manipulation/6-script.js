var url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
var character = document.getElementById("character");

fetch(url).then((response) => 
    {
        if(!response.ok)
        {
            throw new Error(`HTTP error: ${response.status}`);
        }

        return response.json();
    })
    .then((json) => {
        character.textContent = json.name;
    })
    .catch((err) => console.error(`Fetch problem: ${err.message}`));