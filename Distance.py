import dist_sensor as dt

d = 1/8
p = 1/4

def calc_VJ_dist():
    for i in range(0,10):
        distance = dt.distance()
        if i == 0:
            m_dist = distance
            SRTT = 0 + d*(distance-0)
            MDEV = 0 + p*(m_dist-0)
        else:
            m_dist = abs(distance-m_dist)
            SRTT = SRTT + d*(distance-SRTT)
            MDEV = MDEV + p*(m_dist-MDEV)
    print("SRTT: ", SRTT/100, "m")
    return SRTT/10
   
