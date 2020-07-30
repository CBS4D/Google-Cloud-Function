


#  Google Cloud Email Function

Host your functions on google cloud and trigger them from your code.

### Prerequisites
```
Google Cloud Account with atleast free trial activated.
Function code in one of supported languages by GCF, here we will use Python.
```
Python 3.8.2
We are using Flask framework to interact/trigger our Google Cloud Function.

Gmail Account
  - activate two-step varification
  - [And generate app password for that account and note it down](https://support.google.com/accounts/answer/185833?hl=en).

### Installing

Create Virtual Environment using one of below command and then activate it.
```
virtaulenv -p python3 vnv
OR
python3 -m venv vnv
```

activate Environment
```
. vnv/bin/activate
```

Install all requirements from 'requirements.txt'.
```
pip install -r path/to/requirements.txt
```

Update config file for flask app for below values
```
GOOGLE_CLOUD_FUNCTION_URL - you will get it when you create a function on google cloud with trigger specified as HTTP
```
GOOGLE_ACCOUNT_PASSWORD - your gamil account [App Password](https://support.google.com/accounts/answer/185833?hl=en).

Go inside project folder and run below command to start flask application.
```
python main.py
```
Once our flask app is running make POST request to below url with JSON data in body and recipient will get an email with provided email body.
http://0.0.0.0:5000/api/v1/send

data sample:
```
{

"subject":  "test subject",

"sender_email":  "test@gmail.com",

"recipient_email":  "recipient@gmail.com",

"email_body":  "Hi User\n This email is from gcloud email function."

}
```