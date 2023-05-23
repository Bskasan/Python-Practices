from rest_framework import Response


def home(request):
    response Response(
        # To change object to JSON.
        {
            'message': 'Hello World'
        }
    )
        
        
    