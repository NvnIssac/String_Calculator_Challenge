import pytest
from string_calculator import add_string

def test_add_empty_string():
    '''
    Assert sum of an empty string as equal to zero
    '''
    assert add_string("")==0

def test_add_string_numbers():
    '''
        Assert sum of string is equal to sum, and throws error if there is a negative number or invalid literal parsing
    '''
    assert add_string("0,0,0,0,0,0,0") == 0
    assert add_string("3,5,6,8")==22
    assert add_string("3,5,6,8,1001") == 22
    assert add_string("3,5,6,8,1000,20007,4000") == 1022
    with pytest.raises(ValueError):
        assert add_string("3,5,6,-1000,4,5,-900,900,800,-50,12")
        assert add_string("35,6,-1000,4,5---900,900,800,-50,12")

def test_add_string_numbers_newline():
    '''
        Assert sum of string is equal to sum with \n in included in the string, and throws error if there is a negative number or invalid literal parsing
    '''
    assert add_string("3,\n5,6,\n8")==22
    assert add_string("3,5,\n6\n,8,1001") == 22
    assert add_string("3,5\n6,8\n1000\n,20007\n,4000") == 1022
    with pytest.raises(ValueError):
        assert add_string("3,5,6,-1000\n4,5\n-900\n900,800,-50,12")
        assert add_string("35,6\n-1000\n4,5---900,900,800,-50,12")

def test_add_string_numbers_single_delimiter():
    '''
        Assert sum of string is equal to sum with a delimiter specified in string and string starts with delimiter //, and throws error if there is a negative number or invalid literal parsing
    '''
    assert add_string("//@\n3@5@6@8")==22
    assert add_string("//,\n3,5,6,8,1001") == 22
    assert add_string("//$\n3$5$6$8$1000$4000") == 1022
    with pytest.raises(ValueError):
        assert add_string("//$\n3$5$6$-1000$4$5$-900$900$800$-50$12")
        assert add_string("//#\n35#6#-1000#4#5---900#900,@@**800,-50,12")

def test_add_string_numbers_multiple_delimiter():
    '''
        Assert sum of string is equal to sum with multiple delimiters specified in string and string starts with delimiter //, and throws error if there is a negative number or invalid literal parsing
    '''
    assert add_string("//@$,\n3@5$6,8")==22
    assert add_string("//,#^&*\n3*5^6,8#1001") == 22
    assert add_string("//$%#\n3$5%6$8%1000#4000") == 1022
    with pytest.raises(ValueError):
        assert add_string("//$@#&\n3$5&6$-1000@4$5$-900#900$800@-50$12")
        assert add_string("//#,$\n35#6,-1000#4$5---900$900,@@800,-50,12")

def test_add_string_numbers_arbitary_length_delimiter():
    '''
        Assert sum of string is equal to sum with multiple delimiters of arbitary length specified in string and string starts with delimiter //, and throws error if there is a negative number or invalid literal parsing
    '''
    assert add_string("//@@@$$$***,\n3@@@5$$$6***8") == 22
    assert add_string("//,,****\n3****5,,6,,8****1001") == 22
    assert add_string("//$%%%%#@@@\n3$5@@@6$8%%%%1000@@@@4000") == 1022
    with pytest.raises(ValueError):
        assert add_string("//$@@@@&&\n3$5&&6$-1000$4$5@@@@-900@@@@800@@@@-50$12")
    with pytest.raises(Exception):
        assert add_string("//$@@@@&&\n3$5&&6$-1000$4$5@@@@,,#####-900@@@@800@@@##@-50$12")

