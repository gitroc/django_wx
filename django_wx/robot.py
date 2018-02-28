from werobot import WeRoBot

from django_wx.chatter import chatter
from django_wx.echo import echo

robot = WeRoBot(enable_session=False,
                token='roc1234567890',
                app_id='wx43a2c40cb4d58628',
                app_secret='0e52f97108d00e44d19b89e8e5b4fa05',
                encoding_aes_key='4oLsfXEA1yQDPs3fyPLrvNph2Vpap6FCP4UrYqdxGpG')


@robot.text
def text(message):
    # return chatter(message)
    return echo(message)


@robot.image
def image(message):
    return 'image'


@robot.location
def location(message):
    return 'location'


@robot.link
def link(message):
    return 'link'


@robot.voice
def voice(message):
    return 'voice'


@robot.unknown
def unknown(message):
    return 'unknown'


@robot.subscribe
def subscribe(message):
    return robot.client.get_user_info()


@robot.unsubscribe
def unsubscribe(message):
    return '感谢您曾经注程序员读历史'


@robot.click
def click(message):
    if message.key == "history":
        return 'I`m a history'
    elif message.key == "poem":
        return 'I`m a poem'


@robot.view
def view(message):
    return 'view'


@robot.location_event
def location_event(message):
    return 'location_event'


@robot.unknown_event
def unknown_event(message):
    return 'unknown_event'


@robot.error_page
def error_page(message):
    return 'error_page'
