const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let desenhando = false;

// Inicia o desenho ao pressionar o mouse
function iniciarDesenho(e) {
    desenhando = true;
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
}

// Desenha enquanto o mouse é arrastado
function desenhar(e) {
    if (!desenhando) return;
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.strokeStyle = '#000'; // Cor do traço
    ctx.lineWidth = 2; // Largura do traço
    ctx.stroke();
}

// Para o desenho ao soltar o mouse
function pararDesenho() {
    if (desenhando) {
        desenhando = false;
        ctx.closePath();
    }
}

// Função para limpar o canvas
function limparCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// Exibe uma mensagem de confirmação ao clicar no botão "Confirmar"
document.getElementById('confirmButton').addEventListener('click', function () {
    console.log('Desenho confirmado!');
});

// Adiciona os eventos ao canvas
canvas.addEventListener('mousedown', iniciarDesenho);
canvas.addEventListener('mousemove', desenhar);
canvas.addEventListener('mouseup', pararDesenho);
canvas.addEventListener('mouseout', pararDesenho);
