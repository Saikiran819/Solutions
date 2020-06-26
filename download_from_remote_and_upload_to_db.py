import pandas as pd
from sqlalchemy import create_engine
import pysftp
import re
import threading
import os
import time


"""
Method 1:
    
1.Set up SFTP connection with the remote server,
2.Search for the files in the given pattern using regular expressions
3.Download and save the files from the remote location to local
4.Read the saved file using pandas as a dataframe
5.Upload the dataframe into the database
"""

"""
Create the database engine to which you need to push the data.
"""
engine = create_engine("mysql+mysqldb://{user}:{password}@localhost/{db}"
                       .format(user="user",
                               password="password",
                               db="database"))

with pysftp.Connection(host='hostname', username='username', password='password') as sftp:
    for file in sftp.listdir_attr('directory_name'):
        if re.match(r'^Perf(.)+(.csv)$', file.filename):
            remoteFile = 'file.filename'
            localFile = './file.filename'
            sftp.get(remoteFile, localFile)
            while not os.path.exists(localFile):
                time.sleep(1)
            df = pd.read_csv('localFile')
            df.to_sql('CSV_TABLE', con = engine, if_exists = 'append', chunksize = 1000)


"""
Method 2 (Optimal method to save the downloadinf time using Multithreading):
    
1.Set up SFTP connection with the remote server,
2.Search for the files in the given pattern using regular expressions
3.Create a thread and trigger the target to download the files from the remote location to local.
4.Append the thread to a Threads list, start each of the thread.
5.Join all the threads in the Threads list.
6.Go through all the file names stored in local_file_names list and check if they are saved.
7.Read the saved file using pandas as a dataframe
8.Upload the dataframe into the database
"""

"""
Create the database engine to which you need to push the data.
"""
engine = create_engine("mysql+mysqldb://{user}:{password}@localhost/{db}"
                       .format(user="user",
                               password="password",
                               db="database"))

threads = []
local_file_names = []        
with pysftp.Connection(host='hostname', username='username', password='password') as sftp:
    file_names = [file.filename for file in sftp.listdir_attr('directory_name')
                  if re.match(r'^Perf(.)+(.csv)$', file.filename)]
    for file in file_names:
        remoteFile = 'file'
        localFile = '<path>/file'
        local_file_names.append(localFile)
        tn = threading.Thread(target = lambda file:sftp.get(remoteFile, localFile), args = (file,))
        threads.append(tn)
        tn.start()
    for tn in threads:
        tn.join()

for localFile in local_file_names:
    while not os.path.exists(localFile):
        time.sleep(1)
    df = pd.read_csv(localFile)
    df.to_sql('CSV_TABLE', con = engine, if_exists = 'append', chunksize = 1000)