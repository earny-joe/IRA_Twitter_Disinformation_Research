import wget
import glob
import os
from zipfile import ZipFile

def main(url):
    """
    Main program that takes URL to Twitter data set, and downloads it to correct
    """
    #create path variable to primary directory
    path = os.getcwd()
    # download data to zip_data folder
    wget.download(url, os.getcwd() + "/zip_data")
    print("")
    country_name = input("Enter name of country operation originated from.\n")
    try:
        file_interest = glob.glob(f"zip_data/[{country_name}]*.zip")
        for file in file_interest:
            # Create a ZipFile Object and load sample.zip in it
            with ZipFile(file, 'r') as zipObj:
                print("The following files will be extracted:", zipObj.namelist())
                # Extract all the contents of zip file in different directory
                zipObj.extractall("Twitter_disinfo_data")
    except Exception as e:
        print("Uh oh...something didn't work")
        print(e)
    
if __name__ == "__main__":
    url = input("Please enter URL to Twitter Information Operations data set.\n")
    main(url)