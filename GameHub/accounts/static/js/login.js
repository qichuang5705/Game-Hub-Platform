function ChangeBackA(){
    document.getElementById("demo").innerHTML = "After"
}
function ChangeBackB(){
    document.getElementById("demo").innerHTML = "Before"
}


function changeBackground() {
    let randomColor = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;
    document.body.style.backgroundColor = randomColor;
}