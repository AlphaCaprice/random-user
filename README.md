# Random user

This application uses ​https://randomuser.me/api/ for download information about random people.
You can set a number of people you want to download and up to 5 users will be saved to data base per one time.<br>
Application uses SQLAlchemy:SQLite for storage data about users.<br>
You can get information about random user from data base by pushing <br>
<b>Show Random User</b> button

## Installation

### Using git
Clone the project:
```
git clone https://github.com/AlphaCaprice/random-user.git
```
Install requirements:
```
cd random-user
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
Run the application:
```
python flask_server/app.py
```
Application will be available on your <b>localhost:5000</b>
## Example
![alt text](example.png)