def yscr(startSpeed, finalSpeed, time):
    y = (finalSpeed - startSpeed)/time
    return y

def decor(yscr):
    def abc(startSpeed, finalSpeed, time):
        try:
            y = (finalSpeed - startSpeed)/time
        except ValueError:
            print("Vi rukogop")
            return -1
        yscr
        print("Completed distance: ", startSpeed*time + y*time**2/2 )
        return y
    return abc

print(yscr(1, 2, 3))
yscr = decor(yscr)
print(yscr(1, 2, 3))