
## Dbot (Dempuraworks Automated Testing Bot)
A Python based automation software built with selenium, currently compatible for Chrome and Firefox testing

### Set up Instructions
1. Install Selenium in Terminal (using pip or pip3)
```
pip install selenium
```
Or download and install the latest selenium version from [here](https://www.selenium.dev/downloads/)

2. Download Browsers *(instructions below)*

3. Run the program with a compatible code editor or IDE (eg: VS Code, PyCharm *etc*)

4. Test scripts are classified by the number in the filename and the test case document is stored in ```Dbot/Dbot_automated_test_scenarios``` where the behaviour of each sript can be referred to

5. Sciprt is operated in the ```source_code/desktop_test_script.py``` file for desktop based testing and ```source_code/mobile_test_script.py``` for mobile based testing, ```source_code/const.py``` can be used to change parameters
    
### Driver installation instructions
**Chrome Driver** 

1. Open Google Chrome
2. On the Chrome address bar, type:
```
chrome://version
```
You will see the following at the top of the screen:

    Google Chrome: your version of google chrome

3. Go to [this page](https://chromedriver.storage.googleapis.com/index.html) and click the file name that is equivalent to your version of google chrome (this contains the drivers to perform the automated tests on google chrome)

4. Download the file name based on your operating system

5. Download or move the file to directory:
```Dbot/Dbot_automated_test_scenarios```

6. The setup for chrome driver is complete

**Firefox Driver**
1. Go [here](https://github.com/mozilla/geckodriver/releases) and download the latest version of the driver for your operating system

2. *macOS 10.15 (Catalina) and later:*

    *Due to the requirement from Apple that all programs must be
    notarized, geckodriver will not work on Catalina if you manually
    download it through another notarized program, such as Firefox*

    *Whilst we are working on a repackaging fix for this problem, you can
    find more details on how to work around this issue in the [macOS
    notarization](https://firefox-source-docs.mozilla.org/testing/geckodriver/Notarization.html) section of the documentation*

3.  Download or move the file to directory:
```Dbot/Dbot_automated_test_scenarios```

4. The setup for firefox driver is complete






