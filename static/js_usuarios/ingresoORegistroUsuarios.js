const registerUsuarioBtn = document.getElementById("registerUsuarioBtn");
const loginUsuarioBtn = document.getElementById("loginUsuarioBtn");

registerUsuarioBtn.addEventListener("click", function () {
  window.location.href = "/templates/sub_pages/usuariosRegisterForm.html";
});

loginUsuarioBtn.addEventListener("click", function () {
  window.location.href = "/templates/sub_pages/usuariosLoginForm.html";
});
