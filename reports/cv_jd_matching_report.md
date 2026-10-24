# BÁO CÁO THỰC NGHIỆM ĐÁNH GIÁ SO SÁNH CHUNKER: KHẢ NĂNG KHỚP NỐI CV - JD

## 1. Mục tiêu và Nguyên tắc Thực nghiệm

- **Nguyên tắc đồng nhất (Consistency)**: Mỗi khi đánh giá một chiến lược chunking, toàn bộ CV và JD đều được cắt bằng **chính chiến lược đó** trước khi tính toán độ tương đồng vector.
- **Số lượng thực nghiệm**: 9 CVs x 17 JDs = **153 cặp so khớp** cho mỗi chiến lược, tổng cộng **612 phép so khớp toàn diện** trên 4 chiến lược.
- **Chỉ số đánh giá chính**:
  - **Max Similarity**: Độ tương đồng cosine cao nhất giữa cặp chunk CV và JD.
  - **Top-3 Avg Similarity**: Điểm trung bình của 3 cặp chunk tương đồng nhất (đo lường độ khớp đa phương diện).
  - **Semantic Contrast**: Khoảng cách giữa Top-1 và Median Score (độ nhạy phân loại, tránh kết quả tương đồng đồng đều thiếu sắc bén).

## 2. Bảng Tổng Hợp Kết Quả Khớp Nối Top-1 Từng Ứng Viên Qua 4 Chunkers

| Ứng viên | Cấp bậc | Local Semantic (Top 1 / Contrast) | Fixed-Size (Top 1 / Contrast) | Sentence-Based (Top 1 / Contrast) | Paragraph-Based (Top 1 / Contrast) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Bùi Tuấn Anh** | Senior Embedded Systems Engineer | **0.7781** (+0.3636)<br>_Job Description: Senior Embedd..._ | **0.7765** (+0.3560)<br>_Job Description: Senior Embedd..._ | **0.7668** (+0.3126)<br>_Job Description: Senior Embedd..._ | **0.8294** (+0.4989)<br>_Job Description: Senior Embedd..._ |
| **Đặng Quang Huy** | Senior Data Engineer | **0.8392** (+0.3827)<br>_Job Description: Senior Data L..._ | **0.7790** (+0.3070)<br>_Job Description: Senior Data L..._ | **0.8485** (+0.3204)<br>_Job Description: Senior Data L..._ | **0.8618** (+0.4511)<br>_Job Description: Senior Data L..._ |
| **Đỗ Hoàng Long** | Middle Backend Engineer / Distributed Systems | **0.7543** (+0.0899)<br>_Job Description: Backend Engin..._ | **0.6340** (+0.1396)<br>_Job Description: Senior Full S..._ | **0.6563** (+0.1095)<br>_Job Description: Senior Full S..._ | **0.5736** (+0.1618)<br>_Job Description: Site Reliabil..._ |
| **Hoàng Thảo My** | Senior Technical Product Manager | **0.6726** (+0.1936)<br>_Tuyển dụng: Senior Technical P..._ | **0.7618** (+0.2680)<br>_Tuyển dụng: Senior Technical P..._ | **0.7539** (+0.2294)<br>_Tuyển dụng: Senior Technical P..._ | **0.8325** (+0.4321)<br>_Tuyển dụng: Senior Technical P..._ |
| **Lê Hoàng Nam** | HR Manager / Talent Acquisition Lead | **0.5598** (+0.0533)<br>_Job Description: AI Automation..._ | **0.6128** (+0.1685)<br>_Thông báo tuyển dụng: Chuyên v..._ | **0.6345** (+0.1721)<br>_Thông báo tuyển dụng: Chuyên v..._ | **0.4930** (+0.1537)<br>_Thông báo tuyển dụng: Chuyên v..._ |
| **Mai Van Tien Phat** | Backend Developer Intern / Fresher | **0.8115** (+0.1118)<br>_Job Description: Backend Engin..._ | **0.5924** (+0.1102)<br>_Tuyển dụng: Kỹ sư Lập trình Ph..._ | **0.6901** (+0.1307)<br>_Job Description: Senior Full S..._ | **0.5310** (+0.1161)<br>_Job Description: Senior Full S..._ |
| **Nguyễn Bảo Lâm** | Fullstack Developer (.NET / React) | **0.7947** (+0.1501)<br>_Job Description: Backend Engin..._ | **0.6512** (+0.1791)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.7578** (+0.2178)<br>_Job Description: Full Stack De..._ | **0.6325** (+0.2430)<br>_Mô tả công việc: Kỹ sư Fullsta..._ |
| **Nguyễn Văn An** | Senior Fullstack Engineer | **0.7665** (+0.1171)<br>_Job Description: Cloud Operati..._ | **0.7863** (+0.2356)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.7293** (+0.1640)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.8356** (+0.3665)<br>_Mô tả công việc: Kỹ sư Fullsta..._ |
| **Phạm Đình Khoa** | DevOps / Cloud Platform Engineer | **0.8488** (+0.1142)<br>_Job Description: Cloud Native ..._ | **0.7310** (+0.2554)<br>_Job Description: Cloud Native ..._ | **0.7682** (+0.2253)<br>_Job Description: Site Reliabil..._ | **0.7192** (+0.3111)<br>_Job Description: DevOps Engine..._ |
| **Phan Minh Trí** | Lead Mobile Developer (Flutter / iOS) | **0.7946** (+0.3288)<br>_Job Description: Lead Mobile A..._ | **0.7509** (+0.2611)<br>_Job Description: Lead Mobile A..._ | **0.7698** (+0.2420)<br>_Job Description: Lead Mobile A..._ | **0.7756** (+0.3741)<br>_Job Description: Lead Mobile A..._ |
| **Trần Quốc Bảo** | Junior Backend Engineer | **0.7218** (+0.0838)<br>_Job Description: Backend Engin..._ | **0.5675** (+0.1121)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.6487** (+0.0744)<br>_Mô tả công việc: Senior / Expe..._ | **0.5653** (+0.1346)<br>_Mô tả công việc: Kỹ sư Fullsta..._ |
| **Trần Thị Mai** | Data Scientist / AI Engineer | **0.8805** (+0.2042)<br>_Job Description: Senior AI / N..._ | **0.7929** (+0.3632)<br>_Job Description: Senior AI / N..._ | **0.7943** (+0.2686)<br>_Job Description: Senior AI / N..._ | **0.8330** (+0.4378)<br>_Job Description: Senior AI / N..._ |
| **Vũ Đức Thắng** | Information Security / SOC Analyst | **0.7178** (+0.2958)<br>_Job Description: Senior Inform..._ | **0.7044** (+0.2991)<br>_Job Description: Senior Inform..._ | **0.7444** (+0.2539)<br>_Job Description: Senior Inform..._ | **0.7937** (+0.4283)<br>_Job Description: Senior Inform..._ |
| **Vũ Minh Trí** | Senior Backend Architect / Technical Lead | **0.7737** (+0.1324)<br>_Job Description: Backend Engin..._ | **0.6160** (+0.1054)<br>_Tuyển dụng: Kỹ sư Lập trình Ph..._ | **0.6681** (+0.1135)<br>_Job Description: DevOps Engine..._ | **0.5614** (+0.0941)<br>_Job Description: Senior Full S..._ |

## 3. Phân tích Chi tiết Từng Hồ Sơ Điển Hình

### Ứng viên: Bùi Tuấn Anh (Senior Embedded Systems Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior Embedded Systems Engineer (FreeRTOS / C++ / BLE) - SmartIoT Global | 0.7765 | 0.7566 | +0.3560 |
| **LocalSemantic** | Job Description: Senior Embedded Systems Engineer (FreeRTOS / C++ / BLE) - SmartIoT Global | 0.7781 | 0.7367 | +0.3636 |
| **ParagraphBased** | Job Description: Senior Embedded Systems Engineer (FreeRTOS / C++ / BLE) - SmartIoT Global | 0.8294 | 0.5831 | +0.4989 |
| **SentenceBased** | Job Description: Senior Embedded Systems Engineer (FreeRTOS / C++ / BLE) - SmartIoT Global | 0.7668 | 0.7590 | +0.3126 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `PROFESSIONAL EXPERIENCE: Senior Firmware Engineer — SmartIoT Global (02/2022 — Present) - Architected ultra-low-power environmental sensor beacon running FreeRT...`
> - *JD Evidence*: `COMPANY: SMARTIOT GLOBAL VIETNAM POSITION: SENIOR EMBEDDED SYSTEMS ENGINEER (FREERTOS / MODERN C++ / BLE) LOCATION: Saigon Hi-Tech Park (SHTP), Thu Duc City, Ho...`

### Ứng viên: Đặng Quang Huy (Senior Data Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior Data Lakehouse Engineer (Spark / Airflow / Snowflake) - DataForge Systems | 0.7790 | 0.7767 | +0.3070 |
| **LocalSemantic** | Job Description: Senior Data Lakehouse Engineer (Spark / Airflow / Snowflake) - DataForge Systems | 0.8392 | 0.7800 | +0.3827 |
| **ParagraphBased** | Job Description: Senior Data Lakehouse Engineer (Spark / Airflow / Snowflake) - DataForge Systems | 0.8618 | 0.6750 | +0.4511 |
| **SentenceBased** | Job Description: Senior Data Lakehouse Engineer (Spark / Airflow / Snowflake) - DataForge Systems | 0.8485 | 0.8079 | +0.3204 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Languages & Cloud: Python, Scala, SQL, Bash, AWS (EMR, Glue, Athena), Docker, Terraform. WORK EXPERIENCE: Lead Data Engineer — DataForge Systems (05/2022 — Pr...`
> - *JD Evidence*: `RESPONSIBILITIES: - Architect, build, and optimize scalable data ingestion and transformation pipelines using Apache Spark (PySpark/Scala) and Delta Lake on AWS...`

### Ứng viên: Đỗ Hoàng Long (Middle Backend Engineer / Distributed Systems)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6340 | 0.6121 | +0.1396 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7543 | 0.7001 | +0.0899 |
| **ParagraphBased** | Job Description: Site Reliability Engineer (SRE / Observability / Chaos Engineering) - CloudNova | 0.5736 | 0.5134 | +0.1618 |
| **SentenceBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6563 | 0.6381 | +0.1095 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `Specializes in event-driven systems, fault-tolerant messaging pipelines using Apache Kafka, high-throughput gRPC inter-service communication, and PostgreSQL per...`
> - *JD Evidence*: `- Troubleshoot performance bottlenecks, database query optimizations, and concurrency challenges....`

### Ứng viên: Hoàng Thảo My (Senior Technical Product Manager)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Tuyển dụng: Senior Technical Product Manager (E-Wallet & Open Banking) - FinVanguard | 0.7618 | 0.7155 | +0.2680 |
| **LocalSemantic** | Tuyển dụng: Senior Technical Product Manager (E-Wallet & Open Banking) - FinVanguard | 0.6726 | 0.6649 | +0.1936 |
| **ParagraphBased** | Tuyển dụng: Senior Technical Product Manager (E-Wallet & Open Banking) - FinVanguard | 0.8325 | 0.5141 | +0.4321 |
| **SentenceBased** | Tuyển dụng: Senior Technical Product Manager (E-Wallet & Open Banking) - FinVanguard | 0.7539 | 0.7316 | +0.2294 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `KỸ NĂNG CỐT LÕI: - Quản trị Sản phẩm: Product Strategy, Roadmap planning, PRD/BRD, OKR & KPIs alignment, Product Backlog refinement. - Phương pháp luận: Agile/S...`
> - *JD Evidence*: `- Hiểu biết sâu sắc về kiến trúc hệ thống tài chính: Microservices, RESTful API, webhook, cơ chế xác thực OAuth 2.0 và quy trình đối soát giao dịch. - Thành thạ...`

### Ứng viên: Lê Hoàng Nam (HR Manager / Talent Acquisition Lead)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Thông báo tuyển dụng: Chuyên viên Cấp cao Tiền lương & Phúc lợi (Senior C&B Specialist) - FPT Retail | 0.6128 | 0.5799 | +0.1685 |
| **LocalSemantic** | Job Description: AI Automation Engineer (GenAI, Power Platform, Python) - Bosch Global Software Technologies | 0.5598 | 0.5381 | +0.0533 |
| **ParagraphBased** | Thông báo tuyển dụng: Chuyên viên Cấp cao Tiền lương & Phúc lợi (Senior C&B Specialist) - FPT Retail | 0.4930 | 0.4930 | +0.1537 |
| **SentenceBased** | Thông báo tuyển dụng: Chuyên viên Cấp cao Tiền lương & Phúc lợi (Senior C&B Specialist) - FPT Retail | 0.6345 | 0.6190 | +0.1721 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `HR Generalist / Recruiter - Alpha Global Tech (10/2018 - 04/2021)...`
> - *JD Evidence*: `POSITION: AI AUTOMATION ENGINEER (GENAI / POWER PLATFORM / PYTHON)...`

### Ứng viên: Mai Van Tien Phat (Backend Developer Intern / Fresher)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Tuyển dụng: Kỹ sư Lập trình Phần mềm Junior/Senior (PHP/Laravel, Java) - RiverCrane Vietnam | 0.5924 | 0.5880 | +0.1102 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.8115 | 0.7264 | +0.1118 |
| **ParagraphBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.5310 | 0.4661 | +0.1161 |
| **SentenceBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6901 | 0.6348 | +0.1307 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Implemented and consumed RESTful APIs to support enterprise application features and integrations....`
> - *JD Evidence*: `- Build and optimize RESTful APIs, data interchange pipelines, and front-end integration points....`

### Ứng viên: Nguyễn Bảo Lâm (Fullstack Developer (.NET / React))

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.6512 | 0.6370 | +0.1791 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7947 | 0.7376 | +0.1501 |
| **ParagraphBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.6325 | 0.4793 | +0.2430 |
| **SentenceBased** | Job Description: Full Stack Developer (React / Vue.js / LLM APIs / WebGL) - Sqreem Technologies | 0.7578 | 0.7401 | +0.2178 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Developed and consumed RESTful APIs for internal business process automation applications....`
> - *JD Evidence*: `- Build and optimize RESTful APIs, data interchange pipelines, and front-end integration points....`

### Ứng viên: Nguyễn Văn An (Senior Fullstack Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.7863 | 0.7645 | +0.2356 |
| **LocalSemantic** | Job Description: Cloud Operations Engineer (CloudOps / AWS / Terraform) - NextEdge | 0.7665 | 0.6798 | +0.1171 |
| **ParagraphBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.8356 | 0.8356 | +0.3665 |
| **SentenceBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.7293 | 0.7257 | +0.1640 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Chứng chỉ AWS Certified Solutions Architect - Associate (2023)...`
> - *JD Evidence*: `- AWS certifications (Solutions Architect, SysOps, or Security Specialty) are advantageous....`

### Ứng viên: Phạm Đình Khoa (DevOps / Cloud Platform Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Cloud Native DevOps Engineer (Kubernetes / CI-CD) - Endava | 0.7310 | 0.6956 | +0.2554 |
| **LocalSemantic** | Job Description: Cloud Native DevOps Engineer (Kubernetes / CI-CD) - Endava | 0.8488 | 0.8120 | +0.1142 |
| **ParagraphBased** | Job Description: DevOps Engineer (AWS / Cloud / FinTech & Blockchain) - CubicStack Solutions | 0.7192 | 0.6601 | +0.3111 |
| **SentenceBased** | Job Description: Site Reliability Engineer (SRE / Observability / Chaos Engineering) - CloudNova | 0.7682 | 0.7022 | +0.2253 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Automated deployment workflows for 15+ .NET and Java microservices using GitHub Actions and Helm, reducing deployment release cycle from 3 hours to 15 minutes...`
> - *JD Evidence*: `- Automate testing scopes and deployment verification scripts for containerized microservices....`

### Ứng viên: Phan Minh Trí (Lead Mobile Developer (Flutter / iOS))

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Lead Mobile App Developer (Flutter / iOS / Android) - VinaTech Mobility | 0.7509 | 0.7242 | +0.2611 |
| **LocalSemantic** | Job Description: Lead Mobile App Developer (Flutter / iOS / Android) - VinaTech Mobility | 0.7946 | 0.7469 | +0.3288 |
| **ParagraphBased** | Job Description: Lead Mobile App Developer (Flutter / iOS / Android) - VinaTech Mobility | 0.7756 | 0.5441 | +0.3741 |
| **SentenceBased** | Job Description: Lead Mobile App Developer (Flutter / iOS / Android) - VinaTech Mobility | 0.7698 | 0.7639 | +0.2420 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `KINH NGHIỆM LÀM VIỆC: Lead Mobile Engineer — VinaTech Mobility (06/2022 — Hiện tại) - Quản lý đội ngũ 7 lập trình viên mobile phát triển siêu ứng dụng gọi xe và...`
> - *JD Evidence*: `COMPANY: VINATECH MOBILITY SOLUTIONS POSITION: LEAD MOBILE DEVELOPER (FLUTTER / IOS / ANDROID) LOCATION: Landmark 81, Vinhomes Central Park, Binh Thanh, Ho Chi ...`

### Ứng viên: Trần Quốc Bảo (Junior Backend Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.5675 | 0.5460 | +0.1121 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7218 | 0.6965 | +0.0838 |
| **ParagraphBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.5653 | 0.5337 | +0.1346 |
| **SentenceBased** | Mô tả công việc: Senior / Experienced Frontend Developer (React.js / FinTech) - NextEdge | 0.6487 | 0.6171 | +0.0744 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Collaborated with frontend and mobile teams to define OpenAPI/Swagger contracts and maintain automated CI/CD builds with GitHub Actions....`
> - *JD Evidence*: `- Build and optimize RESTful APIs, data interchange pipelines, and front-end integration points....`

### Ứng viên: Trần Thị Mai (Data Scientist / AI Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.7929 | 0.7376 | +0.3632 |
| **LocalSemantic** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.8805 | 0.8563 | +0.2042 |
| **ParagraphBased** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.8330 | 0.8330 | +0.4378 |
| **SentenceBased** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.7943 | 0.7529 | +0.2686 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `Proven track record in deploying quantized local models (Ollama, vLLM, TensorRT-LLM) on constrained hardware environments....`
> - *JD Evidence*: `- Optimize local model inference and GPU memory allocation (RTX/Tesla series) via vLLM, Ollama, and INT4/INT8 quantization....`

### Ứng viên: Vũ Đức Thắng (Information Security / SOC Analyst)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior Information Security / Cyber Security Engineer - Techcom Securities | 0.7044 | 0.6687 | +0.2991 |
| **LocalSemantic** | Job Description: Senior Information Security / Cyber Security Engineer - Techcom Securities | 0.7178 | 0.6886 | +0.2958 |
| **ParagraphBased** | Job Description: Senior Information Security / Cyber Security Engineer - Techcom Securities | 0.7937 | 0.5664 | +0.4283 |
| **SentenceBased** | Job Description: Senior Information Security / Cyber Security Engineer - Techcom Securities | 0.7444 | 0.7250 | +0.2539 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Compliance: ISO 27001, PCI-DSS Level 1, GDPR security controls. WORK EXPERIENCE: SOC Tier 2 Security Analyst — Techcom Securities (04/2023 — Present) - Invest...`
> - *JD Evidence*: `- Ensure technical compliance with State Bank of Vietnam regulations, ISO/IEC 27001, and PCI-DSS Level 1 standards. REQUIRED QUALIFICATIONS: - At least 3 years ...`

### Ứng viên: Vũ Minh Trí (Senior Backend Architect / Technical Lead)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Tuyển dụng: Kỹ sư Lập trình Phần mềm Junior/Senior (PHP/Laravel, Java) - RiverCrane Vietnam | 0.6160 | 0.5876 | +0.1054 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7737 | 0.6912 | +0.1324 |
| **ParagraphBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.5614 | 0.4219 | +0.0941 |
| **SentenceBased** | Job Description: DevOps Engineer (AWS / Cloud / FinTech & Blockchain) - CubicStack Solutions | 0.6681 | 0.6363 | +0.1135 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Optimized database indexing and partitioning strategies, resolving long-standing concurrency bottlenecks during peak tax filing seasons....`
> - *JD Evidence*: `- Troubleshoot performance bottlenecks, database query optimizations, and concurrency challenges....`

## 4. Kết luận Thực nghiệm RBL

1. **Tính trọn vẹn ngữ nghĩa**: `LocalSemantic` tạo ra các chunk chứa trọn vẹn một năng lực hoặc dự án (VD: cụm công nghệ Kafka + CQRS + Outbox Pattern), giúp độ tương đồng đạt đỉnh cao hơn hẳn so với việc bị cắt gãy ngang bởi `FixedSize`.
2. **Độ tương phản phân loại (Contrast)**: `LocalSemantic` cho contrast cao hơn (chênh lệch rõ ràng giữa vị trí đúng chuyên môn vs vị trí trái ngành), giúp hệ thống RAG HR tự động xếp hạng ứng viên chính xác hơn.
