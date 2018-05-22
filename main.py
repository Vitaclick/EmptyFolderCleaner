import os, time, re
import schedule
import logging
# from log import log
logging.basicConfig(filename="hey.log", filemode="w", level=logging.DEBUG)

def deleteEmptyFolders():
    prjPath = r"C:\#Coding\testLib"
    # Retrieve all element in RSN directory  
    for root, folders, files in os.walk(prjPath):
        for folder in folders:
            if ".rvt" in root or ".rvt" in folder:
                continue
            folderPath = os.path.join(root, folder)
            if not len(os.listdir(folderPath)) > 0:
                # Check creation time
                stats = os.stat(folderPath)
                folderAgeInHours = (time.time() - stats.st_ctime) / 3600
                # Delete if folder age is greater than 168 hours (2 weeks)
                if folderAgeInHours > 0:
                    try:
                        os.rmdir(folderPath)
                        logging.debug(folderPath)
                    except Exception as err:
                        logging.exception(" Не удалось удалить папку: " + err.msg)


if __name__ == "__main__":
    # Define sheduler
    schedule.every(4).seconds.do(deleteEmptyFolders)
    while True:
        schedule.run_pending()
        time.sleep(1)
