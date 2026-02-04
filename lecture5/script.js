// ========================================
// 15 ESSENTIAL JAVASCRIPT CONCEPTS
// ========================================
// This file demonstrates the most important JavaScript techniques
// you'll need for building real websites
// ========================================

// ========================================
// CONCEPT 1: querySelector() & querySelectorAll()
// ========================================
// querySelector - finds FIRST matching element
// querySelectorAll - finds ALL matching elements
// Use CSS selectors: ".class", "#id", "tag", "[attribute]"

const selectDemoBtn = document.querySelector("#select-demo-btn");

selectDemoBtn.addEventListener("click", () => {
    // Get first paragraph with class "demo-text"
   
    const firstPara = document.querySelector(".demo-text");
     // .querySelector() is a method ⬆️ METHOD (has parentheses)
    firstPara.style.color = "red";
    // .style.color is property  ⬆️ PROPERTY (no parentheses)

    firstPara.textContent = "I was selected first!";
    
    // Get ALL paragraphs with class "demo-text"
    const allParas = document.querySelectorAll(".demo-text");
    allParas.forEach((para, index) => {
        para.style.fontWeight = "bold";
        console.log(`Paragraph ${index + 1}: ${para.textContent}`);
    });
});

// ========================================
// CONCEPT 2: getElementById()
// ========================================
// Fastest way to get a single element by its unique ID
// No # symbol needed (unlike querySelector)

const uniqueDiv = document.getElementById("unique-div");
selectDemoBtn.addEventListener("click", () => {
    uniqueDiv.style.backgroundColor = "lightblue";
    uniqueDiv.textContent = "Found by ID!";
});

// ========================================
// CONCEPT 3: Form Handling with preventDefault()
// ========================================
// preventDefault() stops the default form submission behavior
// This prevents page reload and lets us handle data with JavaScript

const contactForm = document.getElementById("contact-form");
const nameInput = document.getElementById("name-input");
const emailInput = document.getElementById("email-input");
const formResult = document.getElementById("form-result");

contactForm.addEventListener("submit", (e) => {
    // ⭐ CRITICAL: Prevent page from refreshing
    e.preventDefault();
    
    // Get the values from form inputs
    const name = nameInput.value;
    const email = emailInput.value;
    
    // Display the submitted data
    formResult.innerHTML = `
        <p style="color: green;">✓ Form submitted successfully!</p>
        <p>Name: ${name}</p>
        <p>Email: ${email}</p>
    `;
    
    // Clear the form after submission
    contactForm.reset();
    
    console.log("Form data:", { name, email });
});

// ========================================
// CONCEPT 4: Getting/Setting Input Values
// ========================================
// .value property gets or sets what's in an input field
// Common for text inputs, textareas, select dropdowns

const usernameInput = document.getElementById("username-input");
const usernameFeedback = document.getElementById("username-feedback");
const passwordInput = document.getElementById("password-input");
const showValuesBtn = document.getElementById("show-values-btn");
const valuesOutput = document.getElementById("values-output");

// Real-time validation as user types
usernameInput.addEventListener("input", () => {
    const value = usernameInput.value; // Get current input value
    
    if (value.length === 0) {
        usernameFeedback.textContent = "";
        usernameInput.style.borderColor = "";
    } else if (value.length < 3) {
        usernameFeedback.textContent = "❌ Too short (min 3 characters)";
        usernameFeedback.style.color = "red";
        usernameInput.style.borderColor = "red";
    } else {
        usernameFeedback.textContent = "✓ Looks good!";
        usernameFeedback.style.color = "green";
        usernameInput.style.borderColor = "green";
    }
});

// Display all input values when button is clicked
showValuesBtn.addEventListener("click", () => {
    const username = usernameInput.value;
    const password = passwordInput.value;
    
    valuesOutput.innerHTML = `
        <p>Username: ${username || '(empty)'}</p>
        <p>Password: ${password ? '•'.repeat(password.length) : '(empty)'}</p>
    `;
});

// ========================================
// CONCEPT 5: classList Methods
// ========================================
// classList.add() - adds a class
// classList.remove() - removes a class
// classList.toggle() - adds if missing, removes if present
// classList.contains() - checks if class exists

const box = document.getElementById("box");
const addClassBtn = document.getElementById("add-class-btn");
const removeClassBtn = document.getElementById("remove-class-btn");
const toggleClassBtn = document.getElementById("toggle-class-btn");
const classStatus = document.getElementById("class-status");

// Function to update class status display
const updateClassStatus = () => {
    const classes = box.className;
    classStatus.textContent = `Current classes: ${classes || '(none)'}`;
};

addClassBtn.addEventListener("click", () => {
    box.classList.add("highlight"); // Add highlight class
    updateClassStatus();
});

removeClassBtn.addEventListener("click", () => {
    box.classList.remove("highlight"); // Remove highlight class
    updateClassStatus();
});

toggleClassBtn.addEventListener("click", () => {
    // Toggle - add if missing, remove if present
    box.classList.toggle("active");
    updateClassStatus();
});

// Initialize status
updateClassStatus();

// ========================================
// CONCEPT 6 & 7: createElement() & appendChild()
// ========================================
// createElement() - creates new HTML element in memory
// appendChild() - adds element to the page (makes it visible)

const todoInput = document.getElementById("todo-input");
const addTodoBtn = document.getElementById("add-todo-btn");
const todoList = document.getElementById("todo-list");

addTodoBtn.addEventListener("click", () => {
    const todoText = todoInput.value.trim();
    
    // Validate input
    if (todoText === "") {
        alert("Please enter a todo item!");
        return;
    }
    
    // Create new list item
    const li = document.createElement("li");
    li.className = "todo-item";
    
    // Create text span
    const span = document.createElement("span");
    span.textContent = todoText;
    
    // Create delete button
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.className = "delete-btn";
    
    // Append elements: span and button go inside li
    li.appendChild(span);
    li.appendChild(deleteBtn);
    
    // Append li to the ul list (makes it visible)
    todoList.appendChild(li);
    
    // Clear input field
    todoInput.value = "";
    
    console.log(`Added todo: ${todoText}`);
});

// Allow pressing Enter to add todo
todoInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        addTodoBtn.click();
    }
});

// ========================================
// CONCEPT 8: Removing Elements & Event Delegation
// ========================================
// element.remove() - removes element from DOM
// Event delegation - attach listener to parent, check what was clicked
// More efficient than adding listeners to every child element

// Event delegation on the todo list
todoList.addEventListener("click", (e) => {
    // Check if clicked element is a delete button
    if (e.target.classList.contains("delete-btn")) {
        // Remove the parent li element
        const todoItem = e.target.parentElement;
        todoItem.remove();
        console.log("Todo item deleted");
    }
});

// ========================================
// CONCEPT 9: Show/Hide Elements
// ========================================
// Common methods:
// - style.display = "none" / "block" (removes from layout)
// - style.visibility = "hidden" / "visible" (keeps space)
// - classList.toggle("hidden") (with CSS class)

const modal = document.getElementById("modal");
const toggleModalBtn = document.getElementById("toggle-modal-btn");
const closeModalBtn = document.getElementById("close-modal-btn");

// Open modal
toggleModalBtn.addEventListener("click", () => {
    modal.style.display = "block"; // Show modal
    console.log("Modal opened");
});

// Close modal (button)
closeModalBtn.addEventListener("click", () => {
    modal.style.display = "none"; // Hide modal
    console.log("Modal closed");
});

// Close modal when clicking outside content
modal.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.style.display = "none";
    }
});

// ========================================
// CONCEPT 10: Data Attributes (dataset)
// ========================================
// data-* attributes store custom data in HTML
// Access via element.dataset.attributeName
// Useful for storing IDs, settings, metadata

const productButtons = document.querySelectorAll(".product-btn");
const productInfo = document.getElementById("product-info");

productButtons.forEach(button => {
    button.addEventListener("click", () => {
        // Access data attributes using dataset
        const productId = button.dataset.productId;
        const productName = button.dataset.productName;
        const price = button.dataset.price;
        
        // Display product information
        productInfo.innerHTML = `
            <div style="padding: 10px; background: #e8f5e9; border-radius: 5px; margin-top: 10px;">
                <h4>Product Details:</h4>
                <p><strong>ID:</strong> ${productId}</p>
                <p><strong>Name:</strong> ${productName}</p>
                <p><strong>Price:</strong> $${price}</p>
            </div>
        `;
        
        console.log("Product data:", { productId, productName, price });
    });
});

// ========================================
// CONCEPT 11: Keyboard Events
// ========================================
// keydown - fires when key is pressed down
// keyup - fires when key is released
// key property - tells you which key was pressed

const keyboardInput = document.getElementById("keyboard-input");
const keyDisplay = document.getElementById("key-display");

// Listen for keys in specific input
keyboardInput.addEventListener("keydown", (e) => {
    keyDisplay.innerHTML = `
        <p>Key pressed: <strong>${e.key}</strong></p>
        <p>Key code: ${e.code}</p>
    `;
    
    // Special key handling
    if (e.key === "Enter") {
        keyDisplay.innerHTML += `<p style="color: green;">Enter key detected! Form would submit.</p>`;
    } else if (e.key === "Escape") {
        keyDisplay.innerHTML += `<p style="color: orange;">Escape pressed! Modal would close.</p>`;
        keyboardInput.value = "";
    }
});

// Global keyboard shortcuts (work anywhere on page)
document.addEventListener("keydown", (e) => {
    // Press 'h' to trigger action
    if (e.key === "h" || e.key === "H") {
        console.log("Global shortcut 'H' pressed!");
        alert("You pressed 'H' - this works anywhere on the page!");
    }
    
    // Press Escape to close modal
    if (e.key === "Escape") {
        modal.style.display = "none";
    }
});

// ========================================
// CONCEPT 12: Fetch API
// ========================================
// fetch() - gets data from servers/APIs
// Returns a Promise - use .then() or async/await
// Common for loading data, submitting forms to backend

const fetchUsersBtn = document.getElementById("fetch-users-btn");
const fetchQuoteBtn = document.getElementById("fetch-quote-btn");
const fetchResult = document.getElementById("fetch-result");

// Fetch random users from API
fetchUsersBtn.addEventListener("click", () => {
    fetchResult.innerHTML = "<p>Loading users...</p>";
    
    // fetch returns a Promise
    fetch("https://randomuser.me/api/?results=3")
        .then(response => response.json()) // Convert response to JSON
        .then(data => {
            // Process the data
            const users = data.results;
            let html = "<h4>Random Users:</h4>";
            
            users.forEach(user => {
                html += `
                    <div style="margin: 10px 0; padding: 10px; background: #f5f5f5; border-radius: 5px;">
                        <img src="${user.picture.thumbnail}" alt="User photo" style="border-radius: 50%;">
                        <p><strong>${user.name.first} ${user.name.last}</strong></p>
                        <p>Email: ${user.email}</p>
                    </div>
                `;
            });
            
            fetchResult.innerHTML = html;
        })
        .catch(error => {
            // Handle errors
            fetchResult.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
            console.error("Fetch error:", error);
        });
});

// Fetch random quote
fetchQuoteBtn.addEventListener("click", () => {
    fetchResult.innerHTML = "<p>Loading quote...</p>";
    
    fetch("https://api.quotable.io/random")
        .then(response => response.json())
        .then(data => {
            fetchResult.innerHTML = `
                <div style="padding: 20px; background: #fff3cd; border-radius: 5px; margin-top: 10px;">
                    <p style="font-size: 18px; font-style: italic;">"${data.content}"</p>
                    <p style="text-align: right;">— ${data.author}</p>
                </div>
            `;
        })
        .catch(error => {
            fetchResult.innerHTML = `<p style="color: red;">Error loading quote</p>`;
            console.error("Error:", error);
        });
});

// ========================================
// CONCEPT 13: LocalStorage
// ========================================
// localStorage.setItem(key, value) - saves data
// localStorage.getItem(key) - retrieves data
// localStorage.removeItem(key) - deletes data
// localStorage.clear() - deletes everything
// Data persists even after closing browser!

const storageInput = document.getElementById("storage-input");
const saveStorageBtn = document.getElementById("save-storage-btn");
const loadStorageBtn = document.getElementById("load-storage-btn");
const clearStorageBtn = document.getElementById("clear-storage-btn");
const storageDisplay = document.getElementById("storage-display");

// Save to localStorage
saveStorageBtn.addEventListener("click", () => {
    const value = storageInput.value;
    
    if (value.trim() === "") {
        alert("Please enter some text!");
        return;
    }
    
    // Save to localStorage (key-value pair)
    localStorage.setItem("myData", value);
    
    // Also save with timestamp
    const timestamp = new Date().toLocaleString();
    localStorage.setItem("saveTime", timestamp);
    
    storageDisplay.innerHTML = `
        <p style="color: green;">✓ Data saved to localStorage!</p>
        <p>Saved at: ${timestamp}</p>
    `;
    
    console.log("Saved to localStorage:", value);
});

// Load from localStorage
loadStorageBtn.addEventListener("click", () => {
    // Retrieve data from localStorage
    const savedData = localStorage.getItem("myData");
    const saveTime = localStorage.getItem("saveTime");
    
    if (savedData === null) {
        storageDisplay.innerHTML = `<p style="color: orange;">No data found in localStorage</p>`;
    } else {
        storageInput.value = savedData;
        storageDisplay.innerHTML = `
            <p style="color: blue;">✓ Data loaded from localStorage!</p>
            <p>Data: ${savedData}</p>
            <p>Saved at: ${saveTime}</p>
        `;
        console.log("Loaded from localStorage:", savedData);
    }
});

// Clear localStorage
clearStorageBtn.addEventListener("click", () => {
    localStorage.removeItem("myData");
    localStorage.removeItem("saveTime");
    // Or use: localStorage.clear(); to remove everything
    
    storageInput.value = "";
    storageDisplay.innerHTML = `<p style="color: red;">✓ localStorage cleared!</p>`;
    console.log("localStorage cleared");
});

// Load saved data on page load (if exists)
window.addEventListener("load", () => {
    const savedData = localStorage.getItem("myData");
    if (savedData) {
        storageInput.value = savedData;
        console.log("Auto-loaded data from localStorage");
    }
});

// ========================================
// CONCEPT 14: setTimeout & setInterval
// ========================================
// setTimeout(function, milliseconds) - runs once after delay
// setInterval(function, milliseconds) - runs repeatedly
// clearTimeout() / clearInterval() - stops timers

const timeoutBtn = document.getElementById("timeout-btn");
const startCounterBtn = document.getElementById("start-counter-btn");
const stopCounterBtn = document.getElementById("stop-counter-btn");
const counterDisplay = document.getElementById("counter-display");

let counterValue = 0;
let intervalId = null;

// setTimeout - runs once after delay
timeoutBtn.addEventListener("click", () => {
    timeoutBtn.textContent = "Alert coming in 3 seconds...";
    timeoutBtn.disabled = true;
    
    // Wait 3 seconds (3000 milliseconds) then show alert
    setTimeout(() => {
        alert("3 seconds have passed!");
        timeoutBtn.textContent = "Show Alert in 3 Seconds";
        timeoutBtn.disabled = false;
    }, 3000);
});

// setInterval - runs repeatedly
startCounterBtn.addEventListener("click", () => {
    // Prevent multiple intervals
    if (intervalId !== null) {
        return;
    }
    
    counterValue = 0;
    counterDisplay.textContent = `Counter: ${counterValue}`;
    
    // Run every 1 second (1000 milliseconds)
    intervalId = setInterval(() => {
        counterValue++;
        counterDisplay.textContent = `Counter: ${counterValue}`;
        console.log("Counter:", counterValue);
    }, 1000);
    
    console.log("Counter started");
});

// clearInterval - stops the interval
stopCounterBtn.addEventListener("click", () => {
    if (intervalId !== null) {
        clearInterval(intervalId);
        intervalId = null;
        console.log("Counter stopped at:", counterValue);
    }
});

// ========================================
// CONCEPT 15: Scroll Events
// ========================================
// window.addEventListener("scroll", ...) - fires when user scrolls
// window.scrollY - current vertical scroll position
// window.scrollTo() - scroll to specific position

const scrollStatus = document.getElementById("scroll-status");
const scrollToTopBtn = document.getElementById("scroll-to-top-btn");
const backToTopBtn = document.getElementById("back-to-top");

// Track scroll position
window.addEventListener("scroll", () => {
    const scrollPosition = window.scrollY;
    scrollStatus.textContent = `Scroll position: ${Math.round(scrollPosition)}px`;
    
    // Show/hide back-to-top button based on scroll position
    if (scrollPosition > 300) {
        backToTopBtn.style.display = "block";
    } else {
        backToTopBtn.style.display = "none";
    }
    
    // Change header background on scroll (example)
    const header = document.querySelector("h1");
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

// Scroll to top button
scrollToTopBtn.addEventListener("click", () => {
    // Smooth scroll to top
    window.scrollTo({
        top: 0,
        behavior: "smooth" // Smooth scrolling animation
    });
});

// Back to top floating button
backToTopBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

// ========================================
// BONUS: Scroll to specific section
// ========================================
// You can also scroll to specific elements
// Example: scroll to a specific section when button clicked
/*
const scrollToSection = (sectionId) => {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: "smooth" });
};
*/


//CS 50 counter 

// CS50 counter
let counter = 0;

const display = document.getElementById("CS50-counter-display");
const increaseCountBtn = document.querySelector("#Increase-count-btn");
const decreaseCountBtn = document.querySelector("#Decrease-count-btn");
const resetCountBtn    = document.querySelector("#Reset-count-btn");
const title            = document.querySelector("#counter-title");

// --- helpers ---
function render() {
  display.textContent = "Count: " + counter;
}

function maybeAlert() {
  if (counter !== 0 && counter % 10 === 0) {
    alert(`Count is now ${counter}`);
  }
}

function toggleTitle() {
  title.textContent = (title.textContent.trim() === "Counter") ? "Brendan" : "Counter";
}

// One place where counter changes
function applyChange(delta) {
  counter += delta;
  render();
  toggleTitle();
  maybeAlert();
}

// --- event handlers ---
increaseCountBtn.addEventListener("click", () => applyChange(+1));
decreaseCountBtn.addEventListener("click", () => applyChange(-1));
resetCountBtn.addEventListener("click", () => {
  counter = 0;
  render();
  // optional: decide if reset should toggle the title or not
  // toggleTitle();
});









// ========================================
// 🎉 ALL 15 CONCEPTS COMPLETE!
// ========================================
console.log("✅ All 15 JavaScript concepts loaded successfully!");
console.log("Concepts covered:");
console.log("1. querySelector/querySelectorAll");
console.log("2. getElementById");
console.log("3. Form handling (preventDefault)");
console.log("4. Input values & validation");
console.log("5. classList methods");
console.log("6. createElement");
console.log("7. appendChild");
console.log("8. Removing elements");
console.log("9. Show/hide elements");
console.log("10. Data attributes");
console.log("11. Keyboard events");
console.log("12. Fetch API");
console.log("13. LocalStorage");
console.log("14. setTimeout/setInterval");
console.log("15. Scroll events");