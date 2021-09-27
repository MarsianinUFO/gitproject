from flask import Flask, render_template , request

from decryptor import dec_message
from encryptor import enc_message
from flask_mail import Message, Mail

app = Flask(__name__)
mail_from_user = ''


password = ''
with open('pass.txt') as file:
    password = file.read()



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] ='ivankucer04@gmail.com'
app.config['MAIL_PASSWORD'] = password


mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Encode')
def Encode():
    return render_template('Encode.html')


@app.route('/encode_message', methods=['POST'])
def encode_message():
    encode_message = request.form['encode_message']
    encode_message = enc_message(encode_message)
    global mail_from_user
    mail_from_user = encode_message
    return render_template('encode_message.html', encode_message=encode_message)


@app.route('/send_message', methods=['GET', 'POST'])
def sending_message():
    email = request.form['user_email']
    msg=Message('message from me to me', sender='ivankucer04@gmail.com', body=mail_from_user, recipients=['',email])
    mail.send(msg)

    return '<p>Post pigeon was sended</p>'



@app.route('/Decode')
def Decode():
    return render_template('Decode.html')


@app.route('/decode_message', methods=['POST'])
def decode_message():
    decode_message = request.form['decode_message']
    decode_message = dec_message(decode_message)
    return render_template('decode_message.html', decode_message=decode_message)


app.run(debug=True)
