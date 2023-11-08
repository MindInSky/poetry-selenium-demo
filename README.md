# Petco demo

Testing for the petco page as a quick example.

## Getting started

These instructions assume you are using a Mac for development. For Windows, ask for help.

#### Requirements:

- [HomeBrew](https://brew.sh/) - The primary package manager for open source applications on a mac
- [pipx](https://pypa.github.io/pipx/installation/) - Package manager and creator / Install and Run Python Applications in Isolated Environments
- [Poetry](https://python-poetry.org/docs/) - Dependency manager and packager in Python
- Python 3.8+

1. Install pipx

   ```zsh
   brew install pipx &&
   pipx ensurepath &&
   pipx completions &&
   autoload -U bashcompinit &&
   bashcompinit
   ```

1. Install poetry

   ```zsh
   pipx install poetry &&
   pipx upgrade poetry
   ```

1. `Optional` As part of poetry some functions are recommended, in my case to use with zsh and OMZ

   ```zsh
   mkdir ~/.zfunc
   touch ~/.zfunc/_poetry
   poetry completions zsh > ~/.zfunc/_poetry
   ```

### Building and running

1. **Clone the repository**
   SSH is recommended.

   ```zsh
   git clone git@github.com:MindInSky/poetry-selenium-demo.git
   ```

1. **Install dependencies** We are using
   [Poetry](https://python-poetry.org/docs) as a
   package manager

   ```zsh
   poetry install
   ```

1. **Run the tests** at the moment we run tests separately, example:

   ```zsh
   poetry run python petco_demo/login.py
   ```

<!-- ## Writting Tests

### Dictionary:

- **Page** is used the tests to describe a valid URL target in the application.
- **Screen** is used to refer to different states within the same Page.
 -->

## 🧐 What's inside?

A quick look at the top-level files and directories you'll see in this project.

      .
      ├── /petco_demo
      ├── /tests
      ├── .env
      ├── poetry.lock
      ├── poetry.toml
      └── pyproject.toml


**`/petco_demo`**: This directory contains all of the code related to the tests created per the requirements presented.

**`/tests`** : Automatically created by poetry, will be removed eventually.

**`.env`** : enviroment variables to be used, at the moment these **must** include at least:
   - BASE_URL= url of the application to be tested (https://www.petco.com.mx/ in this case)
   - USER_EMAIL= valid username email
   - USER_PASSWORD= valid password
   - USER_NAME= Name of the user ( first name for now, so we can confirm it was logged in)
   - USER_FIRST_LASTNAME= Name of the user
   - USER_SECOND_LASTNAME= Name of the user
   - USER_ZIPCODE= Zip code, must be valid!
   - USER_COLONIA= must match zipcode area
   - USER_CALLE= Any string here seems to work
   - USER_NUMERO_EXT=Any number here seems to work
   - USER_PHONE=Any number here seems to work
   - USER_REFERENCE=Any string here seems to work
   - USER_STREET_A=Any string here seems to work
   - USER_STREET_B=Any string here seems to work
   - USER_CC_NUMBER= Any 16 length number seems to work here as long as it starts with a valid BIN 446137 or 465283 are suggestions
   - USER_CC_YEAR= Any year in the future in 4 digit format
   - USER_CC_MONTH= month in number
   - USER_CC_CVV= 3 digits for a CVV


**`poetry.lock`** : Similar to other package manager lock files, not to be edited by hand

**`poetry.toml`**: Created by poetry configs, might be removed later on

**`pyproject.toml`**: SImilar to package.json in storing information of this software
