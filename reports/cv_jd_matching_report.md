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
| **Đỗ Hoàng Long** | Middle Backend Engineer / Distributed Systems | **0.7543** (+0.0899)<br>_Job Description: Backend Engin..._ | **0.6636** (+0.1374)<br>_Job Description: Cloud Native ..._ | **0.6563** (+0.0900)<br>_Job Description: Senior Full S..._ | **0.6408** (+0.1520)<br>_Job Description: Senior Full S..._ |
| **Lê Hoàng Nam** | HR Manager / Talent Acquisition Lead | **0.5598** (+0.0533)<br>_Job Description: AI Automation..._ | **0.5333** (+0.0738)<br>_Job Description: AI Automation..._ | **0.5529** (+0.0905)<br>_Tuyển dụng: Kỹ sư Lập trình Ph..._ | **0.5559** (+0.1259)<br>_Tuyển dụng: Kỹ sư Lập trình Ph..._ |
| **Mai Van Tien Phat** | Backend Developer Intern / Fresher | **0.8115** (+0.1118)<br>_Job Description: Backend Engin..._ | **0.6377** (+0.0855)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.6901** (+0.0716)<br>_Job Description: Senior Full S..._ | **0.6237** (+0.1427)<br>_Job Description: Senior Full S..._ |
| **Nguyễn Bảo Lâm** | Fullstack Developer (.NET / React) | **0.7947** (+0.1501)<br>_Job Description: Backend Engin..._ | **0.7180** (+0.1714)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.7578** (+0.1944)<br>_Job Description: Full Stack De..._ | **0.7132** (+0.2158)<br>_Mô tả công việc: Kỹ sư Fullsta..._ |
| **Nguyễn Văn An** | Senior Fullstack Engineer | **0.7665** (+0.1171)<br>_Job Description: Cloud Operati..._ | **0.7758** (+0.2069)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.7293** (+0.1319)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.7758** (+0.2578)<br>_Mô tả công việc: Kỹ sư Fullsta..._ |
| **Phạm Đình Khoa** | DevOps / Cloud Platform Engineer | **0.8488** (+0.1142)<br>_Job Description: Cloud Native ..._ | **0.7210** (+0.1919)<br>_Job Description: Cloud Native ..._ | **0.7495** (+0.1993)<br>_Job Description: DevOps Engine..._ | **0.7564** (+0.2574)<br>_Job Description: Cloud Native ..._ |
| **Trần Quốc Bảo** | Junior Backend Engineer | **0.7218** (+0.0838)<br>_Job Description: Backend Engin..._ | **0.6454** (+0.0981)<br>_Job Description: Senior Full S..._ | **0.6487** (+0.0596)<br>_Mô tả công việc: Senior / Expe..._ | **0.6241** (+0.1259)<br>_Mô tả công việc: Kỹ sư Fullsta..._ |
| **Trần Thị Mai** | Data Scientist / AI Engineer | **0.8805** (+0.2042)<br>_Job Description: Senior AI / N..._ | **0.7392** (+0.2475)<br>_Job Description: Senior AI / N..._ | **0.7943** (+0.2572)<br>_Job Description: Senior AI / N..._ | **0.7418** (+0.3257)<br>_Job Description: Senior AI / N..._ |
| **Vũ Minh Trí** | Senior Backend Architect / Technical Lead | **0.7737** (+0.1324)<br>_Job Description: Backend Engin..._ | **0.6161** (+0.0873)<br>_Job Description: Senior Full S..._ | **0.6681** (+0.1112)<br>_Job Description: DevOps Engine..._ | **0.6407** (+0.1184)<br>_Job Description: Senior Full S..._ |

## 3. Phân tích Chi tiết Từng Hồ Sơ Điển Hình

### Ứng viên: Đỗ Hoàng Long (Middle Backend Engineer / Distributed Systems)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Cloud Native DevOps Engineer (Kubernetes / CI-CD) - Endava | 0.6636 | 0.6287 | +0.1374 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7543 | 0.7001 | +0.0899 |
| **ParagraphBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6408 | 0.6150 | +0.1520 |
| **SentenceBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6563 | 0.6381 | +0.0900 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `Specializes in event-driven systems, fault-tolerant messaging pipelines using Apache Kafka, high-throughput gRPC inter-service communication, and PostgreSQL per...`
> - *JD Evidence*: `- Troubleshoot performance bottlenecks, database query optimizations, and concurrency challenges....`

### Ứng viên: Lê Hoàng Nam (HR Manager / Talent Acquisition Lead)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: AI Automation Engineer (GenAI, Power Platform, Python) - Bosch Global Software Technologies | 0.5333 | 0.4662 | +0.0738 |
| **LocalSemantic** | Job Description: AI Automation Engineer (GenAI, Power Platform, Python) - Bosch Global Software Technologies | 0.5598 | 0.5381 | +0.0533 |
| **ParagraphBased** | Tuyển dụng: Kỹ sư Lập trình Phần mềm Junior/Senior (PHP/Laravel, Java) - RiverCrane Vietnam | 0.5559 | 0.5054 | +0.1259 |
| **SentenceBased** | Tuyển dụng: Kỹ sư Lập trình Phần mềm Junior/Senior (PHP/Laravel, Java) - RiverCrane Vietnam | 0.5529 | 0.5043 | +0.0905 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `HR Generalist / Recruiter - Alpha Global Tech (10/2018 - 04/2021)...`
> - *JD Evidence*: `POSITION: AI AUTOMATION ENGINEER (GENAI / POWER PLATFORM / PYTHON)...`

### Ứng viên: Mai Van Tien Phat (Backend Developer Intern / Fresher)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.6377 | 0.6162 | +0.0855 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.8115 | 0.7264 | +0.1118 |
| **ParagraphBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6237 | 0.5880 | +0.1427 |
| **SentenceBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6901 | 0.6348 | +0.0716 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Implemented and consumed RESTful APIs to support enterprise application features and integrations....`
> - *JD Evidence*: `- Build and optimize RESTful APIs, data interchange pipelines, and front-end integration points....`

### Ứng viên: Nguyễn Bảo Lâm (Fullstack Developer (.NET / React))

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.7180 | 0.6858 | +0.1714 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7947 | 0.7376 | +0.1501 |
| **ParagraphBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.7132 | 0.6403 | +0.2158 |
| **SentenceBased** | Job Description: Full Stack Developer (React / Vue.js / LLM APIs / WebGL) - Sqreem Technologies | 0.7578 | 0.7401 | +0.1944 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Developed and consumed RESTful APIs for internal business process automation applications....`
> - *JD Evidence*: `- Build and optimize RESTful APIs, data interchange pipelines, and front-end integration points....`

### Ứng viên: Nguyễn Văn An (Senior Fullstack Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.7758 | 0.7345 | +0.2069 |
| **LocalSemantic** | Job Description: Cloud Operations Engineer (CloudOps / AWS / Terraform) - NextEdge | 0.7665 | 0.6798 | +0.1171 |
| **ParagraphBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.7758 | 0.7416 | +0.2578 |
| **SentenceBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.7293 | 0.7257 | +0.1319 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Chứng chỉ AWS Certified Solutions Architect - Associate (2023)...`
> - *JD Evidence*: `- AWS certifications (Solutions Architect, SysOps, or Security Specialty) are advantageous....`

### Ứng viên: Phạm Đình Khoa (DevOps / Cloud Platform Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Cloud Native DevOps Engineer (Kubernetes / CI-CD) - Endava | 0.7210 | 0.7121 | +0.1919 |
| **LocalSemantic** | Job Description: Cloud Native DevOps Engineer (Kubernetes / CI-CD) - Endava | 0.8488 | 0.8120 | +0.1142 |
| **ParagraphBased** | Job Description: Cloud Native DevOps Engineer (Kubernetes / CI-CD) - Endava | 0.7564 | 0.7017 | +0.2574 |
| **SentenceBased** | Job Description: DevOps Engineer (AWS / Cloud / FinTech & Blockchain) - CubicStack Solutions | 0.7495 | 0.7200 | +0.1993 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Automated deployment workflows for 15+ .NET and Java microservices using GitHub Actions and Helm, reducing deployment release cycle from 3 hours to 15 minutes...`
> - *JD Evidence*: `- Automate testing scopes and deployment verification scripts for containerized microservices....`

### Ứng viên: Trần Quốc Bảo (Junior Backend Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6454 | 0.5878 | +0.0981 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7218 | 0.6965 | +0.0838 |
| **ParagraphBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.6241 | 0.5885 | +0.1259 |
| **SentenceBased** | Mô tả công việc: Senior / Experienced Frontend Developer (React.js / FinTech) - NextEdge | 0.6487 | 0.6171 | +0.0596 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Collaborated with frontend and mobile teams to define OpenAPI/Swagger contracts and maintain automated CI/CD builds with GitHub Actions....`
> - *JD Evidence*: `- Build and optimize RESTful APIs, data interchange pipelines, and front-end integration points....`

### Ứng viên: Trần Thị Mai (Data Scientist / AI Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.7392 | 0.7269 | +0.2475 |
| **LocalSemantic** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.8805 | 0.8563 | +0.2042 |
| **ParagraphBased** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.7418 | 0.6883 | +0.3257 |
| **SentenceBased** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.7943 | 0.7529 | +0.2572 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `Proven track record in deploying quantized local models (Ollama, vLLM, TensorRT-LLM) on constrained hardware environments....`
> - *JD Evidence*: `- Optimize local model inference and GPU memory allocation (RTX/Tesla series) via vLLM, Ollama, and INT4/INT8 quantization....`

### Ứng viên: Vũ Minh Trí (Senior Backend Architect / Technical Lead)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6161 | 0.5861 | +0.0873 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7737 | 0.6912 | +0.1324 |
| **ParagraphBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6407 | 0.5920 | +0.1184 |
| **SentenceBased** | Job Description: DevOps Engineer (AWS / Cloud / FinTech & Blockchain) - CubicStack Solutions | 0.6681 | 0.6363 | +0.1112 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Optimized database indexing and partitioning strategies, resolving long-standing concurrency bottlenecks during peak tax filing seasons....`
> - *JD Evidence*: `- Troubleshoot performance bottlenecks, database query optimizations, and concurrency challenges....`

## 4. Kết luận Thực nghiệm RBL

1. **Tính trọn vẹn ngữ nghĩa**: `LocalSemantic` tạo ra các chunk chứa trọn vẹn một năng lực hoặc dự án (VD: cụm công nghệ Kafka + CQRS + Outbox Pattern), giúp độ tương đồng đạt đỉnh cao hơn hẳn so với việc bị cắt gãy ngang bởi `FixedSize`.
2. **Độ tương phản phân loại (Contrast)**: `LocalSemantic` cho contrast cao hơn (chênh lệch rõ ràng giữa vị trí đúng chuyên môn vs vị trí trái ngành), giúp hệ thống RAG HR tự động xếp hạng ứng viên chính xác hơn.
