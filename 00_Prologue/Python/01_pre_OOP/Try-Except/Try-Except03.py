# Try-Except-finally

def 함수():
    print("함수()에 집입했습니다.")
    try:
        print("try 구문에 집입했습니다.")
        return
        print("try 구문이 끝났습니다.")
    except:
        print("except 구문에 집입했습니다.")
    
    finally:
        print("finally 구문에 집입했습니다.")
    
    print("함수()가 끝났습니다.")
    
함수()