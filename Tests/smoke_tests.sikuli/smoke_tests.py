import unittest
from _lib import *
import HtmlXmlTestRunner_pkg.HtmlXmlTestRunner as HtmlXmlTestRunner

class SmokeTests(unittest.TestCase):

    # def test_100_Start_Browser(self):
    #     print("XXXXXXXXX Test started XXXXXXXXX")
    #     Browser.Start("google.com")
    #     sleep(1)
    #     Browser.Maximize()

    def test_200_LogIn(self):
        print("XXXXXXXXX Successful Log in XXXXXXXXX")
        LogIn.Start("google.com")
        sleep(1)
        LogIn.Maximize()
        sleep(1)
        LogIn.PageDown()
        sleep(1)
        click(LogIn_UI.enter_username)
        type("Nadya")
        sleep(1)
        click(LogIn_UI.enter_password)
        type("12345")
        sleep(1)
        click(LogIn_UI.log_button)
        assert exists(LogIn_UI.successful_loggedin,3)

suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
HtmlXmlTestRunner.HTMLTestRunner(file(r"Report.html", "w")).run(suite)










# # It's not the shortest version, but for sure it works stable for years :)
# # Recommended to use it
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
#     

#     # Use it to add manually test cases - handy when debugging a specific part of the set
#	  #suite = unittest.TestSuite()
#     #suite.addTest(SmokeTests('test_100_Start_Browser'))
#     #suite.addTest(SmokeTests('FREE_SLOT_FOR_THE_NEXT_TEST'))

#     outfile = open("Report.html", "w")
#     runner = HtmlXmlTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report', description="Description")
#     runner.run(suite)
#     outfile.close()

