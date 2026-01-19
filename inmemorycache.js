/**
 * SimpleCache stores key-value pairs that expire after a set time.
 */
class SimpleCache {
    constructor() {
        this.cache = new Map();
    }

    /**
     * Store a value in the cache.
     * @param {string} key - The identifier.
     * @param {any} value - The data to store.
     * @param {number} ttl - Time To Live in milliseconds.
     */
    set(key, value, ttl = 5000) {
        const expiry = Date.now() + ttl;
        this.cache.set(key, { value, expiry });
        
        // Auto-delete after TTL
        setTimeout(() => this.cache.delete(key), ttl);
    }

    get(key) {
        const data = this.cache.get(key);
        if (!data) return null;

        // Check if data is expired
        if (Date.now() > data.expiry) {
            this.cache.delete(key);
            return null;
        }
        return data.value;
    }
}

// Test usage
const myCache = new SimpleCache();
myCache.set("apiKey", "12345-ABCDE", 2000); // Expires in 2 seconds

console.log(myCache.get("apiKey")); // Exists
setTimeout(() => console.log("After 3s:", myCache.get("apiKey")), 3000); // Expired (null)
