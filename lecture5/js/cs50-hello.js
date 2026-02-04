// CS50 hello

export function initCS50Hello() {
  // 1. SELECTORS: Grab the HTML elements.
  const display = document.getElementById("CS50-hello-display");
  const helloBtn = document.getElementById("CS50-hello-btn");
  const title = document.getElementById("CS50-title");

  // 2. GUARD CLAUSE: Stop if any element is missing.
  if (!display || !helloBtn || !title) return;

  // 3. HELPER FUNCTION: Toggle the title text.
  //"If the current (cleaned) title is '17: CS50 Hello', change it to 'Hello, CS50!'.Otherwise, set it back to '17: CS50 Hello'."

 function toggleTitle() {
  if (title.textContent.trim() === "17: CS50 Hello") {
    title.textContent = "Hello, CS50!";
  } else {
    title.textContent = "17: CS50 Hello";
  }
}

  // 4. EVENT LISTENER: When the button is clicked, toggle the title.
  helloBtn.addEventListener("click", () => {
    toggleTitle();
  });
}

