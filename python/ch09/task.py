class Phone:
    def __init__(self, company, date, color):
        print("휴대폰 생성")
        self.company = company
        self.date = date
        self.color = color

    def info(self):
        print("제조사", self.company)
        print("출고년도", self.date)
        print("색상", self.color)

    def setInfo(self, company, date, color):
        self.company = company
        self.date = date
        self.color = color
        print("제조사", self.company)
        print("출고년도", self.date)
        print("색상", self.color)


my_phone = Phone("삼성", "2025-07-18", "블랙")
my_phone.info()
my_phone.setInfo("아이폰", "2015-05-22", "실버")
