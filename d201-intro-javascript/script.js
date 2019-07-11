let name = prompt('Seu nome?');
let escadas = prompt('Quantos lances de escadas?');
let material = prompt('Qual material da escada?');
let choice = material;

let i = 0;
while(i < escadas) {
    console.log(`${material}`);
    material = material + choice;
    i++
}
console.log(`Toma ai suas escadas usando: ${choice}, ${name}`);


// let i = 0;
// let arr = [];
// while(i < 10) {
//     arr.push(i);
//     i++
// }

// for(i; i < 10; i++) {
//     console.log(i);
// }

// console.log(arr);