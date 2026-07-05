document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const button = form.querySelector("button[type='submit']");

    form.addEventListener("submit", () => {

        button.disabled = true;

        button.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2"></span>
            Predicting...
        `;

    });

    const inputs = document.querySelectorAll("input[type='number']");

    inputs.forEach(input => {

        input.addEventListener("input", () => {

            if (input.value < 0) {
                input.value = 0;
            }

        });

    });

});