import hashlib
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://s.gravatar.com/avatar/eaf49822488b0f40c87a3068a68ba3a5?s=80'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url