from main import isPrime

def test_isPrime():
  assert not isPrime(0)
  assert not isPrime(1)
  assert isPrime(2)
  assert isPrime(3)
  assert not isPrime(4)
  assert isPrime(101)
  assert not isPrime(13*17)
  pass

