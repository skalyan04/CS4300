import pathlib
import sys
import subprocess

# Add src/ to path for imports
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "src"))
import task7


def test_github_api_status():
    status = task7.get_github_api_status()
    # 200 is the expected response code for a successful GET request which was 
    # seen when running the actual task7.py script.
    assert status == 200


def test_task7_console_output():
    script_path = pathlib.Path(__file__).parent.parent / "src" / "task7.py"
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    output = result.stdout.strip()

    # The output should include the status code
    assert "GitHub API status code:" in output
    assert "200" in output
