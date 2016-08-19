import requests


def main(user_name, repo_name):
    GITHUB_URL_PTN = "https://api.github.com/repos/{0}/{1}/issues"
    url = GITHUB_URL_PTN.format(user_name, repo_name)

    r = requests.get(url)
    if r.ok:
        issues = r.json()
        for issue in issues:
            print(issue["title"])


if __name__ == "__main__":
    user_name = "tensorflow"
    repo_name = "tensorflow"
    main(user_name, repo_name)
