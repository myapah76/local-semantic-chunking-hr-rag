# HRTech RAG - Local Semantic Chunking Benchmark Suite (MSS301 - RBL)

Bộ khung thực nghiệm định lượng và so sánh hiệu năng của giải pháp **Local Semantic Chunking** đối với các tài liệu nhân sự (CV, JD, Quy chế/Chính sách nội bộ) phục vụ nghiên cứu môn học **MSS301 (Research-Based Learning - RBL)**.

---

## 1. Mục tiêu Nghiên cứu & Câu hỏi Nghiên cứu (RQs)

- **RQ1 (Retrieval Performance & Baseline Comparison)**:
  *Local Semantic Chunking* có cải thiện độ chính xác truy xuất (Recall@3, Recall@5, MRR) so với các phương pháp Baseline truyền thống (*Fixed-size*, *Sentence-based*, *Paragraph-based*) khi cùng triển khai trên phần cứng cục bộ và chung mô hình embedding không?
- **RQ2 (HR Document Subtype Sensitivity)**:
  Mức độ cải thiện của Semantic Chunking khác biệt như thế nào giữa các tiểu loại văn bản nhân sự:
  - **CVs**: Lưu trữ thông tin phi cấu trúc, danh sách kỹ năng và khối kinh nghiệm dài.
  - **JDs**: Phân cấp rõ ràng theo đầu mục (Responsibilities, Requirements, Benefits).
  - **Policies**: Các điều khoản quy định nội bộ mang tính quy phạm.
- **Computational Trade-off & Data Privacy**:
  Đo lường thời gian tiền xử lý, độ trễ chunking và tài nguyên phần cứng (VRAM / RAM), qua đó chứng minh ưu thế bảo mật 100% dữ liệu nhân sự nhạy cảm với chi phí API bằng $0.

---

## 2. Cấu trúc Thư mục

```text
D:\UNI_FPT\SPRING26\MSS301\RBL\
├── config.py                 # Cấu hình chung (Ollama URL, model name, threshold, top-k)
├── requirements.txt          # Danh sách thư viện phụ thuộc
├── baselines/                # Module chứa 4 chiến lược Chunking
│   ├── base.py               # Abstract BaseChunker & Chunk model
│   ├── fixed_size_chunker.py # Baseline 1: Cửa sổ trượt cố định (500 chars, 100 overlap)
│   ├── sentence_chunker.py   # Baseline 2: Nhóm câu cố định (3 sentences, 1 overlap)
│   ├── paragraph_chunker.py  # Baseline 3: Phân đoạn theo đoạn văn bản (\n\n)
│   └── semantic_chunker.py   # Proposed: Semantic Chunker qua Cosine Similarity cục bộ
├── data/                     # Dữ liệu & Ground Truth
│   ├── dataset_schema.py     # Schema chuẩn (HRDocument, GroundTruthQuery, DocumentType)
│   ├── data_loader.py        # Tiện ích nạp và tiền xử lý dữ liệu
│   ├── sample_data/          # Bộ mẫu tài liệu chuẩn hóa
│   │   ├── cv_samples.json   # Mẫu CV thực tế (Anh/Việt)
│   │   ├── jd_samples.json   # Mẫu JD thực tế (Anh/Việt)
│   │   └── policy_samples.json# Mẫu Quy chế, chính sách nhân sự
│   └── ground_truth.json     # Bộ Test Query kèm nhãn Ground Truth (đoán trúng thông tin)
├── evaluation/               # Module Đánh giá & Benchmark
│   ├── metrics.py            # Hàm tính toán Recall@K (K=3, 5) và MRR
│   ├── profiler.py           # Giám sát phần cứng (RAM, VRAM, Latency)
│   ├── retriever.py          # Vector search engine in-memory (Cosine similarity)
│   ├── benchmark_runner.py   # Kịch bản tự động chạy toàn bộ thực nghiệm
│   └── visualize.py          # Tự động xuất biểu đồ trực quan hóa
└── reports/                  # Kết quả xuất ra phục vụ báo cáo / slide
    ├── results_rq1.csv       # Bảng số liệu tổng hợp RQ1
    ├── results_rq2.csv       # Bảng số liệu phân rã theo loại tài liệu RQ2
    ├── summary_report.md     # Báo cáo tổng kết dạng Markdown
    ├── rq1_retrieval_comparison.png # Biểu đồ so sánh RQ1
    └── rq2_subtype_mrr_comparison.png # Biểu đồ phân rã theo loại tài liệu RQ2
```

---

## 3. Hướng dẫn Sử dụng & Chạy Thực nghiệm

### Bước 1: Kiểm tra cấu hình tại `config.py`
Nếu bạn đang chạy Ollama cục bộ với model `qwen3-embedding:0.6b`:
```python
ollama_base_url = "http://localhost:11434"
embedding_model = "qwen3-embedding:0.6b"
```
*(Nếu Ollama đang tắt, hệ thống sẽ tự động chuyển sang chế độ dự phòng thông minh để vẫn chạy mượt mà mà không bị crash).*

### Bước 2: Chạy Benchmark Runner
Mở terminal tại thư mục `D:\UNI_FPT\SPRING26\MSS301\RBL` và chạy:
```bash
py -3.13 evaluation/benchmark_runner.py
```
Lệnh này sẽ tự động:
1. Nạp toàn bộ tài liệu và bộ câu hỏi Ground Truth.
2. Lần lượt chạy 4 chiến lược chunking và đo đạc tài nguyên (RAM, VRAM, độ trễ ms/doc).
3. Index vector và thực hiện truy xuất tìm kiếm ngữ nghĩa.
4. Tính toán **Recall@3**, **Recall@5**, và **MRR**.
5. Xuất báo cáo ra console và ghi nhận vào các file CSV, Markdown tại `reports/`.

### Bước 3: Xuất biểu đồ trực quan hóa (Figures cho Paper)
Chạy lệnh:
```bash
py -3.13 evaluation/visualize.py
```
Biểu đồ chất lượng cao (300 DPI) sẽ được lưu tại:
- `reports/rq1_retrieval_comparison.png`
- `reports/rq2_subtype_mrr_comparison.png`

---

## 4. Hướng dẫn Mở rộng Dataset Thực tế (100–200 CVs, 20–50 JDs)

Để nạp thêm dữ liệu thực tế vào đánh giá:
1. Thêm các đối tượng tài liệu vào file JSON tương ứng trong `data/sample_data/`:
   ```json
   {
     "doc_id": "CV_xxx",
     "doc_type": "CV",
     "title": "CV Tên Ứng Viên",
     "language": "vi",
     "metadata": {"role": "Backend", "experience_years": 3},
     "content": "Toàn bộ nội dung văn bản sau khi bóc tách từ PDF/Docx..."
   }
   ```
2. Thêm các câu truy vấn thực tế vào `data/ground_truth.json`:
   ```json
   {
     "query_id": "Q_CV_xxx",
     "query": "Câu hỏi truy vấn thông tin cụ thể?",
     "doc_type": "CV",
     "target_doc_id": "CV_xxx",
     "ground_truth_snippets": [
       "Đoạn văn bản/sự kiện cốt lõi bắt buộc phải xuất hiện trong chunk được tìm thấy"
     ],
     "difficulty": "medium"
   }
   ```
3. Chạy lại `benchmark_runner.py` để tự động cập nhật số liệu mới nhất.
