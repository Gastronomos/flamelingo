from fastapi_sso.sso.facebook import FacebookSSO
from fastapi_sso.sso.fitbit import FitbitSSO
from fastapi_sso.sso.github import GithubSSO
from fastapi_sso.sso.gitlab import GitlabSSO
from fastapi_sso.sso.google import GoogleSSO
from fastapi_sso.sso.kakao import KakaoSSO
from fastapi_sso.sso.line import LineSSO
from fastapi_sso.sso.linkedin import LinkedInSSO
from fastapi_sso.sso.microsoft import MicrosoftSSO
from fastapi_sso.sso.naver import NaverSSO
from fastapi_sso.sso.notion import NotionSSO
from fastapi_sso.sso.spotify import SpotifySSO
from fastapi_sso.sso.twitter import TwitterSSO
from fastapi_sso.sso.yandex import YandexSSO

avaliable_sso = {
    "google": GoogleSSO,
    "github": GithubSSO,
    "facebook": FacebookSSO,
    "fitbit": FitbitSSO,
    "gitlab": GitlabSSO,
    "yandex": YandexSSO,
    "kakao": KakaoSSO,
    "line": LineSSO,
    "microsoft": MicrosoftSSO,
    "linkedin": LinkedInSSO,
    "naver": NaverSSO,
    "notion": NotionSSO,
    "spotify": SpotifySSO,
    "twitter": TwitterSSO,
}
