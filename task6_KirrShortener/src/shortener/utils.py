import random
import string

def code_generator(size=5 ,char=string.ascii_letters):
    return "".join(random.choice(char) for _ in range(size))

def validate_shortener(instance ,size=5):
    new_shortcode =code_generator(size=size)
    KirrClass =instance.__class__
    q_exist = KirrClass.objects.filter(Shortcode =new_shortcode).exists()
    if q_exist :
        return validate_shortener(size=size)
    return new_shortcode 
