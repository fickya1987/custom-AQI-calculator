def get_PM10_Sub_Index(value):
    
    if value > 430:
        return 400 + (value + 430) * (100/80)
    elif value > 350:
        return 300 + (value - 350) * (100/80)
    elif value > 250:
        return 200 + (value - 250)
    elif value > 100:
        return 100 + (value - 100) * (100/150)
    elif value > 50:
        return value
    elif value <= 50:
        return value
    else:
        return 0

def get_PM25_Sub_Index(value):
    
    if value > 250:
        return 400 + (value - 250) * (100/130)
    elif value > 120:
        return 300 + (value - 120) * (100/130)
    elif value > 90:
        return 200 + (value - 90) * (100/30)
    elif value > 60:
        return 100 + (value - 60) * (100/30)
    elif value > 30:
        return 50 + (value - 30) * (50/30)
    elif value <= 30:
        return value * (50/30)
    else:
        return 0

def get_SO2_Sub_Index(value):
    
    if value > 1600:
        return 400 + (value - 1600) * (100/800)
    elif value > 800:
        return 300 + (value - 800) * (100/800)
    elif value > 380:
        return 200 + (value - 380) * (100/420)
    elif value > 80:
        return 100 + (value - 80) * (100/300)
    elif value > 40:
        return 50 + (value - 40) * (50/40)
    elif value <= 40:
        return value * (50/40)
    else:
        return 0

def get_NOx_Sub_Index(value):
    
    if value > 400:
        return 400 + (value - 400) * (100/120)
    elif value > 280:
        return 300 + (value - 280) * (100/120)
    elif value > 180:
        return 200 + (value - 180) * (100/100)
    elif value > 80:
        return 100 + (value - 80) * (100/100)
    elif value > 40:
        return 50 + (value - 40) * (50/40)
    elif value <= 40:
        return value * (50/40)
    else:
        return 0
    
def get_CO_Sub_Index(value):

    if value > 34:
        return 400 + (value - 34) * (100/17)
    elif value > 17:
        return 300 + (value - 17) * (100/17)
    elif value > 10:
        return 200 + (value - 10) * (100/7)
    elif value > 2:
        return 100 + (value - 2) * (100/8)
    elif value > 1:
        return 50 + (value - 1) * (50/1)
    elif value <= 1:
        return value * (50/1)
    else:
        return 0
    
def get_O3_Sub_Index(value):

    if value > 748:
        return 400 + (value - 400) * (100/539)
    elif value > 208:
        return 300 + (value - 208) * (100/539)
    elif value > 168:
        return 200 + (value - 168) * (100/40)
    elif value > 100:
        return 100 + (value - 100) * (100/68)
    elif value > 50:
        return 50 + (value - 50) * (50/50)
    elif value <= 50:
        return value * (50/50)
    else:
        return 0
    
def get_NH3_Sub_Index(value):

    if value > 1800:
        return 400 + (value - 1800) * (100/600)
    elif value > 1200:
        return 300 + (value - 1200) * (100/600)
    elif value > 800:
        return 200 + (value - 800) * (100/400)
    elif value > 400:
        return 100 + (value - 400) * (100/400)
    elif value > 200:
        return 50 + (value - 200) * (50/200)
    elif value <= 200:
        return value * (50/200)
    else:
        return 0