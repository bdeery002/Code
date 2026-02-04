// ========================================
// CONCEPT 3: Form Handling with preventDefault()
// ========================================
// preventDefault() stops the default form submission behavior
// This prevents page reload and lets us handle data with JavaScript

export function initFormDemo() {
  const contactForm = document.getElementById("contact-form");
  const nameInput = document.getElementById("name-input");
  const emailInput = document.getElementById("email-input");
  const formResult = document.getElementById("form-result");

  if (!contactForm || !nameInput || !emailInput || !formResult) return;

  contactForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = nameInput.value;
    const email = emailInput.value;

    formResult.innerHTML = `
      <p style="color: green;">✓ Form submitted successfully!</p>
      <p>Name: ${name}</p>
      <p>Email: ${email}</p>
    `;

    contactForm.reset();
    console.log("Form data:", { name, email });
  });
}