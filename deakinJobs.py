#! python3
# deakinJobs.py – Gets the latest jobs from Deakin University's job directory. 

import requests
import os
import bs4
import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

deakinURL = "https://deakintalent.deakin.edu.au/jobs-and-internships/"

browser = webdriver.Safari()
browser.get(deakinURL)

POPUP_CSS_XPATH = '''//*[@id="popmake-50104"]/button'''
JOB_XPATH = '''//*[@id="post-23622"]/div/div[2]/div/div/div/div[3]/ul/li[8]/a/div[1]/h3'''

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, POPUP_CSS_XPATH))).click()


JOBS = browser.find_elements_by_class_name('job-type-pre-graduate-role')


for job in JOBS:
	cleanJobStr = str(job.text).strip(' \t\n\r')
	print(cleanJobStr)
