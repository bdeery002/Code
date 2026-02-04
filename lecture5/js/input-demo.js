// ========================================
// CONCEPT 4: Getting/Setting Input Values
// ========================================
// .value property gets or sets what's in an input field
// Common for text inputs, textareas, select dropdowns

export function initInputDemo() {
  const usernameInput = document.getElementById("username-input");
  const usernameFeedback = document.getElementById("username-feedback");
  const passwordInput = document.getElementById("password-input");
  const showValuesBtn = document.getElementById("show-values-btn");
  const valuesOutput = document.getElementById("values-output");

  if (!usernameInput || !usernameFeedback || !passwordInput || !showValuesBtn || !valuesOutput) return;

  usernameInput.addEventListener("input", () => {
    const value = usernameInput.value;

    if (value.length === 0) {
      usernameFeedback.textContent = "";
      usernameInput.style.borderColor = "";
    } else if (value.length < 3) {
      usernameFeedback.textContent = "❌ Too short (min 3 characters)";
      usernameFeedback.style.color = "red";
      usernameInput.style.borderColor = "red";
    } else {
      usernameFeedback.textContent = "✓ Looks good!";
      usernameFeedback.style.color = "green";
      usernameInput.style.borderColor = "green";
    }
  });

  showValuesBtn.addEventListener("click", () => {
    const username = usernameInput.value;
    const password = passwordInput.value;

    valuesOutput.innerHTML = `
      <p>Username: ${username || "(empty)"}</p>
      <p>Password: ${password ? "•".repeat(password.length) : "(empty)"}</p>
    `;
  });
}