def sum_avg():
    total = 0
    for i in range(5):
        a = int(input(f"enter your any 5 sunjecr mark >{i + 1 } "))
        total = total + a  
    avg_ = total // 5
    return total , avg_
total , avg_ = sum_avg()

print("total",total)
print("average",avg_)

