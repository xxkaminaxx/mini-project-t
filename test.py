x = 2
x > 3


def test_env():
    assert ( x > 3 ),""
    print("working")

try:
    test_env()
except:
     print("didnt work ")
