### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
### zip파일 암호 풀기 프로그램



'''
1숫자맞추기 게임/2컴퓨터내외부 IP/3텍스트음성변환/4QR코드생성기/5컴퓨터정보확인
6압축암호풀기/7환율변환기/8파일압축하기/9영어문서한글번역/10이메일수집엑셀저장
11엑셀에서자동이멜발송/12가짜개인정보엑셀저장/13단위변환기/14실시간주가조회/15알림프로그램
16맞춤법검사기/17날씨예보/18음악재생프로그램/19패스워드생성기/20오늘의명언프로그램
21인터넷라디오스트리밍/22MBTI성격검사/23날짜계산기/24가상화폐표시/25가상화폐데이터저장
26데이터베이스 데이터 읽어 그래프그리기/27로또번호/28컴퓨터예약종료/29음식추천/30단어암기
31자동백업/32이미지에서글자추출OCR/33사진얼굴모자이크/34플라스크사진서버/35플라스크게시판
36플라스크투표/37음성인식비서/38인공지능챗봇/39자연어처리/40머신러닝
'''


import zipfile
import itertools
import string

# zip파일 경로와 암호 범위 설정
zip_file_path = "JooAcademy/pythonStudy/example.zip"
password_range = range(1, 10)

# 암호를 찾기 위한 함수 정의
def find_password(zip_file_path, password_range):
    chars = ""
    '''
    if digits:
        chars = chars +"0123456789"
    if letters:
        chars = chars +"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    '''
    # 암호 후보 생성
    for i in password_range:
        password_candidates = itertools.product(string.ascii_letters + string.digits, repeat=i)
        
        # zip파일 열기
        for password in password_candidates:
            password = ''.join(password)
            
            # zip파일 열기
            try:
                with zipfile.ZipFile(zip_file_path, 'r', zipfile.ZIP_DEFLATED) as zip_file:
                    # 암호 입력 후 zip파일 열기
                    zip_file.extractall(pwd=bytes(password, 'utf-8'))
                    print("암호를 찾았습니다. 암호는 {}입니다.".format(password))
                    return password
            except zipfile.BadZipFile:
                print("zip파일이 손상되었습니다.")
            except zipfile.LargeZipFile:
                print("zip파일이 너무 큽니다.")
            except zipfile.BadZipFile:
                print("zip파일이 암호화되어 있습니다.")

# 함수 호출
password = find_password(zip_file_path, password_range)