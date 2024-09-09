length = float(input())
width = float(input())
height = float(input())
percentage = float(input())

volume = length * width * height
volume_in_litters = volume * 0.001
required_litters = volume_in_litters * (1 - percentage/100)

print(required_litters)
