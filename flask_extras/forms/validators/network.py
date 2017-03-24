import re

import socket

from netaddr import iter_iprange
from netaddr.core import AddrFormatError


def is_ip(addr):
    """Determine if a string is really an ip, or a hostname instead.

    Args:
        addr (str): The ip address string to check

    Returns:
        bool: Whether or not `addr` is a valid ip.
    """
    if '.' not in addr:
        return False
    parts = addr.split('.')
    for part in parts:
        try:
            int(part)
        except ValueError:
            return False
    return True


def is_hostname(addr):
    """Determine if a string is a hostname.

    Based on https://en.wikipedia.org/wiki
        /Hostname#Restrictions_on_valid_hostnames

    Args:
        addr (str): The address string to check

    Returns:
        bool: Whether or not `addr` is a valid hostname.
    """
    if any([
        '_' in addr,
        '.' not in addr,
        addr.endswith('-'),
        is_ip(addr),
    ]):
        return False
    return True


def valid_hosts(formcls, field):
    """Validate a list of IPs (Ipv4) or hostnames using python stdlib.

    This is more robust than the WTForm version as it also considers hostnames.

    Comma separated values:
    e.g. '10.7.223.101,10.7.12.0'
    Space separated values:
    e.g. '10.223.101 10.7.223.102'
    Ranges:
    e.g. '10.7.223.200-10.7.224.10'
    Hostnames:
    e.g. foo.x.y.com, baz.bar.z.com

    :param formcls (object): The form class.
    :param field (str): The list of ips.
    """
    ip_range_re = re.compile(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}')
    data = field.data
    if ',' in data:
        ips = [ip for ip in data.split(',') if ip]
    elif ' ' in data:
        ips = [ip for ip in data.split(' ') if ip]
    elif '-' in data and re.match(ip_range_re, data):
        try:
            start, end = data.split('-')
            ips = iter_iprange(start, end)
            ips = [str(ip) for ip in list(ips)]
        except ValueError:
            raise ValueError(
                'Invalid range specified. Format should be: '
                'XXX.XXX.XXX.XXX-XXX.XXX.XXX.XXX '
                '(e.g. 10.7.223.200-10.7.224.10)')
        except AddrFormatError as e:
            raise ValueError(e)
    else:
        # Just use the single ip
        ips = [data]
    # If any fails conversion, it is invalid.
    for ip in ips:
        # Skip hostnames
        if not is_ip(ip):
            if not is_hostname(ip):
                raise ValueError('Invalid hostname: "{}"'.format(ip))
            else:
                continue
        try:
            socket.inet_aton(ip)
        except socket.error:
            raise ValueError('Invalid IP: {}'.format(ip))
