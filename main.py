import functions_framework
import requests

@functions_framework.http
def hello_world(request):
    """Simple Cloud Function to demonstrate deployment."""
    # Using requests to show dependency usage
    return f"Hello! Requests version: {requests.__version__}"
