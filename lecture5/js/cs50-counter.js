// CS50 counter

// CS50 counter module
export function initCS50Counter() {
  // 1. STATE: This variable lives in memory and tracks the current number.
  let counter = 0;

  // 2. SELECTORS: We grab the HTML elements so JS can "talk" to them.
  const display = document.getElementById("CS50-counter-display");
  const increaseCountBtn = document.querySelector("#Increase-count-btn");
  const decreaseCountBtn = document.querySelector("#Decrease-count-btn");
  const resetCountBtn = document.querySelector("#Reset-count-btn");
  const title = document.querySelector("#counter-title");

  // 3. GUARD CLAUSE: If any element is missing from the HTML, stop immediately.
  // This prevents the "Cannot read property of null" error.
  if (!display || !increaseCountBtn || !decreaseCountBtn || !resetCountBtn || !title) return;

  // 4. HELPER FUNCTIONS: Small, reusable "recipes" for specific tasks.

  // Updates the text on the screen to match the current 'counter' variable.
  function render() {
    display.textContent = "Count: " + counter;
  }

  // Logic to show an alert only on multiples of 10 (except 0).
  function maybeAlert() {
    if (counter !== 0 && counter % 10 === 0) {
      alert(`Count is now ${counter}`);
    }
  }

  // The "Toggle": Flips the title text back and forth.
  // We wrap this in a function so we can run it every time a button is clicked.
  function toggleTitle() {
    title.textContent = (title.textContent.trim() === "Counter") ? "Brendan Deery" : "Counter";
  }

  // The "Orchestrator": This coordinates all the changes at once.
  function applyChange(delta) {
    counter += delta; // Update the math (state)
    render();        // Update the screen (UI)
    toggleTitle();   // Flip the title (UI)
    maybeAlert();    // Check for alerts (Logic)
  }

  // 5. EVENT LISTENERS: This connects the "Logic" to the "User Interface."
  
  // When 'Increase' is clicked, run applyChange with a +1
  increaseCountBtn.addEventListener("click", () => applyChange(+1));

  // When 'Decrease' is clicked, run applyChange with a -1
  decreaseCountBtn.addEventListener("click", () => applyChange(-1));

  // Reset is handled slightly differently—it just sets counter to 0 and renders.
  resetCountBtn.addEventListener("click", () => {
    counter = 0;
    render();
  });

  // 6. INITIALIZATION: Run render once immediately so the page doesn't look empty.
  render(); 
}