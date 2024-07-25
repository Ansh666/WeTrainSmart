import random
import string

def generate_session_token():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))