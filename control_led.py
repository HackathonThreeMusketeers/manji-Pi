import aiy.voicehat

status_ui = aiy.voicehat.get_status_ui()

def starting():
    status_ui.status('starting')

def ready():
    status_ui.status('ready')

def listening():
    status_ui.status('listening')

def stopping():
    status_ui.status('stopping')
