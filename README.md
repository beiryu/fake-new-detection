# Fake news detection

## Tổng quan

Tin giả đang là một vấn đề nhức nhối của xã hội, đặc biệt trong thời đại bùng nổ thông tin hiện nay. Đồ án này sẽ cho phép các bạn làm việc với dữ liệu văn bản tiếng Việt, xây dựng mô hình dự đoán tin giả và deploy mô hình này lên một trang web đơn giản.

1. Nguồn dữ liệu
- [VNFD Dataset](https://github.com/thanhhocse96/vfnd-vietnamese-fake-news-datasets/blob/master/CSV/vn_news_223_tdlfr.csv), tập dữ liệu 223 record bản tin tiếng Việt, gồm 2 nhãn: 1 (tin giả) và 0 (tin thật).
- Mô tả dữ liệu: [Mô tả tập VNFD](https://github.com/thanhhocse96/vfnd-vietnamese-fake-news-datasets/tree/master/CSV).
 
2. Tiền xử lý văn bản tiếng Việt
- Các bước tiền xử lý văn bản cơ bản gồm: lowercase, loại stopwords, stemming, normalize tùy theo từng lĩnh vực, loại noise (HTML tag, các ký hiệu đặc biệt như @, #,...), dấu câu.
- [Sơ lược về tiền xử lý văn bản](https://maelfabien.github.io/machinelearning/NLP_1/#i-what-is-preprocessing)
- [Stopword](https://github.com/stopwords/vietnamese-stopwords/blob/master/vietnamese-stopwords.txt)
- [Tokenizer](https://github.com/vncorenlp/VnCoreNLP#install)

3. Deploy mô hình
- Thư viện: [Streamlit](https://streamlit.io/gallery) cho phép code giao diện một cách đơn giản hoàn toàn bằng Python để hỗ trợ deploy mô hình máy học lên web miễn phí, phục vụ việc demo.
