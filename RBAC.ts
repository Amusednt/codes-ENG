/**
 * Enum for User Roles to avoid magic strings.
 */
enum Role {
    ADMIN = 'ADMIN',
    EDITOR = 'EDITOR',
    VIEWER = 'VIEWER'
}

/**
 * Type defining specific permissions.
 */
type Permission = 'read' | 'write' | 'delete';

/**
 * Interface for Role Configuration mapping roles to permissions.
 */
interface RoleConfig {
    readonly role: Role;
    readonly permissions: Permission[];
}

class AccessControl {
    private static readonly systemRoles: Record<Role, Permission[]> = {
        [Role.ADMIN]: ['read', 'write', 'delete'],
        [Role.EDITOR]: ['read', 'write'],
        [Role.VIEWER]: ['read']
    };

    /**
     * Checks if a specific role has the required permission.
     */
    static canAccess(role: Role, action: Permission): boolean {
        const allowedActions = this.systemRoles[role];
        const isAllowed = allowedActions.includes(action);
        
        console.log(`Access Check: ${role} attempting to ${action} -> ${isAllowed ? '✅ GRANTED' : '❌ DENIED'}`);
        return isAllowed;
    }
}

// Example usage:
AccessControl.canAccess(Role.EDITOR, 'delete'); // Should be False
AccessControl.canAccess(Role.ADMIN, 'write');   // Should be True
