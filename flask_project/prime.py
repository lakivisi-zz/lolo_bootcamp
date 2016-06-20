from flask import Flask
from prime_num import get_n_primes

app = Flask(__name__)

@app.route('/')
def hundred_primes():
	return str(get_n_primes(100))


@app.route('/<int:n>' , methods=['GET'])
def n_primes(n):
	return str(get_n_primes(n))

if __name__ == '__main__':
	app.run(debug = True)
