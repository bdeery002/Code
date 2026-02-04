// ========================================
// CONCEPT 15: Scroll Events
// ========================================
// window.addEventListener("scroll", ...) - fires when user scrolls
// window.scrollY - current vertical scroll position
// window.scrollTo() - scroll to specific position

export function initScrollDemo() {
  const scrollStatus = document.getElementById("scroll-status");
  const scrollToTopBtn = document.getElementById("scroll-to-top-btn");
  const backToTopBtn = document.getElementById("back-to-top");

  // If the page doesn’t have these elements, skip.
  if (!scrollStatus || !scrollToTopBtn || !backToTopBtn) return;

  window.addEventListener("scroll", () => {
    const scrollPosition = window.scrollY;
    scrollStatus.textContent = `Scroll position: ${Math.round(scrollPosition)}px`;

    backToTopBtn.style.display = scrollPosition > 300 ? "block" : "none";

    const header = document.querySelector("h1");
    if (!header) return;

    if (scrollPosition > 100) {
      header.style.backgroundColor = "#4CAF50";
      header.style.color = "white";
      header.style.padding = "10px";
      header.style.borderRadius = "5px";
    } else {
      header.style.backgroundColor = "";
      header.style.color = "";
      header.style.padding = "";
    }
  });

  const scrollTop = () =>
    window.scrollTo({ top: 0, behavior: "smooth" });

  scrollToTopBtn.addEventListener("click", scrollTop);
  backToTopBtn.addEventListener("click", scrollTop);
}