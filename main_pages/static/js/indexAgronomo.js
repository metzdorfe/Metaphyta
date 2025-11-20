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

  // Sidebar Interatividade
  const navLinks = document.querySelectorAll(".nav-link");
  navLinks.forEach(link => {
    link.addEventListener("click", () => {
      navLinks.forEach(l => l.classList.remove("active"));
      link.classList.add("active");
    });
  });
});