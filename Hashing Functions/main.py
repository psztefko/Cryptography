import hashlib as hs
import logging
import random
import string
import timeit
import plotly.express as px


def calculate_hash_time(input: str) -> list:

    """Hash input and calculate time for each hashing function"""

    logger = logging.getLogger('hashing function')
    logging.basicConfig(level=logging.DEBUG)

    listOfTimes = []
    listOfHashes = []

    #hash input using every avaliable hashing method
    for hash in hs.algorithms_available:

        out = hs.new(hash, input.encode('UTF-8'))

        #calculate time of hashing
        time = timeit.timeit(lambda: hs.new(hash, input.encode("UTF-8")))

        #shake hashes require additional argument so we're catching them here
        if hash.startswith('shake'):
            s = str(out.hexdigest(16))
        else:
            s = str(out.hexdigest())
        logger.info(hash + ': ' + s + ' , (t = ' + str(time) + ')')
        listOfHashes.append(out)
        listOfTimes.append(time)

    return listOfTimes

def hash_file(filename: str) -> str:

    """ Hash file using filename passed to function """

    try:
        with open(filename, 'rb') as file:
            out = hs.md5()
            while True:
                chunk = file.read(out.block_size)
                if not chunk:
                    break
                out.update(chunk)
        return out.hexdigest()

    except FileNotFoundError:
        raise FileNotFoundError('File not found')

def generate_string(size: int = 10) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

def draw_hash_time_plot(size: int = 10):

    """ Creates list of sting lengths and time """

    data = {
        'length': [],
        'time': []
    }
    for i in range(1, size + 1):
        randomString = generate_string(i)
        data['length'].append(len(randomString))
        data['time'].append(timeit.timeit(lambda: hs.new('md5', randomString.encode("UTF-8"))))

    plot = px.line(data, x='length', y='time')
    plot.show()




print(calculate_hash_time('text'))

print(hash_file('file.txt'))

draw_hash_time_plot()