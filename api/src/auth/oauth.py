from httpx_oauth.clients.google import GoogleOAuth2
from httpx_oauth.clients.linkedin import LinkedInOAuth2
from httpx_oauth.clients.microsoft import MicrosoftGraphOAuth2

from api.src.settings import settings

enabled_providers = []

if settings.GOOGLE_CLIENT_ID and settings.GOOGLE_CLIENT_SECRET:
    enabled_providers.append(GoogleOAuth2(settings.GOOGLE_CLIENT_ID, settings.GOOGLE_CLIENT_SECRET))
if settings.LINKEDIN_CLIENT_ID and settings.LINKEDIN_CLIENT_SECRET:
    enabled_providers.append(LinkedInOAuth2(settings.LINKEDIN_CLIENT_ID, settings.LINKEDIN_CLIENT_SECRET))
if settings.MICROSOFT_CLIENT_ID and settings.MICROSOFT_CLIENT_SECRET:
    enabled_providers.append(MicrosoftGraphOAuth2(settings.MICROSOFT_CLIENT_ID, settings.MICROSOFT_CLIENT_SECRET))
