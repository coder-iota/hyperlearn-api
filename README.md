# Data API and Web Scraping
This is an internship task project by Hyperlearn.

## Instructions to use
___
1. Run the scraping script for the API to generate the JSON file.
2. Install the node dependencies.
3. Run the express.js app using node.js
  
## Running the scraping script
___
To run the python script in `api-scrapping` directory,  we need to install the dependencies using `pip`.  
Run the following command to install all dependencies with `/api-scrapping` as present working directory.
```
pip install -r requirements.txt
```
> This requires [python3](https://www.python.org/downloads/) and [pip](https://pypi.org/project/pip/) package manager on your machine, you can also use a [virtual environment](https://pypi.org/project/virtualenv/) for python.  

Then run the script using
```
py scrapper.py
```

This extracts the data from the original API and filters out the required field from it, and stores the results in a JSON file.  
The details of fields extracted and file path can be found in the script.

## Running the API
___
Before running the application for the first time, install the node dependencies by running
```
npm install
```

Then run the application using,
```
node index.js
```
The application will start running on port 5000 of your local machine. Access it on the following address,
```
http://localhost:5000/
```

## Interacting with the API
___
The API accepts two query parametes `limit` and `offset` that have default values of 10 and 0 respectively, and be used as,
```
http://localhost:5000/?limit=6&offset=10
```

This would return a JSON array with 6 objects starting at object at index 10 in original file.