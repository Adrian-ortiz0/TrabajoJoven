document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("formularioUsuarios");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    if (validateForm()) {
      form.submit();
    }
  });

  function validateForm() {
    let isValid = true;
    const requiredInputs = form.querySelectorAll(
      "input[required], select[required]"
    );

    requiredInputs.forEach((input) => {
      if (!input.value.trim()) {
        isValid = false;
        input.classList.add("error");
      } else {
        input.classList.remove("error");
      }
    });

    if (!isValid) {
      alert("Por favor, llena todos los campos requeridos.");
    }

    return isValid;
  }
});
