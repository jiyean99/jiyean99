<a id="top"></a>

# 경력 상세 · Experience

> 각 프로젝트를 **문제 정의 → 요구사항 → UX → 시스템 설계 → 구현 → 검증 → 결과**의 한 흐름으로 정리한 End-to-End Case Study 모음입니다.
> 산출물을 나열하지 않고, **앞 단계의 어떤 문제가 다음 단계의 어떤 결정을 만들었는지**를 기준으로 씁니다.

[`← README로`](../README.md)

---

## 문서 원칙

| 원칙 | 의미 |
|---|---|
| **모든 수치는 실측** | 저장소·마이그레이션·테스트·개발원장에서 직접 확인한 값만 적습니다. 확인 경로와 스냅샷 기준일을 함께 남깁니다 |
| **없는 것은 없다고 적습니다** | 수행하지 않은 사용자 조사·KPI·성능 측정은 "미수행"으로 명시합니다. 있는 것처럼 쓰지 않습니다 |
| **회사 자산은 넣지 않습니다** | 트래픽 지표·고객사 데이터·내부 화면은 공개 문서에 기재하지 않습니다 |

---

## 경력 개요

| 소속 | 역할 | 기간 | 성격 |
|---|---|---|---|
| **(주)에이아이지먼트** | Full-stack Engineer | `2026.06 – 2026.08` | B2B SaaS·고객사 PoC 단독 전담 |
| **한화 SW CAMP** | Backend · Cloud | `2025.11 – 2026.05` | 백엔드·클라우드 확장 · 우수 수료생 |
| **(주)잼퍼블릭** | Frontend Project Lead | `2023.03 – 2025.08` | 실시간 웹 서비스 단독 설계·운영 (2년 6개월) |

```text
실시간 웹 프론트엔드 2년 6개월
        ↓  화면을 만들수록 문제의 원인이 화면 밖에 있었다
        ↓  실시간 배당 불일치도, 대시보드 지연도 결국 연결·정합성·쿼리의 문제
백엔드 · 클라우드 7개월
        ↓  Spring · Kafka · Kubernetes를 팀 프로젝트로 채움
풀스택 단독 수행 3개월
        ↓  제품 전 과정을 혼자 책임지며, 합의를 CI 게이트·유일키로 강제하는 방식 확립
```

---

# Case Studies

## <img align="absmiddle" src="https://github.com/user-attachments/assets/4bbaa6d3-8930-4a92-bc6d-113ade64dfe2" height="20" alt="AIgement" /> (주)에이아이지먼트 &nbsp;`2026.06 – 2026.08`

**Full-stack Engineer** · B2B SaaS·PoC를 기획·디자인·개발·QA까지 단독 전담

3개월 동안 **주력 2건 · 인수 1건 · 대외 1건 · 전사 과제 1건**을 병행했습니다. 다섯 건의 무게는 같지 않으며, PLYN과 정시성 PoC가 시간의 대부분을 차지합니다.

<br/>

### [PLYN — AI-Native SRM 플랫폼](case-studies/plyn.md) &nbsp;<sub>`주력`</sub>

기업 구매 지출을 분류·분석해 절감 기회를 찾고 공급사 매칭까지 잇는 B2B SaaS.

```text
PROBLEM   구매 지출이 표준화되지 않아 집계·절감·공급사 선정이 사람의 경험에 의존
SOLUTION  인테이크 → 분류 → 절감 → 매칭을 한 시스템으로 잇고, 산출에 판단 근거를 병기
ROLE      엔지니어 1인 — 기획 · 설계 · 개발 · QA 단독
```

| 핵심 결정 | 내용 |
|---|---|
| 모듈러 모놀리스 | 물리는 모놀리스, 논리는 MSA 규약 — 운영 비용을 늘리지 않고 분해 가역성 확보 |
| 도메인 경계 CI 게이트 | `import-linter` 계약 2건이 커밋 전에 위반을 차단 (2 kept · 0 broken) |
| 물리 FK 배제 | 테스트가 FK 부재를 단언 + 논리 참조 51관계 정찰 러너 |
| PostgreSQL SKIP LOCKED | 작업 상태와 도메인 데이터를 같은 트랜잭션에 두기 위해 Redis를 걷어냄 |

<sub>**실측** — Phase 1 구현 5도메인(설계 9종) · REST 32종 · 테이블 26 · 테스트 308 · Alembic 21<br/>
**기술** — Python · FastAPI · SQLAlchemy 2.0 · PostgreSQL · AWS Cognito · Terraform · React</sub>

[`케이스 스터디 전문 →`](case-studies/plyn.md)

<br/>

### [국제운송 정시성 Visibility PoC](case-studies/shipping-visibility.md) &nbsp;<sub>`주력` `고객사 PoC`</sub>

화물 지연 리스크를 조기 감지하는 정시성 플랫폼. 데이터 적재 파이프라인부터 ETA 산출·모니터링 대시보드까지 단독 구축.

```text
PROBLEM   원천 스냅샷만으로는 "정확한 도착시각 하나"를 약속할 수 없다
SOLUTION  산식을 두 트랙으로 나누고, 값 옆에 근거와 "못 낸 이유"를 함께 낸다
ROLE      백그라운드 · 웹 양 구간 단독 (전체 PoC 기간 중 담당 구간)
```

| 핵심 결정 | 내용 |
|---|---|
| raw · core · svc 3계층 | "원본이 깨져 들어왔는지, 우리가 깨뜨렸는지"를 나중에도 구분하기 위해 |
| ETA 2트랙 산출 | 구간 누적(ETA2) **98.13%** · 모델 산출(ETA3) **85.56%** — 화면에서 전환 |
| 빈 값의 3분류 | 서빙 뷰 없음 / 모델 입력 없음 / 트랙 미실행 — 어디를 고쳐야 값이 느는지 남김 |
| 감시 단위 재설계 | systemd는 프로세스를 보는데 죽은 건 asyncio 태스크 → 2단 계층으로 하향 |

<sub>**실측** — 조인 쿼리 2h 8m → **15s** · AIS 무응답 13h → **30초 감지** · 항만 키 조인 일치율 99.6%<br/>
**기술** — Python · FastAPI · PostgreSQL · Alembic · Vue 3 · Docker · AWS</sub>

[`케이스 스터디 전문 →`](case-studies/shipping-visibility.md)

<br/>

### [스토리지니 — AI 동화책 생성 서비스](case-studies/storygenie.md) &nbsp;<sub>`인수인계`</sub>

App/Agent 2프로세스 구조의 AI 동화책 생성 서비스를 **전임자 퇴사 시점에 인수**해 무중단 이관·안정화.

```text
PROBLEM   서비스가 돌아가는 중에 담당자가 떠났고, 실패 경로가 문서화돼 있지 않았다
SOLUTION  코드와 실행 경로를 직접 따라가 실패 지점을 특정하고, 호출 관계를 재문서화
ROLE      인수인계 · 파이프라인 안정화 · 온보딩 문서 작성
```

<sub>**실측** — App/Agent 2프로세스 · 통신 3채널(REST · 콜백 · 잡 큐) · REST 98종 · 외부 연동 7종</sub>

[`케이스 스터디 전문 →`](case-studies/storygenie.md)

<br/>

### [R&D 전수 검토 · 대외 활동 · 팀 운영](case-studies/aigement-others.md) &nbsp;<sub>`검토` `전사 과제`</sub>

사내 R&D 저장소를 **문서의 주장에 의존하지 않고 직접 실행해** 검증한 과제와, 대외 출품·팀 협업 체계 정비.

```text
PROBLEM   대외에 나갈 수치가 저장소의 주장 그대로 옮겨지고 있었다
SOLUTION  clean venv에서 직접 실행 · 오프라인 dry-run으로 산출물 생성까지 검증
RESULT    테스트 416개 통과 · 32,237 LOC 전수 검토 · 대외 수치 3건 정정 제안
```

<sub>본인이 발견한 린트 292건이 **저장소가 아니라 로컬 환경 문제**임을 스스로 규명해 오보를 막은 사례를 포함합니다.</sub>

[`케이스 스터디 전문 →`](case-studies/aigement-others.md)

---

## <img align="absmiddle" src="https://www.google.com/s2/favicons?domain=zempublic.co.kr&sz=64" width="18" /> (주)잼퍼블릭 &nbsp;`2023.03 – 2025.08` <sub>(2년 6개월)</sub>

**Frontend Project Lead** · 실시간 웹 서비스와 사내 시스템 프론트엔드를 단독 설계·운영

기능 기획서 · 디자인 시안 · 프론트엔드 개발 · QA를 **한 사람 안에서 연결**했습니다. 모노레포 누적 6,441커밋 중 **926커밋** 기여, 저장소 6개 동시 담당.

<br/>

### [승부사 온라인 — 대규모 실시간 스포츠 베팅 웹앱](case-studies/adventurer.md) &nbsp;<sub>`주력` `2년 6개월`</sub>

실시간 배당·경기 상태가 초 단위로 바뀌는 환경에서 2년 6개월간 기능 추가와 장애 대응을 이어간 프로덕션.

```text
PROBLEM   연결이 끊기거나 환경이 막히면 실시간 값이 어긋나고, 설정 하나 바꾸는 데 배포가 필요했다
SOLUTION  이중 소켓 구현 + 폴백, 도메인 단위 상태 분리, 무배포 설정 제어
ROLE      프론트엔드 단독 설계 · 운영
```

| 핵심 결정 | 내용 |
|---|---|
| 이중 소켓 | Socket.io + Native WebSocket 두 구현을 런타임 전환, 막힌 환경은 polling 폴백 |
| wildcard 단일 진입점 | 이벤트 26종을 리스너 26개가 아니라 `.on('*')` 한 경로로 라우팅 |
| MobX 도메인 스토어 29종 | 화면이 아니라 도메인으로 분리해 변경된 값 구독자만 리렌더 |
| Remote Config 250키 | enum 중앙 정의 + 소켓 갱신 — **값을 바꾸는 데 배포가 필요하면 그건 설정이 아니라 상수** |

<sub>**실측** — 741 파일(TSX 538 · TS 203) · 포털 소켓 이벤트 26종 · 라이브 프로토콜 12종 · Remote Config 250키<br/>
<b>트래픽 지표(DAU·동시접속)는 회사 자산이라 기재하지 않았습니다.</b></sub>

[`케이스 스터디 전문 →`](case-studies/adventurer.md)

<br/>

### [사내 매출 통계 대시보드](case-studies/dashboard.md)

ADV·Champ 이중 도메인 실시간 리포트. 민감 지표를 **숨기는 게 아니라 렌더링 자체를 차단**하는 이중 권한 설계.

<sub>**기술** — Vue · Vuex · Highcharts · Socket.io · Bootstrap</sub> &nbsp;[`전문 →`](case-studies/dashboard.md)

<br/>

### [챔프포커 웹뷰](case-studies/champpoker.md)

Unity 웹보드 게임의 웹뷰 프론트엔드. **게임 클라이언트 배포 주기와 무관하게 콘텐츠만 갱신**할 수 있는 구조 확보.

<sub>**기술** — HTML/CSS · JavaScript · Unity WebView · JS Bridge</sub> &nbsp;[`전문 →`](case-studies/champpoker.md)

<br/>

### [신규 사업부 모바일 러닝 MVP](case-studies/mobile-mvp.md)

Expo / React Native 크로스 플랫폼. EAS Build·OTA로 스토어 심사 없이 반영, **2개월 내 iOS·Android 동시 배포**.

<sub>**기술** — Expo · React Native · Zustand · NativeWind · EAS</sub> &nbsp;[`전문 →`](case-studies/mobile-mvp.md)

<br/>

### [프론트엔드 리드 · 기능 기획](case-studies/frontend-lead.md)

디자인팀 소속으로 프론트엔드 리드 · 기능 기획 · 트렌드 조사를 병행. **무엇을 만들지 정하는 자리**에 있었기 때문에 만들지 않기로 하는 판단도 함께 했습니다.

<sub>기획 → 시안 → 구현 → QA를 같은 사람이 수행해 기획 의도 손실이 없었던 대신, **결정을 기록으로 남기는 일**이 중요해졌습니다.</sub> &nbsp;[`전문 →`](case-studies/frontend-lead.md)

---

## <img align="absmiddle" src="https://www.hanwhacorp.co.kr/_resource/hanwha/images/hanwha/ci/ci_logo_s.png" width="17" /> 한화 SW CAMP &nbsp;`2025.11 – 2026.05`

**Backend & Cloud Engineer** · 백엔드·클라우드까지 확장한 7개월 · **우수 수료생**

<br/>

### [Workforce — MSA 기반 통합 HRMS](case-studies/workforce.md) &nbsp;<sub>`팀 4인`</sub>

근태·급여·결재·평가를 통합한 마이크로서비스 HRMS. **팀 프로젝트이므로 git 이력으로 확인한 실제 기여만 적습니다.**

```text
MY SCOPE  목표·평가(OKR) 도메인 E2E · 실시간 채팅 · K8s 무중단 배포
NOT MINE  MSA 전체 설계 · AI 챗봇 · RBAC 권한 · 통합 검색 (타 팀원 담당)
```

| 담당 | 실측 기여 |
|---|---|
| OKR 도메인 E2E | `goal-service` — 변경 파일 **697** (2위 26) |
| 실시간 채팅 | `memberchat` — 변경 파일 **108**, 커밋 13건 중 **12건** |
| 무중단 배포 | 커밋 `6f1d02a` 한 건으로 7개 서비스에 RollingUpdate + HPA · PDB |

<sub>**실측** — 3개 저장소 누적 1,461커밋 중 **325커밋**(BE 193 · FE 130 · DevOps 2)<br/>
**기술** — Java · Spring Boot · Spring Cloud · Kafka · Redis · STOMP · Kubernetes · AWS EKS</sub>

[`케이스 스터디 전문 →`](case-studies/workforce.md)

<br/>

### [짐꽁 — 피트니스 수업 예약·출석·결제 관리](case-studies/gymkkong.md) &nbsp;<sub>`팀 3인`</sub>

회원·트레이너·관리자 세 역할이 하나의 앱에서 수업 예약·출석·결제를 처리하는 통합 관리 시스템.

```text
PROBLEM   세 역할이 같은 자원을 다른 권한으로 만지고,
          인기 수업의 마지막 한 자리에서 동시 요청이 겹친다
SOLUTION  인증 주체를 하나로 두고 권한 강제를 4층으로 분리 ·
          예약을 한 트랜잭션에서 락으로 직렬화 · 전 시나리오 E2E 재현 검증
ROLE      백엔드 · 앱 · 데이터 모델 · 검증 체계 (커밋 73/100)
```

| 핵심 결정 | 내용 |
|---|---|
| 인증 주체 단일화 | `app_user` 하나가 인증을 책임지고 역할별 프로필을 분리 — JWT subject 고정 |
| 동시성 두 겹 | `SELECT … FOR UPDATE` + 유일키, **락 순서 고정**으로 교착 회피 |
| 오류 번역 | DB 제약 위반을 500이 아니라 `ALREADY_RESERVED` 도메인 오류로 |
| RBAC 4단 방어 | 화면은 편의일 뿐 — 실제 방어선은 API·서비스·DB에 있다고 문서에 명시 |

<sub>**실측** — main 100커밋 중 **73커밋** · 엔드포인트 68 · 테이블 23 · **E2E 28/28 · 스모크 22/22** · 증적(스크린샷 46 · 녹화 58) · mermaid 34<br/>
**기술** — Java · Spring Boot 3.4.1 · JPA · Spring Security · JWT · MariaDB · Expo/React Native · Playwright</sub>

[`케이스 스터디 전문 →`](case-studies/gymkkong.md)

<br/>

### [Articket — 공연 예매 플랫폼](case-studies/articket.md) &nbsp;<sub>`팀 리드(PM)`</sub>

실시간 좌석 선점·결제로 예매를 확정하는 플랫폼. 팀 리드로 일정·범위·역할 분담과 통합을 책임지며 인증·인가와 SSE 실시간 알림을 직접 구현.

<sub>**기술** — Java · Spring Boot · Redis · JWT · OAuth2 · SSE · MariaDB</sub> &nbsp;[`전문 →`](case-studies/articket.md)

---

## 개인 프로젝트

### [지출 분석 AI 에이전트](case-studies/finance-agent.md) &nbsp;<sub>`2026.07 – 진행중`</sub>

지출을 분석하는 AI 에이전트와, **그 에이전트 자체를 관측하는 비용·관측 대시보드**를 함께 만드는 프로젝트.

```text
문제의식   LLM을 쓰는 서비스는 한 번의 요청이 얼마를 썼는지, 왜 그 답을 냈는지가 기본적으로 안 보인다
목표      응답의 근거와 비용을 둘 다 화면에 올린다
```

| 설계 원칙 | 내용 |
|---|---|
| 쓰기 소유권 단일화 | 원장 쓰기는 Domain 단독. Agent·BFF는 금지 — 금전 데이터의 단일 진실 원천 고정 |
| 멱등키 필수 | 모든 쓰기에 `Idempotency-Key`. 동일 키는 원장 무변경 + 저장된 결과 반환 |
| 계약 우선 | OpenAPI로 스키마를 선정의한 뒤 구현 |

<sub>3-언어 백엔드(NestJS BFF · FastAPI Agent · Spring Domain)는 **학습 목적**이며, 실무라면 하나로 갔을 구성입니다.</sub>

[`케이스 스터디 전문 →`](case-studies/finance-agent.md)

---

<p align="right">

[`← README로`](../README.md) &nbsp;·&nbsp; [`기술 스택 전체 →`](tech-stack.md) &nbsp;·&nbsp; [↑ 맨 위로](#top)

</p>
