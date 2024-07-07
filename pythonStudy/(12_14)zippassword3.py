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

    # zip파일 경로와 암호 범위 설정
zip_file_path = "JooAcademy/pythonStudy/example.zip"

def find_password(zip_file_path, digits, letters, max_length):

    # 암호를 찾기 위한 함수 정의

    chars = ""
    
    if digits:
        chars +="1234567890"
    if letters:
        chars +="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    password_candidates = itertools.chain.from_iterable(itertools.product(chars, repeat=i) for i in range(1, max_length+1))
        
    # zip파일 열기
    
    #with zipfile.ZipFile(zip_file_path, 'r', zipfile.ZIP_DEFLATED) as zip_file:
    with zipfile.ZipFile(zip_file_path) as zip_file:
        # 암호 입력 후 zip파일 열기
        for j in password_candidates:
            print(j)
            str_pass = "".join(j)
            print(str_pass)
            try:
                zip_file.extractall(pwd=password_candidates.encode())
                print("암호를 찾았습니다. 암호는 {}입니다.".format(str_pass))
                return str_pass
            except:
                pass
    
    #비밀번호를 못찾을 경우 모름 반환
    return None    

# 함수 호출
password = find_password(zip_file_path, True, True, 2)
#password = find_password(zip_file_path, digits=True, letters=True, max_length=1)
print("비밀번호는:", password)