class score:
    def __init__(self, chinese=None, english=None, math=None, physics=None):
        self.Chinese = chinese
        self.English = english
        self.Math = math
        self.Physics = physics
    def show(self):
        print(f"学生成绩为")
#继承
class Student(score):
    def __init__(self, name=None, id=None, chinese=None, english=None, math=None, physics=None):
        #调用父类成员
        super().__init__(chinese, english, math, physics)
        self.name = name
        self.id = id
    #复写
    def show(self):
        print(f"学生姓名: {self.name}")
        print(f"学号: {self.id}")
        print(f"语文: {self.Chinese}")
        print(f"英语: {self.English}") 
        print(f"数学: {self.Math}")
        print(f"物理: {self.Physics}")

#多态
s1=Student("张三",1,100,90,80,70)
s2=Student("李四",2,60,50,40,30)        
s1.show()
s2.show()


