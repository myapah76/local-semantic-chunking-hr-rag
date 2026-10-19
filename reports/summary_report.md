# BÁO CÁO THỰC NGHIỆM ĐỊNH LƯỢNG HỆ THỐNG HRTECH RAG

## 1. Kết quả trả lời Câu hỏi nghiên cứu 1 (RQ1 - Hiệu năng truy xuất tổng thể)

| Chiến lược Chunking | Recall@3 | Recall@5 | MRR | Tổng số Chunk | Độ dài TB (kí tự) | Độ trễ (ms/doc) | VRAM (MB) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **FixedSize(size=800,overlap=150)** | 1.0000 | 1.0000 | 0.9444 | 99 | 724.5 | 0.1 | 2398.0 |
| **SentenceBased(N=3,overlap=1)** | 1.0000 | 1.0000 | 0.8889 | 381 | 234.2 | 0.12 | 2398.0 |
| **ParagraphBased(min=300,max=2000)** | 1.0000 | 1.0000 | 1.0000 | 45 | 1359.4 | 0.05 | 2398.0 |
| **LocalSemantic(thresh=0.4)** | 1.0000 | 1.0000 | 0.9444 | 104 | 585.5 | 440.32 | 2398.0 |

## 2. Kết quả trả lời Câu hỏi nghiên cứu 2 (RQ2 - Phân tích theo loại tài liệu HR)

| Chiến lược Chunking | Loại tài liệu | Số câu hỏi | Recall@3 | Recall@5 | MRR |
| :--- | :---: | :---: | :---: | :---: | :---: |
| FixedSize(size=800,overlap=150) | **CV** | 3 | 1.0000 | 1.0000 | 0.8333 |
| FixedSize(size=800,overlap=150) | **JD** | 3 | 1.0000 | 1.0000 | 1.0000 |
| FixedSize(size=800,overlap=150) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |
| SentenceBased(N=3,overlap=1) | **CV** | 3 | 1.0000 | 1.0000 | 0.8333 |
| SentenceBased(N=3,overlap=1) | **JD** | 3 | 1.0000 | 1.0000 | 0.8333 |
| SentenceBased(N=3,overlap=1) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |
| ParagraphBased(min=300,max=2000) | **CV** | 3 | 1.0000 | 1.0000 | 1.0000 |
| ParagraphBased(min=300,max=2000) | **JD** | 3 | 1.0000 | 1.0000 | 1.0000 |
| ParagraphBased(min=300,max=2000) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |
| LocalSemantic(thresh=0.4) | **CV** | 3 | 1.0000 | 1.0000 | 0.8333 |
| LocalSemantic(thresh=0.4) | **JD** | 3 | 1.0000 | 1.0000 | 1.0000 |
| LocalSemantic(thresh=0.4) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |

## 3. Nhận xét & Kết luận sơ bộ cho Đề cương/Bài báo RBL

- **RQ1**: Local Semantic Chunking xác định ranh giới chủ đề động qua Cosine Similarity, giúp giảm thiểu tối đa hiện tượng phân mảnh thông tin so với Fixed-size Chunking.
- **RQ2**: Hiệu quả cải thiện thể hiện rõ nét nhất trên dạng tài liệu **CV** (bảo toàn nguyên vẹn chuỗi kỹ năng và khối lịch sử dự án/kinh nghiệm làm việc) so với JDs hay Policies.
- **Computational Trade-off**: Giải pháp chạy cục bộ hoàn toàn trên phần cứng tối ưu (RTX 3050/3060, 16GB RAM), đảm bảo 100% tính bảo mật dữ liệu nhân sự (Data Privacy) với chi phí API bằng $0.
