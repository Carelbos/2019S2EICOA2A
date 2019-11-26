import check50
import check50.c

@check50.check()
def exists():
    """cla_lab_4_1_4_1-A.c exists"""
    check50.exists("cla_lab_4_1_4_1-A.c")
    
@check50.check(exists)
def compiles():
    """cla_lab_4_1_4_1-A.c compiles"""
    check50.c.compile("cla_lab_4_1_4_1-A.c")

@check50.check(compiles)
def test1():
    """ 1 outputs January"""
    check50.run("./cla_lab_4_1_4_1-A").stdin("1").stdout("January[\n]").exit(0)

@check50.check(compiles)
def test2():
    """ 6 outputs June"""
    check50.run("./cla_lab_4_1_4_1-A").stdin("6").stdout("June[\n]").exit(0)
    
@check50.check(compiles)
def test3():
    """ 12 outputs December"""
    check50.run("./cla_lab_4_1_4_1-A").stdin("12").stdout("December[\n]").exit(0)
    
@check50.check(compiles)
def test4():
    """ -1 outputs Error: no such month in my calendar"""
    check50.run("./cla_lab_4_1_4_1-A").stdin("-1").stdout("Error: no such month in my calendar[\n]").exit(0)
    
@check50.check(compiles)
def test5():
    """ 13 outputs Error: no such month in my calendar"""
    check50.run("./cla_lab_4_1_4_1-A").stdin("13").stdout("Error: no such month in my calendar[\n]").exit(0)
