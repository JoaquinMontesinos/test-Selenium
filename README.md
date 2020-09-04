# test-Selenium

Steps of Selenium Tests:
- Create a WebDriver instance.
- Navigate to a Web page.
- Locate an HTML element on the Web page.
- Perform an action on an HTML element.
- Anticipate the browser response to the action.
- Run tests and record test results using a test framework.
- Conclude the test.

 Requeriments:  
- You need to specify the path where your chromedriver is located: 
- Download chromedriver for your desired platform: https://sites.google.com/a/chromium.org/chromedriver/downloads
- Place chromedriver on your system path, or where your code is. 
''' browser = webdriver.Chrome('C:/Users/JM/Documents/chromedriver') '''
- Look here for more info in case it doesn't run: https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver

 Sample test:  
In this test it is scraped data from https://contrataciondelestado.es
