import check50
import check50.c

@check50.check()
def exists():
    """max.c exists"""
    check50.exists("max.c")

@check50.check(exists)
def compiles():
    """max.c compiles"""
    check50.c.compile("max.c")

@check50.check(exists)
def simple():
    """returns maximum from 3, 19, 7"""
    check_max(numbers=[3, 19, 7])


@check50.check(exists)
def negetive():
    """returns maximum from -9, -101, -53, -74"""
    check_max(numbers=[-9, -101, -53, -74])


@check50.check(exists)
def mixed():
    """returns maximum from -993, 139, 22, -45"""
    check_max(numbers=[-993, 139, 22, -45])


def check_max(numbers: list):
    code = check50.run("./max")
    code.stdin(str(len(numbers)))
    for i in numbers:
        code.stdin(str(numbers[i]))
    program.stdout(str(max(numbers)))
    
