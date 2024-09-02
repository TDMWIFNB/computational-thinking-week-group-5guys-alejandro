from file import naming as name_v
from alejandro import get_name as name_a
from daniel import get_name as name_d
from sina import get_name as name_s
from walter import get_name as name_w
from name import get_name as name_g

def group_story():
    return "This is Team 5 Guys + Alejandro. We are: "+ name_v() + " " + name_a() + " " + name_d() + " " + name_s() + " " + name_w() + " " + name_g()

print(group_story())




