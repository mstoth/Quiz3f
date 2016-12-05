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

        Final Web Site Problem. 
	
		Make the following tests pass. 

        """

		# here is the first test
        self.browser.get('http://localhost:8000/index.html')

        # now we test for a header that says "Quiz3"
        a=self.browser.find_element_by_tag_name('h1')

        # make sure it says Quiz3
        self.assertIn('Quiz3',a.text)

        # Add a test for a link to Credits
        a=self.browser.find_element_by_link_text('Credits')

        # Make sure when you click on it you go to the credits.html page
        a.click()
        self.assertIn('credits.html',self.browser.current_url)

        # See if you have a link to go back
        a=self.browser.find_element_by_link_text('Back')

        # click on it
        a.click()

        # see if you are on the home page
        self.assertIn('index.html',self.browser.current_url)


if __name__=="__main__":
        unittest.main(warnings="ignore")

