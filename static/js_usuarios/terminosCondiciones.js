const btnNoAceptoUsuario = document.getElementById("btnNoAceptoUsuario");
const btnAceptoUsuario = document.getElementById("btnAceptoUsuario");

btnNoAceptoUsuario.addEventListener("click", function () {
  window.location.href = "/";
});
btnAceptoUsuario.addEventListener("click", function () {
  window.location.href = "/perfil-usuario";
});
