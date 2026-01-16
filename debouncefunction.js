/**
 * Limits the execution of a function until after a specific wait time.
 * Excellent for search inputs or window resize events.
 * @param {Function} func - The function to be debounced.
 * @param {number} delay - The wait time in milliseconds.
 */
function debounce(func, delay = 500) {
    let timeoutId;

    return (...args) => {
        // Clear the previous timer if the function is called again
        if (timeoutId) {
            clearTimeout(timeoutId);
        }

        // Set a new timer
        timeoutId = setTimeout(() => {
            func.apply(null, args);
        }, delay);
    };
}

// Example: Handling a search input
const processSearch = debounce((query) => {
    console.log(`Searching for: ${query} (API Request sent)`);
}, 1000);

// Even if called multiple times, it only fires once after 1 second of inactivity
processSearch("A");
processSearch("Ap");
processSearch("Apple");
