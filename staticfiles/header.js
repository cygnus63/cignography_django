function fetchPage(name){
    fetch(name).then(function(response){
        response.text().then(function(text){
            document.querySelector('article').innerHTML = text;
        })
    });
}

function addScript(src) {
    var s = document.createElement('new');
    s.type = 'text/javascript';
    s.src = src+'.js';
}

fetchPage('intro.html')