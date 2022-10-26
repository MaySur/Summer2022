from world import hello

def test_world():
    assert hello('MAYUR') == 'hello, MAYUR'
    
    
    
def test():
    assert hello() == 'hello, world'