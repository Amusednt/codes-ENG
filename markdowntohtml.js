/**
 * Converts basic Markdown links into HTML anchor tags.
 * @param {string} text - The raw text containing markdown links.
 * @returns {string} - The processed string with HTML tags.
 */
function convertMarkdownLinks(text) {
    // Regex pattern: [Text](URL)
    const linkPattern = /\[([^\]]+)\]\(([^)]+)\)/g;

    // Use .replace() with capturing groups
    return text.replace(linkPattern, (match, linkText, url) => {
        return `<a href="${url}" target="_blank" rel="noopener">${linkText}</a>`;
    });
}

// Example usage:
const rawText = "Check my [GitHub Profile](https://github.com/user) for more.";
const htmlOutput = convertMarkdownLinks(rawText);

console.log(htmlOutput); 
// Output: Check my <a href="https://github.com/user" target="_blank" rel="noopener">GitHub Profile</a> for more.
