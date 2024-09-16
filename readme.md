# WordPress Dark Mode Automation Test Suite

This repository contains an automation test suite for managing the "WP Dark Mode" plugin in a WordPress environment. The test suite performs the following tasks:

- Logs into a WordPress site.
- Checks if the "WP Dark Mode" plugin is active.
- Installs and activates the plugin if it is not already active.
- Enables Dark Mode for the WordPress Admin Dashboard.
- Modifies various customization settings for the Dark Mode plugin.
- Validates that the Dark Mode is functioning both on the Admin Dashboard and the frontend.
- Stores login credentials securely using environment variables.

## Technologies Used

- **Programming Language:** Python
- **Test Framework:** Selenium
- **Browser:** Chrome WebDriver
- **Environment Variables:** `python-dotenv` package for storing credentials

## Prerequisites

- **Python** 3.9 installed on your machine.
- **pip** (Python package manager) installed.
- **Google Chrome** browser.
- **ChromeDriver**: Ensure you have the correct version of ChromeDriver installed that matches your version of Chrome. [Download ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/).
- **WordPress Installation**: You need a running WordPress instance where you have admin access.

## Installation

1. Clone the repository:

   ```bash
   git clone <https://github.com/naba-mamba/WooCommerceAutomationTestSuit.git>
   cd <AutomationTestSuit>
   ```
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```
3. Install the dependencies:

  ```bash
  pip install -r requirements.txt
  ```
4. Set up your environment variables:

 - Create a .env file in the root directory with the following content:

  ```bash
  MY_APP_USERNAME=<your-wordpress-username>
  MY_APP_PASSWORD=<your-wordpress-password>
   ```
- Example .env file structure is provided in the .env.example file.

5. Place the ChromeDriver executable in your system's PATH or specify its location in the code by uncommenting and updating the serv_obj line in the test files.

## Test Files
- TestLogIn.py: Logs into your WordPress site.
- TestWPDarkMode.py: Checks if the WP Dark Mode plugin is active, installs and activates it if not.
- EnableWPDarkMode.py: Enables Admin Dashboard Dark Mode from the plugin settings.
- ChangeFloatingSwitchStyle.py: Changes the floating switch style in WP Dark Mode plugin.
- CustomSwitchSize.py: Changes the custom switch size and scales it to 220.
- DisableKeyboardShortcut.py: Disables the keyboard shortcut for toggling Dark Mode.
- FloatingSwitchPosition.py: Changes the floating switch position to the left.
- EnablePageTransitionAnimation.py: Enables the page-transition animation with a custom effect.
- ValidateFrontendDarkMode.py: Validates if Dark Mode is enabled on the frontend.
## How to Run the Test Suite
1. Activate the virtual environment:

  ```bash
  source venv/bin/activate  # For Linux/Mac
  venv\Scripts\activate  # For Windows
  ```
2. Run any of the test scripts using Python:

  ```bash
  python <script-name>.py
  ```
For example:

  ```bash
  python TestLogIn.py
  ```
Ensure the WordPress site is running, and the URL in the script points to the correct instance.

## Environment Variables
Store your sensitive credentials in a .env file in the following format:

  ```bash
  MY_APP_USERNAME=<your-wordpress-username>
  MY_APP_PASSWORD=<your-wordpress-password>
  ```
Add a .env.example file as a guide to create the .env file.