// Botões de tipo de conta
const btnAgronomo = document.getElementById('btnAgronomo');
const btnProdutor = document.getElementById('btnProdutor');
const tipoContaInput = document.getElementById('tipoConta');
const campoCREA = document.getElementById('campoCREA');

btnAgronomo.addEventListener('click', () => {
    tipoContaInput.value = 'Agronomo';
    btnAgronomo.classList.add('selected');
    btnProdutor.classList.remove('selected');
    campoCREA.style.display = 'block';
});

btnProdutor.addEventListener('click', () => {
    tipoContaInput.value = 'Produtor';
    btnProdutor.classList.add('selected');
    btnAgronomo.classList.remove('selected');
    campoCREA.style.display = 'none';
});

window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    preloader.style.opacity = '0';
    setTimeout(() => {
        preloader.style.display = 'none';
    }, 500); // tempo igual ao transition do CSS
});

