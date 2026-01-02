
// Utility: set current year in footer
document.addEventListener("DOMContentLoaded", () => {
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});

// Greeting banner (Bootstrap alert) — dynamic per time of day
document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("greeting");
  if (!container) return;

  const hour = new Date().getHours();
  const timeOfDay = hour < 12 ? "morning" : hour < 18 ? "afternoon" : "evening";
  container.innerHTML = `
    <div class="alert alert-info alert-dismissible fade show" role="alert">
      Good ${timeOfDay}! Welcome to my homepage 👋
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>`;
});

// Theme toggle (light/dark) using Bootstrap 5 data-bs-theme + localStorage
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("themeToggle");
  const root = document.documentElement;

  // Load saved theme
  const saved = localStorage.getItem("theme");
  if (saved === "dark") {
    root.setAttribute("data-bs-theme", "dark");
    if (btn) btn.textContent = "🌙 Dark";
  }

  if (!btn) return;
  btn.addEventListener("click", () => {
    const isDark = root.getAttribute("data-bs-theme") === "dark";
    root.setAttribute("data-bs-theme", isDark ? "light" : "dark");
    localStorage.setItem("theme", isDark ? "light" : "dark");
    btn.textContent = isDark ? "🌞 Light" : "🌙 Dark";
  });
});

// Rotating motivational quotes
document.addEventListener("DOMContentLoaded", () => {
  const quotes = [
    "A person who never made a mistake never tried anything new.",
    "Success consists of going from failure to failure without loss of enthusiasm.",
    "Ever tried. Ever failed. No matter. Try Again. Fail again. Fail better.",
    "The only time you mustn't fail is the last time you try.."
  ];
  const el = document.getElementById("quote");
  if (!el) return;

  let i = 0;
  el.textContent = quotes[i];
  setInterval(() => {
    i = (i + 1) % quotes.length;
    el.textContent = quotes[i];
  }, 6000);
});

// Back-to-top visibility + behavior
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("backToTop");
  if (!btn) return;

  window.addEventListener("scroll", () => {
    const y = window.scrollY || document.documentElement.scrollTop;
    btn.style.display = y > 300 ? "block" : "none";
  });

  btn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
});

// Contact form validation (client-side)
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("contactForm");
  const success = document.getElementById("formSuccess");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = document.getElementById("name");
    const email = document.getElementById("email");
    const message = document.getElementById("message");

    // Simple validators
    const validName = name.value.trim().length > 0;
    const validEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value);
    const validMsg = message.value.trim().length > 0;

    // Toggle Bootstrap invalid styles
    [name, email, message].forEach((field) => {
      const ok =
        field === name ? validName : field === email ? validEmail : field === message ? validMsg : false;
      field.classList.toggle("is-invalid", !ok);
      field.classList.toggle("is-valid", ok);
    });

    if (validName && validEmail && validMsg) {
      // Demo "success"
      success?.classList.remove("d-none");
      form.reset();
      [name, email, message].forEach((f) => f.classList.remove("is-valid"));
    }
  });
});
