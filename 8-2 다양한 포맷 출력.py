# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

#양수일 땐 +로 표시, 음수일 땐 -로 표시 -> 숫자 앞에 부호 적기
print("{0: >+10}".format(+500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000000))

# 3자리 마다 콤마를 찍어주고, +- 부호도 붙이기 # {}안에는 + 만 적기 
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))

# 3자리 마다 콤마 찍고, +-부호 붙이고, 빈칸엔 ^표시, 왼쪽 정렬
print("{0:^<+30,}".format(100000000000000))

#소수점 출력 {0:f} , n째자리까지만 표시 {0:.nf}
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))






