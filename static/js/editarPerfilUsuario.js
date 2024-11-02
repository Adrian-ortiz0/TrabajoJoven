// Manejar el botón de cambiar foto
document
  .getElementById("btnCambiarFoto")
  .addEventListener("click", function () {
    document.getElementById("inputFotoPerfil").click();
  });

// Manejar la selección de archivo
document
  .getElementById("inputFotoPerfil")
  .addEventListener("change", function () {
    if (this.files && this.files[0]) {
      document.getElementById("formFotoPerfil").submit();
    }
  });
// También permitir hacer clic en la foto para cambiarla
document
  .querySelector(".foto-perfil-container")
  .addEventListener("click", function () {
    document.getElementById("inputFotoPerfil").click();
  });
