const loginUsuarioBtn = document.getElementById("loginUsuarioBtn");
const loginEmpresaBtn = document.getElementById("loginEmpresaBtn");

loginEmpresaBtn.addEventListener("click", function(){
    window.location.href = "/sub_pages/empresas.html";
});

loginUsuarioBtn.addEventListener("click", function(){
    window.location.href = "/sub_pages/usuarios.html";
});
