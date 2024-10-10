class Billiard: #테이블을 나타내는 객체 클래스
    
    def __init__(self,tableuse,name,start,end,paper_day,card_day):
        self.tableuse = tableuse # 사용중이면 1, 아니면 0
        self.name = name # table1~table6
        self.start = 0 # 시작 시간
        self.end = 0  # 종료 시간
        self.paper_day = 0 # 현금 수입
        self.card_day = 0 # 카드 수입
        
    def calc(self,t1,t2): # 사용 시간 체크
        t3=t2-t1
        return t3