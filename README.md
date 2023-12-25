# 3D-Sharing-Django
Django를 이용한 3D 모델링 파일 공유 사이트
<br><br>

## 프로젝트 소개
Django를 이용한 3D 모델링 파일 공유 사이트로, 모델링 파일 공유, 자유 게시판, 콘테스트(투표를 통해 1등을 뽑는 대회), 마이페이지를 구현하였습니다.
<br><br>

## 개발 기간
- 2023.11.28 ~ 2023.12.25
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
<br><br>

### Community
커뮤니티는 자유 게시판으로 검색 필터링 및 페이지네이션이 구현되어있습니다.<br>
다음 5가지로 구분하여 검색을 할 수 있습니다.
- 제목 + 내용
- 제목
- 내용
- 작성자
- 댓글

![image](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/57867855-fea8-497e-9892-5b2c2f13f063)
<br><br>

CKEditor를 이용하여 여러 기능을 게시글에 적용할 수 있게 하였습니다.<br><br>
![image](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/4aabd6c4-3593-43ce-af80-83fbfbdc080f)
![image](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/480e9514-9b1b-44db-bd9f-fe661383b195)
<br><br>

### Contest
콘테스트 페이지는 주어진 기간 동안 참가 및 투표를 하고 1등을 가리는 페이지입니다.<br>
이전 우승 작품을 볼 수 있고, 참가 기간일 경우 참가, 투표 기간일 경우 투표를 할 수 있습니다.<br><br>
![image](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/2059c058-3229-462e-b9bd-19e9eb3c42ac)
<br><br>

콘테스트에서 추천 수가 가장 많아서 우승한 작품들은 회차가 넘어가면 이전 콘테스트 우승 작품 부분으로 이동하게 됩니다.<br>
만약 1등이 여러 작품일 경우 모두 우승 작품으로 처리합니다.<br>
우승 작품이 많아질 경우 마우스를 통해 좌우로 넘겨서 볼 수 있습니다.<br><br>
![Screenshot 2023-12-21 at 13 51 23](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/e2b3151f-f658-4470-bd69-7154d2c01022)
<br><br>

상단에서 현재 몇 회 콘테스트인지, 신청 기간 및 투표 기간이 언제인지를 표시하였습니다.<br>
django-apscheduler를 이용하여 자동으로 2주마다 회차가 넘어가게 구현하였습니다.<br>
또한, 무한 스크롤을 구현하여 페이지 최하단으로 스크롤 하였을 때 추가로 불러올 모델이 있을 경우 아래쪽에 표시합니다.<br>

(참가 기간)<br>
![ezgif com-video-to-gif-converted (1)](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/954054c9-0058-42f2-ab72-aa6bae806791)<br>
(투표 기간)<br>
![image](https://github.com/magic7549/3D-Sharing-Django/assets/32091601/b3622208-e2f5-426a-9060-bad519297c71)<br>

참가하기 버튼을 클릭하면 창을 띄워 콘테스트에 참가할 모델을 선택할 수 있습니다.<br>
참가할 모델 리스트에는 자신이 앞서 Modeling 페이지에서 작성한 모델만 표시되게 하였습니다.<br>
