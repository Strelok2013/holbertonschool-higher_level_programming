window.onload = () =>
{
    var hello = document.getElementById("hello");
    var url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

    fetch(url)
    .then((response) => 
        {
            if (!response.ok)
            {
                throw new Error(`HTTP Error: ${response.status}`);
            }
            return response.json();
        })
        .then((json) =>
        {
            hello.textContent = json.hello;
        })
        .catch((err) => console.error(`Fetch problem: ${err.message}`));
}