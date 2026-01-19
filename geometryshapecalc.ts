/**
 * Abstract base class for all geometric shapes.
 */
abstract class Shape {
    constructor(public readonly name: string) {}

    /**
     * Abstract method that must be implemented by subclasses.
     */
    abstract getArea(): number;

    describe(): void {
        console.log(`Shape: ${this.name} | Area: ${this.getArea().toFixed(2)}`);
    }
}

/**
 * Circle implementation of Shape.
 */
class Circle extends Shape {
    private readonly PI: number = 3.14159;

    constructor(private radius: number) {
        super("Circle");
    }

    getArea(): number {
        return this.PI * (this.radius ** 2);
    }
}

/**
 * Rectangle implementation of Shape.
 */
class Rectangle extends Shape {
    constructor(private width: number, private height: number) {
        super("Rectangle");
    }

    getArea(): number {
        return this.width * this.height;
    }
}

// Example usage:
const shapes: Shape[] = [
    new Circle(5),
    new Rectangle(10, 20)
];

shapes.forEach(shape => shape.describe());
