# -*- coding: utf-8 -*-
"""순서 재배치 · 기간 정정 · Articket 카드 보강 · 커밋/파일 수 제거."""
import io, sys

def rd(p): return io.open(p, encoding="utf-8").read()
def wr(p, s): io.open(p, "w", encoding="utf-8").write(s)

def rep(s, a, b, label, path):
    if a not in s:
        print("!! 미적중 [%s] %s : %s" % (path, label, a[:55].replace("\n", "|"))); sys.exit(1)
    return s.replace(a, b)


# ════════════════════════════ docs/experience.md
P = "docs/experience.md"
s = rd(P)

# ── 짐꽁 카드를 잘라내 Articket 뒤로 이동 + 기간 정정
gym_start = s.index("### [짐꽁 — 피트니스 수업 예약·출석·결제 관리]")
gym_end = s.index("### [Articket — 공연 예매 플랫폼]")
gym = s[gym_start:gym_end].rstrip() + "\n"
s = s[:gym_start] + s[gym_end:]

# ── Articket 카드를 Workforce·짐꽁과 같은 포맷으로 보강
art_old = """### [Articket — 공연 예매 플랫폼](case-studies/articket.md) &nbsp;<sub>`팀 리드(PM)`</sub>

실시간 좌석 선점·결제로 예매를 확정하는 플랫폼. 팀 리드로 일정·범위·역할 분담과 통합을 책임지며 인증·인가와 SSE 실시간 알림을 직접 구현.

<sub>**기술** — Java · Spring Boot · Redis · JWT · OAuth2 · SSE · MariaDB</sub> &nbsp;[`전문 →`](case-studies/articket.md)
"""
art_new = """### [Articket — 공연 예매 플랫폼](case-studies/articket.md) &nbsp;<sub>`팀 리드(PM)`</sub>

실시간 좌석 선점·결제로 예매를 확정하는 공연 예매 플랫폼. 팀 리드로 일정·범위·역할 분담과 통합을 책임졌습니다.

```text
PROBLEM   선점과 결제 확정 사이에 좌석 상태가 흔들리면
          중복 판매 또는 재고 잠김이 발생한다
SOLUTION  선점을 제3의 상태로 두고 TTL 로 자동 만료 ·
          결제 확정 시점에 선점 유효성을 재검증
ROLE      팀 리드(PM) · 인증 인가 설계 · SSE 실시간 알림 · FE 아키텍처 설계
```

| 핵심 결정 | 내용 |
|---|---|
| 좌석 상태 3분 | "빈 좌석 / 팔린 좌석" 둘로는 **결제 중인 좌석**을 표현할 수 없다 |
| TTL 자동 만료 | 선점을 Redis TTL 로 두어 별도 정리 배치 없이 재고 잠김 방지 |
| 확정 시 재검증 | 선점이 만료된 뒤 결제가 성공하는 경합을 확정 시점 재확인으로 차단 |
| SSE 선택 | 좌석 상태는 **서버 → 클라이언트 단방향** — 양방향이 필요 없으면 SSE 가 더 싸다 |

<sub>**한계** : 경합 창을 좁혔을 뿐 제거하지 못했고, 동시성을 정량 검증하지 않았습니다.<br/>
**기술** : Java · Spring Boot · Redis · JWT · OAuth2 · SSE · MariaDB · PortOne · KakaoMap</sub>

[`케이스 스터디 전문 →`](case-studies/articket.md)
"""
s = rep(s, art_old, art_new + "\n<br/>\n\n" + gym, "Articket 보강 + 짐꽁 이동", P)

# ── 짐꽁 기간 정정
s = rep(s, "| **팀** | 3인 · `main` 100커밋 중 **73커밋** 기여 |", "", "(카드엔 없음)", P) if False else s

# ── Workforce 카드 : 수치 → 소유 범위
s = rep(s, """| 담당 | 실측 기여 |
|---|---|
| OKR 도메인 E2E | `goal-service` — 변경 파일 **697** (2위 26) |
| 실시간 채팅 | `memberchat` — 변경 파일 **108**, 커밋 13건 중 **12건** |
| 무중단 배포 | 커밋 `6f1d02a` 한 건으로 7개 서비스에 RollingUpdate + HPA · PDB |

<sub>**실측** — 3개 저장소 누적 1,461커밋 중 **325커밋**(BE 193 · FE 130 · DevOps 2)<br/>
**기술** — Java · Spring Boot · Spring Cloud · Kafka · Redis · STOMP · Kubernetes · AWS EKS</sub>""",
"""| 담당 | 내용 |
|---|---|
| OKR 도메인 E2E | 목표 정렬·진척·평가를 도메인 설계부터 API·테스트까지 단독 |
| 실시간 채팅 | STOMP + Redis Pub/Sub 으로 인스턴스 간 메시지 fan-out |
| 무중단 배포 | 7개 서비스에 RollingUpdate(maxUnavailable 0) + HPA · PDB 신설 |

<sub>**기술** : Java · Spring Boot · Spring Cloud · Kafka · Redis · STOMP · Kubernetes · AWS EKS</sub>""",
"Workforce 수치 제거", P)

# ── 잼퍼블릭 인트로 커밋 수 제거
s = rep(s, "기능 기획서 · 디자인 시안 · 프론트엔드 개발 · QA를 **한 사람 안에서 연결**했습니다. 모노레포 누적 6,441커밋 중 **926커밋** 기여, 저장소 6개 동시 담당.",
        "기능 기획서 · 디자인 시안 · 프론트엔드 개발 · QA를 **한 사람 안에서 연결**했습니다. 모노레포 내 저장소 6개를 동시에 담당했습니다.",
        "잼퍼블릭 인트로", P)

# ── 짐꽁 카드 기간·기여 표기
s = rep(s, "ROLE      백엔드 · 앱 · 데이터 모델 · 검증 체계 (커밋 73/100)",
        "ROLE      백엔드 · 앱 · 데이터 모델 · 검증 체계", "짐꽁 ROLE", P)
wr(P, s); print("OK", P)


# ════════════════════════════ README.md — Side Projects 순서 + 기간
P = "README.md"; s = rd(P)
i_gym = s.index("- **짐꽁 (GymKKong)**")
i_art = s.index("- **Articket**")
gym_blk = s[i_gym:i_art]
s = s[:i_gym] + s[i_art:]
i_art = s.index("- **Articket**")
art_end = s.index("\n\n<br/>", i_art)
s = s[:art_end] + "\n\n" + gym_blk.rstrip() + s[art_end:]
s = rep(s, "- **짐꽁 (GymKKong)** &nbsp;`2025.12 – 2026.08`", "- **짐꽁 (GymKKong)** &nbsp;`2025.12`", "짐꽁 기간", P)
wr(P, s); print("OK", P)


# ════════════════════════════ docs/case-studies/workforce.md
P = "docs/case-studies/workforce.md"; s = rd(P)
s = rep(s, """<sub>실측 기준 — `workforce-be` · `workforce-fe` · `workforce-be-devops` 3개 저장소를 직접 파싱(`git shortlog` · 파일 변경 이력).
부하 테스트 수치는 팀 공용 클러스터 기준이라 제 성과로 기재하지 않았습니다.</sub>""",
"""<sub>담당 범위는 저장소 이력으로 확인한 것만 적었습니다.
부하 테스트 수치는 팀 공용 클러스터 기준이라 제 성과로 기재하지 않았습니다.</sub>""", "실측 기준", P)

s = rep(s, """| 영역 | 실측 기여 | 내용 |
|---|---|---|
| **목표·평가(OKR) 도메인** | `goal-service` 변경 파일 **697** (2위 26) | 도메인 설계부터 API·테스트까지 E2E |
| **실시간 채팅** | `memberchat` 변경 파일 **108**, 커밋 13건 중 **12건** | STOMP + Redis Pub/Sub 인스턴스 간 fan-out |
| **무중단 배포** | 커밋 `6f1d02a` (2026-05-09) 한 건 | 7개 서비스에 RollingUpdate + HPA · PDB 신설 |""",
"""| 영역 | 내용 |
|---|---|
| **목표·평가(OKR) 도메인** | 목표 정렬·진척·평가를 도메인 설계부터 API·테스트까지 단독 담당 |
| **실시간 채팅** | STOMP + Redis Pub/Sub 으로 인스턴스 간 메시지 fan-out 구현 |
| **무중단 배포** | 7개 서비스에 RollingUpdate(maxUnavailable 0) + HPA · PDB 신설 |""", "담당 표", P)

s = rep(s, """### 전체 기여 분포

```text
3개 저장소 누적 1,461커밋 중 본인 325커밋
  BE      193 / 998
  FE      130 / 368
  DevOps    2 /  95
내가 만진 파일 872
```

---""", "---", "기여 분포 블록", P)

s = rep(s, "인스턴스 수와 무관하게 메시지가 도달합니다. `memberchat` 패키지 커밋 13건 중 **12건이 제 커밋**입니다.",
        "인스턴스 수와 무관하게 메시지가 도달합니다. 이 패키지는 제가 단독으로 구현했습니다.", "fan-out 결과", P)

s = rep(s, "커밋 `6f1d02a`(2026-05-09) 한 건으로 **7개 서비스**에 적용했습니다.",
        "**7개 서비스에 동일한 설정으로 일괄 적용**했습니다.", "무중단 배포 도입부", P)

s = rep(s, """### 검증 가능한 기여

| 항목 | 값 | 확인 방법 |
|---|---|---|
| 전체 커밋 기여 | **325 / 1,461** (BE 193 · FE 130 · DevOps 2) | `git shortlog -sne --all` |
| `goal-service` 변경 파일 | **697** (2위 26) | 경로별 변경 이력 |
| `memberchat` 커밋 | **12 / 13** | 패키지별 커밋 이력 |
| 무중단 배포 적용 | 커밋 1건 → **7개 서비스** | `6f1d02a` |
| 내가 만진 파일 | **872** | 변경 파일 실측 |""",
"""### 담당 범위

| 영역 | 내용 |
|---|---|
| 목표·평가(OKR) 도메인 | 설계 · API · 테스트까지 단독 |
| 실시간 채팅 | STOMP + Redis Pub/Sub fan-out 구현 |
| 무중단 배포 | 7개 서비스 일괄 적용 (RollingUpdate · HPA · PDB) |""", "Result 표", P)

s = rep(s, """KEY CONTRIBUTION
  goal-service 변경 파일 697 (2위 26)
  memberchat 커밋 13건 중 12건 — STOMP + Redis Pub/Sub 인스턴스 간 fan-out
  커밋 6f1d02a 한 건으로 7개 서비스 RollingUpdate + HPA · PDB 신설""",
"""KEY CONTRIBUTION
  목표·평가(OKR) 도메인을 설계부터 API · 테스트까지 단독 담당
  실시간 채팅 STOMP + Redis Pub/Sub 인스턴스 간 fan-out 구현
  7개 서비스에 RollingUpdate + HPA · PDB 일괄 적용""", "Summary", P)

s = rep(s, """RESULT
  3개 저장소 1,461커밋 중 325커밋 기여 · 내가 만진 파일 872
  (무중단 배포는 설정 수준 구성까지 — 부하 검증 미수행)""",
"""RESULT
  마이크로서비스 7 · Kafka 토픽 10 / 리스너 21 (팀 공동 산출)
  (무중단 배포는 설정 수준 구성까지 — 부하 검증 미수행)""", "Summary RESULT", P)

s = rep(s, """### 전체 팀 규모 (참고 — 공동 산출)

마이크로서비스 7 · REST 엔드포인트 561 · Kafka 토픽 10 / 리스너 21 · HPA 대상 서비스 7""",
"""### 팀 전체 규모 (참고 — 공동 산출)

마이크로서비스 7 · REST 엔드포인트 561 · Kafka 토픽 10 / 리스너 21 · HPA 대상 서비스 7""",
"팀 규모 제목", P) if "### 전체 팀 규모 (참고 — 공동 산출)" in s else s
wr(P, s); print("OK", P)


# ════════════════════════════ docs/case-studies/gymkkong.md
P = "docs/case-studies/gymkkong.md"; s = rd(P)
s = rep(s, """<sub>실측 기준 — 저장소 직접 파싱(`git shortlog` · 애노테이션 수 · 테스트 수).
`main` 기준 100커밋 중 **73커밋**이 제 커밋입니다.</sub>""",
"""<sub>수치는 저장소를 직접 파싱해 확인한 값입니다(애노테이션 수 · 테스트 수 · 테이블 수).</sub>""", "실측 기준", P)
s = rep(s, "백엔드 · 앱 · 데이터 모델 · 검증 체계 (팀 3인 중 커밋 73/100)",
        "백엔드 · 앱 · 데이터 모델 · 검증 체계", "ROLE", P)
s = rep(s, "| **기간** | `2025.12 – 2026.08` · 한화 SW CAMP |\n| **팀** | 3인 · `main` 100커밋 중 **73커밋** 기여 |",
        "| **기간** | `2025.12` · 한화 SW CAMP |\n| **팀** | 3인 |", "기간·팀", P)
s = rep(s, "| 커밋 기여 | **73 / 100** (`main`) | `git shortlog` |\n", "", "Result 커밋행", P)
s = rep(s, "  백엔드 · 앱 · 데이터 모델 · 검증 체계 (팀 3인 중 커밋 73/100)",
        "  백엔드 · 앱 · 데이터 모델 · 검증 체계 (팀 3인)", "Summary ROLE", P)
s = rep(s, "  main 100커밋 중 73커밋 · 엔드포인트 68 · 테이블 23 ·",
        "  엔드포인트 68 · 엔티티 22 · 테이블 23 ·", "Summary RESULT", P)
wr(P, s); print("OK", P)


# ════════════════════════════ docs/case-studies/adventurer.md
P = "docs/case-studies/adventurer.md"; s = rd(P)
s = rep(s, "| 모노레포 기여 | 누적 6,441커밋 중 **926커밋** | `git shortlog` (2023.04 – 2025.08) |\n", "", "커밋 행", P)
s = rep(s, "  Remote Config 250키 · 모노레포 6,441커밋 중 926커밋 기여",
        "  Remote Config 250키 · 모노레포 내 저장소 6개 동시 담당", "Summary", P)
s = rep(s, "<sub>실측 기준 — 백업 저장소를 직접 파싱해 산출(파일 수 · enum 멤버 수 · `git shortlog`).",
        "<sub>실측 기준 — 백업 저장소를 직접 파싱해 산출(파일 수 · enum 멤버 수).", "실측 기준", P)
wr(P, s); print("OK", P)

print("\n구조 재배치 · 수치 제거 완료")
