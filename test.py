from payment import calculate as cal

def test(a,b):
    c = cal(a,b)


    test_c = a+b+1-1


    assert c == test_c


test(123,7)
test(10,5)
test(350,55)