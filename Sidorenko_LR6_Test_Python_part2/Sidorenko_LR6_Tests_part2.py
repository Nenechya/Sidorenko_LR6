from Sidorenko_LR6_Methods_part2 import one_or_more, cut_info, a_to_z

def test_cut_info():
    assert cut_info('a-1') == False
    assert cut_info('aaa') == False
    assert cut_info('a-z') == True

def test_one_more():
    assert one_or_more('aaa') == False
    assert one_or_more('a-a') == True
    assert one_or_more('a-z') == False

def test_a_z():
    assert a_to_z('a-z') == 'abcdefghijklmnopqrstuvwxyz'
    assert a_to_z('A-Z') == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert a_to_z('h-o') == 'hijklmno'
    assert a_to_z('Q-Z') == 'QRSTUVWXYZ'
    assert a_to_z('J-J') == 'J'