import pytest
from typer.testing import CliRunner
from src.session_8.main import app

runner = CliRunner()

def test_second_number():

    result = runner.invoke(app, ["5", "--sum"])  

    assert result.exit_code == 0

    assert "If you didn't insert a second number, it means that by default we consider it as 0" in result.output

    assert "Result of sum is 5" in result.output
