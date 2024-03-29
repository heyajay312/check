import check50
import check50.c


@check50.check()
def exists():
    """max.c exists"""
    check50.exists("max.c")


@check50.check(exists)
def compiles():
    """max.c compiles"""
    check50.c.compile("max.c", lcs50=True)


@check50.check(compiles)
def simple():
    """returns maximum from 3, 7, 19"""
    check_max(numbers=[3, 7, 19])


@check50.check(compiles)
def negetive():
    """returns maximum from -9, -101, -53, -74"""
    check_max(numbers=[-9, -101, -53, -74])


@check50.check(compiles)
def mixed():
    """returns maximum from 993, -139, 22, -45"""
    check_max(numbers=[993, -139, 22, -45])


def check_max(numbers: list):
    program = check50.run("./max")
    program.stdin(str(len(numbers)))
    for i in numbers:
        program.stdin(str(i))
    program.stdout(str(max(numbers)))
