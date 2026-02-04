/**
 * Validates the existence of required environment variables.
 * Prevents the application from running in an unstable state.
 */
function validateEnv(variables: string[]): void {
    const missing: string[] = [];

    variables.forEach((variable) => {
        // In Node.js, variables are accessed via process.env
        // Here we simulate the check
        if (!process.env[variable]) {
            missing.push(variable);
        }
    });

    if (missing.length > 0) {
        throw new Error(
            `❌ Deployment Error: Missing required environment variables: ${missing.join(', ')}`
        );
    }

    console.log("✅ Environment validation successful.");
}

// Example usage:
// validateEnv(['DATABASE_URL', 'STRIPE_API_KEY', 'JWT_SECRET']);
