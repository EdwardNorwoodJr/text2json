import json
import oci
from oci.ai_language import language_client

# OCI configuration details (replace with your values)
config = {
    "user": "ocid1.user.oc1..aaaa...",
    "key_file": "/path/to/private_key.pem",
    "fingerprint": "12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef",
    "tenancy": "ocid1.tenancy.oc1..aaaa...",
    "region": "us-ashburn-1"  # Replace with your region
}

# Create a language client
language_client = language_client.LanguageClient(config)

def classify_text(text):
    try:
        # Create a document classification request
        request = language_client.create_document_classification_request(
            body={"text": text}
        )

        # Send the request and get the response
        response = language_client.invoke_document_classification(request)

        # Extract the classification results
        classifications = response.data.classifications
        return classifications

    except Exception as e:
        print("Error classifying text:", e)
        return None

# Example usage:
text_to_classify = "This is a sample text to classify."
classifications = classify_text(text_to_classify)
print(classifications)