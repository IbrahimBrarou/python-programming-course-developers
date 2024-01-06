# To install a package: pip install requests
# To install specific version of a package: pip install requests==2.9.0
# pip install requests==2.9.* >> To install latest compatible version in 2.9; which means all patches and bugs found fixed in version 2.9
# pip list >> to list all packages
# pip uninstall requets >> to remove a package
# pip install requests~=2.9.0 is exatctly the same as pip install requests==2.9.*
import requests


response = requests.get("https://google.com")
print(response)
