function initCS50officialCounter() {
  console.log("✅ CS50 Official Counter module loaded");

  // The "Model": This holds the state of our counter.
  let counter = 5;

 // 1. SELECTORS: Grab the HTML elements.
  const display = document.getElementById("CS50-officialcounter-display");
  const counterincrBtn = document.getElementById("CS50-officialcounterincr-btn");
  const counterdecrBtn = document.getElementById("CS50-officialcounterdecr-btn");
  const title = document.getElementById("CS50-officialcounter-title");
  
   // 2. GUARD CLAUSE: Stop if any element is missing.
    if (!display || !counterincrBtn || !counterdecrBtn || !title) return;

    // 3. UPDATE DISPLAY: Show the current counter value.
    function updateDisplay() {
      display.textContent = `Count: ${counter}`;
    }

    // 4. EVENT HANDLER: Increment the counter when button is clicked.
    counterincrBtn.addEventListener("click", function() {
      counter++;
      updateDisplay();
    });

    //5. EVENT HANDLER: Decrement the counter when button is clicked.
    if (counterdecrBtn) {
      counterdecrBtn.addEventListener("click", function() {
        counter--;
        updateDisplay();
      });
    }

    // 6. INITIALIZE DISPLAY: Show the initial value.
    updateDisplay();
  
}

// Export the module
export { initCS50officialCounter };
