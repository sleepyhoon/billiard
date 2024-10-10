import sys
sys.path.append("C:\\Users\\My\\Desktop\\billiard")
import endTimer
import startTimer
import Billiard
import random

print("1~6번 당구대가 준비되어 있습니다.")
print("1,2번은 포켓볼 전용, 3~6번은 사구 전용 테이블 입니다.")

table1 = Billiard.Billiard(False,"table1",0,0,0,0) # 테이블 6개 생성
table2 = Billiard.Billiard(False,"table2",0,0,0,0)
table3 = Billiard.Billiard(False,"table3",0,0,0,0)
table4 = Billiard.Billiard(False,"table4",0,0,0,0)
table5 = Billiard.Billiard(False,"table5",0,0,0,0)
table6 = Billiard.Billiard(False,"table6",0,0,0,0)

table = [table1,table2,table3,table4,table5,table6] # 원활한 코딩을 위해 리스트 작성함

lasttable=[] # 사용하지 않은 테이블 리스트


while True:
    
    print("-"*60)
    print("-"*60)
    
    inputNum=int(input("손님이 오셨다면 1번, 계산하실 땐 2번, 빈 테이블 확인은 3번, 매출 확인은 4번, 프로그램 종료는 5번>>>"))
    
    if inputNum==1: # 손님이 오심
        
        service=int(input("포켓볼은 1번, 사구는 2번>>>")) 
        
        if service==1:
            
            while True:
                
                pocket=int(random.randint(1,2)) # 1,2번 테이블 중 랜덤 배정
                if table[pocket-1].tableuse == False: # 테이블이 빈 테이블이라면
                    print("table",pocket,"을 이용하세요")
                    table[pocket-1].tableuse = True # 이제 배정된 테이블은 사용불가
                    table[pocket-1].start = int(startTimer.timer2()) # 타이머 시작
                    break
                if table1.tableuse == True and table1.tableuse == True: #남은 자리가 없다면
                    print("포켓볼 테이블이 꽉 찼습니다. 죄송합니다.")
                    break
            for i in range(6):
                 if table[i].tableuse == False:
                     if table[i].name not in lasttable: # 이미 lasttable의 요소라면 추가x
                        lasttable.append(table[i].name)
                 elif table[i].tableuse == True:
                     if table[i].name in lasttable: # 사용중이라면 lasttable에서 제거
                         string = table[i].name
                         lasttable.remove(string)
                         
            print("현재 남은 테이블:",lasttable) 
            
        if service==2:
            
            while True:
                pocket=int(random.randint(3,6)) 
                if table[pocket-1].tableuse == False: 
                    print("table",pocket,"을 이용하세요")
                    table[pocket-1].tableuse = True
                    table[pocket-1].start = int(startTimer.timer2())
                    break
                if table3.tableuse == True and table4.tableuse == True and table5.tableuse == True and table6.tableuse == True:
                    print("사구 테이블이 꽉 찼습니다. 죄송합니다.")
                    break
                          
            for i in range(6):
                 if table[i].tableuse == False:
                     if table[i].name not in lasttable:
                         lasttable.append(table[i].name)
                 elif table[i].tableuse == True:
                     if table[i].name in lasttable:
                         string = table[i].name
                         lasttable.remove(string)
                
            print("현재 남은 테이블:",lasttable)
            
    if inputNum==2: # 손님이 다 이용하시고 계산할 때
        
        tablename=input("이용하신 테이블 이름 입력>>>") # table1 이런식으로 입력
    
        for i in range(1,7):
            
            if tablename==table[i-1].name:
                table[i-1].end = int(endTimer.timer3()) #작동되던 타이머 스탑
                time=table[i-1].calc(table[i-1].start,table[i-1].end) # 사용시간 계산
                table[i-1].tableuse = False # 이제 이 테이블 사용 가능
                print("이용하신 시간:{}초".format(time))
                cost = time*2.5 # 10분에 1500원 ---> 1초에 2.5원
                print("총 금액:{}원".format(cost))
                
                HowtoPay=int(input("결제 방법 선택(1은 카드,2은 현금)>>>"))                
                if HowtoPay==1: # 카드 결제
                    print("카드로 결제 되었습니다. 안녕히 가세요.")
                    table[i-1].card_day = table[i-1].card_day + cost # 카드 수익
                    
                if HowtoPay==2: # 현금 결제
                    
                    print("현금으로 결제 하겠습니다.")
                   
                    while True:
                        
                        total=int(input("받은 금액 입력>>>"))
                        
                        if total < cost :
                            print("내신 금액이 부족합니다.")
                            
                        if total >= cost:
                            print("계산이 완료되었습니다. 감사합니다.")
                            rest = total - cost
                            print("잔돈:{}원".format(rest))
                            break
                    table[i-1].paper_day = table[i-1].paper_day + cost # 현금 수익
                lasttable.append(table[i-1].name) # 빈 테이블 리스트에 추가
        
        
    if inputNum==3: # 현재 빈 테이블 리스트 보여주기
        print("현재 비어있는 테이블:",lasttable) 

    if inputNum==4:    #매출 관리하기
        sum=0
        for i in range(6):
            sum=sum+table[i].card_day+table[i].paper_day # 현금 수익과 카드 수익 합치기
        print("총 수입:{}원".format(sum))
        
    if inputNum==5: # 프로그램 종료
        print("프로그램을 종료합니다.")
        break
