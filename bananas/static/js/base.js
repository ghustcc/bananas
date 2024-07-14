const addLot = document.getElementById('add-lot');
const dialogAdd = document.getElementById('dialog-add-lot');
const dialogExit = document.getElementById('dialog-sair');

addLot.addEventListener('click', ()=>{
    dialogAdd.showModal();
})

dialogExit.addEventListener('click', ()=>{
    dialogAdd.close();
})