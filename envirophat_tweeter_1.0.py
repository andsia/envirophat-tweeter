import twitter
import time
from envirophat import light, motion, weather, leds

out = open('enviro.log', 'w')
out.write('light\trgb\tmotion\theading\ttemp\tpress\n')

# Connect to Twitter
# Insert your keys and secrets here
api = twitter.Api(consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='')

while True:

    try:
        lux = light.light()
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ', '')
        leds.off()
        acc = str(motion.accelerometer())[1:-1].replace(' ', '')
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure()
        out.write('%i\t%s\t%s\t%i\t%i\t%i\n' % (lux, rgb, acc, heading, temp, press))
        time.sleep(1)
        
       # Tweet
        out_str = ("Light: %i,\t RGB: %s,\t Motion: %s,\t Temp: %i,\t Press: %i,\n" %(lux, rgb, acc, temp, press))
        print(out_str)
        api.PostUpdate(out_str)
        time.sleep(900)
    except IOError:
        print("Error")
    except KeyboardInterrupt:
        exit()
    except:
        print("Twitter Error")
