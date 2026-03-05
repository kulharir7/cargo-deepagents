# Docstring Guide

## Python Docstrings

### Function

def calculate_total(items, tax_rate=0.1):
    '''Calculate total price with tax.
    
    Args:
        items: List of item dicts with 'price' and 'quantity'.
        tax_rate: Tax rate as decimal (default: 0.1).
    
    Returns:
        Total price including tax.
    
    Raises:
        ValueError: If items is empty or tax_rate is negative.
    
    Example:
        >>> items = [{'price': 10, 'quantity': 2}]
        >>> calculate_total(items)
        22.0
    '''
    pass

### Class

class UserStore:
    '''Manages user data storage.
    
    Attributes:
        db_path: Path to the database file.
        cache: In-memory cache for frequently accessed users.
    
    Example:
        >>> store = UserStore('/data/users.db')
        >>> store.add({'name': 'John', 'email': 'john@example.com'})
    '''
    pass

## JavaScript JSDoc

/**
 * Fetches user data from the API.
 * @async
 * @param {string} userId - The user identifier.
 * @returns {Promise<User>} The user object.
 * @throws {NotFoundError} If user does not exist.
 */
async function fetchUser(userId) {}
