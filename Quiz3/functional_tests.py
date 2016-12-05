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

	1. Add a test for a page title on the home page and then add the title
	2. Add a test for an h1 type heading on the home page and then add the heading
	3. Add a test for an image of your choice and then insert the image into the home page. 
	4. Add a test for a clickable area on the image then add the clickable image area going
	   to the web page called "newpage.html"
	5. Add a test for the result of clicking on the image area (the new page)
	   then add the web page called "newpage.html" to make it pass
	6. Test for a header on the new page and then add the header. 

	When you are done, do the following:
	    Create a repository in your github account called Quiz3
	    Remove the .git directory from your cloned Quiz3
	    type
	        git init .
	    in the same directory that you removed .git
	    type
	        git add .
	    type
	        git commit -a -m "my submission" 
	    follow the instructions on github to push your work to your Quiz3
	    
	    Make sure you have pushed your work by typing
	        git push

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

