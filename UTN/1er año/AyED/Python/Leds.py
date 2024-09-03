def led(num):
    luz = 0
    leds = {"1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6, "0":6}
    for i in range(len(num)):
        luz += (leds[num[i]])
    return luz

nums = []
trys = int(input())
for i in range(trys):
    num = str("")
    num = input()
    nums.append(led(num))
for i in range(len(nums)):
    print(nums[i], "leds")


