# -*- 생성자와 소멸자 -*-
class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    def __del__(self):
        print("Instance is deleted!")


#인스턴스 생성

m1 = MyClass(5)
#메모리 관리 자동
#del m1

print( "전체 코드 실행 종료")

