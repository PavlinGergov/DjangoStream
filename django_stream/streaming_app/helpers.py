from django.utils.six.moves import range
from time import sleep


# Example streaming of json
def stream_json():
    yield "["
    for i in range(0, 5):
        if i != 4:
            yield '{{ "Number": {} }},'.format(i)
        else:
            yield '{{ "Number": {} }}'.format(i)
        sleep(2)
    yield "]"
