from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Mock database for FAQs
FAQ_DATA = {
    "pricing": "Our basic plan starts at $20/month, and the Pro plan is $50/month.",
    "hours": "We are open Monday to Friday, from 9:00 AM to 6:00 PM.",
    "location": "We are located in Downtown Tech City, Building 404.",
}

# Link for scheduling (e.g., Calendly)
SCHEDULING_LINK = "https://calendly.com/your-business/meeting"

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    # Get the message sent by the user
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    responded = False

    # 1. Logic for Greeting
    if 'hello' in incoming_msg or 'hi' in incoming_msg:
        msg.body("Hello! I'm your virtual assistant. How can I help you today?\n\n1. Pricing\n2. Hours\n3. Schedule a Meeting")
        responded = True

    # 2. Logic for FAQs
    elif 'pricing' in incoming_msg:
        msg.body(FAQ_DATA["pricing"])
        responded = True
    elif 'hours' in incoming_msg:
        msg.body(FAQ_DATA["hours"])
        responded = True

    # 3. Logic for Scheduling
    elif 'schedule' in incoming_msg or 'meeting' in incoming_msg or 'appointment' in incoming_msg:
        msg.body(f"I'd love to get you on the calendar! You can book a time directly here: {SCHEDULING_LINK}")
        responded = True

    # 4. Default Fallback
    if not responded:
        msg.body("I'm sorry, I didn't quite get that. You can ask about our 'pricing', 'hours', or say 'schedule' to book a meeting.")

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
