document.addEventListener("DOMContentLoaded", () => {
    
  // Botão Adicionar Propriedade
  const btnAddProperty = document.getElementById("btn-add-property");
  if (btnAddProperty) {
    btnAddProperty.addEventListener("click", (e) => {
      e.preventDefault();
      alert("Aqui você poderá abrir um modal ou redirecionar para cadastro de propriedade.");
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
