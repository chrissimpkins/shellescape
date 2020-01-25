# shellescape

## Description

The shellescape Python module defines the `shellescape.quote()` function that returns a shell-escaped version of a Python string.  This is a backport of the `shlex.quote()` function from Python 3.8 that makes it accessible to users of Python 3 versions < 3.3 and all Python 2.x versions.


### quote(s)

*From the Python documentation*:

Return a shell-escaped version of the string s. The returned value is a string that can safely be used as one token in a shell command line, for cases where you cannot use a list.

This idiom would be unsafe:

```python
>>> filename = 'somefile; rm -rf ~'
>>> command = 'ls -l {}'.format(filename)
>>> print(command)  # executed by a shell: boom!
ls -l somefile; rm -rf ~
```

`quote()` lets you plug the security hole:

```python
>>> command = 'ls -l {}'.format(quote(filename))
>>> print(command)
ls -l 'somefile; rm -rf ~'
>>> remote_command = 'ssh home {}'.format(quote(command))
>>> print(remote_command)
ssh home 'ls -l '"'"'somefile; rm -rf ~'"'"''
```

The quoting is compatible with UNIX shells and with `shlex.split()`:

```python
>>> remote_command = split(remote_command)
>>> remote_command
['ssh', 'home', "ls -l 'somefile; rm -rf ~'"]
>>> command = split(remote_command[-1])
>>> command
['ls', '-l', 'somefile; rm -rf ~']
```


## Usage

Include `shellescape` in your project setup.py file `install_requires` dependency definition list:

```python
setup(
    ...
    install_requires=['shellescape'],
    ...
)
```

Then import the `quote` function into your module(s) and use it as needed:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shellescape import quote

filename = "somefile; rm -rf ~"
escaped_shell_command = 'ls -l {}'.format(quote(filename))
```

## License

[LICENSE](https://github.com/chrissimpkins/shellescape/blob/master/docs/LICENSE)


