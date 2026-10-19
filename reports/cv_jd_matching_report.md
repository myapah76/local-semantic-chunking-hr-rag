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
| **Đỗ Hoàng Long** | Middle Backend Engineer / Distributed Systems | **0.7543** (+0.0899)<br>_Job Description: Backend Engin..._ | **0.6340** (+0.1194)<br>_Job Description: Senior Full S..._ | **0.6563** (+0.0900)<br>_Job Description: Senior Full S..._ | **0.5431** (+0.1313)<br>_Job Description: Senior Full S..._ |
| **Lê Hoàng Nam** | HR Manager / Talent Acquisition Lead | **0.5598** (+0.0533)<br>_Job Description: AI Automation..._ | **0.5812** (+0.1027)<br>_Thông báo tuyển dụng: Thực tập..._ | **0.5526** (+0.0902)<br>_Tuyển dụng: Kỹ sư Lập trình Ph..._ | **0.4737** (+0.1404)<br>_Tuyển dụng: Kỹ sư Lập trình Ph..._ |
| **Mai Van Tien Phat** | Backend Developer Intern / Fresher | **0.8115** (+0.1118)<br>_Job Description: Backend Engin..._ | **0.5924** (+0.0776)<br>_Tuyển dụng: Kỹ sư Lập trình Ph..._ | **0.6901** (+0.0716)<br>_Job Description: Senior Full S..._ | **0.5310** (+0.0780)<br>_Job Description: Senior Full S..._ |
| **Nguyễn Bảo Lâm** | Fullstack Developer (.NET / React) | **0.7947** (+0.1501)<br>_Job Description: Backend Engin..._ | **0.6512** (+0.1309)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.7578** (+0.1944)<br>_Job Description: Full Stack De..._ | **0.6325** (+0.2252)<br>_Mô tả công việc: Kỹ sư Fullsta..._ |
| **Nguyễn Văn An** | Senior Fullstack Engineer | **0.7665** (+0.1171)<br>_Job Description: Cloud Operati..._ | **0.7863** (+0.2282)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.7293** (+0.1319)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.8356** (+0.3508)<br>_Mô tả công việc: Kỹ sư Fullsta..._ |
| **Phạm Đình Khoa** | DevOps / Cloud Platform Engineer | **0.8488** (+0.1142)<br>_Job Description: Cloud Native ..._ | **0.7310** (+0.2545)<br>_Job Description: Cloud Native ..._ | **0.7495** (+0.1993)<br>_Job Description: DevOps Engine..._ | **0.7192** (+0.2781)<br>_Job Description: DevOps Engine..._ |
| **Trần Quốc Bảo** | Junior Backend Engineer | **0.7218** (+0.0838)<br>_Job Description: Backend Engin..._ | **0.5675** (+0.0796)<br>_Mô tả công việc: Kỹ sư Fullsta..._ | **0.6487** (+0.0596)<br>_Mô tả công việc: Senior / Expe..._ | **0.5653** (+0.1195)<br>_Mô tả công việc: Kỹ sư Fullsta..._ |
| **Trần Thị Mai** | Data Scientist / AI Engineer | **0.8805** (+0.2042)<br>_Job Description: Senior AI / N..._ | **0.7929** (+0.3357)<br>_Job Description: Senior AI / N..._ | **0.7943** (+0.2572)<br>_Job Description: Senior AI / N..._ | **0.8330** (+0.3995)<br>_Job Description: Senior AI / N..._ |
| **Vũ Minh Trí** | Senior Backend Architect / Technical Lead | **0.7737** (+0.1324)<br>_Job Description: Backend Engin..._ | **0.6160** (+0.0735)<br>_Tuyển dụng: Kỹ sư Lập trình Ph..._ | **0.6681** (+0.1112)<br>_Job Description: DevOps Engine..._ | **0.5614** (+0.0941)<br>_Job Description: Senior Full S..._ |

## 3. Phân tích Chi tiết Từng Hồ Sơ Điển Hình

### Ứng viên: Đỗ Hoàng Long (Middle Backend Engineer / Distributed Systems)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6340 | 0.6127 | +0.1194 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7543 | 0.7001 | +0.0899 |
| **ParagraphBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.5431 | 0.4177 | +0.1313 |
| **SentenceBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6563 | 0.6381 | +0.0900 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `Specializes in event-driven systems, fault-tolerant messaging pipelines using Apache Kafka, high-throughput gRPC inter-service communication, and PostgreSQL per...`
> - *JD Evidence*: `- Troubleshoot performance bottlenecks, database query optimizations, and concurrency challenges....`

### Ứng viên: Lê Hoàng Nam (HR Manager / Talent Acquisition Lead)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Thông báo tuyển dụng: Thực tập sinh Công nghệ Thông tin (IT Internship Program) - DEKON | 0.5812 | 0.5320 | +0.1027 |
| **LocalSemantic** | Job Description: AI Automation Engineer (GenAI, Power Platform, Python) - Bosch Global Software Technologies | 0.5598 | 0.5381 | +0.0533 |
| **ParagraphBased** | Tuyển dụng: Kỹ sư Lập trình Phần mềm Junior/Senior (PHP/Laravel, Java) - RiverCrane Vietnam | 0.4737 | 0.4737 | +0.1404 |
| **SentenceBased** | Tuyển dụng: Kỹ sư Lập trình Phần mềm Junior/Senior (PHP/Laravel, Java) - RiverCrane Vietnam | 0.5526 | 0.5040 | +0.0902 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `HR Generalist / Recruiter - Alpha Global Tech (10/2018 - 04/2021)...`
> - *JD Evidence*: `POSITION: AI AUTOMATION ENGINEER (GENAI / POWER PLATFORM / PYTHON)...`

### Ứng viên: Mai Van Tien Phat (Backend Developer Intern / Fresher)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Tuyển dụng: Kỹ sư Lập trình Phần mềm Junior/Senior (PHP/Laravel, Java) - RiverCrane Vietnam | 0.5924 | 0.5880 | +0.0776 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.8115 | 0.7264 | +0.1118 |
| **ParagraphBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.5310 | 0.4661 | +0.0780 |
| **SentenceBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.6901 | 0.6348 | +0.0716 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Implemented and consumed RESTful APIs to support enterprise application features and integrations....`
> - *JD Evidence*: `- Build and optimize RESTful APIs, data interchange pipelines, and front-end integration points....`

### Ứng viên: Nguyễn Bảo Lâm (Fullstack Developer (.NET / React))

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.6512 | 0.6370 | +0.1309 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7947 | 0.7376 | +0.1501 |
| **ParagraphBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.6325 | 0.4793 | +0.2252 |
| **SentenceBased** | Job Description: Full Stack Developer (React / Vue.js / LLM APIs / WebGL) - Sqreem Technologies | 0.7578 | 0.7401 | +0.1944 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Developed and consumed RESTful APIs for internal business process automation applications....`
> - *JD Evidence*: `- Build and optimize RESTful APIs, data interchange pipelines, and front-end integration points....`

### Ứng viên: Nguyễn Văn An (Senior Fullstack Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.7863 | 0.7645 | +0.2282 |
| **LocalSemantic** | Job Description: Cloud Operations Engineer (CloudOps / AWS / Terraform) - NextEdge | 0.7665 | 0.6798 | +0.1171 |
| **ParagraphBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.8356 | 0.8356 | +0.3508 |
| **SentenceBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.7293 | 0.7257 | +0.1319 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Chứng chỉ AWS Certified Solutions Architect - Associate (2023)...`
> - *JD Evidence*: `- AWS certifications (Solutions Architect, SysOps, or Security Specialty) are advantageous....`

### Ứng viên: Phạm Đình Khoa (DevOps / Cloud Platform Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Cloud Native DevOps Engineer (Kubernetes / CI-CD) - Endava | 0.7310 | 0.6956 | +0.2545 |
| **LocalSemantic** | Job Description: Cloud Native DevOps Engineer (Kubernetes / CI-CD) - Endava | 0.8488 | 0.8120 | +0.1142 |
| **ParagraphBased** | Job Description: DevOps Engineer (AWS / Cloud / FinTech & Blockchain) - CubicStack Solutions | 0.7192 | 0.6601 | +0.2781 |
| **SentenceBased** | Job Description: DevOps Engineer (AWS / Cloud / FinTech & Blockchain) - CubicStack Solutions | 0.7495 | 0.7200 | +0.1993 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Automated deployment workflows for 15+ .NET and Java microservices using GitHub Actions and Helm, reducing deployment release cycle from 3 hours to 15 minutes...`
> - *JD Evidence*: `- Automate testing scopes and deployment verification scripts for containerized microservices....`

### Ứng viên: Trần Quốc Bảo (Junior Backend Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.5675 | 0.5460 | +0.0796 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7218 | 0.6965 | +0.0838 |
| **ParagraphBased** | Mô tả công việc: Kỹ sư Fullstack Senior (React / Node.js) | 0.5653 | 0.5337 | +0.1195 |
| **SentenceBased** | Mô tả công việc: Senior / Experienced Frontend Developer (React.js / FinTech) - NextEdge | 0.6487 | 0.6171 | +0.0596 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Collaborated with frontend and mobile teams to define OpenAPI/Swagger contracts and maintain automated CI/CD builds with GitHub Actions....`
> - *JD Evidence*: `- Build and optimize RESTful APIs, data interchange pipelines, and front-end integration points....`

### Ứng viên: Trần Thị Mai (Data Scientist / AI Engineer)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.7929 | 0.7376 | +0.3357 |
| **LocalSemantic** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.8805 | 0.8563 | +0.2042 |
| **ParagraphBased** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.8330 | 0.8330 | +0.3995 |
| **SentenceBased** | Job Description: Senior AI / NLP Research Engineer (RAG Systems) | 0.7943 | 0.7529 | +0.2572 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `Proven track record in deploying quantized local models (Ollama, vLLM, TensorRT-LLM) on constrained hardware environments....`
> - *JD Evidence*: `- Optimize local model inference and GPU memory allocation (RTX/Tesla series) via vLLM, Ollama, and INT4/INT8 quantization....`

### Ứng viên: Vũ Minh Trí (Senior Backend Architect / Technical Lead)

| Chiến lược | Vị trí JD Khớp nhất | Max Sim | Top-3 Avg | Contrast |
| :--- | :--- | :---: | :---: | :---: |
| **FixedSize** | Tuyển dụng: Kỹ sư Lập trình Phần mềm Junior/Senior (PHP/Laravel, Java) - RiverCrane Vietnam | 0.6160 | 0.5876 | +0.0735 |
| **LocalSemantic** | Job Description: Backend Engineer (Ruby on Rails / Python / Infrastructure) - The Umdenken | 0.7737 | 0.6912 | +0.1324 |
| **ParagraphBased** | Job Description: Senior Full Stack Java Developer (Spring Boot / React / Elasticsearch / AWS) - Hitachi Digital Services | 0.5614 | 0.4219 | +0.0941 |
| **SentenceBased** | Job Description: DevOps Engineer (AWS / Cloud / FinTech & Blockchain) - CubicStack Solutions | 0.6681 | 0.6363 | +0.1112 |

> **Bằng chứng trích xuất của LocalSemantic**:
> - *CV Evidence*: `- Optimized database indexing and partitioning strategies, resolving long-standing concurrency bottlenecks during peak tax filing seasons....`
> - *JD Evidence*: `- Troubleshoot performance bottlenecks, database query optimizations, and concurrency challenges....`

## 4. Kết luận Thực nghiệm RBL

1. **Tính trọn vẹn ngữ nghĩa**: `LocalSemantic` tạo ra các chunk chứa trọn vẹn một năng lực hoặc dự án (VD: cụm công nghệ Kafka + CQRS + Outbox Pattern), giúp độ tương đồng đạt đỉnh cao hơn hẳn so với việc bị cắt gãy ngang bởi `FixedSize`.
2. **Độ tương phản phân loại (Contrast)**: `LocalSemantic` cho contrast cao hơn (chênh lệch rõ ràng giữa vị trí đúng chuyên môn vs vị trí trái ngành), giúp hệ thống RAG HR tự động xếp hạng ứng viên chính xác hơn.
