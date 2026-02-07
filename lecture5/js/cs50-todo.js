export function initcs50todo() {
       // 1. SELECTORS: Grab the HTML elements.
         const title = document.getElementById("cs50-todo-title");
            const input = document.getElementById("cs50-todo-input");
            const addButton = document.getElementById("cs50-todo-add");
            const list = document.getElementById("cs50-todo-list");

            // 2. GUARD CLAUSE: Stop if any element is missing.
            if (!input || !addButton || !list) return;

            // 3. EVENT LISTENER: When the add button is clicked, add a new todo item.
            addButton.addEventListener("click", () => {
                const todoText = input.value.trim();
                if (todoText) {
                    const listItem = document.createElement("li");
                    listItem.textContent = todoText;
                    list.appendChild(listItem);
                    input.value = ""; // Clear the input field
                }
            });

            // 4. OPTIONAL: Add event listener to the list to handle item removal.
            list.addEventListener("click", (event) => {
                if (event.target.tagName === "LI") {
                    event.target.remove(); // Remove the clicked list item
                }
            });
 }