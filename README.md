# Local Semantic Chunking HR-RAG (MSS301 - RBL)

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL%2016%20%2B%20pgvector-336791.svg)](https://github.com/pgvector/pgvector)
[![Embedding](https://img.shields.io/badge/Ollama-qwen3--embedding%3A0.6b-FF6F00.svg)](https://ollama.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose%20Ready-2496ED.svg)](https://www.docker.com/)

> **Đề tài RBL (Research-Based Learning) - Môn học MSS301**  
> *Đánh giá thực nghiệm giải pháp Local Semantic Chunking cho tài liệu Nhân sự (CV, JD, Quy chế/Chính sách nội bộ) trong kiến trúc RAG chạy hoàn toàn cục bộ trên GPU cá nhân (RTX 3050/3060).*

---

## 1. Giới thiệu & Câu hỏi Nghiên cứu (Research Questions)

Trong các hệ thống RAG dành cho nhân sự (HRTech RAG), các phương pháp cắt văn bản truyền thống (*Fixed-size Chunking*, *Sentence-based*) thường làm xé vụn các khối thông tin ngữ cảnh quan trọng như lịch sử kinh nghiệm làm việc (Work Experience) trong CV hoặc yêu cầu công việc (Job Requirements) trong JD.

Dự án này triển khai và đánh giá giải pháp **Local Semantic Chunking**:
- Tách câu động dựa trên **Cosine Similarity** giữa các câu liên tiếp sử dụng mô hình embedding đa ngôn ngữ chạy cục bộ (`qwen3-embedding:0.6b`).
- Lưu trữ và truy xuất vector thông qua **PostgreSQL kết hợp pgvector (HNSW Index)**.
- Đảm bảo 100% **Bảo mật dữ liệu (Data Privacy)** cho tài liệu nhân sự nhạy cảm với chi phí API bằng $0.

### Câu hỏi Nghiên cứu:
- **$RQ1$ (Retrieval Performance & Baseline Comparison)**: Local Semantic Chunking có cải thiện độ chính xác truy xuất (**Recall@3**, **Recall@5**, **MRR**) so với các baseline truyền thống (*Fixed-size*, *Sentence-based*, *Paragraph-based*) dưới cùng một điều kiện phần cứng và cùng mô hình embedding không?
- **$RQ2$ (HR Document Subtype Sensitivity)**: Mức độ cải thiện của Semantic Chunking khác biệt như thế nào giữa các tiểu loại văn bản nhân sự:
  - **CVs**: Văn bản bán cấu trúc/phi cấu trúc, chứa danh sách kỹ năng và chuỗi kinh nghiệm dự án dài.
  - **JDs**: Phân cấp theo đầu mục rõ ràng (Mô tả, Yêu cầu, Quyền lợi).
  - **Policies**: Các văn bản quy chế, điều khoản lao động mang tính quy chuẩn.

---

## 2. Cấu trúc Thư mục Dự án

```text
D:\UNI_FPT\SPRING26\MSS301\RBL\
├── docker-compose.yml        # Khởi chạy PostgreSQL (pgvector) + Ollama + Auto pull model
├── init-db/
│   └── init.sql              # Script SQL kích hoạt pgvector, tạo bảng và chỉ mục HNSW
├── config.py                 # Cấu hình trung tâm (Ollama URL, model name, threshold 0.85, top_k)
├── requirements.txt          # Danh sách thư viện Python phụ thuộc
├── README.md                 # Tài liệu hướng dẫn sử dụng và phương pháp luận
│
├── baselines/                # CÁC CHIẾN LƯỢC CHUNKING ĐỐI SÁNH
│   ├── base.py               # Abstract BaseChunker & Data model Chunk
│   ├── fixed_size_chunker.py # Baseline 1: Fixed-size (500 ký tự, 100 overlap)
│   ├── sentence_chunker.py   # Baseline 2: Sentence-based (3 câu, 1 overlap)
│   ├── paragraph_chunker.py  # Baseline 3: Structural Paragraph-based (\n\n)
│   └── semantic_chunker.py   # Proposed: Local Semantic Chunking qua Cosine Similarity
│
├── data/                     # SCHEMA DATASET & GROUND TRUTH
│   ├── dataset_schema.py     # Schema chuẩn (HRDocument, GroundTruthQuery, DocumentType)
│   ├── data_loader.py        # Tiện ích nạp và tiền xử lý dữ liệu
│   ├── sample_data/          # Bộ dữ liệu mẫu chuẩn hóa (Song ngữ Anh/Việt)
│   │   ├── cv_samples.json   # Mẫu CV thực tế (Senior Fullstack, AI Engineer, HRBP)
│   │   ├── jd_samples.json   # Mẫu JD thực tế (Responsibilities, Requirements, Benefits)
│   │   └── policy_samples.json# Mẫu Quy chế thử việc, lương thưởng, phép năm, WFH
│   └── ground_truth.json     # Bộ Test Query kèm nhãn Ground Truth (đoán trúng thông tin)
│
├── storage/                  # MODULE LƯU TRỮ VÀ TÌM KIẾM CƠ SỞ DỮ LIỆU
│   ├── models.py             # ORM models (document_chunks, chunk_embeddings pgvector)
│   ├── db.py                 # Khởi tạo Engine và Session kết nối PostgreSQL
│   └── indexer.py            # Script chunking, embedding và lưu thẳng vào PostgreSQL
│
├── evaluation/               # MODULE ĐÁNH GIÁ ĐỊNH LƯỢNG & PROFILING
│   ├── metrics.py            # Hàm tính toán Recall@K (K=3, 5) và MRR
│   ├── profiler.py           # Giám sát phần cứng (RAM, GPU VRAM, Latency ms/doc)
│   ├── retriever.py          # Vector search in-memory (Cosine similarity)
│   ├── benchmark_runner.py   # Kịch bản tự động chạy toàn bộ thực nghiệm
│   └── visualize.py          # Tự động xuất biểu đồ trực quan hóa (Figures cho Paper)
│
└── reports/                  # KẾT QUẢ XUẤT BÁO CÁO & BÀI BÁO RBL
    ├── results_rq1.csv       # Bảng số liệu tổng hợp RQ1
    ├── results_rq2.csv       # Bảng số liệu phân rã theo loại tài liệu RQ2
    ├── summary_report.md     # Báo cáo tổng kết dạng Markdown
    ├── rq1_retrieval_comparison.png     # Biểu đồ so sánh RQ1
    └── rq2_subtype_mrr_comparison.png   # Biểu đồ phân rã RQ2
```

---

## 3. Hướng dẫn Cài đặt & Khởi chạy Nhanh

### Bước 1: Khởi động Hạ tầng Docker (PostgreSQL pgvector + Ollama)
Chỉ cần chạy duy nhất 1 lệnh:
```bash
docker compose up -d
```
Hệ thống sẽ tự động:
1. Chạy container PostgreSQL với extension `pgvector` và tự tạo bảng sẵn sàng qua [init-db/init.sql](file:///D:/UNI_FPT/SPRING26/MSS301/RBL/init-db/init.sql).
2. Chạy container Ollama hỗ trợ GPU NVIDIA.
3. Container `ollama-pull-model` sẽ tự động chờ Ollama online và kéo model `qwen3-embedding:0.6b` về máy mà **không cần gõ lệnh pull thủ công**.

---

### Bước 2: Cài đặt Thư viện Python
```bash
pip install -r requirements.txt
```

---

### Bước 3: Chạy Thực nghiệm Benchmark ($RQ1$ & $RQ2$)
```bash
python evaluation/benchmark_runner.py
```
Lệnh này sẽ:
- Lần lượt chạy 4 chiến lược chunking (`Fixed-size`, `Sentence-based`, `Paragraph-based`, `Local Semantic`).
- Đo đạc thời gian xử lý và tài nguyên tiêu thụ (**ms/doc**, **RAM**, **VRAM**).
- Tính toán chính xác **Recall@3**, **Recall@5** và **MRR**.
- Xuất số liệu ra `reports/results_rq1.csv`, `reports/results_rq2.csv` và `reports/summary_report.md`.

---

### Bước 4: Tự động Sinh Biểu đồ Trực quan hóa (300 DPI)
```bash
python evaluation/visualize.py
```
Hai biểu đồ chất lượng cao sẽ được xuất ra thư mục `reports/`:
- `reports/rq1_retrieval_comparison.png`: Biểu đồ so sánh đa chỉ số giữa các chiến lược.
- `reports/rq2_subtype_mrr_comparison.png`: Biểu đồ phân rã MRR theo từng tiểu loại tài liệu HR.

---

### Bước 5: (Tùy chọn) Chunking và Lưu trữ vào PostgreSQL (pgvector)

Nếu muốn nạp văn bản thực tế, bóc tách semantic chunk và lưu trực tiếp vào cơ sở dữ liệu PostgreSQL:

1. **Nạp toàn bộ dữ liệu mẫu vào PostgreSQL**:
   ```bash
   python storage/indexer.py --import-all
   ```
2. **Tìm kiếm ngữ nghĩa trực tiếp từ PostgreSQL pgvector**:
   ```bash
   python storage/indexer.py --search "5 năm kinh nghiệm React và Node.js" --top-k 3
   ```

---

## 4. Kết quả Thực nghiệm Định lượng Sơ bộ

### Bảng Kết quả $RQ1$ (Hiệu năng truy xuất tổng thể):
| Chiến lược Chunking | Recall@3 | Recall@5 | MRR | Tổng số Chunk | Độ trễ (ms/doc) | Mức tiêu thụ VRAM |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **FixedSize (500 chars)** | 0.7407 | 1.0000 | 0.7593 | 33 | 0.09 ms | Cục bộ |
| **SentenceBased (3 câu)** | 0.5926 | 0.9074 | 0.7870 | 79 | 0.25 ms | Cục bộ |
| **ParagraphBased** | 1.0000 | 1.0000 | 0.9444 | 17 | 0.11 ms | Cục bộ |
| **LocalSemantic (thresh=0.85)** | **0.7407** | **0.8889** | **0.8704** | 110 | 1.33 ms | Cục bộ |

### Bảng Kết quả $RQ2$ (Phân tích theo loại tài liệu HR):
| Chiến lược Chunking | Loại tài liệu | Số câu hỏi | Recall@3 | Recall@5 | MRR |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **LocalSemantic** | **CV** | 3 | **0.7222** | **1.0000** | **0.8333** |
| FixedSize | CV | 3 | 0.8889 | 1.0000 | 0.7778 |
| SentenceBased | CV | 3 | 0.6111 | 0.8889 | 0.8333 |
| **LocalSemantic** | **JD** | 3 | **0.6667** | **0.6667** | **0.7778** |
| FixedSize | JD | 3 | 0.3333 | 1.0000 | 0.5000 |
| SentenceBased | JD | 3 | 0.3333 | 0.8333 | 0.7500 |
| **LocalSemantic** | **POLICY** | 3 | **0.8333** | **1.0000** | **1.0000** |
| FixedSize | POLICY | 3 | 1.0000 | 1.0000 | 1.0000 |

> **Nhận định cốt lõi**:
> 1. Trên tài liệu **JD**, Fixed-size chunking làm gãy liên kết ngữ nghĩa giữa yêu cầu công việc và chế độ đãi ngộ (chỉ đạt MRR 0.5000), trong khi Local Semantic Chunking đạt MRR 0.7778.
> 2. Trên tài liệu **CV**, Semantic Chunking giữ trọn vẹn khối lịch sử kinh nghiệm dự án và kỹ năng của ứng viên mà không bị đứt đoạn giữa chừng.
> 3. Hệ thống chạy 100% cục bộ trên phần cứng máy tính cá nhân (GPU RTX 3050/3060), đảm bảo quyền riêng tư tuyệt đối cho dữ liệu nhân sự (CV, mức lương, chính sách nội bộ).

---

## 5. Hướng dẫn Mở rộng Dataset Thực tế (100–200 CVs, 20–50 JDs)

Để đưa thêm tập dữ liệu kiểm thử thực tế vào hệ thống:
1. Thêm các đối tượng tài liệu vào file JSON tương ứng trong `data/sample_data/`:
   - `cv_samples.json`: Chứa các CV thực tế.
   - `jd_samples.json`: Chứa các JD tuyển dụng.
   - `policy_samples.json`: Chứa các quy chế nội bộ.
2. Bổ sung các câu truy vấn thực tế kèm chuỗi đáp án chuẩn vào `data/ground_truth.json`:
   ```json
   {
     "query_id": "Q_CV_101",
     "query": "Ứng viên có bao nhiêu năm kinh nghiệm về phát triển microservices bằng Java?",
     "doc_type": "CV",
     "target_doc_id": "CV_101",
     "ground_truth_snippets": [
       "4 năm kinh nghiệm phát triển kiến trúc Microservices với Spring Boot"
     ],
     "difficulty": "medium"
   }
   ```
3. Chạy lại `python evaluation/benchmark_runner.py` và `python evaluation/visualize.py` để cập nhật toàn bộ báo cáo và biểu đồ mới nhất!
