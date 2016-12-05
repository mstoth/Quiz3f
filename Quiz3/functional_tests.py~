# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

        Quiz 3. Add A Page for me.
	
	To this web site, do the following: 

	1. Add a test for a title on the home page and then add the title
	2. Add a test for an image of your choice and then insert the image into the home page. 
	3. Add a test for a clickable area on the image then add the clickable image area
	4. Add a test for the result of clicking on the image area (the new page) then add the web page to make it pass
	5. Test for a header on the new page and then add the header. 

        """

        self.browser.get('http://localhost:8000/index.html')

if __name__=="__main__":
        unittest.main(warnings="ignore")

