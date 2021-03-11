import hashlib as hs
import logging
import random
import string
import timeit
import plotly.express as px


def Hash(input: str) -> list:

    logger = logging.getLogger('hashing function')
    logging.basicConfig(level=logging.DEBUG)

    listOfTimes = []
    listOfHashes = []

    for hash in hs.algorithms_available:

        out = hs.new(hash, input.encode('UTF-8'))

        time = timeit.timeit(lambda: hs.new(hash, input.encode("UTF-8")))

        if hash.startswith('shake'):
            s = str(out.hexdigest(16))
        else:
            s = str(out.hexdigest())
        logger.info(hash + ': ' + s + ' , (t = ' + str(time) + ')')
        listOfHashes.append(out)
        listOfTimes.append(time)

    return listOfTimes

def HashFile(filename: str):
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

def GenerateString(size: int = 10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

def RepresentHashTime(size: int = 10):
    data = {
        'length': [],
        'time': []
    }
    for i in range(1, size + 1):
        randomString = GenerateString(i)
        data['length'].append(len(randomString))
        data['time'].append(timeit.timeit(lambda: hs.new('md5', randomString.encode("UTF-8"))))

    plot = px.line(data, x='length', y='time')
    plot.show()




print(Hash('text'))

print(HashFile('file.txt'))

RepresentHashTime()