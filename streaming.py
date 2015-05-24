# Importacion de metodos de la libreria Tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables que contienen las credenciales para acceder al API de Twitter
access_token = '554542781-28K3apsD3Rzr6JbINZiREyNGKLie0zTCNxiVgx6z'
access_token_secret = 'ES7Pp8P9Q1r0uiX5HjOCzqh8bRpi5od8t79a0BwXMDNhI'
consumer_key = 'Biz8D2UdBQds3wqo7EiSfyGzE'
consumer_secret = 'V5nQCb69W7LvPgBxfbl61JTU7Ql7TA2ARMOoFsdFHf7tqaJVO2'

# Listener que imprime la info de los tweets que va captando..
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    # Maneja la autentificacion de Twitter y la conexion al API del mismo.
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Filtra el flujo de datos de Twitter para obtener palabras clave como: 'podemos', 'psoe', 'pp'
    stream.filter(track=['podemos', 'pp', 'psoe'])
