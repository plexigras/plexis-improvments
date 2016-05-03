import os

command="convert  {0}.png  {1}.png -composite {2}.png"
def add(backround,over,output):
    os.system(command.format(backround,over,output))

def create(name="name",s1=0,s2=0,s3=0,s4=0,c1=0,c2=0,c3=0,c4=0):
    add("b","b",name)
    if s1 == 1:
        add(name,"s1",name)
    if s2 == 1:
        add(name,"s2",name)
    if s3 == 1:
        add(name,"s3",name)
    if s4 == 1:
        add(name,"s4",name)
    if c1 == 1:
        add(name,"c1",name)
    if c2 == 1:
        add(name,"c2",name)
    if c3 == 1:
        add(name,"c3",name)
    if c4 == 1:
        add(name,"c4",name)

create(0 ,1,1,1,1 ,0,0,0,0)
create(1 ,1,0,1,1 ,0,0,0,0)
create(2 ,1,0,1,0 ,0,0,0,0)
create(3 ,1,1,1,0 ,0,0,0,0)
create(4 ,1,0,0,1 ,0,0,1,0)
create(5 ,1,1,0,0 ,0,0,0,1)
create(6 ,0,0,0,1 ,0,1,1,0)
create(7 ,1,0,0,0 ,0,0,1,1)
create(8 ,0,0,0,0 ,1,0,1,1)
create(9 ,0,0,0,0 ,1,1,0,1)

create(10 ,0,0,0,0 ,0,1,1,0)
create(11 ,0,0,0,0 ,0,0,1,1)
create(12 ,1,1,0,1 ,0,0,0,0)
create(13 ,1,0,0,1 ,0,0,0,0)
create(14 ,1,0,0,0 ,0,0,0,0)
create(15 ,1,1,0,0 ,0,0,0,0)
create(16 ,0,0,1,1 ,0,1,0,0)
create(17 ,0,1,1,0 ,1,0,0,0)
create(18 ,0,0,1,0 ,1,1,0,0)
create(19 ,0,1,0,0 ,1,0,0,1)

create(20 ,0,0,0,0 ,0,1,1,1)
create(21 ,0,0,0,0 ,1,1,1,0)
create(22 ,0,0,0,0 ,1,1,0,0)
create(23 ,0,0,0,0 ,1,0,0,1)
create(24 ,0,1,0,1 ,0,0,0,0)
create(25 ,0,0,0,1 ,0,0,0,0)
create(26 ,0,0,0,0 ,0,0,0,0)
create(27 ,0,1,0,0 ,0,0,0,0)
create(28 ,0,0,0,1 ,0,1,0,0)
create(29 ,1,0,0,0 ,0,0,1,0)

create(30 ,0,0,0,1 ,0,0,1,0)
create(31 ,1,0,0,0 ,0,0,0,1)
create(32 ,0,0,0,0 ,0,0,1,0)
create(33 ,0,0,0,0 ,0,0,0,1)
create(34 ,0,0,0,0 ,1,0,1,0)
create(35 ,0,0,0,0 ,0,1,0,1)
create(36 ,0,1,1,1 ,0,0,0,0)
create(37 ,0,0,1,1 ,0,0,0,0)
create(38 ,0,0,1,0 ,0,0,0,0)
create(39 ,0,1,1,0 ,0,0,0,0)

create(40 ,0,0,1,0 ,1,0,0,0)
create(41 ,0,1,0,0 ,0,0,0,1)
create(42 ,0,0,1,0 ,0,1,0,0)
create(43 ,0,1,0,0 ,1,0,0,0)
create(44 ,0,0,0,0 ,0,1,0,0)
create(45 ,0,0,0,0 ,1,0,0,0)
create(46 ,0,0,0,0 ,1,1,1,1)


