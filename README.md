# Flask로 공부하는 백엔드

### 미니터 핵심 기능
* 회원가입
* 로그인
* 트윗
* 팔로우/언팔로우
* 타임라인

### 배운 점
1. 오류 처리
200, 500 뿐만 아니라 400, 404에 대한 처리가 반드시 필요하다.
2. Encoder
인코더가 없으면 만들면 된다.
3. 자료형에 대한 이해
* 딕셔너리: setdefault, get
* set: 거의 안써서 잊고 살았는데, 중복을 없애기에 더없이 좋은 도구!
4. 인증
* hashlib
    * Rainbow Attack: memoization으로 풀 수 있다.
* bcrypt
    * salting: 비밀번호에 랜덤 값 더하기 -> 레인보우 어택 무력화.
    * 키 스트레칭: MD5 기준 연산 5억 번 -> 5번
* JWT
    * header, payload, signature, and secret_key
5. Decoration


### Reference
[깔끔한 파이썬 탄탄한 백엔드, 송은우 저](https://kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791186697757&orderClick=JAj)
