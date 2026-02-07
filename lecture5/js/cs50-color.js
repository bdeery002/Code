// CS50 color
export function initCS50ColorButtons() {
    // 1. SELECTORS: Grab the HTML elements.
    const title = document.getElementById("cs50-button-title");
  const button1 = document.getElementById("cs50button1");
  const button2 = document.getElementById("cs50button2");
  const button3 = document.getElementById("cs50button3");

  // 2. GUARD CLAUSE: Stop if any element is missing.
  if (!button1 || !button2 || !button3) return;

  // 3. EVENT LISTENER: When the select changes, update button and title colors.
  document.querySelector('select').addEventListener('change', (event) => {
    const selectedColor = event.target.value;
    if (selectedColor) {
      title.style.color = selectedColor.toLowerCase();
      title.textContent = `Selected Color: ${selectedColor}`;
    }
  })

  // 3. EVENT LISTENER: When the button is clicked, change the output text color.
  button1.addEventListener("click", () => {
    button1.style.color = "red";
    button1.textContent = "Clicked!";
    button1.style.fontWeight = "bold";
    button1.style.fontSize = "20px";
    button1.style.backgroundColor = "yellow";
    title.style.color = "red";
  });
  button2.addEventListener("click", () => {
    button2.style.color = "blue";
    title.style.color = "blue";
  });
  button3.addEventListener("click", () => {
    button3.style.color = "green";
    button3.style.fontWeight = "bold";
    button3.style.fontSize = "20px";
    button3.style.backgroundColor = "lightgreen";
    button3.style.border = "2px solid green";
    button3.style.borderRadius = "5px";
    title.style.color = "green";
    title.style.fontStyle = "italic";
    title.style.textDecoration = "underline";
    title.style.fontSize = "24px";
    title.style.backgroundColor = "lightgray";
    title.style.padding = "10px";
    title.style.borderRadius = "5px";
    title.style.border = "2px solid green";
    title.style.boxShadow = "2px 2px 5px rgba(0, 128, 0, 0.5)";
    title.style.transition = "all 0.3s ease";
  });
}