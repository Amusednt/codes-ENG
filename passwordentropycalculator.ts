/**
 * Calculates the bit-strength (entropy) of a password string.
 * High entropy = harder to crack via brute force.
 */
function calculatePasswordEntropy(password: string): number {
    let poolSize = 0;

    // Check character variety to determine the pool size
    if (/[a-z]/.test(password)) poolSize += 26;
    if (/[A-Z]/.test(password)) poolSize += 26;
    if (/[0-9]/.test(password)) poolSize += 10;
    if (/[^a-zA-Z0-9]/.test(password)) poolSize += 33;

    if (poolSize === 0 || password.length === 0) return 0;

    // Formula: Entropy = L * log2(R)
    // L = Password length, R = Pool of possible characters
    const entropy = password.length * (Math.log(poolSize) / Math.log(2));
    return Math.round(entropy);
}

// Example usage:
const strength = calculatePasswordEntropy("P@ssw0rd123!");
console.log(`Entropy: ${strength} bits`); // > 60 bits is usually considered good
