// console.log("oi");

// let userName = "Lira";
// let age = "22";
// let vivo = false;

// console.log(userName, age, vivo);

// let nome = prompt("Qual o seu nome?");
// console.log(`Bom dia, ${nome}`);



// setInterval(() => {
//     let ran = Math.floor(Math.random() * (11 - 1) + 1);
//     console.log(ran);
// }, 500);


let name = prompt("Qual o seu nome?");
let age = prompt("Qual a sua idade?");
let programador = confirm("Você é um programador?");

if(programador) {
    console.log(`Bom dia, ${name}. Idade: ${age}. God`);
}else {
    console.log("Pow, cara");
}