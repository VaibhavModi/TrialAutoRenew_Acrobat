import os, time
import xml.etree.ElementTree as ET 

#Function to search and get the file location using walk method..
def file_search(path="C:\\"):

	folder_name="Acrobat 2017"
	file_location=""    

	print("\n----------------------------------------------------------")
	print("\nSearching for the application folder location in...") 
	print(path+"...")

	for root,dirs,files in os.walk(path):
		if folder_name in dirs:
			for root,dirs,files in os.walk(os.path.join(root,folder_name)):
				if "application.xml" in files:
					file_location=str(os.path.join(root,"application.xml"))
					return file_location

	if file_location=="":
		print("\n## Could not find the Adobe installation folder in {}".format(path))
		new_location=str(input("\nPlease write the DRIVE alphabet where the Adobe Acrobat 2017 is installed [Only Alphabet]: ")[0])
		return file_search(new_location.upper()+":\\")	


#Initial main variable to start with.. 
if __name__ == "__main__":
	
	print("\n                  WELCOME!!\n")
	print("----------------------------------------------------------\n")
	print("""This is a tool to renew Adobe Acrobat 2017 trial period incase someone has missed 
the opportunity to get the real trial out of it. (For Educational Purpose Only)\n""")
	input("Press Enter to continue...")
	time.sleep(2)
	file_location=file_search()
	print("\nFile has been found: "+file_location)  


#parsing XML document to read and modify the data..
try:
	tree = ET.parse(file_location)
	root = tree.getroot()

	#Changing the Trial Serial number..
	new_trial=int(root[0][8].text)+1
	root[0][8].text=str(new_trial)
	tree.write(file_location)

except Exception as e:
	print("\n-------------------------------------------------------------")
	time.sleep(2)
	print("\n## Encountered an Error! Try the following: ")
	time.sleep(1)
	print("\n",e)
	print("\nTo Do:\n1. Try running the script with administrator privilege")
	print("""2. Rerun the script and make sure the drive location is correct. 
Installation of Acrobat is preferred in default C:\\ drive!""")
	input("\nPress Enter to exit...")

else:
	print("\n-----------------------------------------------------------\n")
	time.sleep(2)
	print("--- SUCCESSFULL!!! Your 07 Days trial has been renewed with the new TrialSerialNumber - {}".format(root[0][8].text))
	print("\n --> Now launch Acrobat 2017, wait for sign in page, sign in.. have fun!")
	print(" --> The Future updates will bring auto renewal after every 07 days. Stay tuned, enjoy editing! :)")
	print("\n-----------------------------------------------------------\n")
	input("\nPress Enter to exit...")