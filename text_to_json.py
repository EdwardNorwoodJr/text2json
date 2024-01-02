import json

def save_text_as_json(text, filename):
    """
    Saves the given text as a JSON document with the specified filename.

    Args:
        text (str): The text to be saved.
        filename (str): The name of the JSON file to create.
    """

    # Create a dictionary to hold the text data
    data = {"text": text}

    # Write the dictionary to a JSON file
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)  # Indent is optional gives you more space.

# Example usage:
text_to_save = "This is some sample text."
filename = "my_text_data.json"
save_text_as_json(text_to_save, filename)