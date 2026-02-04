// ========================================
// CONCEPT 5: classList Methods
// ========================================
// classList.add() - adds a class
// classList.remove() - removes a class
// classList.toggle() - adds if missing, removes if present
// classList.contains() - checks if class exists

export function initClassListDemo() {
  const box = document.getElementById("box");
  const addClassBtn = document.getElementById("add-class-btn");
  const removeClassBtn = document.getElementById("remove-class-btn");
  const toggleClassBtn = document.getElementById("toggle-class-btn");
  const classStatus = document.getElementById("class-status");

  if (!box || !addClassBtn || !removeClassBtn || !toggleClassBtn || !classStatus) return;

  const updateClassStatus = () => {
    const classes = box.className;
    classStatus.textContent = `Current classes: ${classes || "(none)"}`;
  };

  addClassBtn.addEventListener("click", () => {
    box.classList.add("highlight");
    updateClassStatus();
  });

  removeClassBtn.addEventListener("click", () => {
    box.classList.remove("highlight");
    updateClassStatus();
  });

  toggleClassBtn.addEventListener("click", () => {
    box.classList.toggle("active");
    updateClassStatus();
  });

  updateClassStatus();
}