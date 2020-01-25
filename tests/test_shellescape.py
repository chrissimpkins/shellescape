import shlex

import pytest

from shellescape import quote


def test_shellescape():
    filename = "somefile; rm -rf dir"
    command = 'ls -l {}'.format(quote(filename))
    assert(quote(command) == "'ls -l '\"'\"'somefile; rm -rf dir'\"'\"''")


def test_shellescape_followed_by_split():
    filename = "somefile; rm -rf dir"
    command = 'ls -l {}'.format(quote(filename))
    split_string = shlex.split(command)
    assert(split_string == ['ls', '-l', 'somefile; rm -rf dir'])

