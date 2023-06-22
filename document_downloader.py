import requests

from pypdf import PdfReader
from pypdf.errors import PdfReadError

from meeting_entry import meeting_entry
import time, os
from urllib.parse import urlparse
from datetime import datetime

class document_downloader:
    
	def __init__(self, csv_file_name) -> None:
		myFile = open(csv_file_name)
		
		csv_line = myFile.readline()
		while csv_line != "":
			data_arr = csv_line.strip().split(",")
			date_raw		= data_arr[0].strip()
			meeting_type	= data_arr[1].strip()
			url_agenda		= data_arr[2].strip()
			url_minutes		= data_arr[3].strip()

			datetime_object = datetime.strptime(date_raw, '%m/%d/%y')

			
			
			file_name_agenda = datetime_object.strftime("%Y-%m-%d") + "." + meeting_type + ".Agenda.pdf"
			if url_agenda is not "":
				self.download_url(url_agenda, file_name_agenda)
			else:
				print("-" + file_name_agenda)


			file_name_minute = datetime_object.strftime("%Y-%m-%d") + "." + meeting_type + ".Minutes.pdf"
			if url_minutes is not "":
				self.download_url(url_minutes, file_name_minute)
			else:
				print("-" + file_name_minute)

			# text = text.strip()
			# print(date, meeting_type, url_agenda, url_minutes)

			csv_line = myFile.readline()
		myFile.close()

	def download_url(self, url: str, file_name: str):
		url = url.strip()
		file_name = file_name.replace("/", "-").strip()

		file_path = os.getcwd() + "/downloads/"
		
		if os.path.exists(file_path) is False:
			os.makedirs(file_path)
			
			try:
				1 * 1
				# r = requests.get(url, allow_redirects=True)
			except:
				print("FAILED: `" + url + "`")
			else:
				open(file_path + file_name, 'wb').write(r.content)

		self.pdf_valid(file_path + file_name)

		
	def pdf_valid(self, full_file_path: str) -> bool:
		if os.path.isfile(full_file_path):
			try:
				PdfReader(full_file_path)
			except PdfReadError:
				print("`" + full_file_path + "`")
				print("Invalid PDF: " + full_file_path)