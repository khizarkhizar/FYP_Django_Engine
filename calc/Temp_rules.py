import numpy as np

from matplotlib.pyplot import plot


def rules(fire_lo, fire_md, fire_hi, temp_level_lo, temp_level_md, temp_level_hi, sensor_level_lo, sensor_level_md, sensor_level_hi):

    # Fuzzy Rules for temparature and gas sensors
    # Rule 1:  If temparature sensor value is <=40 and Gas sensor detect <=20ppm then Fire chances are zero[0 %]
    # Rule 2:  If temparature sensor value is >40 and <70 and Gas sensor detect <=20ppm then Fire chances are Low[20%]
    # Rule 3:  If temparature sensor value is <40  and Gas sensor detect >30ppm and <40ppm then Fire chances are Low[0-20%]

    # Equation  is   (  temp_level_lo || temp_level_md)&(gas level_lo||sensor_level_md) => fire lo

    fire_activation_lo = np.zeros_like(fire_lo)
    fire_activation_md = np.zeros_like(fire_md)
    fire_activation_hi = np.zeros_like(fire_hi)

    active_rule1 = np.fmin(temp_level_lo, temp_level_md)  # ||
    print(active_rule1)
    gas_active_lo = np.fmax(sensor_level_lo, sensor_level_md)
    act = np.fmin(active_rule1, gas_active_lo)  # &
    fire_activation_lo = np.fmin(act, fire_lo)  # &
    print("Low fire", fire_activation_lo)

    # Rule 4:  If temparature sensor value is med and Gas sensor detect med then Fire chances are mediem[20-60%]
    # Rule 5:  If temparature sensor value is >70 and <100 and Gas sensor detect >30ppm and <40ppm then Fire chances are medium[20-60%]

    # Rule 6:  If temparature sensor value is >40 and <70 and Gas sensor detect >40ppm and <60ppm then Fire chances are mediem[20-60%]
    #                        ( temp_level_md || temp_level_hi)&(gas level_md||sensor_level_hi) => fire md

    active_rule2 = np.fmax(temp_level_md, temp_level_hi)  # ||

    gas_active_md = np.fmax(sensor_level_hi, sensor_level_md)
    Act2 = np.fmin(active_rule2, gas_active_md)  # &
    fire_activation_md = np.fmin(Act2, fire_md)  # &
    print(" md fire", fire_activation_md)

    # Rule 6:  If temparature sensor value is  >100 and Gas sensor detect >60ppm then Fire chances are High[60-100%]
    # (temp level hi)&(gas level hi)=>hi

    active_rule3 = np.fmin(temp_level_hi, sensor_level_hi)
    print(active_rule3)
    fire_activation_hi = np.fmin(active_rule3, fire_hi)
    print("high fire", fire_activation_hi)

    # aggregated = np.fmax(fire_activation_lo,
    #                      np.fmax(fire_activation_md, fire_activation_hi))
    # print(aggregated)
    # # Calculate defuzzified result
    # fire = fuzz.defuzz(x_fire, aggregated, 'centroid')
    # print(fire)
    # fire_activation = fuzz.interp_membership(x_fire, aggregated, fire)  # for plot
    # print(fire_activation)

    return fire_activation_lo, fire_activation_md, fire_activation_hi


mp(data1):
    #     x_temp = np.arange(0, 151, 1)
    #     temp_lo = fuzz.trimf(x_temp, [0, 0, 50])
    #     temp_md = fuzz.trimf(x_temp, [40, 60, 81])
    #     temp_hi = fuzz.trimf(x_temp, [70, 151, 151])
    #     temp_level_lo = fuzz.interp_membership(x_temp, temp_lo, data1)
    #     # x_temp is from 0 to 100 array and temp_lo is 1.0  to 0 , now we get .85 and .825 in 6th and 7th index respectivily . so .85/2=.425 and .825/2 =.4124 then add both which is .837 which is qual_level_lo  value.
    #     temp_level_md = fuzz.interp_membership(x_temp, temp_md, data1)
    #     temp_level_hi = fuzz.interp_membership(x_temp, temp_hi, data1)
    #     return temp_level_lo, temp_level_md, temp_level_hi

    # def gas(data):
    #     x_Gas = np.arange(0, 601, 1)
    #     Gas_lo = fuzz.trimf(x_Gas, [0, 0, 200])
    #     Gas_md = fuzz.trimf(x_Gas, [150, 250, 400])
    #     Gas_hi = fuzz.trimf(x_Gas, [350, 601, 601])
    #     Gas_level_lo = fuzz.interp_membership(x_Gas, Gas_lo, data)
    #     Gas_level_md = fuzz.interp_membership(x_Gas, Gas_md, data)
    #     Gas_level_hi = fuzz.interp_membership(x_Gas, Gas_hi, data)
    #     return Gas_level_lo, Gas_level_md, Gas_level_hi

    # def flame(data):
    #     x_Flame = np.arange(50, 1000, 1)
    #     Flame_lo = fuzz.trimf(x_Flame, [50, 50, 200])
    #     Flame_md = fuzz.trimf(x_Flame, [150, 250, 500])
    #     Flame_hi = fuzz.trimf(x_Flame, [450, 550, 1000])
    #     Flame_level_lo = fuzz.interp_membership(x_Flame, Flame_lo, data)
    #     Flame_level_md = fuzz.interp_membership(x_Flame, Flame_md, data)
    #     Flame_level_hi = fuzz.interp_membership(x_Flame, Flame_hi, data)
    #     return Flame_level_lo, Flame_level_md, Flame_level_hi

    # def IR(data):
    #     x_Flame = np.arange(50, 1000, 1)
    #     Flame_lo = fuzz.trimf(x_Flame, [50, 50, 200])
    #     Flame_md = fuzz.trimf(x_Flame, [150, 250, 500])
    #     Flame_hi = fuzz.trimf(x_Flame, [450, 550, 1000])
    #     Flame_level_lo = fuzz.interp_membership(x_Flame, Flame_lo, data)
    #     Flame_level_md = fuzz.interp_membership(x_Flame, Flame_md, data)
    #     Flame_level_hi = fuzz.interp_membership(x_Flame, Flame_hi, data)
    #     return Flame_level_lo, Flame_level_md, Flame_level_hi

    # def Press(data):
    #     x_Flame = np.arange(50, 1000, 1)
    #     Flame_lo = fuzz.trimf(x_Flame, [50, 50, 200])
    #     Flame_md = fuzz.trimf(x_Flame, [150, 250, 500])
    #     Flame_hi = fuzz.trimf(x_Flame, [450, 550, 1000])
    #     Flame_level_lo = fuzz.interp_membership(x_Flame, Flame_lo, data)
    #     Flame_level_md = fuzz.interp_membership(x_Flame, Flame_md, data)
    #     Flame_level_hi = fuzz.interp_membership(x_Flame, Flame_hi, data)
    #     return Flame_level_lo, Flame_level_md, Flame_level_hi

    # def Sonar(data):
    #     x_Flame = np.arange(50, 1000, 1)
    #     Flame_lo = fuzz.trimf(x_Flame, [50, 50, 200])
    #     Flame_md = fuzz.trimf(x_Flame, [150, 250, 500])
    #     Flame_hi = fuzz.trimf(x_Flame, [450, 550, 1000])
    #     Flame_level_lo = fuzz.interp_membership(x_Flame, Flame_lo, data)
    #     Flame_level_md = fuzz.interp_membership(x_Flame, Flame_md, data)
    #     Flame_level_hi = fuzz.interp_membership(x_Flame, Flame_hi, data)
    #     return Flame_level_lo, Flame_level_md, Flame_level_hi

    # def Accelo(data):
    #     x_Flame = np.arange(50, 1000, 1)
    #     Flame_lo = fuzz.trimf(x_Flame, [50, 50, 200])
    #     Flame_md = fuzz.trimf(x_Flame, [150, 250, 500])
    #     Flame_hi = fuzz.trimf(x_Flame, [450, 550, 1000])
    #     Flame_level_lo = fuzz.interp_membership(x_Flame, Flame_lo, data)
    #     Flame_level_md = fuzz.interp_membership(x_Flame, Flame_md, data)
    #     Flame_level_hi = fuzz.interp_membership(x_Flame, Flame_hi, data)
    #     return Flame_level_lo, Flame_level_md, Flame_level_hi

    # def Humidity(data):
    #     x_Flame = np.arange(50, 1000, 1)
    #     Flame_lo = fuzz.trimf(x_Flame, [50, 50, 200])
    #     Flame_md = fuzz.trimf(x_Flame, [150, 250, 500])
    #     Flame_hi = fuzz.trimf(x_Flame, [450, 550, 1000])
    #     Flame_level_lo = fuzz.interp_membership(x_Flame, Flame_lo, data)
    #     Flame_level_md = fuzz.interp_membership(x_Flame, Flame_md, data)
    #     Flame_level_hi = fuzz.interp_membership(x_Flame, Flame_hi, data)
    #     return Flame_level_lo, Flame_level_md, Flame_level_hi

    # def Assign_sensor_values(lo, md, hi, sensors):
    #     print(lo[0, sensors-1], md[0, sensors-1], hi[0, sensors-1])
    #     return lo[0, sensors-1], md[0, sensors-1], hi[0, sensors-1]

    # def fu(request):

    #     # Fire prediction
    #     # fire parameters
    #     x_fire = np.arange(0, 101, 1)
    #     fire_zero = fuzz.trimf(x_fire, [0, 0, 0])

    #     fire_lo = fuzz.trimf(x_fire, [0, 0, 20])
    #     fire_md = fuzz.trimf(x_fire, [20, 40, 60])
    #     fire_hi = fuzz.trimf(x_fire, [50, 101, 101])

    #     fire0 = np.zeros_like(x_fire)

    #     print("1 for temp")
    #     print("2 for IR")
    #     print("3 for gas")
    #     print("4 for flame")
    #     print("5 for sonar")
    #     print("6 for pressure")
    #     print("7 for accelorameter")
    #     print("8 for humidity")

    #     print("Atleast two sensor would be selected")

    #     print(request.GET)

    #     if request.GET == {'9': ['on']}:
    #         C1 = "Potentionmeter"
    #     if request.GET == {'8': ['on']}:
    #         C1 = "sonar"
    #     if request.GET == {'7': ['on']}:
    #         C1 = "Accelerometer"
    #     if request.GET == {'6': ['on']}:
    #         C1 = "Mosture"
    #     if request.GET == {'5': ['on']}:
    #         C1 = "IIR"
    #     if request.GET == {'4': ['on']}:
    #         C1 = "Pressure"
    #     if request.GET == {'3': ['on']}:
    #         C1 = "Gas"
    #     if request.GET == {'2': ['on']}:
    #         C1 = "Flame"
    #     if request.GET == {'1': ['on']}:
    #         C1 = "Temp"

    #     total_no_sensor = 8
    #     sensors = {}
    #     workbook = xlsxwriter.Workbook(
    #         'C:/Users/khiza/projectsan/web/DataToStore.xlsx')

    #     # By default worksheet names in the spreadsheet will be
    #     # Sheet1, Sheet2 etc., but we can also specify a name.
    #     worksheet = workbook.add_worksheet("My sheet")

    #     no_of_sensors_to_fuzzy = input("input the total sensor to use")
    #     while no_of_sensors_to_fuzzy == "1":
    #         no_of_sensors_to_fuzzy = input("input the total sensor to use")
    #     for i in range(0, int(no_of_sensors_to_fuzzy)):

    #         sensors[0, i] = input("enter which sensors uses")
    #     print(sensors)

    #     loc = "C:/Users/khiza/Desktop/desktop data/keywords.xlsx"

    #     # wb = xlrd.open_workbook(loc)
    #     # sheet = wb.sheet_by_index(0)

    #     # for k in range(1, sheet.nrows):

    #     lo = {}
    #     md = {}
    #     hi = {}

    #     for i in range(0, total_no_sensor):
    #         lo[0, i] = 0
    #         md[0, i] = 0
    #         hi[0, i] = 0

    #     # we have to add excel file here:

    #     # print("tempdata", sheet.cell_value(k, 0))
    #     TempData = 150
    #     IRData = 40
    #     GasData = 600
    #     FlameData = 400
    #     SonarData = 400
    #     PresData = 400
    #     AcceloData = 400
    #     HumdData = 400
    #     lo[0, 0], md[0, 0], hi[0, 0] = temp(TempData)
    #     lo[0, 1], md[0, 1], hi[0, 1] = IR(IRData)
    #     lo[0, 2], md[0, 2], hi[0, 2] = gas(GasData)
    #     lo[0, 3], md[0, 3], hi[0, 3] = flame(FlameData)
    #     lo[0, 4], md[0, 4], hi[0, 4] = Sonar(SonarData)
    #     lo[0, 5], md[0, 5], hi[0, 5] = Press(PresData)
    #     lo[0, 6], md[0, 6], hi[0, 6] = Accelo(AcceloData)
    #     lo[0, 7], md[0, 7], hi[0, 7] = Humidity(HumdData)

    #     s1_level_lo, s1_level_md, s1_level_hi = Assign_sensor_values(
    #         lo, md, hi, int(sensors[0, 0]))
    #     # s2_level_lo,s2_level_md,s2_level_hi=Assign_sensor2_values(lo,md,hi,sensors[0,1])

    #     for i in range(0, int(no_of_sensors_to_fuzzy)-1):

    #         s2_level_lo, s2_level_md, s2_level_hi = Assign_sensor_values(
    #             lo, md, hi, int(sensors[0, i+1]))

    #         # for exponantially increase or linearly increase
    #         if sensors[0, i] == "1" or sensors[0, i] == "3" or sensors[0, i] == "4" or sensors[0, i] == "5" or sensors[0, i] == "2":
    #             s1_level_lo, s1_level_md, s1_level_hi = Temp_rules.rules(
    #                 fire_lo, fire_md, fire_hi, s1_level_lo, s1_level_md, s1_level_hi, s2_level_lo, s2_level_md, s2_level_hi)

    #         if sensors[0, i] == "6" or sensors[0, i] == "7" or sensors[0, i] == "8":
    #             s1_level_lo, s1_level_md, s1_level_hi = Temp_rules.rules(fire_lo, fire_md, fire_hi, s1_level_lo, s1_level_md, s1_level_hi, s2_level_lo,
    #                                                                      s2_level_md, s2_level_hi)
    #         aggregated = np.fmax(s1_level_lo,
    #                              np.fmax(s1_level_md, s1_level_hi))
    #         print(aggregated)
    #         # Calculate defuzzified result
    #         fire = fuzz.defuzz(x_fire, aggregated, 'centroid')
    #         print("Defuzzify", fire)
    #         fire_activation = fuzz.interp_membership(
    #             x_fire, aggregated, fire)  # for plot
    #         print(fire_activation)
    #     print(fire)

    #     # Iterate over the data and write it out row by row.

    #     worksheet.write(1, 0, TempData)
    #     worksheet.write(1, 1, GasData)
    #     worksheet.write(1, 2, FlameData)
    #     worksheet.write(1, 3, TempData)
