var list_movies = document.getElementById("list_movies");
var url = "https://swapi-api.hbtn.io/api/films/?format=json";

fetch(url)
    .then((response) => 
    {
        if (!response.ok)
        {
            throw new Error(`HTTP error: ${response.status}`);
        }
        return response.json();
    })
    .then((json) =>
    {
        for (var movie of json.results)
        {
            var new_item = document.createElement("li");
            new_item.textContent = movie.title;

            list_movies.appendChild(new_item);
        }
    })
    .catch((err) => console.error(`Fetch problem: ${err.message}`));