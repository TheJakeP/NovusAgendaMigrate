import os, time, calendar

class meeting_entry:

	csv_path = None

	_date			= None
	_type			= None
	_url_agenda		= None
	_url_minutes	= None

	def __init__(self, meeting_date: str, meeting_type: str, meeting_agenda_url: str, meeting_minutes_url: str) -> None:
		self._date			= meeting_date
		self._type			= meeting_type
		self._url_agenda	= meeting_agenda_url
		self._url_minutes	= meeting_minutes_url

		self._write_to_csv()

	def _write_to_csv(self):
		if meeting_entry.csv_path is None:
			gmt = time.gmtime()
			meeting_entry.csv_path = os.getcwd() + "/" + str(calendar.timegm(gmt)) + ".csv"
		
		data = [self._date, self._type, self._url_agenda, self._url_minutes]
		line = ",".join(data) + "\r"
		f = open(meeting_entry.csv_path,'a')
		f.write(line)
		f.close()