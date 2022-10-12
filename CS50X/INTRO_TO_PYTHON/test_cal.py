from calculator import square



def test_pos():
    assert square(2) == 4
    assert square(3) == 9 
def test_neg():
    assert square(-2) == 4
    assert square(-3) == 9 
def test_z():
    assert square(0) == 0 



'''
####################assert##################
def test_squ():
    try:
        assert square(2) ==4
    except AssertionError:
        print('2 square is not 4') 
    try:
        assert square(3) ==9
    except AssertionError:
        print('3 square is not 9')


'''
