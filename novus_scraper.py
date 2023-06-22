from selenium import webdriver 
from selenium.webdriver.support.ui import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 

from webdriver_manager.chrome import ChromeDriverManager 

from meeting_entry import meeting_entry
from datetime import datetime

import os, time

class novus_scraper:
	_current_page = 1
	_page_sleep = 15
	_url = None

	_start_date = "1/1/2000"
	
	def __init__(self, url) -> None:
		self._url = url
		self._setup_driver()
		self._run_driver()


	def _setup_driver(self):
		chromeOptions = webdriver.ChromeOptions()
		prefs = {"download.default_directory" : os.getcwd() + "/downloads"}
		chromeOptions.add_experimental_option("prefs",prefs)

	def _run_driver(self):
		with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver: 
			driver.implicitly_wait(1)
			driver.get(self._url)

			self._setup_search_form(driver)

			page_count = 1
			
			print("Page " + str(page_count) + ", " + str(self._current_page))
			self._iterate_table(driver)

			while self._page_next(driver):
				print("Page " + str(self._current_page))
				self._iterate_table(driver)

			print ("No more pages")
			driver.close()


	def _setup_search_form(self, driver: webdriver.chrome.webdriver.WebDriver):
		self._change_select_to_custom_range(driver)
		self._set_date_from(driver,	self._start_date)


		# Set Date to Today
		date_today = '{d.month}/{d.day}/{d.year}'.format(d=datetime.now())
		self._set_date_to(driver,		date_today)

		self._search_form(driver)
		time.sleep(10)



	def _change_select_to_custom_range(self, driver: webdriver.chrome.webdriver.WebDriver):
		element = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_SearchAgendasMeetings_ddlDateRange')
		element.click()
		select = Select(element)

		select.select_by_visible_text("Last Year")
		select.select_by_visible_text("Custom Date Range")
		time.sleep(1)

	def _set_date_from(self, driver: webdriver.chrome.webdriver.WebDriver, date_str: str):
		time.sleep(0.5)
		input = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_SearchAgendasMeetings_radCalendarFrom_dateInput')
		input.click()
		driver.execute_script("arguments[0].setAttribute('value','" + date_str + "')",input)
		time.sleep(0.5)

	def _set_date_to(self, driver: webdriver.chrome.webdriver.WebDriver, date_str: str):
		time.sleep(0.5)
		input = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_SearchAgendasMeetings_radCalendarTo_dateInput')
		input.click()
		driver.execute_script("arguments[0].setAttribute('value','" + date_str + "')",input)
		time.sleep(0.5)


	def _search_form(self, driver: webdriver.chrome.webdriver.WebDriver):
		input = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_SearchAgendasMeetings_imageButtonSearch')
		input.click()

	def _page_next(self, driver: webdriver.chrome.webdriver.WebDriver):
		time.sleep(self._page_sleep)
		try:
			input = driver.find_element(By.XPATH, "//a[@title='Next Page']")
		except Exception as e:
			print("No Next Page")
			return False
		else:
			input.click()
			self._current_page += 1
		return True

	def _page_previous(self, driver: webdriver.chrome.webdriver.WebDriver):
		time.sleep(self._page_sleep)
		try:
			input = driver.find_element(By.XPATH, "//a[@title='Previous Page']")
		except Exception as e:
			print("No Previous Page")
			return False
		else:
			input.click()
			self._current_page -= 1
		return True

	def _iterate_table(self, driver: webdriver.chrome.webdriver.WebDriver):
		html_table = self._get_table(driver)
		print(html_table)
		if (html_table is False):
			return

		for row in html_table.find_elements(By.CSS_SELECTOR, 'tr'):
			# trs_arr = row.find_elements(By.CSS_SELECTOR, 'td')
			tr_text = list()
			a_hrefs = list()
			tds = row.find_elements(By.CSS_SELECTOR, 'td')
			
			if (len(tds) != 6):
				continue
			
			for cell in tds:
				tr_text.append(cell.text)

				href_elems = cell.find_elements(By.TAG_NAME, "A")

				if (len(href_elems) == 1):
					href = href_elems[0].get_attribute("href")
				else:
					href = ""
				a_hrefs.append(href)


			meeting_date = tr_text[0]
			meeting_type = tr_text[1]

			meeting_agenda = a_hrefs[4]
			meeting_minutes = a_hrefs[5]

			meeting_entry(meeting_date, meeting_type, meeting_agenda, meeting_minutes)
			
			print (meeting_date, meeting_type, meeting_agenda, meeting_minutes)

	def _get_table(self, driver: webdriver.chrome.webdriver.WebDriver):
		time.sleep(5)
		try:
			table = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_SearchAgendasMeetings_radGridMeetings_ctl00')
		except Exception as e:
			print("No Table Found")
			return False
		else:
			return table