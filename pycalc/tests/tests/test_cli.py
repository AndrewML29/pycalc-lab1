import pytest
from toolkit.__main__ import main
import sys
from unittest.mock import patch

def test_cli_calc_success():
    with patch('sys.argv', ['toolkit', 'calc', '2+2']):
        main()

def test_cli_convert_success():
    with patch('sys.argv', ['toolkit', 'convert', '100', '--from', 'g', '--to', 'kg']):
        main()

def test_cli_invalid_command():
    with patch('sys.argv', ['toolkit', 'unknown_command']):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 2
