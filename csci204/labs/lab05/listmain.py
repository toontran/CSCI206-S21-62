from arraylist import *
from ListException import *
import traceback

def main():
    x = List()
    # x.insert("a", 0)
    test(x)
   
def test(x):
    if len(x) != 0: print("original len bad. Expected: 0 Got:", len(x))
    try:
        z = x.peek(-3)
        print("Peek index -3 did not raise an exception")
    except ListException:
        pass
    except:
        print(traceback.format_exc())
        print("Negative index caused peek to raise an exception but it wasn't a list exception")
    try:
        z = x.peek(0)
        print("Peek index 0 on an empty list did not raise an exception")
    except ListException:
        pass
    except:
        print("Index 0 caused peek to raise an exception when the list was empty but it wasn't a list exception")
    try:
        z = x.peek(1)
    except ListException:
        pass
    except:
        print("Index 1 caused peek to raise an exception when the list was empty but it wasn't a list exception")
    try:
        z = x.peek(5000)
        print("Peek index 5000 did not raise an exception on an empty list")
    except ListException:
        pass
    except:
        print("Index 5000 caused peek to raise an exception when the list was empty but it wasn't a list exception")

    # insert only
    x.insert('a', 0)
    if len(x) != 1: print("len bad after insert-only. Expected: 1 Got:", len(x))
    #if str(x) != "a ": print("order/contents bad after insert-only. Expected: a Got:", str(x))
    try:
        z = x.peek(-3)
    except ListException:
        pass
    except:
        print("Negative index caused peek to raise an exception but it wasn't a list exception")
    try:
        z = x.peek(1)
    except ListException:
        pass
    except:
        print("Index 1 caused peek to raise an exception (when only index 0 was filled) but it wasn't a list exception")
    try:
        z = x.peek(0)
        if z != 'a': print("peek bad after insert-only. Expected 'a' in index 0, Got", z)
    except:
        print("Peek after insert-only raised an exception on a good index")

    # insert first
    x.insert('b', 0)
    if len(x) != 2: print("len bad after insert-first. Expected: 2 Got:", len(x))
    #if str(x) != "b a ": print("order/contents bad after insert-first. Expected: b a Got:", str(x))
    try:
        z = x.peek(0)
        if z != 'b': print("peek bad after insert-only. Expected 'b' in index 0, Got", z)
    except:
        print("Peek after insert-first raised an exception on a good index")
    try:
        z = x.peek(1)
        if z != 'a': print("peek bad after insert-only. Expected 'a' in index 1, Got", z)
    except:
        print("Peek after insert-only raised an exception on a good index")

    # insert last
    x.insert('c',2)
    if len(x) != 3: print("len bad after insert-last. Expected: 3 Got:", len(x))
    #if str(x) != "b a c ": print("order/contents bad after insert-last. Expected: b a c Got:", str(x))
    try:
        z = x.peek(0)
        if z != 'b': print("peek bad after insert-only. Expected 'b' in index 0, Got", z)
    except:
        print("Peek after insert-last raised an exception on a good index")
    try:
        z = x.peek(1)
        if z != 'a': print("peek bad after insert-only. Expected 'a' in index 1, Got", z)
    except:
        print("Peek after insert-last raised an exception on a good index")
    try:
        z = x.peek(2)
        if z != 'c': print("peek bad after insert-only. Expected 'c' in index 2, Got", z)
    except:
        print("Peek after insert-last raised an exception on a good index")

    # insert middle
    x.insert('d', 1)
    if len(x) != 4: print("len bad after insert-middle. Expected: 4 Got:", len(x))
    #if str(x) != "b d a c ": print("order/contents bad after insert-middle. Expected: b d a c Got:", str(x))
    try:
        z = x.peek(0)
        if z != 'b': print("peek bad after insert-middle. Expected 'b' in index 0, Got", z)
    except:
        print("Peek after insert-middle raised an exception on a good index")
    try:
        z = x.peek(1)
        if z != 'd': print("peek bad after insert-middle. Expected 'd' in index 1, Got", z)
    except:
        print("Peek after insert-middle raised an exception on a good index")
    try:
        z = x.peek(2)
        if z != 'a': print("peek bad after insert-middle. Expected 'a' in index 2, Got", z)
    except:
        print("Peek after insert-middle raised an exception on a good index")
    try:
        z = x.peek(3)
        if z != 'c': print("peek bad after insert-middle. Expected 'c' in index 3, Got", z)
    except:
        print("Peek after insert-middle raised an exception on a good index")

    # insert middle again and again
    x.insert('e', 2)
    x.insert('f', 2)
    if len(x) != 6: print("len bad after several inserts. Expected: 6 Got:", len(x))
    #if str(x) != "b d f e a c ": print("order/contents bad after several inserts. Expected: b d f e a c Got:", str(x))

    # delete last
    x.delete(5)
    if len(x) != 5: print("len bad after delete-last. Expected: 5 Got:", len(x))
    #if str(x) != "b d f e a ": print("order/contents bad after delete-last. Expected: b d f e a Got:", str(x))
    try:
        z = x.peek(3)
        if z != 'e': print("peek bad after delete-last. Expected 'e' in index 3, Got", z)
    except:
        print("Peek after delete-last raised an exception on a good index")
    try:
        z = x.peek(4)
        if z != 'a': print("peek bad after insert-middle. Expected 'a' in index 4, Got", z)
    except:
        print("Peek after delete-last raised an exception on a good index")
    try:
        z = x.peek(5)
        print("Peek index 5 on a list with good indices 0-4 did not raise an exception after a delete-last")
    except:
        pass

    # delete first
    x.delete(0)
    if len(x) != 4: print("len bad after delete-first. Expected: 4 Got:", len(x))
    #if str(x) != "d f e a ": print("order/contents bad after delete-first. Expected: d f e a Got:", str(x))
    try:
        z = x.peek(0)
        if z != 'd': print("peek bad after delete-first. Expected 'd' in index 0, Got", z)
    except:
        print("Peek after delete-first raised an exception on a good index")
    try:
        z = x.peek(3)
        if z != 'a': print("peek bad after delete-first. Expected 'a' in index 3, Got", z)
    except:
        print("Peek after delete-first raised an exception on a good index")
    try:
        z = x.peek(4)
        print("Peek index 4 on a list with good indices 0-3 did not raise an exception after a delete-first")
    except:
        pass

    # delete middle
    x.delete(2)
    if len(x) != 3: print("len bad after delete-middle. Expected: 3 Got:", len(x))
    #if str(x) != "d f a ": print("order/contents bad after delete-middle. Expected: d f a Got:", str(x))
    x.delete(1)
    x.insert('g', 1)
    if len(x) != 3: print("len bad after delete-then-insert. Expected: 3 Got:", len(x))
    #if str(x) != "d g a ": print("order/contents bad after delete-then-insert. Expected: d g a Got:", str(x))
    try:
        z = x.peek(0)
        if z != 'd': print("peek bad after delete-middle. Expected 'd' in index 0, Got", z)
    except:
        print("Peek after delete-middle raised an exception on a good index")
    x.delete(2)
    x.delete(1)

    # delete only
    x.delete(0)
    if len(x) != 0: print("len bad after delete-only. Expected: 0 Got:", len(x))
    #if str(x) != "": print("order/contents bad after delete-only. Expected: Got:", str(x))
    try:
        z = x.peek(0)
        print("Peek index 0 on an empty list did not raise an exception after delete-only")
    except ListException:
        pass
    except:
        print("Index 0 caused peek to raise an exception when the list was empty after delete-only but it wasn't a list exception")

main()
