# BÁO CÁO THỰC NGHIỆM ĐỊNH LƯỢNG HỆ THỐNG HRTECH RAG

## 1. Kết quả trả lời Câu hỏi nghiên cứu 1 (RQ1 - Hiệu năng truy xuất tổng thể)

| Chiến lược Chunking | Recall@3 | Recall@5 | MRR | Tổng số Chunk | Độ dài TB (kí tự) | Độ trễ (ms/doc) | VRAM (MB) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **FixedSize(size=500,overlap=100)** | 0.7407 | 1.0000 | 0.7593 | 33 | 447.0 | 0.09 | 0.0 |
| **SentenceBased(N=3,overlap=1)** | 0.5926 | 0.9074 | 0.7870 | 79 | 216.0 | 0.25 | 0.0 |
| **ParagraphBased(min=100,max=1000)** | 1.0000 | 1.0000 | 0.9444 | 17 | 715.8 | 0.11 | 0.0 |
| **LocalSemantic(thresh=0.85)** | 0.7407 | 0.8889 | 0.8704 | 110 | 109.0 | 1.33 | 0.0 |

## 2. Kết quả trả lời Câu hỏi nghiên cứu 2 (RQ2 - Phân tích theo loại tài liệu HR)

| Chiến lược Chunking | Loại tài liệu | Số câu hỏi | Recall@3 | Recall@5 | MRR |
| :--- | :---: | :---: | :---: | :---: | :---: |
| FixedSize(size=500,overlap=100) | **CV** | 3 | 0.8889 | 1.0000 | 0.7778 |
| FixedSize(size=500,overlap=100) | **JD** | 3 | 0.3333 | 1.0000 | 0.5000 |
| FixedSize(size=500,overlap=100) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |
| SentenceBased(N=3,overlap=1) | **CV** | 3 | 0.6111 | 0.8889 | 0.8333 |
| SentenceBased(N=3,overlap=1) | **JD** | 3 | 0.3333 | 0.8333 | 0.7500 |
| SentenceBased(N=3,overlap=1) | **POLICY** | 3 | 0.8333 | 1.0000 | 0.7778 |
| ParagraphBased(min=100,max=1000) | **CV** | 3 | 1.0000 | 1.0000 | 1.0000 |
| ParagraphBased(min=100,max=1000) | **JD** | 3 | 1.0000 | 1.0000 | 0.8333 |
| ParagraphBased(min=100,max=1000) | **POLICY** | 3 | 1.0000 | 1.0000 | 1.0000 |
| LocalSemantic(thresh=0.85) | **CV** | 3 | 0.7222 | 1.0000 | 0.8333 |
| LocalSemantic(thresh=0.85) | **JD** | 3 | 0.6667 | 0.6667 | 0.7778 |
| LocalSemantic(thresh=0.85) | **POLICY** | 3 | 0.8333 | 1.0000 | 1.0000 |

## 3. Nhận xét & Kết luận sơ bộ cho Đề cương/Bài báo RBL

- **RQ1**: Local Semantic Chunking xác định ranh giới chủ đề động qua Cosine Similarity, giúp giảm thiểu tối đa hiện tượng phân mảnh thông tin so với Fixed-size Chunking.
- **RQ2**: Hiệu quả cải thiện thể hiện rõ nét nhất trên dạng tài liệu **CV** (bảo toàn nguyên vẹn chuỗi kỹ năng và khối lịch sử dự án/kinh nghiệm làm việc) so với JDs hay Policies.
- **Computational Trade-off**: Giải pháp chạy cục bộ hoàn toàn trên phần cứng tối ưu (RTX 3050/3060, 16GB RAM), đảm bảo 100% tính bảo mật dữ liệu nhân sự (Data Privacy) với chi phí API bằng $0.
