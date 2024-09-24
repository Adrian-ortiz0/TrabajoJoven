const btnNoAceptoUsuario = document.getElementById("btnNoAceptoUsuario");
const btnAceptoUsuario = document.getElementById("btnAceptoUsuario");

btnNoAceptoUsuario.addEventListener("click", function () {
  window.location.href = "/templates/index.html";
});
btnAceptoUsuario.addEventListener("click", function () {
  window.location.href = "/templates/sub_pages/perfilUsuario.html";
});
