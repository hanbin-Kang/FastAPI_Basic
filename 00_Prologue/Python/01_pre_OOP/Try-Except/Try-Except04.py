# 두 가지 숫자를 입력받고 그 값을 나누기
nums = input("숫자 입력> ").split()

try:
	int_nums = [int(x) for x in nums]
	print(int_nums[0] / int_nums[1])
except ValueError:
	print("숫자를 입력해주세요.")
except ZeroDivisionError:
	print("0으로 나눌 수 없습니다.")
except IndexError:
    print("두 가지 숫자를 입력해야 합니다.")
else:
	print("계산 성공!")
finally:
	print("프로그램 종료")
