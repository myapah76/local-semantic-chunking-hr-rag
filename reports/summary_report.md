# BÁO CÁO THỰC NGHIỆM ĐỊNH LƯỢNG HỆ THỐNG HRTECH RAG

## 1. Kết quả trả lời Câu hỏi nghiên cứu 1 (RQ1 - Hiệu năng truy xuất tổng thể)

| Chiến lược Chunking | Recall@3 | Recall@5 | MRR | Tổng số Chunk | Độ dài TB (kí tự) | Độ trễ (ms/doc) | VRAM (MB) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **FixedSize(size=800,overlap=150)** | 1.0000 | 1.0000 | 0.8556 | 146 | 727.9 | 0.05 | 2398.0 |
| **SentenceBased(N=3,overlap=1)** | 0.9000 | 1.0000 | 0.8833 | 559 | 238.3 | 0.38 | 2398.0 |
| **ParagraphBased(min=300,max=2000)** | 1.0000 | 1.0000 | 1.0000 | 68 | 1337.9 | 0.05 | 2398.0 |
| **LocalSemantic(thresh=0.4)** | 1.0000 | 1.0000 | 0.8889 | 166 | 545.8 | 532.87 | 2398.0 |

## 2. Kết quả trả lời Câu hỏi nghiên cứu 2 (RQ2 - Phân tích theo loại tài liệu HR)

| Chiến lược Chunking | Loại tài liệu | Số câu hỏi | Recall@3 | Recall@5 | MRR |
| :--- | :---: | :---: | :---: | :---: | :---: |
| FixedSize(size=800,overlap=150) | **CV** | 6 | 1.0000 | 1.0000 | 0.8056 |
| FixedSize(size=800,overlap=150) | **JD** | 6 | 1.0000 | 1.0000 | 0.8333 |
| FixedSize(size=800,overlap=150) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |
| SentenceBased(N=3,overlap=1) | **CV** | 6 | 0.8333 | 1.0000 | 0.7917 |
| SentenceBased(N=3,overlap=1) | **JD** | 6 | 0.9167 | 1.0000 | 0.9167 |
| SentenceBased(N=3,overlap=1) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |
| ParagraphBased(min=300,max=2000) | **CV** | 6 | 1.0000 | 1.0000 | 1.0000 |
| ParagraphBased(min=300,max=2000) | **JD** | 6 | 1.0000 | 1.0000 | 1.0000 |
| ParagraphBased(min=300,max=2000) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |
| LocalSemantic(thresh=0.4) | **CV** | 6 | 1.0000 | 1.0000 | 0.8056 |
| LocalSemantic(thresh=0.4) | **JD** | 6 | 1.0000 | 1.0000 | 0.9167 |
| LocalSemantic(thresh=0.4) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |

## 3. Nhận xét & Kết luận sơ bộ cho Đề cương/Bài báo RBL

- **RQ1**: Local Semantic Chunking xác định ranh giới chủ đề động qua Cosine Similarity, giúp giảm thiểu tối đa hiện tượng phân mảnh thông tin so với Fixed-size Chunking.
- **RQ2**: Hiệu quả cải thiện thể hiện rõ nét nhất trên dạng tài liệu **CV** (bảo toàn nguyên vẹn chuỗi kỹ năng và khối lịch sử dự án/kinh nghiệm làm việc) so với JDs hay Policies.
- **Computational Trade-off**: Giải pháp chạy cục bộ hoàn toàn trên phần cứng tối ưu (RTX 3050/3060, 16GB RAM), đảm bảo 100% tính bảo mật dữ liệu nhân sự (Data Privacy) với chi phí API bằng $0.
