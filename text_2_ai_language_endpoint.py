import json
import oci
from oci.ai_language import language_client

def classify_text_using_custom_model(text, endpoint_id):
    """
    Saves the given text as a JSON file, sends it to an Oracle Language Service custom model endpoint
    for text classification, and returns the classification results.

    Args:
        text (str): The text to classify.
        endpoint_id (str): The OCID of the custom model endpoint.

    Returns:
        list: The classification results, or None if an error occurred.
    """

    try:
        # Save text as JSON
        filename = "text_to_classify.json"
        save_text_as_json(text, filename)

        # Create language client
        config = {
            "user": "ocid1.user.oc1..aaaa...",  # Replace with your user OCID
            "key_file": "/path/to/private_key.pem",  # Replace with your private key file path
            "fingerprint": "12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef",  # Replace with your fingerprint
            "tenancy": "ocid1.tenancy.oc1..aaaa...",  # Replace with your tenancy OCID
            "region": "us-chicago-1"  # Replace with your region
        }
        language_client = language_client.LanguageClient(config)

        # Classify text using the custom model endpoint
        with open(filename, "r") as f:
            data = json.load(f)
        response = language_client.invoke_document_classification(
            endpoint_id=endpoint_id,
            body=data
        )

        # Return classification results
        return response.data.classifications

    except Exception as e:
        print("Error classifying text:", e)
        return None

# Example usage:
text_to_classify = "This is a sample text to classify."
endpoint_id = "ocid1.languageendpoint.oc1.iad.aaaa..."  # Replace with your custom model endpoint OCID
classifications = classify_text_using_custom_model(text_to_classify, endpoint_id)
print(classifications)