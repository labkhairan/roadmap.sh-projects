# GitHub User Activity CLI 

This is a simple Command Line Interface (CLI) application that allows you to fetch and display a GitHub user’s recent public activity.
The application uses the GitHub Public Events API to show activities such as pushing commits, opening issues, pull requests, and starring repositories.

This project is part of the **roadmap.sh GitHub User Activity** challenge.

## Features

- View recent GitHub activity of any public user.
- Displays activities in a human-readable format.
- Supports multiple event types:
    - Push events
    - Issues events
    - Pull request events
    - Star (watch) events
- Simple and lightweight CLI
- No authentication required (uses public GitHub API)

## Getting Started

### Prerequisites

- **Python** installed on your machine (version 3 or higher).

### Installation

1. **Clone the repository** or download the `github-activity.py` file to your project folder.
2. **Make the script executable**
```bash
chmod +x github-activity.py
```

### Usage

Run the CLI using the following command:

```bash
./github-activity.py <username>
```
Where `<username>` is a valid GitHub username.


#### Example Usage

```bash
./github-activity.py labkhairan
```

#### Example Output

```bash
Pushed 1 commits to labkhairan/roadmap.sh-projects
Pushed 2 commits to labkhairan/roadmap.sh-projects
Pushed 3 commits to labkhairan/roadmap.sh-projects
Pushed 4 commits to labkhairan/roadmap.sh-projects
Pushed 5 commits to labkhairan/roadmap.sh-projects
Pushed 6 commits to labkhairan/roadmap.sh-projects
```

#### Supported Event Types

The CLI currently supports the following GitHub events:
- **PushEvent**: Displays the number of commits pushed to a repository.
- **IssuesEvent**: Displays actions such as opening or closing an issue.
- **PullRequestEvent**: Displays pull request actions (opened, closed, merged, etc).
- **WatchEvent**: Displays repositories starred by the user.

#### Error Handling

- Displays a usage message if the username is not provided.
- Handles invalid usernames or API failures gracefully.
- Skips unsupported or malformed events safely.

### Notes

- This application uses the public GitHub Events API:
```bash
https://api.github.com/users/<username>/events/public
```
- No GitHub authentication token is required.
- The API is rate-limited for unauthenticated requests (60 requests/hour).
- Only public activity is shown.

### Project Reference

This project is based on the roadmap.sh challenge:
**GitHub User Activity**


## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).