# NovusAGENDA (Novus Agenda) Migration Tool

## License
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


## Purpose
This tool is designed for a migration of NovusDocs minutes and agendas by downloading published PDF's. Before using this tool, ensure all minutes are published in the tool and available.

## Use Case
This script is only tested to crawl novus public documents with the url in following format: "https://<em><b>{{entity-subdomain}}</b></em>.novusagenda.com/AgendaPublic/" where <em><b>{{entity-subdomain}}</em></b> is your entity's Novus Docs sub-domain.

For example: https://<em><b>sunnysideschools</em></b>.novusagenda.com/AgendaPublic/


## How this script works
1. This script crawls the novus link and captures all the links to download PDF's of Agendas and Minutes.
2. We then (manually) upload the downloaded PDF files to Google Drive and display them in a Google Sheet. 

# How to Use
1. In the file main.py, on line 11, update the </em></b>entity_subdomain</em></b> variable to your organization's novus sub-domain. In the example above, this is <em><b>sunnysideschools</em></b> , our subdomain.
2. Ensure the python requirements are installed by first navigating your terminal to this directory, then running the following command: ``` pip install -r requirements.txt ```
3. To start the process, run the main.py with the following command: ``` python main.py ```. Depending on how many entries there are, this will take several hours.
4. Upon completion of step 3, you will have a ```.csv``` named with the timestamp of when the files began scraping and a directory named ```downloads```. PDF's will be saved in the format of ```YYYY-MM-DD.Meeting Type.(Agenda or Minutes).pdf```.

## How we used this
1. We ran the script and downloaded all the PDF's.
2. Upload the PDF's to a Google Drive folder.
3. Share the Google Directory so anyone with the link can view the documents.
4. Capture the Google Drive Directory ID. When you are viewing the page, this will be in the URL, https://drive.google.com/drive/u/0/folders/<em><b>{{ThisReallyLongStringIStheDirectoryID}}/</em></b> and update it on line 4 of ```google_sheets_script.js```.
4. Create a new Google Sheet outside of the directory with the PDF's.
5. Follow instructions to [Install a Google Script](https://developers.google.com/apps-script/guides/sheets/functions#:~:text=Click%20Extensions%20%3E%20Apps%20Script%20to,script%20editor%20of%20another%20spreadsheet.). Copy and paste the content from page ```google_sheets_script.js``` into the Apps Script Editor.
6. Click Run. After around 20-30 seconds, check the Google Sheet and you will see one column with the inventory of the directory and a second column with all the links.
7. You now have a Google Sheet with your file names and URL's. We posted this to our website as is, but now you have all the data in a format you can program with as well as the added benefits of Google Drive's backups for auditing purposes.
