/**
 * Interface representing a standard API Response structure.
 * Using a Generic <T> allows this to work with any data type.
 */
interface ApiResponse<T> {
    status: 'success' | 'error';
    data?: T;
    message?: string;
    timestamp: string;
}

/**
 * Interface for a User entity.
 */
interface User {
    id: number;
    username: string;
    email: string;
}

/**
 * Mock function to simulate fetching a user from a database.
 * Returns a Promise wrapped in our ApiResponse interface.
 */
async function getUser(id: number): Promise<ApiResponse<User>> {
    // Simulating an API delay
    const mockUser: User = { id, username: "dev_user", email: "dev@example.com" };

    return {
        status: 'success',
        data: mockUser,
        timestamp: new Date().toISOString()
    };
}

// Example usage:
getUser(1).then(response => {
    if (response.status === 'success' && response.data) {
        console.log(`User found: ${response.data.username}`);
    } else {
        console.error(response.message);
    }
});
