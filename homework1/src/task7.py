# task7.py
import requests

def get_github_api_status():
    """
    Uses the requests package to fetch the GitHub API status.
    Returns the HTTP status code (200 means OK).
    """
    response = requests.get("https://api.github.com")
    return response.status_code


if __name__ == "__main__":
    status = get_github_api_status()
    print(f"GitHub API status code: {status}")
