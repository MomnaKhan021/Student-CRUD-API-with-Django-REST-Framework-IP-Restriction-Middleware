from django.http import JsonResponse
from django.conf import settings

class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        allowed_ips = getattr(settings, 'ALLOWED_IPS', [])
        if ip not in allowed_ips:
            return JsonResponse({"error": "Forbidden: You do not have access to this API."}, status=403)

        response = self.get_response(request)
        return response
