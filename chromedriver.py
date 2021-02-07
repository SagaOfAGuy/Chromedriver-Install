import textwrap
import subprocess
import re
import os
import argparse
# Get Operating System 
def get_operating_system() -> str:
	return os.uname().sysname
# Get Chrome Version
def get_version() -> str: 
	chrome_version_output=subprocess.check_output(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome","--version"])
	chrome_version_text = chrome_version_output.decode('ascii')
	pattern = re.search('[0-9][0-9]',chrome_version_text)
	first_two = pattern.group(0)
	return first_two
# Download chromedriver
def download_versions_catalog(filepath: str):
	version = get_version()
	operating_system = get_operating_system()
	download_platform = {'Darwin':'chromedriver_mac64.zip','Linux':'chromedriver_linux64.zip','Windows':'chromedriver_win32.zip'}
	subprocess.check_output(["wget","https://chromedriver.storage.googleapis.com", "-O", f"{filepath}/index.html"])
	with open(f'{filepath}/index.html', 'r') as file:
		data = file.read()
		file.close()
	chromedriver_versions = re.findall(f'[0-9][0-9][.][0-9][.][0-9][0-9][0-9][0-9][.][0-9][0-9]/{download_platform[operating_system]}',data)
	chromedriver_versions.reverse()
	matching_links = [chrome_version for chrome_version in chromedriver_versions if version in chrome_version]
	subprocess.check_output(["wget",f"https://chromedriver.storage.googleapis.com/{matching_links[len(matching_links)-1]}", "-O", f"{filepath}/{download_platform[operating_system]}"])
	print("Downloading Chromedriver...")
	print("Download Success.")
	subprocess.check_output(["unzip",f"{filepath}/{download_platform[operating_system]}"])
	subprocess.check_output(["mv", "chromedriver", f"{filepath}/chromedriver"])
	print("Unzipping Chromedriver...")
	subprocess.check_output(["rm","-rf",f"{filepath}/{download_platform[operating_system]}", f"{filepath}/index.html"])
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
Chromedriver Update Script
--------------------------
Example: python3 chromedriver.py ~/Documents
Example: python3 chromedriver.py /Users/$USER/Downloads
        '''))
parser.add_argument("filepath", type=str, help='filepath for chromedriver download')
args = parser.parse_args()
if __name__=="__main__":
	download_versions_catalog(args.filepath)
