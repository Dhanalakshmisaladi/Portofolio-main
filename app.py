@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    send_email(name, email, message)
    return "<h3>Thanks for contacting us!</h3><a href='/'>Back to Home</a>"

def send_email(name, email, message):
    msg = EmailMessage()
    msg['Subject'] = 'New Contact Form Submission'
    msg['From'] = 'satyasaimanojna@gmail.com'
    msg['To'] = 'satyasaimanojna@gmail.com'
    msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('satyasaimanojna@gmail.com', 'qucrkornhvhebkxx')
        smtp.send_message(msg)