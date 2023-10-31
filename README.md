# test

![header](https://capsule-render.vercel.app/api?type=waving&color=87CEEB&height=300&section=header&text=데이콘XHD%20RookieMa%20팀&fontSize=70)

### 데이터 출처
예술의 전당 데이터를 사용
-------------------------------


### 목적
항만 內 선박 대기 시간 예측을 위한 선박 항차 데이터 분석 AI 알고리즘 개발

-------------------------------
### 개발 배경 및 목적

코로나19 이후 물류 정체로 인해 다수의 항만에서 선박 대기 시간이 길어지고, 이로 인한 물류 지연이 화두가 되고 있습니다. 

특히 전 세계 물동량의 85%를 차지하는 해운 물류 분야에서 항만 정체는 큰 문제로 인식되고 있는 상황입니다. 

본 대회에서는 접안(배를 육지에 대는 것;Berthing) 전에 선박이 해상에 정박(해상에 닻을 바다 밑바닥에 내려놓고 운항을 멈추는 것;Anchorage)하는 시간을 대기시간으로 정의하고, 선박의 제원 및 운항 정보를 활용하여 산출된 항차(voyage; 선박의 여정) 데이터를 활용하여 항만 內 선박의 대기 시간을 예측하는 AI 알고리즘을 개발을 제안합니다.

이를 통해 선박의 접안 시간 예측이 가능해지고, 선박의 대기시간을 줄임으로써 연료 절감 및 온실가스 감축효과를 기대할 수 있습니다.

---------------------------

### 분석 과정

1. Package Import & Data Load

2. Data Preprocessing

3. 모델 학습 및 특성 중요도 확인

4. 특성 중요도로부터 Feature Selection

5. K-Fold Model Fitting & Validation

6. Submission

-------------------------------------

### 데이터 설명

| Feature Name        | Description                                     | 단위           | 비고                                                |
|---------------------|-------------------------------------------------|--------------|----------------------------------------------------|
| ARI_CO              | 도착항의 소속국가(도착항 앞 2글자)          |              |                                                    |
| ARI_PO              | 도착항의 항구명(도착항 뒤 글자)             |              |                                                    |
| SHIP_TYPE_CATEGORY  | 선종 통합 바탕으로 5대 선종으로 분류     |              |                                                    |
| DIST                | 정박지(ber_port)와 접안지 사이의 거리    | km           |                                                    |
| ATA                 | anc_port에 도착한 시점의 utc. 실제 정박 시각(Actual Time of Arrival) | hour |                                                    |
| ID                  | 선박식별 일련번호                            |              |                                                    |
| BREADTH             | 선박의 폭                                      | m            |                                                    |
| BUILT               | 선박의 연령                                  | year         |                                                    |
| DEADWEIGHT          | 선박의 재화중량톤수                        | ton          |                                                    |
| DEPTH               | 선박의 깊이                                  | m            |                                                    |
| DRAUGHT             | 흘수 높이                                  | m            |                                                    |
| GT                  | 용적톤수(Gross Tonnage)값                | GT(m^3)      |                                                    |
| LENGTH              | 선박의 길이                                  | m            |                                                    |
| SHIPMANAGER         | 선박 소유주                                 |              |                                                    |
| FLAG                | 선박의 국적                                  |              |                                                    |
| U_WIND              | 풍향 u벡터                                 | m/s          | ATA 시점 이전에 생성된 예보 데이터             |
| V_WIND              | 풍향 v벡터                                 | m/s          |                                                    |
| AIR_TEMPERATURE     | 기온                                         | ºC          |                                                    |
| BN                  | 보퍼트 풍력 계급                          |              |                                                    |
| ATA_LT              | anc_port에 도착한 시점의 현지 정박 시각(Local Time of Arrival)(단위 : H) | hour |                                                 |
| PORT_SIZE           | 접안지 폴리곤 영역의 크기                 | km^2         |                                                    |
| CI_HOUR             | 대기시간                                   | hour         | Target                                            |

-------------------------------------

### 모델선정

- lgbm 모델 선정 (회귀 모델 중, randomforest, decisiontree, xgboost 등의 모델을 쓴 결과 가장 MAE값이 낮았음.)

  - 모델의 하이퍼 마라미터는 GridSearch를 이용하여, MAE 값을 낮출 수 있는 최선의 하이퍼 파라미터를 모색함.

 -------------------------------------


  
