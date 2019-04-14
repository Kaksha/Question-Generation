let inp = document.getElementById('text')
let question = document.getElementById('question')
let options = document.getElementById('option')
let selectedOption = ''

inp.addEventListener('keydown', (e)=>{
    if(e.keyCode == 13 && !e.shiftKey){
        e.preventDefault()
    }
})

inp.addEventListener('keyup', (e) => {
    if(e.keyCode == 13){
        e.preventDefault()
        let text = e.target.innerHTML.trim()
        if(text){
            fetch(`/get-sent?text=${text}&option=${selectedOption}`)
            .then(response => response.json())
            .then(json => {
                console.log(json)
                question.innerHTML = json.text
            })
            .catch(err => {
                console.log(err)
                return null;
            })
        }
    }
})


options.addEventListener('change', (e) => {
    selectedOption = e.target.value
})

document.addEventListener('DOMContentLoaded', (e) => {
    fetch('/get-options')
    .then(response => response.json())
    .then(json => {
        for(let i in json['options']){
            let option = document.createElement('option')
            option.value = json['options'][i]
            option.innerText = json['options'][i]
            options.appendChild(option)
        }

        selectedOption = json['options'][0]
    })
})