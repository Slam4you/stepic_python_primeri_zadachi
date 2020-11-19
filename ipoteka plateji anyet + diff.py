def diff_compute_for_month(t, s, n, k):
    p = (s / n) + (s - (t - 1) * (s / n)) * (k / 1200)
    return p

def anuet_compute_for_month(t, s, n, k):
    ka = k / 1200
    p = ((ka * (1 + ka) ** n) / ((1 + ka) ** n - 1)) * s
    return p


s, n, k = 1000000, 12, 15 # int(input()), int(input()), int(input())
t = 1    # month_count
diff_payments = []
anuet_payments = []
diff_total_bill = 0
anuet_total_bill = 0
for i in range(1, n + 1):
    p = diff_compute_for_month(t, s, n, k)
    diff_payments.append(p)
    diff_total_bill += p
    p = anuet_compute_for_month(t, s, n, k)
    anuet_payments.append(p)
    anuet_total_bill += p
    print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (t, diff_payments[i - 1], anuet_payments[i - 1]))
    t += 1
print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (diff_total_bill - s, anuet_total_bill - s))

