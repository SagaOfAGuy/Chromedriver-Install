# Chromedriver-Install
Python script that installs the proper Chromedriver in accordance to the current Chrome browser version present on the host operating system

# Installation


Navigate to root directory 
```bash
cd ChromedriverInstall
```

Install dependecy packages in root directory using Pip3
```bash
pip3 install .
```

# Example Usage
If you want to download Chromedriver in Documents directory
```bash
ChromedriverInstall ~/Downloads
```

If you want to download Chromedriver in Downloads directory
```bash
ChromedriverInstall ~/Documents
```

If you want to download Chromedriver in the current directory
```bash
ChromedriverInstall .
```
