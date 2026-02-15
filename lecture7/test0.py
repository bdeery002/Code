from prime import is_prime

def test_prime(n, expected):
   if is_prime(n) != expected:
       print(f"Test failed for n={n}: expected {expected}, got {is_prime(n)}")


test_prime(1, False)
test_prime(2, True)
test_prime(3, True)
test_prime(4, False)
test_prime(5, False)