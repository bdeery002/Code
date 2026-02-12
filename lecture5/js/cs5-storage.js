export function initcs50storage() {
  console.log("Initializing CS50 Storage Demo...");

  // Ensure counter exists
  if (!localStorage.getItem("counter")) {
    localStorage.setItem("counter", "0");
  }

  const title = document.querySelector("#cs50-local-storage-title");
  const btn = document.querySelector("#cs50-local-storage-btn");

  if (!title || !btn) return;

  function render() {
    const counter = Number(localStorage.getItem("counter")) || 0;
    title.textContent = `22: CS50 Local Storage (${counter})`;
  }

  function count() {
    const counter = (Number(localStorage.getItem("counter")) || 0) + 1;
    localStorage.setItem("counter", String(counter));
    render();
  }

  btn.addEventListener("click", count);

  render();

  // 10ms is extremely fast; use 1000ms if you want "once per second"
  setInterval(count, 1000);
}
