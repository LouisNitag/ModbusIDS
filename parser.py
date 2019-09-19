import re


def parse_address(h):
    """ Parse address as <host>[:<port=502>]/<register> """

    regex = re.compile("(?P<host>(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?::(?P<port>\d+))?(?:/(?P<register>\d+))")
    h = list(re.finditer(regex, h))
    if len(h) != 1:
        raise ValueError('host not valid')
    h = h[0].groupdict()
    h['port'] = h['port'] or 502
    h['port'], h['register'] = int(h['port']), int(h['register'])
    return h
