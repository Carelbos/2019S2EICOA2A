import check50
import check50.c

@check50.check()
def exists():
    """cla_lab_4_1_4_4-A.c exists"""
    check50.exists("cla_lab_4_1_4_4-A.c")
    
@check50.check(exists)
def compiles():
    """cla_lab_4_1_4_4-A.c compiles"""
    check50.c.compile("cla_lab_4_1_4_4-A.c")

@check50.check(compiles)
def test1():
    """2 There are 31 days before the given month"""
    check50.run("./cla_lab_4_1_4_4-A").stdin("2", prompt = False).stdout("[Tt]here are 3[10] days before the given month").exit(0)

@check50.check(compiles)
def test2():
    """1 There are 0 days before the given month"""
    check50.run("./cla_lab_4_1_4_4-A").stdin("1", prompt = False).stdout("[Tt]here are 0 days before the given month").exit(0)
    
@check50.check(compiles)
def test3():
    """4 There are 91 days before the given month"""
    check50.run("./cla_lab_4_1_4_4-A").stdin("4", prompt = False).stdout("[Tt]here are 9[10] days before the given month").exit(0)
    
@check50.check(compiles)
def test4():
    """12 There are 335 days before the given month"""
    check50.run("./cla_lab_4_1_4_4-A").stdin("12", prompt = False).stdout("[Tt]here are 33[54] days before the given month").exit(0)
    
@check50.check(compiles)
def test5():
    """13 outputs Error: no such month in my calendar"""
    check50.run("./cla_lab_4_1_4_4-A").stdin("13", prompt = False).stdout("Error: no such month in my calend[ae]r").exit(0)
