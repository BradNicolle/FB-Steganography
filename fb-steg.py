import sleekxmpp
import logging
import getpass
logging.basicConfig(level=logging.INFO)

def session_start(event):
    chatbot.send_presence()
    print('Session started')
    chatbot.get_roster()

def message(msg):
    if msg['type'] in ('chat','normal'):
        print('msg received')
        print(msg['body'])

        msg.reply('Thanks').send()

jid = 'brad.nicolle@chat.facebook.com'
password = getpass.getpass()
server = ('chat.facebook.com', 5222)

chatbot = sleekxmpp.ClientXMPP(jid,password)
chatbot.add_event_handler('session_start', session_start)
chatbot.add_event_handler('message', message)
chatbot.auto_reconnect = True
chatbot.connect(server)
chatbot.process(block=True)