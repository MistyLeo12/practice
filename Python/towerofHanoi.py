def move(start,target):
    print("Move from {} to {}".format(start,target))

def moveVia(start,helper,target):
    move(start,helper)
    move(helper,target)

def tower(disks, start, helper, target):
    if disks == 0:
        return
    else:
        tower(disks-1, start, helper, target)
        move(start, target)
        tower(disks-1, helper, start, target)
    
tower(12, "A", "B", "C")

