document.addEventListener("DOMContentLoaded", function () {
  const logoutButton = document.getElementById("logoutButtonJovenes");
  const overlay = document.getElementById("overlay");
  const confirmLogout = document.getElementById("confirmLogout");
  const cancelLogout = document.getElementById("cancelLogout");

  logoutButton.addEventListener("click", (event) => {
    event.preventDefault();
    overlay.style.display = "flex";
  });

  cancelLogout.addEventListener("click", () => {
    overlay.style.display = "none";
  });
});

document
  .getElementById("ajustesUsuarioBtn")
  .addEventListener("click", function () {
    const menu = document.getElementById("ajustesMenu");

    if (menu.style.display === "block") {
      menu.style.display = "none";
    } else {
      menu.style.display = "block";
    }
  });

window.addEventListener("click", function (event) {
  const menu = document.getElementById("ajustesMenu");
  const button = document.getElementById("ajustesUsuarioBtn");

  if (!button.contains(event.target) && !menu.contains(event.target)) {
    menu.style.display = "none";
  }
});

function mostrarFoto(event) {
    const input = event.target;
    const file = input.files[0];
    const img = document.getElementById('fotoPerfil');

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            img.src = e.target.result;
        }
        reader.readAsDataURL(file); // Lee el archivo como URL de datos
    }
}

document.getElementById('nombrePerfil').addEventListener('input', function() {
    const nombreMostrado = document.getElementById('nombreMostrado');
    nombreMostrado.textContent = `Nombre: ${this.value}`; // Actualiza el nombre mostrado
});