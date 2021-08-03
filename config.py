import os
from selenium import webdriver


dirname = os.path.dirname(__file__)
driver = webdriver.Edge(executable_path=f"{dirname}/msedgedriver.exe")
test_link = "https://www.tutorialspoint.com/index.htm"