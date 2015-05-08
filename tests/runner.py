#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shellescape import quote

test_string = "ls -l somefile; 'rm -rf dir"
esc_string = quote(test_string)
print(esc_string)
esc_two_string = quote(esc_string)
print(esc_two_string)
