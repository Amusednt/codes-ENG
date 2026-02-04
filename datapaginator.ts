/**
 * Interface representing the structure of a paginated result.
 */
interface PaginationResult<T> {
    currentPage: number;
    totalPages: number;
    pageSize: number;
    totalItems: number;
    items: T[];
}

/**
 * Generic function to paginate an array of data.
 * @param data - The full array of items.
 * @param page - The requested page number (1-indexed).
 * @param limit - Number of items per page.
 */
function paginate<T>(data: T[], page: number = 1, limit: number = 10): PaginationResult<T> {
    const totalItems = data.length;
    const totalPages = Math.ceil(totalItems / limit);
    
    // Ensure current page doesn't exceed bounds
    const currentPage = Math.max(1, Math.min(page, totalPages));
    
    // Calculate start and end indices
    const startIndex = (currentPage - 1) * limit;
    const endIndex = startIndex + limit;
    
    // Extract the slice of data
    const items = data.slice(startIndex, endIndex);

    return {
        currentPage,
        totalPages,
        pageSize: limit,
        totalItems,
        items
    };
}

// Example usage:
const mockData = Array.from({ length: 55 }, (_, i) => `Item ${i + 1}`);
const result = paginate(mockData, 3, 10);
console.log(`Showing page ${result.currentPage} of ${result.totalPages}`);
