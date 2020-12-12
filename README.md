# Prof_List
A python script that gets Professors Name, Field of Interest, E-mail, Website and University from https://inspirehep.net/ and saves it in a csv file using selenium.

## Startup Script
If you already have python3 installed and are on windows with chrome installed you can simply run start.ps1 with powershell which will take care of everything for you.

## Dependencies

This script requires python3 and selenium installed.Download any version of python3 from <a href="https://www.python.org/downloads/">here.</a>For selenium with python installed just run the following code in powershell or in terminal:

```
pip3 install selenium
```

## Setup

Firstly,download this script.
This script will only work if you have chrome.Download chromedriver from <a href="https://chromedriver.chromium.org/downloads">here.</a>
 
 After the download you should put the driver in the folder containing the script.


## Run

Add the search query and number of professors to save and run the script using python in powershell or in terminal like:

```
python3 prof.py search_query number_of_professors
```

