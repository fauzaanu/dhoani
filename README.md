# Dhoani

Dhoani is a traffic generation script designed to manipulate search rankings on certain platforms by utilizing NordVPN's extensive network of over 6,000 servers. This program automates the process of generating continuous traffic to a specific website by integrating `playwright` for browser automation and `nordvpn_switcher` for rotating VPN servers. While the current implementation provides basic functionality, it serves as a solid foundation for any project requiring automated traffic generation with dynamic IP addresses.

## How It Works

The script follows these steps:

1. **Initialize NordVPN and Connect to a Server**: The script starts by connecting to a random NordVPN server.
2. **Visit a Predefined Google Search Link**: It navigates to the URL specified in the `.env` file under `GOOGLE_SEARCH_LINK`.
3. **Search for a Specific Term**: It looks for the first exact match of the search term defined in the `.env` file as `GOOGLE_SEARCH_TITLE_TEXT`.
4. **Click the Matching Link**: Upon finding the match, the script clicks on the link.
5. **Wait**: It waits for 5 seconds to simulate user interaction.
6. **Close the Browser**: The browser is then closed.
7. **Rotate the VPN Server**: The script switches to a different VPN server.
8. **Repeat**: The entire process repeats indefinitely.

## Prerequisites

To run Dhoani, you'll need:

- **NordVPN Account**: A valid NordVPN account to access the 6,000+ servers.
- **.env File**: A `.env` file configured according to the provided `.env_sample`.
- **Python Packages**: The necessary Python packages can be installed via `poetry` or by using a `requirements.txt` file. The package names can be copied from the `pyproject.toml` file.
- **Playwright Setup**: After installing the required packages, run `playwright install` to download the necessary browser binaries.

### Accepting cookies

todo: accept cookies automatically, handle this as a fallback

If you're running the script for EU servers, you may need to manually accept cookies on the first visit to each website. This is a one-time setup due to the use of a persistent browser session.

## Installation

1. Clone the repository.
2. Set up your `.env` file based on the `.env_sample` template.
3. Install the required Python packages:
   - Using `poetry`: Run `poetry install`.
   - Using `pip`: Create a `requirements.txt` from `pyproject.toml` and run `pip install -r requirements.txt`.
4. Install Playwright browser binaries by running:
   ```bash
   playwright install
   ```

## Usage

To start the program, simply run:

```bash
python main.py
```

The script will begin generating traffic according to the predefined configuration.

---

This program provides a good starting point for more complex traffic generation and search manipulation tasks. Modify it to suit your specific needs.

---

Note that playwright has a code generator that can help you to create the code to interact with the browser.
You can use it to create the code to interact with the browser and then integrate it with the script.

Todo: seperate the playwright code into a different file and import it into the main script to make this more modular.

```bash
npx playwright codegen
```
