#!/usr/bin/env python3

import sys
import requests

API_URL = "https://api.github.com/users/{username}/events"

HEADERS = {
    "User-Agent": "github-activity-cli",
    "Accept": "application/vnd.github+json",
}

def fetch_events(username: str):
    response = requests.get(
        API_URL.format(username=username),
        headers=HEADERS,
        timeout=10,
    )

    if not response.ok:
        return None

    return response.json()

def render_events(events):
    push_count = 0

    for event in events:
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name", "unknown-repo")
        payload = event.get("payload", {})

        if event_type == "PushEvent":
            push_count += 1
            print(f"Pushed {push_count} commits to {repo}")

        elif event_type == "IssuesEvent":
            action = payload.get("action", "closed")
            print(f"{action.capitalize()} an issue in {repo}")

        elif event_type == "PullRequestEvent":
            action = payload.get("action", "updated")
            print(f"{action.capitalize()} a pull request in {repo}")

        elif event_type == "WatchEvent":
            print(f"Starred {repo}")

def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]
    events = fetch_events(username)

    if not events:
        print("Invalid username or API failure.")
        sys.exit(1)

    render_events(events)

if __name__ == "__main__":
    main()
