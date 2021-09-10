import pytest
class NotInRange(Exception):
    def __init__(self,message="value not in range"):
        self.message = message
        super().__init__(self.message)



def test_generic(): # function name must start with TEST
    # assert -> assertion return true(PASSED) if test case PASS.
    # individually we can run this file "pytest -v"
    # we can run this file using tox command also

    # what tox does is it will create a python virtual enviorment using tox ini file and requirements are
    # collected from -rrequirements.txt , command is "tox" if any changes in requirement the "tox -r"
    a=5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
    # OR
    #try:
    #    if a not in range(10, 20):
    #        raise NotInRange
    #except Exception as e:
    #    print(e)