

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
	