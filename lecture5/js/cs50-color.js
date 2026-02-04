// CS50 color
export function initCS50ColorButtons() {
    // 1. SELECTORS: Grab the HTML elements.
  const button1 = document.getElementById("cs50button");
  const button2 = document.getElementById("cs50button2");
  const button3 = document.getElementById("cs50button3");

  // 2. GUARD CLAUSE: Stop if any element is missing.
  if (!button1 || !button2 || !button3) return;

  // 3. EVENT LISTENER: When the button is clicked, change the output text color.
  button1.addEventListener("click", () => {
    button1.style.color = "red";
    button1.textContent = "Clicked!";
    button1.style.fontWeight = "bold";
    button1.style.fontSize = "20px";
    button1.style.backgroundColor = "yellow";
  });
  button2.addEventListener("click", () => {
    button2.style.color = "blue";
  });
  button3.addEventListener("click", () => {
    button3.style.color = "green";
  });
}