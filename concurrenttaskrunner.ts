/**
 * Limits the number of concurrent asynchronous operations.
 * Useful for rate-limiting API calls or heavy processing.
 */
class TaskQueue {
    private queue: (() => Promise<any>)[] = [];
    private activeTasks = 0;

    constructor(private concurrencyLimit: number) {}

    /**
     * Adds a task to the queue and starts processing if under limit.
     */
    async add<T>(task: () => Promise<T>): Promise<T> {
        return new Promise((resolve, reject) => {
            const wrapper = async () => {
                try {
                    const result = await task();
                    resolve(result);
                } catch (error) {
                    reject(error);
                } finally {
                    this.activeTasks--;
                    this.next();
                }
            };

            this.queue.push(wrapper);
            this.next();
        });
    }

    private next() {
        if (this.activeTasks < this.concurrencyLimit && this.queue.length > 0) {
            const task = this.queue.shift();
            if (task) {
                this.activeTasks++;
                task();
            }
        }
    }
}

// Example usage:
const q = new TaskQueue(2); // Only 2 tasks at a time
const mockApi = (id: number) => new Promise(res => setTimeout(() => {
    console.log(`Task ${id} finished`);
    res(id);
}, 1000));

[1, 2, 3, 4].forEach(i => q.add(() => mockApi(i)));
