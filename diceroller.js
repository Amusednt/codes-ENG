/**
 * DiceEngine handles rolling virtual dice with any number of sides.
 */
class DiceEngine {
    constructor() {
        this.history = [];
    }

    /**
     * Rolls a die and stores the result.
     * @param {number} sides - Number of sides on the die (default 6).
     * @returns {number} - The result of the roll.
     */
    roll(sides = 6) {
        if (sides < 2) throw new Error("A die must have at least 2 sides.");
        
        const result = Math.floor(Math.random() * sides) + 1;
        const timestamp = new Date().toLocaleTimeString();
        
        this.history.push({ sides, result, timestamp });
        return result;
    }

    getRecentRolls() {
        return this.history.slice(-5); // Returns the last 5 rolls
    }

    clearHistory() {
        this.history = [];
    }
}

// Example usage:
const d20 = new DiceEngine();
console.log(`You rolled a: ${d20.roll(20)}`);
console.log(`You rolled a: ${d20.roll(20)}`);
console.table(d20.getRecentRolls());
