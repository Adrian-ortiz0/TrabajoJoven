const loginUsuarioBtn = document.getElementById("loginUsuarioBtn");
const loginEmpresaBtn = document.getElementById("loginEmpresaBtn");

loginEmpresaBtn.addEventListener("click", function () {
  window.location.href = "/templates/sub_pages/ingresoORegistroEmpresas.html";
});

loginUsuarioBtn.addEventListener("click", function () {
  window.location.href = "/templates/sub_pages/ingresoORegistroUsuarios.html";
});
