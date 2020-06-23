import os, time, textwrap
import xml.etree.ElementTree as ET 

#Function to search and get the file location using walk method..
def file_search(path="C:\\"):
	folder_name="Acrobat 2017"
	file_name="application.xml"
	file_location=""    
	path_track=""

	print("".center(70,"-"))
	print("\nSearching for the application folder location in...") 
	print(path+"...")

	for root,dirs,files in os.walk(path):
		if file_name in files:
			if folder_name in root:
				file_location=str(os.path.join(root,file_name))
				return file_location

	if file_location=="":
		print("\n## Could not find the Adobe installation folder in {}".format(path))
		new_location=str(input("\nPlease write the DRIVE alphabet where the Adobe Acrobat 2017 is installed [Only Alphabet]: ")[0])
		return file_search(new_location.upper()+":\\")	

#parsing XML document to read and modify the data..
def serialkey_changer():
	global tree,root
	tree = ET.parse(file_location)
	root = tree.getroot()

	#Changing the Trial Serial number..
	new_trial=int(root[0][8].text)+1
	root[0][8].text=str(new_trial)
	tree.write(file_location)

#Actions if encountered any errors
def errorhandling(e):
	print("".center(70,"-"))
	time.sleep(2)
	print("\n## Encountered an Error! Try the following: ")
	time.sleep(1)
	print("\n",e)
	print("\nTo Do:\n1. Try running the script with administrator privilege")
	print("\n".join(textwrap.wrap("2. Rerun the script and make sure the drive location is correct. Installation of Acrobat is preferred in default C:\\ drive!",90)))
	input("\nPress Enter to exit...")
	os.system('cls')

#Post-actions after successful changing the serial key
def successhandling():
	print("".center(70,"-"),"\n")
	time.sleep(2)
	print("--- SUCCESSFULL!!! Your 07 Days trial has been renewed to new TrialSerialNumber - {}".format(root[0][8].text))
	print("\n --> Now launch Acrobat 2017, wait for sign in page, sign in.. have fun!")
	print(" --> The Future updates will bring auto renewal after every 07 days. Stay tuned, enjoy editing! :)")
	print("\n","".center(70,"-"),"\n")
	input("\nPress Enter to exit...")

#Initial main variable to start with.. 
if __name__ == "__main__":
	os.system('cls')
	print("\n","WELCOME!!".center(70),)
	print("".center(70,"-"),"\n")
	print("""This is a tool to renew Adobe Acrobat 2017 trial period incase someone has missed 
the opportunity to get the real trial out of it. (For Educational Purpose Only)\n""")
	input("Press Enter to continue...\n")
	time.sleep(2)
	file_location=file_search()
	print("\nFile has been found: "+file_location,'\n')  
	try:
		serialkey_changer()
	except Exception as e:
		errorhandling(e)
	else:
		successhandling()