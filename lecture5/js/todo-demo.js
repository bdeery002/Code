// ========================================
// CONCEPT 6 & 7: createElement() & appendChild()
// ========================================
// createElement() - creates new HTML element in memory
// appendChild() - adds element to the page (makes it visible)

// ========================================
// CONCEPT 8: Removing Elements & Event Delegation
// ========================================
// element.remove() - removes element from DOM
// Event delegation - attach listener to parent, check what was clicked
// More efficient than adding listeners to every child element


export function initTodoDemo() {
  const todoInput = document.getElementById("todo-input");
  const addTodoBtn = document.getElementById("add-todo-btn");
  const todoList = document.getElementById("todo-list");

  if (!todoInput || !addTodoBtn || !todoList) return;

  addTodoBtn.addEventListener("click", () => {
    const todoText = todoInput.value.trim();
    if (todoText === "") {
      alert("Please enter a todo item!");
      return;
    }

    const li = document.createElement("li");
    li.className = "todo-item";

    const span = document.createElement("span");
    span.textContent = todoText;

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.className = "delete-btn";

    li.appendChild(span);
    li.appendChild(deleteBtn);
    todoList.appendChild(li);

    todoInput.value = "";
    console.log(`Added todo: ${todoText}`);
  });

  todoInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") addTodoBtn.click();
  });

  // Event delegation for deletes
  todoList.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
      e.target.parentElement.remove();
      console.log("Todo item deleted");
    }
  });
}