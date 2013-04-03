import cherrypy
import pywapi
from mako.template import Template

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })

class HelloWorld:
    def index(self):
        tmpl = Template(filename='index.html')
        return tmpl.render(username="berg")
    index.exposed = True

    def berg(self, area):
        the_weather = pywapi.get_weather_from_yahoo(area, "")
          
        tmpl = Template(filename='weather.html')
        tmpl_render = tmpl.render(
            conditions=the_weather['condition']['title'],
            cur_condition=the_weather['condition']['text'],
            cur_temp=the_weather['condition']['temp'],
            humidity=the_weather['atmosphere']['humidity'],
            pressure=the_weather['atmosphere']['pressure'],
            forecast_high=the_weather['forecasts'][1]['high'],
            forecast_low=the_weather['forecasts'][1]['low'], 
            forecast_text = the_weather['forecasts'][1]['text'])

        return tmpl_render
    berg.exposed = True

cherrypy.quickstart(HelloWorld())
