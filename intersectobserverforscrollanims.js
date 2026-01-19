/**
 * Configures an Intersection Observer to detect when elements become visible.
 * Useful for "Reveal on Scroll" effects.
 */
function setupScrollReveal() {
    const options = {
        root: null, // use the viewport
        threshold: 0.1 // trigger when 10% of the element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add a CSS class to trigger the animation
                entry.target.classList.add('visible');
                // Stop observing once the animation is triggered (optional)
                observer.unobserve(entry.target);
                console.log("Element is now visible!");
            }
        });
    }, options);

    // Target all elements with the 'reveal' class
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

// Example CSS requirement:
// .reveal { opacity: 0; transition: opacity 1s; }
// .reveal.visible { opacity: 1; }
