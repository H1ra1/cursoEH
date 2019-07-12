// for(let i = 2; i <= 100; i++) {
//     console.log(i);
//     i++
// }

function find(array, word) {
    for(palavra of array) {
        if(word === palavra) {
           return `Palavra "${palavra}" encontrada na lista`;
        }
    } 
    return 'palavra não encontrada';
}

let lista = ['carro', 'folha', 'arvore'];
console.log(find(lista, 'folha'));