import re
from rest_framework.exceptions import ValidationError


def youtube_url_validator(value):
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$'
    )
    if not youtube_regex.match(value):
        raise ValidationError('The URL must be a YouTube link.')
