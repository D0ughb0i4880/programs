import time, rotatescreen as rs # type: ignore
pd = rs.get_primary_display()
angel_list = [90, 180, 270 0] #type: ignore
for i in range(5):
    for x in angel_list:
        pd.rotate_to(x)
        time.sleep(0.5)