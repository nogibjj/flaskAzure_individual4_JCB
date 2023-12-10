## Auto Scaling Flask App Using Azure Container Apps


### Project Summary


This project is a Flask web application that displays stock price data and plots using the yfinance library. The application is containerized using Docker and deployed using Azure Container Apps. The user can input a stock ticker and the application will display the latest 1 week price plot.


### Key Components

Flask App:
- `app.py` 
    - main Flask application. Contains the routes for the application.
    - utilizes yfinance library to get stock price data
    - utilizes matplotlib library to create the plot
- `templates` - HTML templates for the application including the main page and the plot page.

Docker:
- `Dockerfile` - Dockerfile to containerize the Flask application
![docker](https://github.com/nogibjj/flaskAzure_individual4_JCB/assets/33461065/2826dd60-d487-426e-bc57-7f043b3e8b8a)

Azure Container Apps:
- The Flask app has been successfully deployed using Azure Container Apps. The application is available at the following URL:
http://stock-plots-app.thankfulstone-b8f54cbf.westus2.azurecontainerapps.io
![image](https://github.com/nogibjj/flaskAzure_individual4_JCB/assets/33461065/cbdae10d-6ea1-4c18-821f-4f37dfec7305)


### Example Usage

Following the URL above, the user can input a stock ticker:
![which_ticker](https://github.com/nogibjj/flaskAzure_individual4_JCB/assets/33461065/c2f925ec-b0cb-4b1b-9798-5cfcac63accf)

Afterwards, the user will click on "Generate Plot" and will be redirected to the plot page:
![asan_plot](https://github.com/nogibjj/flaskAzure_individual4_JCB/assets/33461065/c81316f4-1123-4b82-912e-f47acb6f7f28)



### Resources
1) https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app?tabs=web-app-flask
2) https://github.com/ranaroussi/yfinance
3) https://pypi.org/project/yfinance/