#! python3

import subprocess
from pprint import pprint as pp
import shutil
from configparser import ConfigParser
import psycopg2
import json

from psycopg2.extensions import JSON

'''DEPENDENCIES:
	-- dockutil (brew)
	-- shutil (pip)
	-- psycopg2 (pip)
	-- configparser (pip)
'''

# get UUID of Device
def get_hardware_uuid():
	uuidcommand = "system_profiler SPHardwareDataType | grep 'Hardware UUID'"
	uuidresult = subprocess.run(uuidcommand, stdout=subprocess.PIPE, shell=True, check=True)
	UUIDoutput = str(uuidresult.stdout.strip())
	start = "b'Hardware UUID: "
	end = "'"
	deviceUUID = UUIDoutput[UUIDoutput.find(start)+len(start):UUIDoutput.rfind(end)]
	return deviceUUID

# get database config from database.ini 
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db

# open connection to database specified in database.ini file
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# 
if __name__ == '__main__':
    connect()


def insert_dockData():
    # insert dock data into the postgres database
    sql = f"""INSERT INTO "dockGeminiMasters"(id, time, "dockDictionary")
             VALUES('{get_hardware_uuid()}', CURRENT_TIMESTAMP, '{jsondockItems}');"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Gets the users dock items and stores them in a dictionary file which will be used for $dockutil commands
def getDockItems():
	getdockcommand = 'dockutil --list --homeloc \'~/\''

	# runs dockutil and stores the output in listOfItems
	dockItemsOutput = subprocess.getoutput(getdockcommand)
	listOfItems = str(dockItemsOutput).splitlines()

	'''
	dictionaryShema = {
		'DockLocationInt':
			{
				'AppName':'',
				'AppPath':'',
				'Type':'',
				'plistPath':''
			}
	}
	'''

	dictofDockItems = {}

	# for each dock item (index of dockItem aka its location is = DockItemNumber)
	for dockItemNumber, DockItem in enumerate(listOfItems):
		
		#split the line into an iterable list:
		DockEntry = DockItem.split('\t')

		# iterate over a single dock item: APP_NAME, PATH, TYPE, PLIST_PATH
		for index, data in enumerate(DockEntry):
			dockLocation = {dockItemNumber: {}}
			if index == 0:
				dictofDockItems[dockItemNumber] = {}
				dictofDockItems[dockItemNumber]['AppName'] = data
			elif index == 1: 
				dictofDockItems[dockItemNumber]['AppPath'] = data
			elif index == 2:
				dictofDockItems[dockItemNumber]['Type'] = data
			elif index == 3:
				dictofDockItems[dockItemNumber]['plistPath'] = data

	return dictofDockItems

# Get Device UUID
deviceUUID = get_hardware_uuid()

# Get Dock Items
dockItems = getDockItems()

# Store dock items as json file
jsondockItems = json.dumps(dockItems)

# store the plist path
dockPlistPath = dockItems[0]['plistPath']

# make a backup of the plist 
shutil.copy(str(dockPlistPath), str('./'))

# insert the data into the database
insert_dockData()

