import os, time
import xml.etree.ElementTree as ET
from tkinter.filedialog import askdirectory 
from tkinter import messagebox

#Function to search and get the file location using walk method..
def file_search(path="C:\\"):

	file_location=""     

	for root,dirs,files in os.walk(path):
		if "Acrobat 2017" in dirs:
			file_location=os.path.join(root,"Acrobat 2017\\Acrobat\\AMT\\application.xml")
			return file_location

	if file_location=="":	
		new_location= askdirectory()
		messagebox.showinfo("Select the Drive","Please select the DRIVE where the Adobe Acrobat 2017 is installed [Only Drive]")
		file_search(new_location[0:2]+"\\")	


#Initial main variable to start with.. 
if __name__ == "__main__":
	print("\n                  WELCOME!!\n")
	print("----------------------------------------------------------\n")
	print("""This is a tool to renew Adobe Acrobat 2017 trial period incase someone has missed 
the opportunity to get the real trial out of it. (For Educational Purpose Only)\n""")
	input("Press Enter to continue...")
	print("\n----------------------------------------------------------")
	print("\nSearching for file location...")
	time.sleep(2)
	file_location=file_search()
	print("\nFile has been found: "+file_location)
	time.sleep(2)


#parsing XML document to read and modify the data..
try:
	tree = ET.parse(file_location)
	root = tree.getroot()

	#Changing the Trial Serial number..
	new_trial=int(root[0][8].text)+1
	root[0][8].text=str(new_trial)
	tree.write(file_location)

except:
	print("\n-------------------------------------------------------------")
	time.sleep(2)
	print("\n## Encountered an Error! Try the following: ")
	time.sleep(2)
	print("\n1. Try running the script with administrator privilege")
	print("""2. Rerun the script and make sure the drive location is correct. 
Installation of Acrobat is preferred in default C:\\ drive!""")
	input("\nPress Enter to exit...")

else:
	print("\n-----------------------------------------------------------\n")
	time.sleep(2)
	print("SUCCESSFULL!!! Your 07 Days trial has been renewed with the new TrialSerialNumber - {}".format(root[0][8].text))
	print("\n -->Now launch Acrobat 2017, wait for sign in page, sign in.. have fun!")
	print("\n--------------------------------------------\n")
	print(">>>>> The Future updates will bring auto renewal. For now, enjoy editing! :) <<<<<")
	input("\nPress Enter to exit...")
