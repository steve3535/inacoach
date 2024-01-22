from flask import Flask, url_for, flash, redirect,request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = '123456'  # Needed for flashing messages

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'diana@inacoach.com'
app.config['MAIL_PASSWORD'] = 'Stevana2019'
app.config['MAIL_DEFAULT_SENDER'] = 'diana@inacoach.com'
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    # Process the email, e.g., save it to a database
    # print("Received email:", email)
    try:
        # cmd_output=subprocess.run(['ssh',f'ubuntu@{PUBLIC_IP}','sudo','useradd','-m',email,'-s','/bin/bash'],text=True,capture_output=True)
        # print(cmd_output)
        print("Hello")
    except Exception as e: 
        print(e)
    try:
      msg = Message("Inscription workshop 'La confiance en soi'", recipients=[email])
      msg.body = f"Thank you for registering!\nusername = {first_name}"
      mail.send(msg)
    except Exception as e:
        print("bad credentials for the mail or someth else ...",e)

    flash(f"Merci pour votre inscription ! Veuillez vérifier votre email")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="5001")

