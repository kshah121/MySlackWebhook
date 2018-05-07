# MySlackWebhook


## Basic Usage
 - Basically with this integration, we will be able to send messages to the slack channel and also a slash command to get a random image.
 - An app was created to post the messages to the slack channel.
testing webhook integration
Initial steps to start the environments
    - `virtualenv env`
    - `source env/bin/activate`
    - `pip install -r requirements.txt`
    - `source secrets.sh`
    - `lt --port 5000 --subdomain shinynewslash` -- Execute this step in a different terminal. It will generate a url and you will have to use this new url to update the /url path in the settings of the slash command. Eg: 'https://tall-tiger-98.localtunnel.me/hello' 
    - `python webhookintegration.py`


##SlashCommand Details
- Now once the above commands are executed, you can type '/draw' in the slack channel and see a random image being generated.
- Currently the API that is being used, generates a random image when called from a web browser, but when executed in the slack channel it returns the same image.  (i did not want to spend more time debugging it, but it can be fixed probably by using some other available apis out there)


##Webhook weather Details
- The webhook integration can be called by executing the API call "https://tall-tiger-98.localtunnel.me/webhook" (again the initial localtunnel call will change once the server is stopped and restarted)
- By executing the call it will send out the weather details of the static zipcode that is being used within the code.



##Information
- Once we generate the urls as mentioned above, they are valid only for the time the servers are running.
- As soon as the servers are stopped, it will generate new urls and we will have to update again.
- This can be avoided by deploying this on an ongoing AWS or cloud service and keep it running there, but for now i came up with this solution.

    
