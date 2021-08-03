import os
from selenium import webdriver


dirname = os.path.dirname(__file__)
driver = webdriver.Edge(executable_path=f"{dirname}/msedgedriver.exe")
test_link_for_form_submit = "http://localhost:3000/login.php"
test_link_for_navigation = "http://localhost:3000/"
