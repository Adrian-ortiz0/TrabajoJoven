const btnEnviarEmpresaLogin = document.getElementById("btnEnviarEmpresaLogin");
btnEnviarEmpresaLogin.addEventListener("click", function () {
  window.location.href =
    "/templates/sub_pages/terminosCondicionesEmpresas.html";
});

const mainEmpresasRegister = document.getElementById("mainEmpresasRegister");
mainEmpresasRegister.addEventListener("click", function (event) {
  event.preventDefault();
});
