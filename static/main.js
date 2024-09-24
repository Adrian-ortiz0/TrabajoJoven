const loginUsuarioBtn = document.getElementById("loginUsuarioBtn");
const loginEmpresaBtn = document.getElementById("loginEmpresaBtn");

loginEmpresaBtn.addEventListener("click", function () {
  window.location.href = "/empresas";
});

loginUsuarioBtn.addEventListener("click", function () {
  window.location.href = "/usuarios";
});
