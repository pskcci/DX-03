# 상공회의소 부산기술교육센터 인텔교육 DX 3기

## Clone code 

```shell
git clone --recurse-submodules https://github.com/kccistc/intel-03.git
```

* `--recurse-submodules` option 없이 clone 한 경우, 아래를 통해 submodule update

```shell
git submodule update --init --recursive
```

## Preparation

### Git LFS(Large File System)

* 크기가 큰 바이너리 파일들은 LFS로 관리됩니다.

* git-lfs 설치 전

```shell
# Note bin size is 132 bytes before LFS pull

$ find ./ -iname *.bin|xargs ls -l
-rw-rw-r-- 1 <ID> <GROUP> 132 Nov  6 09:41 ./mosaic-9.bin
-rw-rw-r-- 1 <ID> <GROUP> 132 Nov  6 09:41 ./mosaic-9.bin
-rw-rw-r-- 1 <ID> <GROUP> 132 Nov  6 09:41 ./ssdlite_mobilenet_v2_fp16.bin
-rwxrwxr-x 1 <ID> <GROUP> 132 Nov  6 09:41 ./ssdlite_mobilenet_v2_fp16.bin
```

* git-lfs 설치 후, 다음의 명령어로 전체를 가져 올 수 있습니다.

```shell
$ sudo apt install git-lfs

$ git lfs pull
$ find ./ -iname *.bin|xargs ls -l
-rw-rw-r-- 1 <ID> <GROUP> 3358630 Nov  6 09:41 ./mosaic-9.bin
-rw-rw-r-- 1 <ID> <GROUP> 3358630 Nov  6 09:41 ./mosaic-9.bin
-rw-rw-r-- 1 <ID> <GROUP> 8955146 Nov  6 09:41 ./ssdlite_mobilenet_v2_fp16.bin
-rwxrwxr-x 1 <ID> <GROUP> 8955146 Nov  6 09:41 ./ssdlite_mobilenet_v2_fp16.bin
```

### 환경설정

* [Ubuntu](./doc/environment/ubuntu.md)
* [OpenVINO](./doc/environment/openvino.md)
* [OTX](./doc/environment/otx.md)

## Team projects

### 제출방법

1. 팀구성 및 프로젝트 세부 논의 후, 각 팀은 프로젝트 진행을 위한 Github repository 생성

2. [doc/project/README.md](./doc/project/README.md)을 각 팀이 생성한 repository의 main README.md로 복사 후 팀 프로젝트에 맞게 수정 활용

3. 과제 제출시 `인텔교육 3기 Github repository`에 `New Issue` 생성. 생성된 Issue에 하기 내용 포함되어야 함.

    * Team name : Project Name
    * Project 소개
    * 팀원 및 팀원 역활
    * Project Github repository
    * Project 발표자료 업로드

4. 강사가 생성한 `Milestone`에 생성된 Issue에 추가 

### 평가방법

* [assessment-criteria.pdf](./doc/project/assessment-criteria.pdf) 참고

### 제출현황


### Team: VisionPulse — “몸의 움직임으로 세상을 반응시키다”

사용자의 몸동작을 AI가 인식하여, 카메라 화면 상에 즉각적인 시각적 효과(빛, 파티클, 폭발 등)를 구현하는 Vision AI 인터랙션 프로젝트

* Members
  | Name | Role |
  |----|----|
  | 박상수 | 일정 관리, milestone, 발표 자료 총괄 |
  | 조경원 | AI 도구 모델링, Python Code 작성 |
  | 백다빈, 정경준, 김준현 | Gesture Data 수집 정리, Effect Searching, Effect 연출 구현 |
  
* Project Github : https://github.com/GeneralArang/AI_Project

* 발표자료 : https://www.canva.com/design/DAG3iAsPTpg/zg14XLbA-RDOBjkyxyF_1Q/edit



### Team: 마이너 클래스

* 프로젝트 설명: 이 프로젝트는 신경다양인(Neurodivergent individuals)이 면접 상황에서 겪는 비언어적 소통의 어려움을 해소하기 위한 AI 기반 실시간 피드백 훈련 도구입니다.
* 최종 목표: Python을 주력으로 사용하여 웹캠을 통해 사용자의 면접 상황을 분석하고, 시선 회피, 몸 흔들기와 같은 특정 행동을 감지하여 실시간 텍스트 피드백을 제공하는 독립 실행형 GUI 애플리케이션을 구축합니다.


* Members
  | Name | Role |
  |----|----|
  | 민해인 | Project lead, 프로젝트를 총괄하고 망하면 책임진다. |
  | 서준희 | Project manager, 마일스톤을 생성하고 프로젝트 이슈 진행상황을 관리한다. |
  | 이승현 | AI modeling, 원하는 결과가 나오도록 AI model을 선택, data 수집,Architect, 프로젝트의 component를 구성하고 상위 디자인을 책임진다.  training을 수행한다. |
  | 이준혁 | UI design, 사용자 인터페이스를 정의하고 구현한다. |
  
* Project Github : https://github.com/MinorClass/AI_Project.git
* 발표자료 : https://github.com/goodsense/project_aewsome/doc/slide.ppt


### Team: 학습하다 버려짐 ㅠ
쓰레기를 종류 및 오염도에따라 분석하고 그에 맞게 분리수거를 진행한다.
* Members
  | Name | Role |
  |----|----|
  | 변창섭 | Project lead, 전체 프로젝트 총괄 및 로봇 프로그래밍 구현 |
  | 박우현 | AI modeling |
  | 정민수 | Coding, PLC와 AI 모델 간의 데이터 연동 및 시스템 구현 |
  | 박지훈 | 마일스톤을 생성하고 프로젝트 관리한다 |
  | 하진영 | HMI 사용자 인터페이스를 구현한다 |
  | 강부식 | PLC 연동 및 로봇 프로그래밍 구현 |
  | 성승용 | PLC 서브모터 및 컨베이어 구동 작업 진행 |
* Project Github : https://github.com/ByeonChangSeob/trash_T-T
* 발표자료 : 추후 올리겠음


### Team: 마이너 클래스

* 프로젝트 설명: 이 프로젝트는 신경다양인(Neurodivergent individuals)이 면접 상황에서 겪는 비언어적 소통의 어려움을 해소하기 위한 AI 기반 실시간 피드백 훈련 도구입니다.
* 최종 목표: Python을 주력으로 사용하여 웹캠을 통해 사용자의 면접 상황을 분석하고, 시선 회피, 몸 흔들기와 같은 특정 행동을 감지하여 실시간 텍스트 피드백을 제공하는 독립 실행형 GUI 애플리케이션을 구축합니다.


* ### Team: Lonepath
<프로젝트 요약>  
AI 비전 기술을 활용해 제품 라벨과 문자 인식을 수행하는  실무형 비전 검사 프로젝트
* Members
  | Name | Role |
  |----|----|
  |  양원명 | 프로젝트 총괄 및 전략 담당.<br>프로젝트 구조 설계, 데이터 구성 관리 <br>보고서 및 결과 정리 담당. |
  |  | 개발 담당.<br>YOLO 기반 라벨 검출, EasyOCR 문자 인식,<br> Streamlit UI 구현 등 <br> 실제 코드 작성과 테스트 수행. |
  
* Project Github : https://github.com/totocm00/week_vision_project_one.git
* 발표자료 : https://github.com/totocm00/open_vision_factory.git