// ========================================
// CONCEPT 10: Data Attributes (dataset)
// ========================================
// data-* attributes store custom data in HTML
// Access via element.dataset.attributeName
// Useful for storing IDs, settings, metadata

export function initDatasetDemo() {
  const productButtons = document.querySelectorAll(".product-btn");
  const productInfo = document.getElementById("product-info");

  if (!productButtons.length || !productInfo) return;

  productButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const productId = button.dataset.productId;
      const productName = button.dataset.productName;
      const price = button.dataset.price;

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
}