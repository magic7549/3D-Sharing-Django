# 3D-Sharing-Django
Django를 이용한 3D 모델링 파일 공유 사이트
<br><br>

## 프로젝트 소개
Django를 이용한 3D 모델링 파일 공유 사이트로, 모델링 파일 공유, 자유 게시판, 콘테스트(투표를 통해 1등을 뽑는 대회), 마이페이지를 구현하였습니다.
<br><br>

## 개발 기간
- 2023.12.03 ~ 2023.12.25
- 설계 : 2023.12.03 ~ 2023.12.06
- 구현 : 2023.12.07 ~ 2023.12.25
<br><br>

## 개발 환경
- 웹 프레임워크 : Django 4.0.3, Bootstrap 5.3
- 파이썬 : 3.10.7
- 데이터베이스: SQLite3
- 라이브러리 : CKEditor, Three.js, Swiper, apscheduler
<br><br>

## 페이지 소개
### 홈
상단 메뉴바를 이용하여 Home, Modeling, Community, Contest, 로그인, 회원가입 페이지로 이동할 수 있습니다.<br>
Swiper 라이브러리를 이용하여 위아래로 부드럽게 이동 가능하게 하였습니다.<br><br>
![ezgif com-video-to-gif-converted](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/e2a9821c-13de-41cd-bb59-3defc79eeff4)
<br><br>

### Modeling
한 페이지에 30개 모델링이 표시되고 그 이상 검색 결과가 있을 경우 페이징 처리하여 나눠서 볼 수 있게 하였습니다.<br>
검색 필터 조건에 맞춰 검색하고 .fbx나 .glb파일을 구분하여 검색할 수 있습니다.<br>
다음 5가지로 구분하여 검색을 할 수 있습니다.
- 제목 + 내용
- 제목
- 내용
- 작성자
- 댓글

![image](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/ac862fb8-a54f-4cc6-a951-6fe75cf008f5)
<br><br>

상세 페이지에서는 좌측에서 모델링 이미지를 확인할 수 있고, 우측에서 상세정보를 확인할 수 있습니다.<br>
상세정보 하단에서 다운로드와 추천을 할 수 있습니다.<br>
<br>
페이지 하단에서 댓글을 작성할 수 있고, 본인이 작성한 댓글일 경우 수정 및 삭제가 가능합니다.<br><br>
![image](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/91b822ad-d1d4-450f-a999-6265bd46d27a)
<br><br>

또한, 이미지를 클릭해서 모델링 파일을 3d 뷰로 확인할 수 있습니다.<br><br>
![Screenshot 2023-12-21 at 13 43 02](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/512177ce-4ffc-43e5-ab27-28d02ce843d9)
