Copyright (c) 2023 Jacob L Phelps

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


from meeting_entry import meeting_entry
from novus_scraper import novus_scraper
from document_downloader import document_downloader

from datetime import datetime

import os, time, calendar
		
entity_subdomain = "MY-SUBDOMAIN"
site_url = "https://" + entity_subdomain + ".novusagenda.com/AgendaPublic/"

def main():
	scraper = novus_scraper(site_url)
	csv_file = scraper.results_csv()
	
	document_downloader(csv_file)
	

if entity_subdomain != "MY-SUBDOMAIN":
	main()
else:
	print("ERROR:")
	print("**************************************\n")
	print ("-->Please update the entity_subdomain variable with your entity's subdomain.")
	print("\n**************************************")
	
