"""Test WTForm validators."""

from collections import namedtuple

import pytest

from flask_extras.forms.validators import network


class FakeCls(object):
    pass


Field = namedtuple('Field', 'data')


def test_is_ip_valid():
    assert network.is_ip('192.168.1.0')
    assert network.is_ip('0.0.0.0')
    assert network.is_ip('255.255.255.255')


def test_is_ip_invalid():
    assert not network.is_ip('foo.x.y-baz.com')
    assert not network.is_ip('https://www.rad.com')


def test_is_hostname_valid():
    assert network.is_hostname('foo.x.y-baz.com')
    assert network.is_hostname('https://www.rad.com')


def test_is_hostname_invalid_ips():
    assert not network.is_hostname('192.168.1.0')
    assert not network.is_hostname('0.0.0.0')
    assert not network.is_hostname('255.255.255.255')


def test_is_hostname_invalid_noperiod():
    assert not network.is_hostname('foo')


def test_is_hostname_invalid_ends_hyphen():
    assert not network.is_hostname('www.foo.com-')


def test_is_hostname_invalid_underscore():
    assert not network.is_hostname('www.bar.foo_.com')


def test_valid_hosts_invalid():
    with pytest.raises(ValueError):
        network.valid_hosts(FakeCls(), Field(data='foo'))


def test_valid_hosts_invalid_octet():
    with pytest.raises(ValueError):
        network.valid_hosts(FakeCls(), Field(data='192.3.120.1111'))


def test_valid_hosts_valid_hostname_single():
    # Just ensuring it doesn't raise a ValueError
    network.valid_hosts(FakeCls(), Field(data='www.foo.com'))


def test_valid_hosts_valid_hostname_list():
    # Just ensuring it doesn't raise a ValueError
    network.valid_hosts(FakeCls(), Field(data='www.foo.com,bar.baz.rad'))


def test_valid_hosts_valid_hostname_ip_mix():
    # Just ensuring it doesn't raise a ValueError
    network.valid_hosts(FakeCls(), Field(data='0.0.0.0, www.foo.com'))


def test_valid_hosts_valid_single():
    # Just ensuring it doesn't raise a ValueError
    network.valid_hosts(FakeCls(), Field(data='0.0.0.0'))
    network.valid_hosts(FakeCls(), Field(data='192.168.0.1'))


def test_valid_hosts_valid_list():
    # Just ensuring it doesn't raise a ValueError
    network.valid_hosts(FakeCls(), Field(data='192.168.0.1,10.3.20.112'))


def test_valid_hosts_valid_range():
    # Just ensuring it doesn't raise a ValueError
    network.valid_hosts(FakeCls(), Field(data='192.168.0.1-192.168.10.0'))
