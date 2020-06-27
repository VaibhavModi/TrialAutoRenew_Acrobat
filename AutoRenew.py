import os, sys, time, textwrap, re
import xml.etree.ElementTree as ET 
import win32com.shell.shell as shell

def root_check():
	ASADMIN = 'asadmin'
	if sys.argv[-1] != ASADMIN:
		script = os.path.abspath(sys.argv[0])
		params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
		shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

def choices():
	global version_select
	os.system('cls')
	print("\n","WELCOME!!".center(70),)
	print("".center(70,"-"),"\n")
	print("\n".join(textwrap.wrap(">> This is a tool to renew Adobe products' trial period incase someone has missed the opportunity to get the real trial out of it. (For Educational Purpose Only)",75)))	
	print("\nThe list of products supported:\n")
	print("\n".join(textwrap.wrap("1. Adobe Acrobat 2017 2. Adobe Acrobat 2020",22)))

	try:
		version_select=int(input("\nPlease enter the index number of the product from above: "))
		if version_select==1: 
			version_select='Acrobat 2017'
		elif version_select==2: 
			version_select='Acrobat 2020'
		else:
			raise ValueError('Invalid index number.')
	except Exception as e:
		print('\n#error - {}'.format(e))
		print('\nThat was an invalid choice!')
		input('Press Enter to retry..')
		choices()

#Function to search and get the file location using walk method..
def file_search(path="C:\\"):
	folder_name=version_select
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
				print("\nFile has been found: "+file_location,'\n')
				return file_location

	if file_location=="":
		print("\n## Could not find the Adobe installation folder in {}".format(path))
		try:
			new_location=str(input("\nPlease write the DRIVE alphabet where the {} is installed or Press enter to change product: ".format(folder_name)))
			if new_location=='':
				choices()
				return file_search()
			elif new_location.isalpha():
				return file_search(new_location[0].upper()+":\\")
			else:
				raise Exception('Invalid Input.')
		except Exception as e:
			print('#error - ',e)
			input('Press enter to continue..')
			choices()
			return file_search()

#parsing XML document to read and modify the data..
def serialkey_changer():
	global tree,root
	tree = ET.parse(file_location)
	root = tree.getroot()

	#Changing the Trial Serial number..
	new_trial=int(root[0][8].text)+100
	root[0][8].text=str(new_trial)
	tree.write(file_location)

#actions if encountered any errors
def error_handling(e):
	print("".center(70,"-"))
	time.sleep(2)
	print("\n## Encountered an Error! Try the following: ")
	time.sleep(1)
	print("\n",e)
	print("\nTo Do:\n1. Try running the script with administrator privilege")
	print("\n".join(textwrap.wrap("2. Rerun the script and make sure the drive location is correct. Installation of Acrobat is preferred in default C:\\ drive!",90)))
	input("\nPress Enter to exit...")
	os.system('cls')

#post-actions after successful changing the serial key
def success_handling():
	print("".center(70,"-"),"\n")
	time.sleep(2)
	print("--- SUCCESSFULL!!! Your 07 Days trial has been renewed to new TrialSerialNumber - {}".format(root[0][8].text))
	print("\n --> Now launch Acrobat 2017, wait for sign in page, sign in.. have fun!")
	print(" --> The Future updates will bring auto renewal after every 07 days. Stay tuned, enjoy editing! :)")
	print("\n","".center(70,"-"),"\n")
	input("\nPress enter to exit...")

#Starting of the program.. 
if __name__ == "__main__":
	try:
		root_check()
		choices()
		time.sleep(2)
		file_location=file_search()
		serialkey_changer() 
	except Exception as e:
		error_handling(e)
	else:
		success_handling()