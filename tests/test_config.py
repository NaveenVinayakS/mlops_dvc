def test_generic(): # function name must start with TEST
    # assert -> assertion return true(PASSED) if test case PASS.
    # individually we can run this file "pytest -v"
    # we can run this file using tox command also

    # what tox does is it will create a python virtual enviorment using tox ini file and requirements are
    # collected from -rrequirements.txt , command is "tox" if any changes in requirement the "tox -r"
    a=3
    b=3
    assert a==b