# Nearby-search
List of beer restaurants near given address.

# How to run
## Step 1: Create Google_api_key.txt file
1. Create a Google Map API key, follow guilines from [Google Docs](https://developers.google.com/places/web-service/get-api-key)
2. Create a txt file, copy your API key into this file then save as "Google_api_key.txt"
## Step 2: Run script  
1. Open terminal, ```run cd ~ && git clone https://github.com/hoangvux116/Nearby-search```
2. Create a virtual environment:
```cd Nearby-search```  
```virtualenv -p python3 venv```
3. Activate this venv and install requirement packages.  
```source venv/bin/activate```  
```pip install -r requirements.txt```
4. Run script
```python3 nearby_search.py```
