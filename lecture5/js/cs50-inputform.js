// CS50 inputform

// CS50 inputform module
export function initCS50InputForm() {
    // 1. SELECTORS: Grab the HTML elements.
  const form = document.getElementById("CS50-form");
  const input = document.getElementById("CS50-form-input");
  const output = document.getElementById("CS50-form-output");

  // 2. GUARD CLAUSE: Stop if any element is missing.
  if (!form || !input || !output) return;

  // 3. EVENT LISTENER: When the form is submitted, show an alert.
  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    const name = input.value.trim();
    alert(`Hello, ${name}!`);
  });
}