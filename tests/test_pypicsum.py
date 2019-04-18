#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from click.testing import CliRunner
from pypicsum import pypicsum
from pypicsum import cli


# def test_cli():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert "pypicsum.cli.main" in result.output


def test_cli_help():
    """Test the CLI help."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output
