import sys
import dumper

def log(arg):
    f = open("dumper.log", "a")
    f.write(arg + "\n")
    f.close()

def qdump__Hase(d,value):
    log("start")

    size = int(d.call('int', value, 'size'))
    log("size = {}".format(size))

    for pos in range(size):
        log("v = {}".format(pos))
        # d.call('int&', value, 'operator[]',pos)


    d.putValue("i = {}".format(value))
    d.putNumChild(1)
    if d.isExpanded():
        with dumper.Children(d):
            d.putSubItem("numbers[1]", value["numbers"])
    log("end")
