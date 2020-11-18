let score = 0

$('#word-form').submit(function(evt) {
    evt.preventDefault();
    let word = $('#word').val();

    newWord = document.createElement('li')
    newWord.innerText = word
    
    console.log(word)


    const resp = await axios.get("/check-word", { params: { word: word }});


    document.getElementById('foundWords').appendChild(newWord)

})

let timer;
let count = 60;

$("#counter").text(count);
//update display

timer = setTimeout(update, 1000);
function update()
{
    if (count > 0)
    {
       $("#counter").text(--count);
       timer = setTimeout(update, 1000);
    }
    else
    {
        alert("Time's Up!!!");
    }
}