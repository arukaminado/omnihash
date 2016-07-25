import glob
import os
import re
import string
import sys
import unittest

import nose
from nose import case
from nose.pyversion import unbound_method
from nose import util

import click
from click.testing import CliRunner

from omnihash.omnihash import main

# Sanity
def test_hello_world():
    @click.command()
    @click.argument('name')
    def hello(name):
        click.echo('Hello %s!' % name)

    runner = CliRunner()
    result = runner.invoke(hello, ['Peter'])
    assert result.exit_code == 0
    assert result.output == 'Hello Peter!\n'

# Main
def test_omnihash():
    runner = CliRunner()
    result = runner.invoke(main, ['hashme'])
    assert result.exit_code == 0
    assert 'fb78992e561929a6967d5328f49413fa99048d06' in result.output

def test_omnihash2():
    runner = CliRunner()
    result = runner.invoke(main, ['hashme', 'asdf'])
    assert result.exit_code == 0
    assert 'fb78992e561929a6967d5328f49413fa99048d06' in result.output

def test_omnihashfile():
    runner = CliRunner()
    result = runner.invoke(main, ['hashme', 'README.md'])
    assert result.exit_code == 0
    assert 'fb78992e561929a6967d5328f49413fa99048d06' in result.output

def test_omnihashs():
    runner = CliRunner()
    result = runner.invoke(main, ['hashme', 'README.md', '-s'])
    assert result.exit_code == 0
    assert 'fb78992e561929a6967d5328f49413fa99048d06' in result.output

if __name__ == '__main__':
    unittest.main()