const select = {
    squares : document.querySelectorAll('.square'),
    body :  document.querySelector('body')
}

let randomColor = (max, min) => {
    let random = Math.floor(Math.random() * (max - min) + min);
    return random;
}

let randomSize = (max, min) => {
    let random = Math.floor(Math.random() * (max - min) + min);
    return random
}

let style = () => {
    for(square of select.squares) {
        square.style.backgroundColor = `rgb(${randomColor(255, 0)}, ${randomColor(255, 0)}, ${randomColor(255, 0)})`;
        square.style.width = `${randomSize(250, 10)}px`;
        square.style.height = `${randomSize(250, 10)}px`; 
    }
    select.body.style.backgroundColor = `rgb(${randomColor(255, 0)}, ${randomColor(255, 0)}, ${randomColor(255, 0)})`;
}

let animation = (timeI) => {
    const inter = setInterval((e) => {
        style();
    }, timeI);
    
}

animation(300);

