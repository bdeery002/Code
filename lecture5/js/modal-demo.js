// ========================================
// CONCEPT 9: Show/Hide Elements
// ========================================
// Common methods:
// - style.display = "none" / "block" (removes from layout)
// - style.visibility = "hidden" / "visible" (keeps space)
// - classList.toggle("hidden") (with CSS class)

export function initModalDemo() {
  const modal = document.getElementById("modal");
  const toggleModalBtn = document.getElementById("modal-toggle-btn");
  const closeModalBtn = document.getElementById("modal-close-btn");

  if (!modal || !toggleModalBtn || !closeModalBtn) return;

  toggleModalBtn.addEventListener("click", () => {
    modal.style.display = "block";
    console.log("Modal opened");
  });

  closeModalBtn.addEventListener("click", () => {
    modal.style.display = "none";
    console.log("Modal closed");
  });

  modal.addEventListener("click", (e) => {
    if (e.target === modal) modal.style.display = "none";
  });
}