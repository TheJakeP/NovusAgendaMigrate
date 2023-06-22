function get_share_links_in_directory() {

	// https://drive.google.com/drive/u/0/folders/{{ThisReallyLongStringIStheDirectoryID}}
	var directory_id = "{{ThisReallyLongStringIStheDirectoryID}}"
  
	var ss=SpreadsheetApp.getActiveSpreadsheet();
	var s=ss.getActiveSheet();
	// var c=s.getActiveCell();
	var c= s.getRange('A1:B1');
	
	var fldr=DriveApp.getFolderById(directory_id);
	var files=fldr.getFiles();
  
	var names=[],f,str;
	while (files.hasNext()) {
	  f=files.next();
  
	  names.push([f.getName(), f.getUrl()]);
	  
	}
	names.sort();
	s.getRange(c.getRow(),c.getColumn(), names.length, 2).setValues(names);
  }
  
  