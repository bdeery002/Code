// ========================================
// CONCEPT 14: setTimeout & setInterval
// ========================================
// setTimeout(function, milliseconds) - runs once after delay
// setInterval(function, milliseconds) - runs repeatedly
// clearTimeout() / clearInterval() - stops timers

export function initTimersDemo() {
  const timeoutBtn = document.getElementById("timeout-btn");
  const startCounterBtn = document.getElementById("start-counter-btn");
  const stopCounterBtn = document.getElementById("stop-counter-btn");
  const counterDisplay = document.getElementById("counter-display");

  if (!timeoutBtn || !startCounterBtn || !stopCounterBtn || !counterDisplay) return;

  let counterValue = 0;
  let intervalId = null;

  timeoutBtn.addEventListener("click", () => {
    timeoutBtn.textContent = "Alert coming in 3 seconds...";
    timeoutBtn.disabled = true;

    setTimeout(() => {
      alert("3 seconds have passed!");
      timeoutBtn.textContent = "Show Alert in 3 Seconds";
      timeoutBtn.disabled = false;
    }, 3000);
  });

  startCounterBtn.addEventListener("click", () => {
    if (intervalId !== null) return;

    counterValue = 0;
    counterDisplay.textContent = `Counter: ${counterValue}`;

    intervalId = setInterval(() => {
      counterValue++;
      counterDisplay.textContent = `Counter: ${counterValue}`;
    }, 1000);
  });

  stopCounterBtn.addEventListener("click", () => {
    if (intervalId !== null) {
      clearInterval(intervalId);
      intervalId = null;
    }
  });
}