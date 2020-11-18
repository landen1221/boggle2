$('#word-form').submit(async function(evt) {
    evt.preventDefault();
    let word = $('#word').val();
    const resp = await axios.post("/check-word", {word});
    
    console.log(word)  
    console.log(resp)
    console.log(`resp data = ${resp.data.result}`)

    // If 'ok' Add word to list
    if (resp.data.result === 'ok') {
        newWord = document.createElement('li')
        newWord.innerText = word
        document.getElementById('foundWords').appendChild(newWord)
        $('#word').val('')
    } else {
        alert(resp.data.message)
    }
    
    // Update score
    console.log(resp.data.score)
    document.getElementById('score').innerText = resp.data.score
    document.getElementById('high-score').innerText = resp.data.highScore
    

})

let timer;
let count = 45;
$("#counter").text(count);

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
        location.reload();
    }
}