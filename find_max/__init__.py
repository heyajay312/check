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


@check50.check(exists)
def simple():
    """returns 19 from 3, 7, 19"""
    check_max(numbers=[3, 7, 19])


@check50.check(exists)
def negetive():
    """returns -9 from -9, -101, -53, -74"""
    check_max(numbers=[-9, -101, -53, -74])


@check50.check(exists)
def mixed():
    """returns 993 from 993, -139, 22, -45"""
    check_max(numbers=[993, -139, 22, -45])


def check_max(numbers: list):
    program = check50.run("./max")
    program.stdin(str(len(numbers)))
    for i in numbers:
        print(program.stdin(str(i)))
    program.stdout(str(max(numbers)))
