// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    const stockBar = document.getElementById('stock-bar');

    function fetchStocks() {
        fetch('/stocks/')
            .then(response => response.json())
            .then(data => {
                stockBar.innerHTML = '';
                const ul = document.createElement('ul');
                for (const [symbol, price] of Object.entries(data)) {
                    const li = document.createElement('li');
                    li.textContent = `${symbol}: $${price.toFixed(2)}`;
                    ul.appendChild(li);
                }
                stockBar.appendChild(ul);
            });
    }

    fetchStocks(); // Initial fetch
    setInterval(fetchStocks, 60000); // Update every 60 seconds
});
