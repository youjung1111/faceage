from PIL import Image, ImageDraw, ImageFont

# 1. 새 포스터 배경 만들기 (흰색 800x1000)
poster = Image.new('RGB', (800, 1000), color='white')

# 2. 그리기 객체 만들기
draw = ImageDraw.Draw(poster)

# 3. 글꼴 설정 (폰트 파일 경로가 필요함)
try:
    font_title = ImageFont.truetype("C:/Windows/Fonts/malgun.ttf", 50)  # 제목용
    font_text = ImageFont.truetype("C:/Windows/Fonts/malgun.ttf", 30)   # 본문용

except:
    font_title = font_text = None  # 폰트 없으면 기본 폰트

# 4. 텍스트 쓰기
draw.text((50, 30), "실종 아동 찾습니다", font=font_title, fill='black')
draw.text((50, 150), "이름:  미피", font=font_text, fill='black')
draw.text((50, 220), "나이: 7세", font=font_text, fill='black')
draw.text((50, 290), "특징: 귀여움", font=font_text, fill='black')
draw.text((50, 360), "마지막 목격: 서울 용산구 명신관", font=font_text, fill='black')
draw.text((50, 430), "연락처: 010-1234-5678", font=font_text, fill='black')

# 5. 사진 삽입
try:
    child_photo = Image.open('mf.jpg').resize((300, 400))
    poster.paste(child_photo, (450, 150))
except:
    print("사진 파일(child_photo.jpg)이 없으면 생략됨")

# 6. 포스터 저장
poster.save('C:/Users/LG/Pictures/poster/missing_child_poster2.png')

print("포스터 생성 완료!")
