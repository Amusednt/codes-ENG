class DataMapper:
    """
    Dynamically converts a dictionary into a Python object.
    Attributes are created on-the-fly based on dictionary keys.
    """
    def __init__(self, **entries):
        # The __dict__ updates allows direct attribute access
        self.__dict__.update(entries)

    def __repr__(self):
        # Custom representation for easier debugging
        return f"DataMapperObject({self.__dict__})"

def map_raw_data(data_list):
    """Converts a list of dicts into a list of objects."""
    return [DataMapper(**item) for item in data_list]

# Example usage:
raw_json_response = [
    {"id": 1, "name": "Alice", "role": "Developer"},
    {"id": 2, "name": "Bob", "role": "Designer"}
]

users = map_raw_data(raw_json_response)
print(f"User 1 Name: {users[0].name}") # Access via dot notation
