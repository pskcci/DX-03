# Project ABC

프로젝트 설명: 이 프로젝트는 신경다양인(Neurodivergent individuals)이 면접 상황에서 겪는 비언어적 소통의 어려움(특히 시선 처리)을 해소하기 위한 AI 기반 실시간 피드백 훈련 도구의 최소 기능 제품(MVP)입니다.최종 목표: $\text{Python}$과 $\text{PyQt}$를 주력으로 사용하여 웹캠을 통해 사용자의 면접 상황을 분석하고, 시선 회피와 같은 특정 행동을 감지하여 실시간 텍스트 피드백을 제공하는 독립 실행형 $\text{GUI}$ 애플리케이션을 구축합니다

## High Level Design

이 프로젝트는 $\text{GUI}$와 $\text{AI}$ 비전 분석 모듈을 명확히 분리합니다. $\text{PyQt}$가 사용자 인터페이스와 $\text{VideoProcessor}$의 통신을 담당하며, $\text{OpenCV}$와 $\text{MediaPipe}$가 실시간 비디오 분석을 수행합니다.아키텍처 기술:$\text{MainApp (PyQt)}$: 사용자 상호작용 및 $\text{GUI}$ 표시를 담당합니다. $\text{VideoProcessor}$ 스레드로부터 실시간 프레임과 피드백 데이터를 받아 화면에 출력합니다.$\text{VideoProcessor (Thread)}$: $\text{OpenCV}$로 웹캠 데이터를 읽고, $\text{MediaPipe}$를 사용해 얼굴 및 눈의 랜드마크를 추출합니다. $\text{EyeTrackerLogic}$을 호출하여 시선 회피를 판단하고 $\text{MainApp}$에 신호를 보냅니다.$\text{EyeTrackerLogic}$: 추출된 눈 랜드마크를 기반으로 사용자의 **시선이 화면 중앙(가상의 면접관)**을 벗어났는지 여부를 판단하는 핵심 알고리즘을 수행합니다.

## Clone code

* (각 팀에서 프로젝트를 위해 생성한 repository에 대한 code clone 방법에 대해서 기술)

```shell
git clone https://github.com/xxx/yyy/zzz
```

## Prerequite

* (프로잭트를 실행하기 위해 필요한 dependencies 및 configuration들이 있다면, 설치 및 설정 방법에 대해 기술)

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Steps to build

* (프로젝트를 실행을 위해 빌드 절차 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

make
make install
```

## Steps to run

* (프로젝트 실행방법에 대해서 기술, 특별한 사용방법이 있다면 같이 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

cd /path/to/repo/xxx/
python demo.py -i xxx -m yyy -d zzz
```

## Output

* (프로젝트 실행 화면 캡쳐)

![./result.jpg](./result.jpg)

## Appendix

* (참고 자료 및 알아두어야할 사항들 기술)
