// This file is for the JavaScript code that powers the CS50 Todo List demo in hello.html.

// The initcs50todo function is responsible for setting up the interactivity of the To-Do list. Here's how it works:

// 1. SELECTORS: It first selects the form element with the ID "cs50-todo-form" and attaches an onsubmit event handler to it. This means that whenever the form is submitted (e.g., when the user clicks the "Add Todo" button), the function defined in the onsubmit handler will be executed.

// 2. Inside the onsubmit handler, it reads the value from the input field with the ID "cs50-todo-input" and stores it in a variable called task. This is the text that the user wants to add to their To-Do list.

// 3. It then creates a new <li> element using document.createElement('li') and sets its innerHTML to the value of task. This means that the new list item will display the text that the user entered.

// 4. Finally, it appends the new <li> element to the <ul> with the ID "cs50-todo-list" using appendChild. This adds the new task to the visible list on the webpage.

// After adding the task, it clears the input field by setting its value to an empty string, and returns false to prevent the default form submission behavior (which would cause a page reload).

export function initcs50todo() {
   
    // Disable the submit button initially
   document.querySelector('#cs50-todo-submit').disabled =true;

   document.querySelector('#cs50-todo-input').onkeyup = () => {
    if(document.querySelector('#cs50-todo-input').value.length > 0) {
         document.querySelector('#cs50-todo-submit').disabled = false

    }else {
        document.querySelector('#cs50-todo-submit').disabled = true;
    }       
   
   }    
   
    // 1. SELECTORS: Grab the HTML elements.: Finds the <form id="cs50-todo-form">…</form> and attaches an onsubmit event handler to it.
    const form = document.querySelector("#cs50-todo-form").onsubmit = () => {
        
        // reads the input text from the <input id="cs50-todo-input"> and stores it in the variable task.
        const task = document.querySelector('#cs50-todo-input').value;
        
        //creates a new <li> and put the inner html from task text above into it
        const li = document.createElement('li');
        li.innerHTML = task;
       
        //creates a new <li> into the ul
        document.querySelector('#cs50-todo-list').appendChild(li);
        
        // Clear the input field after adding the task
        document.querySelector('#cs50-todo-input').value = '';
        // Disable the submit button again until new input is entered
        document.querySelector('#cs50-todo-submit').disabled = true;
        //Stop form from submitting
        return false;
    }
 }