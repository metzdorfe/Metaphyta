function formatarCPF(cpf) {
    cpf = cpf.replace(/\D/g, "");
    if (cpf.length !== 11) return cpf;
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
}

function formatarTelefone(tel) {
    tel = tel.replace(/\D/g, "");
    if (tel.length === 11) {
        return tel.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
    }
    if (tel.length === 10) {
        return tel.replace(/(\d{2})(\d{4})(\d{4})/, "($1) $2-$3");
    }
    return tel;
}

function formatarData(data) {
    if (data.includes("/")) return data; // já está formatada
    if (!data.includes("-")) return data;

    const [ano, mes, dia] = data.split("-");
    return `${dia}/${mes}/${ano}`;
}

document.addEventListener("DOMContentLoaded", () => {

    const campos = document.querySelectorAll(".details-grid p");

    campos.forEach((campo) => {
        const label = campo.previousElementSibling?.innerText?.trim();

        if (!label) return;

        let valor = campo.textContent.trim();

        if (label === "CPF:") {
            campo.textContent = formatarCPF(valor);
        }

        if (label === "Telefone:") {
            campo.textContent = formatarTelefone(valor);
        }

        if (label === "Data de Nascimento:") {
            campo.textContent = formatarData(valor);
        }
    });

});
