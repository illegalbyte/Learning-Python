#! python3
# zipFile.py - Copies a directory into zip file whose name increments

import zipfile, os

def backupToZip(folder):
	# back up the entire "folder" into a ZIP
	
	folder = os.path.abspath(folder)

	# figure out what to call the zip file 
	number = 1 
	while True:
		zipFilename = os.path.basename(folder)+'_'+str(number)+'.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1 

	# Create Zip file
	print(f'Creating {zipFilename}...')
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	# walk the entire folder tree and compress the files in each folder
		# os.walk() in a for loop returns the iteration's 
		# current folder name, subfolders in that folder, and the filenames in that folder
	for foldername, subfolders, filenames in os.walk(folder):
		print(f'Adding files in {foldername}...')
		# Add the current folder to the zip
		backupZip.write(foldername)

		# Add all the files in this folder to the ZIP file.
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue #dont back up the backup ZIP files
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()
	print('Done.')


backupToZip('/Users/lewis/Documents/GitHub')
