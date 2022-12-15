clock = 0
x_value = {0: 1}
crt_screen = [[" "] * 40 for _ in range(6)]

for instruction in [line.strip() for line in open("input")]:
    clock += 1
    if clock not in x_value:
        x_value[clock] = x_value[clock-1]
    if x_value[clock]-1  <= (clock-1) % 40 <= x_value[clock]+1:
        crt_screen[int((clock-1)/40)][(clock-1)%40] = "█"
    if instruction.startswith("addx"):
        clock += 1
        x_value[clock] = x_value[clock-1]
        if  x_value[clock]-1  <= (clock-1) % 40 <= x_value[clock]+1:
            crt_screen[int((clock-1)/40)][(clock-1)%40] = "█"
        x_value[clock+1] = x_value[clock-1] + int(instruction.split(" ")[1])

print(sum(desired_clock*x_value[desired_clock] for desired_clock in [20, 60, 100, 140, 180, 220]))
for line in crt_screen:
    print("".join(line))
