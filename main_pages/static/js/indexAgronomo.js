document.addEventListener("DOMContentLoaded", () => {

  // Notificações Dinâmicas
  const containerNotificacoes = document.getElementById("containerNotificacoes");

  // Checa se há notificações
  if (containerNotificacoes.children.length === 0) {
    const msg = document.createElement("div");
    msg.classList.add("notification-card");
    msg.innerHTML = "<p>Tudo tranquilo, sem notificações novas.</p>";
    containerNotificacoes.appendChild(msg);
  }

  // Botão Adicionar Cliente
  const btnAddClient = document.getElementById("btn-add-client");
  if (btnAddClient) {
    btnAddClient.addEventListener("click", (e) => {
      e.preventDefault();
      alert("Aqui você poderá abrir um modal ou redirecionar para cadastro de cliente.");
      // Exemplo: window.location.href = "/novo_cliente/";
    });
  }

  // Sidebar Interatividade
  const navLinks = document.querySelectorAll(".nav-link");
  navLinks.forEach(link => {
    link.addEventListener("click", () => {
      navLinks.forEach(l => l.classList.remove("active"));
      link.classList.add("active");
    });
  });
});