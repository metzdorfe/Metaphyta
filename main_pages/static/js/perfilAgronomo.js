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
    if (!data.includes("-")) return data;

    const partes = data.split("-");
    return `${partes[2]}/${partes[1]}/${partes[0]}`;
}

document.addEventListener("DOMContentLoaded", () => {
    const cpfCampo = document.getElementById("view-cpf");
    const telCampo = document.getElementById("view-telefone");
    const dataCampo = document.getElementById("view-dataNascimento");

    if (cpfCampo) cpfCampo.textContent = formatarCPF(cpfCampo.textContent.trim());
    if (telCampo) telCampo.textContent = formatarTelefone(telCampo.textContent.trim());
    if (dataCampo) dataCampo.textContent = formatarData(dataCampo.textContent.trim());
});

document.addEventListener("input", (e) => {
    const input = e.target;

    if (input.id === "cpf") {
        input.value = formatarCPF(input.value);
    }

    if (input.id === "telefone") {
        input.value = formatarTelefone(input.value);
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const btnEdit = document.getElementById("btn-edit");
    const btnCancel = document.getElementById("btn-cancel");

    const viewMode = document.getElementById("view-mode");
    const editMode = document.getElementById("edit-mode");

    if (btnEdit) {
        btnEdit.addEventListener("click", () => {
            viewMode.style.display = "none";
            editMode.style.display = "block";
        });
    }

    if (btnCancel) {
        btnCancel.addEventListener("click", () => {
            editMode.style.display = "none";
            viewMode.style.display = "block";
        });
    }
});
