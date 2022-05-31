# FIND-NEW-NOTICE
- 업로드되기를 기다리는 공지 제목을 입력하면 학교 홈페이지에 올라오는 공지를 크롤링해서 공지가 업로드 되었을 때 실시간으로 알려줍니다.
- "교육청웹호스팅학교홈페이지 민간 SSL 보안인증사이트" 의 학교 홈페이지에서만 작동합니다. (아래 마크)

![image](https://user-images.githubusercontent.com/96960979/171301275-ceadcaad-7397-447b-969a-8bdada917a13.png)

# 변수 정보
- self.page_url : 공지 게시판의 url
- self.time_interval : 몇 초의 간격으로 공지를 확인할 것인지? (너무 작으면 오류 발생, 홈페이지 속도 저하 위험)
- self.target_text : 찾으려는 공지 제목에 포함되는 텍스트 ("if -- in --" 으로 확인)
- self.alarm_sound : 공지가 업로드 된 것을 확인했을 때 재생할 알림음 경로
