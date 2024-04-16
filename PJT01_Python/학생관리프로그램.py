# =================================================================================================
# 클래스명 : 학생
# 속성필드 : 이름, 성적
# 기능역할 : x
#
# 클래스명 : 학생성적관리
# 속성필드 : 학생
# 기능역할 : 학생 정보(이름, 성적) 추가하기, 학생 정보 얻기, 이름으로 학생찾기, 학생 삭제하기, 파일 저장하기
# =================================================================================================

# 학생 클래스
class Student:

    def __init__(self, n, s):
        self.name = n
        self.score = s

    # 문자열로 변환해주는 메서드
    def __str__(self):
        return f'{self.name}, {self.score}'


# 학생성적관리 클래스
class StudentManagement:
    
    def __init__(self):
        self.students = []

    # 학생 정보(이름, 성적) 추가 <- 학생 클래스에서 가져옴
    def addStudent(self, student):
        self.students.append(student)

    # 이름으로 학생 찾기
    def getStudentByName(self, name):
        for x in self.students:
            if (x.name == name):
                return x
        return None  # if문을 만족하지 않으면 None값을 반환

    # 학생 삭제
    def removeStudent(self, idx):
        del self.students[idx]

    # 점수 업데이트
    def updateScore(self, name, score):
        if name in self.students:
            obj = self.getStudentByName(name)
            obj.score = score
        else:
            print(f'{name} 학생이름을 찾을 수 없습니다.')

    # 학생 정보 얻기
    def getStudents(self):    
        return self.students

    # 파일 저장하기
    def save(self, fileName):
        fp = open(fileName, 'w', encoding='utf-8')
            
        for x in self.getStudents():
            fp.write(str(x) + '\n')
        fp.close()

    # 파일 불러오기
    def load(self, fileName):
        fp = open(fileName, 'r', encoding='utf-8')
        strlist = fp.read().split('\n')

        for x in strlist:
            if x.strip() == '':
                continue
            name = x.split(',')[0]
            score = int(x.split(',')[1])
            stmp = Student(name, score)
            self.addStudent(stmp)
            self.getStudents()
        fp.close()


# ----------------------------------------------------
# 객체 생성

s1 = Student('홍길동', 88)
s2 = Student('마징가', 79)
s3 = Student('허유나', 91)
s4 = Student('박소원', 93)
s5 = Student('박윤미', 100)
s6 = Student('윤성원', 99)


sm = StudentManagement()
sm.addStudent(s1)
sm.addStudent(s2)
sm.addStudent(s3)
sm.addStudent(s4)
sm.addStudent(s5)
sm.addStudent(s6)

# ----------------------------------------------------

# self.students의 주소 리스트
# print(sm.getStudents())

# 리스트에서 하나씩 가져오기
for x in sm.getStudents():
    print(x)

# 파일 저장하기
# sm.save('file.txt')

# 파일 불러오기
sm.load('file.txt')

# '홍길동' 이름으로 검색하면 해당 이름과 점수 출력
print(sm.getStudentByName('홍길동').name)
print(sm.getStudentByName('홍길동').score)

