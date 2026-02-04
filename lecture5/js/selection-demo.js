// ========================================
// CONCEPT 1: querySelector() & querySelectorAll()
// ========================================
// querySelector - finds FIRST matching element
// querySelectorAll - finds ALL matching elements
// Use CSS selectors: ".class", "#id", "tag", "[attribute]"

// ========================================
// CONCEPT 2: getElementById()
// ========================================
// Fastest way to get a single element by its unique ID
// No # symbol needed (unlike querySelector)


export function initSelectionDemo() {
  const selectDemoBtn = document.querySelector("#select-demo-btn");
  const uniqueDiv = document.getElementById("unique-div");

  if (!selectDemoBtn) return;

  selectDemoBtn.addEventListener("click", () => {
    const firstPara = document.querySelector(".demo-text");
    if (firstPara) {
      firstPara.style.color = "red";
      firstPara.textContent = "I was selected first!";
    }

    const allParas = document.querySelectorAll(".demo-text");
    allParas.forEach((para, index) => {
      para.style.fontWeight = "bold";
      console.log(`Paragraph ${index + 1}: ${para.textContent}`);
    });

    if (uniqueDiv) {
      uniqueDiv.style.backgroundColor = "lightblue";
      uniqueDiv.textContent = "Found by ID!";
    }
  });
}