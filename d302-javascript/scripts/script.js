let savedImages = ['n1.jpg', 'n2.jpg', 'n3.jpg', 'n4.jpg', 'n5.jpg', 'n6.jpg', 'n7.jpg', 'n8.jpg'];
let images = savedImages.concat(savedImages);

let turned = null;

function shuffle(array) {
    let temporary_value;
    let random_indice;

    for(let i = array.length - 1; i !== 0; i--) {
        random_indice = Math.floor(Math.random() * i);

        temporary_value = array[i];
        array[i] = array[random_indice];
        array[random_indice] = temporary_value;

    }

    return array;
}

let cards = document.querySelectorAll('.card');

images = shuffle(images);

for(let i = 0; i < cards.length; i++) {
    cards[i].style.backgroundImage = `url('imgs/${images[i]}')`;
}

setTimeout(() => {
    for(card of cards) {
        card.style.background = 'red';
        console.log(card.id)
        card.onclick = () => {
            console.log(card.id)
        }
    }
}, 3000)
