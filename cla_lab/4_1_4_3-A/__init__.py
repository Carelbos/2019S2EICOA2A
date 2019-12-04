import check50
import check50.c

@check50.check()
def exists():
    """cla_lab_4_1_4_3-A.c exists"""
    check50.exists("cla_lab_4_1_4_3-A.c")
    
@check50.check(exists)
def compiles():
    """cla_lab_4_1_4_3-A.c compiles"""
    check50.c.compile("cla_lab_4_1_4_3-A.c")

@check50.check(compiles)
def test1():
    """ 1 outputs January"""
    check50.run("./cla_lab_4_1_4_3-A").stdin("1",prompt=false).stdout("January").exit(0)

@check50.check(compiles)
def test2():
    """ 6 outputs June"""
    check50.run("./cla_lab_4_1_4_3-A").stdin("6",prompt=false).stdout("June").exit(0)
    
@check50.check(compiles)
def test3():
    """ 12 outputs December"""
    check50.run("./cla_lab_4_1_4_3-A").stdin("12",prompt=false,prompt=false).stdout("December").exit(0)
    
@check50.check(compiles)
def test4():
    """ -1 outputs Error: no such month in my calendar"""
    check50.run("./cla_lab_4_1_4_3-A").stdin("-1",prompt=false).stdout("Error: no such month in my calendar").exit(0)
    
@check50.check(compiles)
def test5():
    """ 13 outputs Error: no such month in my calendar"""
    check50.run("./cla_lab_4_1_4_3-A").stdin("13",prompt=false).stdout("Error: no such month in my calendar").exit(0)
,prompt=false,prompt=false
