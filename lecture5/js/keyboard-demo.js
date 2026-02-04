// ========================================
// CONCEPT 11: Keyboard Events
// ========================================
// keydown - fires when key is pressed down
// keyup - fires when key is released
// key property - tells you which key was pressed

export function initKeyboardDemo() {
  const keyboardInput = document.getElementById("keyboard-input");
  const keyDisplay = document.getElementById("key-display");
  const modal = document.getElementById("modal");

  if (!keyboardInput || !keyDisplay) return;

  keyboardInput.addEventListener("keydown", (e) => {
    keyDisplay.innerHTML = `
      <p>Key pressed: <strong>${e.key}</strong></p>
      <p>Key code: ${e.code}</p>
    `;

    if (e.key === "Enter") {
      keyDisplay.innerHTML += `<p style="color: green;">Enter key detected! Form would submit.</p>`;
    } else if (e.key === "Escape") {
      keyDisplay.innerHTML += `<p style="color: orange;">Escape pressed! Modal would close.</p>`;
      keyboardInput.value = "";
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "h" || e.key === "H") {
      console.log("Global shortcut 'H' pressed!");
      alert("You pressed 'H' - this works anywhere on the page!");
    }
    if (e.key === "Escape" && modal) {
      modal.style.display = "none";
    }
  });
}