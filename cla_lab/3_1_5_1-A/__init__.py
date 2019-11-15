import check50
import check50.c

@check50.check()
def exists():
    """3_1_5_1-A.c exists"""
    check50.exists("cla_lab_3_1_5_1-A.c")
    
@check50.check(exists)
def compiles():
    """3_1_5_1-A.c compiles"""
    check50.c.compile("cla_lab_3_1_5_1-A.c")
    
@check50.check(compiles)
def test1():
    """First condition is true\nSecond condition is false\nThird condition is true"""
    check50.run("./cla_lab_3_1_5_1-A").stdout("First condition is true\nSecond condition is false\nThird condition is true", regex=True).exit(0)
