document.addEventListener('DOMContentLoaded', () => {
    const cpfInput = document.getElementById('cpf');
    const btnCadastrar = document.getElementById('btnCadastrar');

    // Máscara de CPF
    cpfInput.addEventListener('input', (e) => {
        let value = e.target.value.replace(/\D/g, ""); // remove tudo que não é número
        if (value.length > 3 && value.length <= 6) value = value.replace(/^(\d{3})(\d+)/, "$1.$2");
        else if (value.length > 6 && value.length <= 9) value = value.replace(/^(\d{3})(\d{3})(\d+)/, "$1.$2.$3");
        else if (value.length > 9) value = value.replace(/^(\d{3})(\d{3})(\d{3})(\d+)/, "$1.$2.$3-$4");
        e.target.value = value.substring(0, 14);
    });

    // Botão de cadastro redireciona
    btnCadastrar.addEventListener('click', () => {
        window.location.href = "/cadastro/";
    });
});