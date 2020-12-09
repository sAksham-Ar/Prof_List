# Prof_List
A python script that gets Professors Name, Field of Interest, E-mail, Website and University from https://inspirehep.net/ and saves it in a csv file using selenium.

## Dependencies

This script requires python3 and selenium installed.Download any version of python3 from <a href="https://www.python.org/downloads/">here.</a>For selenium with python installed just run the following code in powershell or in terminal:

```
pip3 install selenium
```

## Setup

Firstly,download this script.
This script will only work if you have chrome.Download chromedriver from <a href="https://chromedriver.chromium.org/downloads">here.</a>

<i>Note:To use it with firefox change ```driver=webdriver.Chrome()``` in line 4 to  ```driver=webdriver.Firefox()``` Then you should download the geckodriver from <a href="https://github.com/mozilla/geckodriver/releases">here.</a>
 </i>
 
 After the download you should put the path of the driver in the file like this:
 
 ```
 driver=webdriver.Chrome(r"C:\Users\aryas\Documents\chromedriver.exe")
 ```


## Run

Add the search query and number of professors to save and run the script using python in powershell or in terminal like:

```
python3 prof.py search_query number_of_professors
```

