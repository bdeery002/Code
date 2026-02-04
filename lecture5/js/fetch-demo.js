// ========================================
// CONCEPT 12: Fetch API
// ========================================
// fetch() - gets data from servers/APIs
// Returns a Promise - use .then() or async/await
// Common for loading data, submitting forms to backend

export function initFetchDemo() {
  const fetchUsersBtn = document.getElementById("fetch-users-btn");
  const fetchQuoteBtn = document.getElementById("fetch-quote-btn");
  const fetchResult = document.getElementById("fetch-result");

  if (!fetchUsersBtn || !fetchQuoteBtn || !fetchResult) return;

  fetchUsersBtn.addEventListener("click", () => {
    fetchResult.innerHTML = "<p>Loading users...</p>";

    fetch("https://randomuser.me/api/?results=3")
      .then((response) => response.json())
      .then((data) => {
        const users = data.results;
        let html = "<h4>Random Users:</h4>";

        users.forEach((user) => {
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
      .catch((error) => {
        fetchResult.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
        console.error("Fetch error:", error);
      });
  });

  fetchQuoteBtn.addEventListener("click", () => {
    fetchResult.innerHTML = "<p>Loading quote...</p>";

    fetch("https://api.quotable.io/random")
      .then((response) => response.json())
      .then((data) => {
        fetchResult.innerHTML = `
          <div style="padding: 20px; background: #fff3cd; border-radius: 5px; margin-top: 10px;">
            <p style="font-size: 18px; font-style: italic;">"${data.content}"</p>
            <p style="text-align: right;">— ${data.author}</p>
          </div>
        `;
      })
      .catch((error) => {
        fetchResult.innerHTML = `<p style="color: red;">Error loading quote</p>`;
        console.error("Error:", error);
      });
  });
}