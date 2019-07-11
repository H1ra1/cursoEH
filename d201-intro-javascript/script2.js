let name = prompt('Qual o seu nome?');
let materia = prompt('Qual a matéria?');
let nota = prompt('Qual a sua nota?');
let media = 7;

if(nota <= 10 && nota >= 1) {
    if(nota >= media) {
        alert(`Parabéns, ${name}. Você passou na materia ${materia}, com a nota: ${nota}`);
    } else if(Number(nota) + 0.5 >= media) {
        alert(`Você foi aprovado pelo sistema com a nota ${nota}.`);
    } else {
        alert('Deu ruim, lindão');
    }
} else {
    alert('Coloque uma nota válida');
}