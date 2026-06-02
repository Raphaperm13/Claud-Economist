import pytest
from src.task.compression import compression

def test_nominal_case_text():
    raw_input = "  Bonjour    mon cher   Jarvis.  \n\n\n  Comment   vas-tu ?  "
    expected = "Bonjour mon cher Jarvis.\nComment vas-tu ?"
    assert compression(raw_input) == expected


def test_nominal_case_code_protection():
    raw_input = 'x = 1\n\nprintf("Nom :\\t\\t%s\\n", nom);\n\ny = 2'
    expected = 'x = 1\nprintf("Nom :\\t\\t%s\\n", nom);\ny = 2'
    assert compression(raw_input) == expected


def test_edge_case_empty_and_whitespace():
    assert compression("") == ""
    assert compression("   ") == ""
    assert compression("\n\n\t\t   \n") == ""


def test_edge_case_multiple_tabs_outside():
    raw_input = "def\t\t\tma_fonction():\n\t\treturn\tTrue"
    expected = "def ma_fonction():\nreturn True"
    assert compression(raw_input) == expected


def test_edge_case_empty_lines_removal():
    raw_input = "Ligne 1\n    \n\t\t\nLigne 2"
    expected = "Ligne 1\nLigne 2"
    assert compression(raw_input) == expected


def test_edge_case_multiple_quotes():
    raw_input = 'print("Hello \t\t World")   and   print("Jarvis \n\n Boss")'
    expected = 'print("Hello \t\t World") and print("Jarvis \n\n Boss")'
    assert compression(raw_input) == expected
