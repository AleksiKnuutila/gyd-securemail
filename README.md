# gyd-securemail

Simple end-to-end encryption done in the browser, without need to install apps. The user only needs to share a link in order to receive files securely. The system is tentatively created for use with [getyourdata.org](getyourdata.org), as a secure replacement for email in the transmission of personal data.

Here’s how the webapp works:

1. First we verify your e-mail. After that, our server will store your public key. We will generate a private key for you to store on your computer.
2. After this, all a sender needs is a link from you. With a simple form, they can send messages that are encrypted before leaving their browser.
3. When you receive a message, we’ll send you an e-mail. You will need your private key to access the message. 


## Development

0. Get `secret.cfg` file and copy it to `./pgpost` (ignored from
   git)
1. Install virtualenv and create a new one using `python 2.7`
2. In the virtualenv, `pip install django==1.9.8`
3. source env/bin/activate
4. pip install -r requirements.txt
5. python dev_manage.py migrate
6. ...
7. go!
