const btnEnviarUsuarioLogin = document.getElementById("btnEnviarUsuarioLogin");

btnEnviarUsuarioLogin.addEventListener("click", function () {
  window.location.href =
    "/templates/sub_pages/terminosCondicionesUsuarios.html";
});

const formularioUsuarios = document.getElementById("formularioUsuarios");
formularioUsuarios.addEventListener("click", async function (event) {
  event.preventDefault();
});
