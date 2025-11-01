document.addEventListener('DOMContentLoaded', () => {
    const btnAgronomo = document.getElementById('btnAgronomo');
    const btnProdutor = document.getElementById('btnProdutor');
    const tipoContaInput = document.getElementById('tipoConta');
    const campoCREA = document.getElementById('campoCREA');
    const form = document.getElementById('form-cadastro');
    const cpfInput = document.getElementById('cpf');
    const telefoneInput = document.getElementById('telefone');
    
    // Preloaderperdão, te mandei o errado
    window.addEventListener('load', () => {
        const preloader = document.getElementById('preloader');
        preloader.style.opacity = '0';
        setTimeout(() => {
            preloader.style.display = 'none';
        }, 500); // o mesmo tempo da transição do CSS
    });

    // Alternância de tipo de conta
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

    // Máscara de CPF
    cpfInput.addEventListener('input', (e) => {
        let v = e.target.value.replace(/\D/g, '');
        if (v.length > 11) v = v.slice(0, 11);
        v = v.replace(/^(\d{3})(\d)/, '$1.$2');
        v = v.replace(/^(\d{3})\.(\d{3})(\d)/, '$1.$2.$3');
        v = v.replace(/^(\d{3})\.(\d{3})\.(\d{3})(\d)/, '$1.$2.$3-$4');
        e.target.value = v;
    });

    // Máscara de telefone
    telefoneInput.addEventListener('input', (e) => {
        let v = e.target.value.replace(/\D/g, '');
        if (v.length > 11) v = v.slice(0, 11);
        v = v.replace(/^(\d{2})(\d)/, '($1) $2');
        v = v.replace(/^(\(\d{2}\) \d{5})(\d)/, '$1-$2');
        e.target.value = v;
    });

    // Limpeza de dados antes de enviar
    const limpar = (s) => s.replace(/\D/g, '');
    const limparEmail = (s) => s.trim().toLowerCase();

    // Validação e envio
    form.addEventListener('submit', (e) => {
        const tipo = tipoContaInput.value;
        const cpf = limpar(cpfInput.value);
        const telefone = limpar(telefoneInput.value);
        const email = limparEmail(document.getElementById('email').value);
        const senha = document.getElementById('senha').value;
        const confirmarSenha = document.getElementById('confirmarSenha').value;

        if (!tipo) { e.preventDefault(); alert('Selecione o tipo de conta'); return; }
        if (cpf.length !== 11) { e.preventDefault(); alert('CPF inválido'); return; }
        if (telefone && telefone.length < 10) { e.preventDefault(); alert('Telefone inválido'); return; }
        if (!email.includes('@') || !email.includes('.')) { e.preventDefault(); alert('E-mail inválido'); return; }
        if (senha.length < 6) { e.preventDefault(); alert('Senha deve ter no mínimo 6 caracteres'); return; }
        if (senha !== confirmarSenha) { e.preventDefault(); alert('As senhas não coincidem'); return; }

        // Atualiza valores limpos
        cpfInput.value = cpf;
        telefoneInput.value = telefone;
        document.getElementById('email').value = email;

        // Botão enviando
        const btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;
        btn.textContent = 'Enviando...';
    });


});