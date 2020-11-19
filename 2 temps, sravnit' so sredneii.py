"""
t0 = [float(i) for i in input().split()]
t12 = [float(i) for i in input().split()]
sr_t = float(input())
for i in range(len(t0)):
    if (t0[i] + t12[i]) / 2 > sr_t:
        print(i)

    """
"""
3.4 0.7 2.0 0.4 2.5 2.6 1.7 0.2 4.0 2.5
6.4 8.3 6.8 6.7 7.4 6.4 8.9 4.7 5.3 7.6
4.5    
    """


# Альтернативный вывод
t0 = [float(i) for i in input().split()]
t12 = [float(i) for i in input().split()]
sr_t = float(input())
print(*[i for i in range(len(t0)) if (t0[i] + t12[i]) / 2 > sr_t], sep='\n')