# Chromedriver-Install
Python script that installs the proper Chromedriver in accordance to the current Chrome browser version

### Installation
```bash 
# Clone this github repository
git clone https://github.com/SagaOfAGuy/Chromedriver-Install.git

# Navigate to root directory 
cd ChromedriverInstall

# Install dependecy packages in root directory using Pip3
pip3 install .
```

### Example Usage
```bash
# If you want to download Chromedriver in the /home/$USER/Documents directory
ChromedriverInstall ~/Downloads

# If you want to download Chromedriver in the /home/$USER/Downloads directory
ChromedriverInstall ~/Documents

# If you want to download Chromedriver in the current directory
ChromedriverInstall .
```
