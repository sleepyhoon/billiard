import time

def timer2():
    print('엔터를 누르면 시작합니다.')
    input()
    start_time = int(time.time()) # 시작 시간 측정
    return start_time