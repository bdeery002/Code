// ========================================
// CONCEPT 13: LocalStorage
// ========================================
// localStorage.setItem(key, value) - saves data
// localStorage.getItem(key) - retrieves data
// localStorage.removeItem(key) - deletes data
// localStorage.clear() - deletes everything
// Data persists even after closing browser!

export function initStorageDemo() {
  const storageInput = document.getElementById("storage-input");
  const saveStorageBtn = document.getElementById("save-storage-btn");
  const loadStorageBtn = document.getElementById("load-storage-btn");
  const clearStorageBtn = document.getElementById("clear-storage-btn");
  const storageDisplay = document.getElementById("storage-display");

  if (!storageInput || !saveStorageBtn || !loadStorageBtn || !clearStorageBtn || !storageDisplay) return;

  saveStorageBtn.addEventListener("click", () => {
    const value = storageInput.value;
    if (value.trim() === "") {
      alert("Please enter some text!");
      return;
    }

    localStorage.setItem("myData", value);
    const timestamp = new Date().toLocaleString();
    localStorage.setItem("saveTime", timestamp);

    storageDisplay.innerHTML = `
      <p style="color: green;">✓ Data saved to localStorage!</p>
      <p>Saved at: ${timestamp}</p>
    `;
  });

  loadStorageBtn.addEventListener("click", () => {
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
    }
  });

  clearStorageBtn.addEventListener("click", () => {
    localStorage.removeItem("myData");
    localStorage.removeItem("saveTime");
    storageInput.value = "";
    storageDisplay.innerHTML = `<p style="color: red;">✓ localStorage cleared!</p>`;
  });

  // optional: load on page load
  const savedData = localStorage.getItem("myData");
  if (savedData) storageInput.value = savedData;
}