/**
 * DatabaseConnector manages a single connection instance.
 * Demonstrates the Singleton Design Pattern.
 */
class DatabaseConnector {
    private static instance: DatabaseConnector | null = null;
    private isConnected: boolean = false;

    // Private constructor prevents direct instantiation with 'new'
    private constructor() {}

    /**
     * Static method to control access to the singleton instance.
     */
    public static getInstance(): DatabaseConnector {
        if (!DatabaseConnector.instance) {
            DatabaseConnector.instance = new DatabaseConnector();
        }
        return DatabaseConnector.instance;
    }

    public connect(): void {
        if (this.isConnected) {
            console.log("Already connected to the database.");
            return;
        }
        this.isConnected = true;
        console.log("Connected to Database successfully.");
    }
}

// Example usage:
const db1 = DatabaseConnector.getInstance();
const db2 = DatabaseConnector.getInstance();

db1.connect();
console.log(`Are both instances the same? ${db1 === db2}`); // true
