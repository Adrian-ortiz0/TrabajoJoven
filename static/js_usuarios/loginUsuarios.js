const btnEnviarUsuarioLogin = document.getElementById("btnEnviarUsuarioLogin");

btnEnviarUsuarioLogin.addEventListener("click", function () {
  window.location.href =
    "/terminos-condiciones";
});

const formularioUsuarios = document.getElementById("formularioUsuarios");
formularioUsuarios.addEventListener("click", function (e) {
  e.preventDefault();
});
