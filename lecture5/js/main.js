// In short: main.js acts as the central control tower for your web application.
//Instead of writing all the logic in one massive, messy file, this script organizes your project by importing specialized "toolkits" (modules) and turning them on only when the page is fully ready.

//Key Responsibilities
//1) Module Orchestration: It uses the import statements at the top to bring in 
//specific functions (like initTodoDemo or initFetchDemo) from other JavaScript files. This keeps the codebase modular and easy to debug.

//2) Wait for the DOM: The window.addEventListener("DOMContentLoaded", ...) ensures that the script doesn't try to interact with buttons, forms, or inputs before the browser has finished building the HTML structure.

//3) Batch Initialization: Once the page is ready, it runs every "init" function in sequence. This essentially "wires up" the interactivity for every section of your site—from the To-Do list to the modal windows.

//4) Confirmation: It logs a success message to the console (✅ All concept modules initialized) to let you know that every feature was loaded without crashing the script.

//Why use this pattern?
//If you had all the code for a To-Do list, a timer, and a modal in one file, finding a bug would be a nightmare. By using main.js as a simple "switcher," you ensure:

//Readability: You can see every feature the site has just by looking at this one file.

//Organization: Each feature lives in its own file (e.g., todo-demo.js).

//Safety: Nothing runs until the HTML is fully loaded, preventing "undefined" errors.


import { initSelectionDemo } from "./selection-demo.js";
import { initFormDemo } from "./form-demo.js";
import { initInputDemo } from "./input-demo.js";
import { initClassListDemo } from "./classlist-demo.js";
import { initTodoDemo } from "./todo-demo.js";
import { initModalDemo } from "./modal-demo.js";
import { initDatasetDemo } from "./dataset-demo.js";
import { initKeyboardDemo } from "./keyboard-demo.js";
import { initFetchDemo } from "./fetch-demo.js";
import { initStorageDemo } from "./storage-demo.js";
import { initTimersDemo } from "./timers-demo.js";
import { initScrollDemo } from "./scroll-demo.js";
import { initCS50Counter } from "./cs50-counter.js";
import { initCS50Hello } from "./cs50-hello.js";
import { initCS50officialCounter } from "./cs50-officialcounter.js";
import { initCS50InputForm } from "./cs50-inputform.js";
import { initCS50ColorButtons } from "./cs50-color.js"; 

// Wait until the HTML document is fully loaded

window.addEventListener("DOMContentLoaded", () => {
  initSelectionDemo();
  initFormDemo();
  initInputDemo();
  initClassListDemo();
  initTodoDemo();
  initModalDemo();
  initDatasetDemo();
  initKeyboardDemo();
  initFetchDemo();
  initStorageDemo();
  initTimersDemo();
  initScrollDemo();
  initCS50Counter();
  initCS50Hello();
  initCS50officialCounter();
  initCS50InputForm();
  initCS50ColorButtons();

  console.log("✅ All concept modules initialized");
});