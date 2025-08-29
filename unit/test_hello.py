
# TESTING STRINGS -----------------------------------------------------------------------------------------------------



# from hello import hello
# def test_hello():
#     assert hello("David") == "hello, David"
#     assert hello() == "hello, world"
    
    
    
# from hello import hello
# def test_default():
#     assert hello() == "hello, world"

# def test_argument():
#     assert hello("David") == "hello, David"

# def test_general():
#     for name in ["David", "Sarah", "John"]:
#         assert hello(name) == f"hello, {name}"




from hello import hello
def test_default():
    assert hello() == "hello, world"
  
def test_argument():
    assert hello("David") == "hello, David"