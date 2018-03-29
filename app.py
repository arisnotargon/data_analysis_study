#针对每条数据的title等预处理并入库
class preHandle():
    def __init__(self,inputDixt):
        self.query_at = inputDixt["queryTime"]
        self.created_at = inputDixt["created_at"]
        self.ua = inputDixt["ua"]
        self.sc = 0

    #数据入库
    def save(self):
        pass

if(__name__ == "__main__"):
    t = preHandle({"queryTime":"2018-03-28","created_at":"2018-03-28","ua":"mozilla"})
    print(t.sc)

