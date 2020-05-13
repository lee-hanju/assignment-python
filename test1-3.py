m_count = [0,0]
n = input("투입한 돈, 물건값: ")

m = n_split(',')
change = int(m[0] - int(m[1])
print("거스름돈: " + str(change))
m_count[0] = int(change/500)
change = change - m_count[0]*500
m_count[1] = int(change/100)
change = change-m_count[0]*100

print("500원 동전의 개수:" + str(m_count[0]))
print("100원 동전의 개수:" + str(m-count[1]))
