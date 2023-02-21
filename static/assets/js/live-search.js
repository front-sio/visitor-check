const url = window.location.href;
const searchForm = document.querySelector('#search-form');
const resultBox = document.querySelector('#result-box');
const resultInput = document.querySelector('#search-input');
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

console.log(csrf)




   function sendSearchData(search){

    }
    searchInput.addEventListener('keyup', e=> {
    console.log(e.target.value)

    sendSearchData(e.target.value)
    })