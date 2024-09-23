const btnNoAceptoUsuario = document.getElementById("btnNoAceptoUsuario");
const btnAceptoUsuario = document.getElementById("btnAceptoUsuario");

btnNoAceptoUsuario.addEventListener("click", function () {
  window.location.href = "/index.html";
});
btnAceptoUsuario.addEventListener("click", function () {
  window.location.href = "/sub_pages/perfilUsuario.html";
});
