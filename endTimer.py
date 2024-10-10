import time

def timer3():
    print("엔터를 누르면 종료합니다.")
    input()
    end_time=int(time.time()) # 종료 시간 측정
    return end_time