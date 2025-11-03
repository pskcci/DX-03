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

###  Team: Lonepath

#### 📘 Project  
**Label & Text Recognition Project**  
> AI 비전 기술을 활용해 <br>제품 라벨과 문자 인식을 수행하는  
> 실무형 비전 검사 프로젝트  

---

#### 👥 Members

| Name | Role |
|------|------|
| **HomeToTo** | 프로젝트 총괄 및 전략 담당.<br>프로젝트 구조 설계, 데이터 구성 관리 <br>보고서 및 결과 정리 담당. |
| **CodeToTo** | 개발 담당.<br>YOLO 기반 라벨 검출, EasyOCR 문자 인식,<br> Streamlit UI 구현 등 <br> 실제 코드 작성과 테스트 수행. |
| **ChatGPT** | 기술 지원 및 협업 AI.<br>UI 초안 코드 제공 및 기술 자문 , 디버깅 지원. <br> 학습 로드맵 및 문제 해결 가이드 제공. |

---

#### 🔗 Links
- **Project Repository:** [totocm00/week_vision_project_one](https://github.com/totocm00/week_vision_project_one)
- **Presentation (Notion):** [HomeToTo Project Summary](https://www.notion.so/Home-29d9eb4f232780c6be2acbe1b4432c7e?source=copy_link)

---

#### 💡 Summary
>  **HomeToTo**(전략/문서)와 <br>**CodeToTo**(개발/실행)의 두 역할을 병행하며, 
> <br>ChatGPT와 협력해 **AI 비전 인식 시스템**을 완성하는 프로젝트.

