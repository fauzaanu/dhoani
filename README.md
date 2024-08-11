# Dhoani

Initially written for the purpose of manipulating the search ranking within a certain unnamed platform for a certain unnamed project. For you, this program is a simple traffic generator that utilizes NordVPN's 6000+ servers to generate traffic for website from multiple locations.

This program does some very basic stuff and you will likely need to modify it to suite your needs. However this program sets a good starting point for any playwright automation project that uses nordvpn to rotate servers due to the integration of both `playwright` and `nordvpn_switcher`.

1. Initializes Nord VPN and connects to a server
2. Visits a google search link or any link that is defined in `.env` as `GOOGLE_SEARCH_LINK`
2. Searches for the first exact match of the search term defined in `.env` as `GOOGLE_SEARCH_TITLE_TEXT`
3. Clicks on the first link that matches the search term
4. Waits 5 seconds
5. Closes the browser
6. Rotates the VPN server
7. Repeats the process...

## Packages Used
- python-dotenv
- playwright
- nordvpn_switcher

## Setup
- You need a NordVPN account to get access to all 6000+ servers
- You need to have a `.env` file in the format of the `.env_sample` file
- poetry would make things easy but if you use `requirements.txt` please copy the package names from the `pyproject.toml` file
- after installation of all packages please run `playwright install` to install the browser binaries
- For EU countries you may have to click the accept cookies once. Since we use a persistance browser, this process will be once per website

## Usage
- Run the program with `python main.py`

