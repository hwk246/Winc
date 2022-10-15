# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting='Hello, <name>!'):

    return greeting.replace('<name>', name)
  

def force(mass, body='earth'):

    surface_gravity = {
    'sun':274,
    'jupiter':24.92,
    'neptune':11.15,
    'saturn':10.44,
    'earth':9.798,
    'uranus':8.87,
    'venus':8.87,
    'mars':3.71,
    'mercury':3.7,
    'moon':1.62,
    'pluto':0.58
    }
    
    return  mass * round(surface_gravity[body],1)

    

def pull(m1,m2,d):

    return (6.674*10**-11*m1*m2)/d**2
  

if __name__ == '__main__':
   greet('Doc') 
   greet('Bob', "What's up, <name>!" )
   force(10)
   force(10, 'neptune')
   pull(0.1,5.972*10**24,6.371*10**6)