import requests # Documentation: docs.python-requests.org
 
key = 'your_dev_key_here' # Get your devKey from here https://pastebin.com/doc_api#1
text = "Wanted text"
t_title = "A paste title"
 
login_data = {
    'api_dev_key': key,
    'api_user_name': 'your_username',
    'api_user_password': 'your_password'
    }
data = {
    'api_option': 'paste',
    'api_dev_key': key,
    'api_paste_code': text,
    'api_paste_name': t_title,
    'api_paste_expire_date': 'example', # See https://pastebin.com/api
    'api_user_key': None,
    'api_paste_format': 'example' # See https://pastebin.com/api
    }
 
login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")
print("User token: ", login.text)
data['api_user_key'] = login.text
 
r = requests.post("https://pastebin.com/api/api_post.php", data=data)
print("Paste sent: ", r.status_code if r.status_code != 200 else "OK/200")
print("Paste URL: ", r.text)