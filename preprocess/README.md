# Các bước tiền xử lý – Phân loại bình luận Spam / Ham tiếng Việt

**Bối cảnh:** Phân loại bình luận sản phẩm trên sàn thương mại điện tử (Điện Máy Xanh) thành **Spam** (quảng cáo, rác, chèo kéo) hoặc **Ham** (đánh giá thật của người dùng).

**Cơ sở:** Chương 2 – Xử lý dữ liệu văn bản (Tách từ → Chuẩn hóa → Cấu trúc ngữ pháp).

---

## 0. Tổng quan pipeline

```
Dữ liệu thô
   │
   ▼
[1] Làm sạch văn bản (Text Cleaning)
   │
   ▼
[2] Chuẩn hóa Unicode & ký tự lặp
   │
   ▼
[3] Chỉnh sửa từ (Word Correction): teencode, viết tắt, không dấu
   │
   ▼
[4] Tách từ tiếng Việt (Tokenization)
   │
   ▼
[5] Loại bỏ từ dừng & ký tự đặc biệt
   │
   ▼
[6] (Tùy chọn) Lemmatization / POS Tagging / Chunking
   │
   ▼
[7] Trích xuất đặc trưng (TF-IDF, đặc trưng thủ công)
   │
   ▼
[8] Chia tập dữ liệu & xử lý mất cân bằng lớp
```

> ⚠️ **Lưu ý quan trọng cho bài toán Spam:** Khác với phân tích cảm xúc thông thường, **URL, số điện thoại, giá tiền, từ khóa quảng cáo** chính là tín hiệu mạnh để nhận diện Spam. Vì vậy **không nên xóa thẳng**, mà nên *thay bằng token đặc biệt* (`<URL>`, `<PHONE>`, `<PRICE>`) hoặc *trích thành đặc trưng riêng* trước khi làm sạch.

---

## 1. Làm sạch văn bản (Text Cleaning)

**Mục tiêu:** Loại bỏ nhiễu không mang ngữ nghĩa nhưng **giữ lại tín hiệu spam**.

| Loại nhiễu | Ví dụ | Cách xử lý đề xuất |
|---|---|---|
| HTML/XML tags | `<br>`, `<a href=...>` | Xóa tag, giữ nội dung |
| URL | `http://shopxyz.com`, `zalo.me/...` | Thay bằng `<URL>` (đồng thời tạo đặc trưng `has_url`) |
| Số điện thoại | `0987.654.321`, `+84 912...` | Thay bằng `<PHONE>` |
| Giá tiền | `99k`, `1.500.000đ` | Thay bằng `<PRICE>` |
| Emoji / icon | 😊 🔥 💰 | Xóa hoặc đếm số lượng thành đặc trưng |
| Ký tự đặc biệt | `!!!`, `###`, `***` | Xóa (có thể đếm `!` làm đặc trưng) |
| Khoảng trắng thừa | `"abc   def "` | Chuẩn hóa về 1 dấu cách, `strip()` |
| Chữ hoa/thường | `"MUA NGAY"` | Chuyển về chữ thường (đếm tỷ lệ CAPS trước khi chuyển) |

```python
import re

URL_RE   = re.compile(r"(https?://\S+|www\.\S+|\b\S+\.(com|vn|net|me)\S*)", re.I)
PHONE_RE = re.compile(r"(\+?84|0)[\s\.\-]?\d{2,3}[\s\.\-]?\d{3}[\s\.\-]?\d{3,4}")
PRICE_RE = re.compile(r"\b\d+([\.,]\d+)*\s?(k|đ|d|vnd|vnđ|tr|triệu|nghìn)\b", re.I)
HTML_RE  = re.compile(r"<[^>]+>")

def clean_text(text: str) -> str:
    text = HTML_RE.sub(" ", text)
    text = URL_RE.sub(" <URL> ", text)
    text = PHONE_RE.sub(" <PHONE> ", text)
    text = PRICE_RE.sub(" <PRICE> ", text)
    text = re.sub(r"[^\w\s<>]", " ", text, flags=re.UNICODE)  # bỏ ký tự đặc biệt/emoji
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    return text
```

---

## 2. Chuẩn hóa Unicode & ký tự lặp

Tiếng Việt có nhiều cách mã hóa dấu (NFC/NFD, dấu cũ/mới) khiến cùng một từ bị coi là khác nhau.

- Chuẩn hóa Unicode về **NFC**.
- Rút gọn ký tự lặp: `"đẹppppp"` → `"đẹp"`, `"tuyệttt vờiii"` → `"tuyệt vời"`.
- Chuẩn hóa vị trí dấu thanh: `hòa`/`hoà` → một dạng thống nhất.

```python
import unicodedata

def normalize_unicode(text: str) -> str:
    return unicodedata.normalize("NFC", text)

def reduce_repeated_chars(text: str) -> str:
    return re.sub(r"(.)\1{2,}", r"\1", text)   # aaaa -> a
```

---

## 3. Chỉnh sửa từ (Word Correction)

Bình luận e-commerce chứa rất nhiều **teencode, viết tắt, gõ không dấu**. Nếu không xử lý, một khái niệm sẽ sinh nhiều "từ" khác nhau làm loãng mô hình.

| Loại lỗi | Ví dụ | Chuẩn hóa |
|---|---|---|
| Viết tắt | `ko`, `k`, `hok`, `kg` | `không` |
| Viết tắt | `dc`, `đc` | `được` |
| Viết tắt | `sp`, `sđt`, `ib`, `inb` | `sản phẩm`, `số điện thoại`, `nhắn tin` |
| Teencode | `ok`, `okie`, `oki` | `ok` |
| Không dấu | `san pham tot` | `sản phẩm tốt` |
| Lỗi gõ | `thich` → `thích`, `tuyet voi` → `tuyệt vời` | Sửa theo từ điển |

**Phương pháp (theo chương 2.4):**
1. **Rule-based / từ điển ánh xạ**: xây dict teencode → từ chuẩn (nhanh, hiệu quả cho viết tắt).
2. **Khoảng cách Levenshtein** với từ điển chuẩn để sửa lỗi gõ.
3. **Mô hình ngôn ngữ / thêm dấu tự động** (ví dụ: model khôi phục dấu tiếng Việt) cho văn bản không dấu.

```python
TEENCODE = {
    "ko": "không", "k": "không", "hok": "không", "kg": "không",
    "dc": "được", "đc": "được", "sp": "sản phẩm",
    "sđt": "số điện thoại", "ib": "nhắn tin", "inb": "nhắn tin",
    "vs": "với", "ntn": "như thế nào", "bt": "bình thường",
}

def fix_teencode(text: str) -> str:
    return " ".join(TEENCODE.get(w, w) for w in text.split())
```

> 💡 Với bài toán Spam, **bình luận không dấu / viết tắt nhiều** cũng là một tín hiệu (spam thường cẩu thả). Có thể tính tỷ lệ này thành đặc trưng *trước* khi sửa.

---

## 4. Tách từ tiếng Việt (Tokenization)

Tiếng Việt là ngôn ngữ đơn lập, **khoảng trắng không phải ranh giới từ** (`"điện thoại"`, `"máy giặt"`, `"khuyến mãi"` là từ ghép). Tách sai sẽ ảnh hưởng toàn bộ các bước sau.

**Các phương pháp (chương 1.1 & 1.3):**

| Phương pháp | Mô tả | Nhận xét |
|---|---|---|
| Tách theo khoảng trắng | Chia theo dấu cách | Sai với từ ghép |
| Longest Matching | Duyệt trái → phải, chọn từ dài nhất có trong từ điển | Đơn giản, dễ nhập nhằng |
| Maximum Matching | Sinh mọi cách tách, chọn cách có **ít từ nhất** | Phụ thuộc từ điển |
| Học máy / hiện đại | `underthesea`, `VnCoreNLP`, `pyvi` | **Khuyến nghị dùng** |

```python
from underthesea import word_tokenize

text = "sản phẩm này giao hàng nhanh chất lượng tốt"
tokens = word_tokenize(text)          # ['sản phẩm', 'này', 'giao hàng', 'nhanh', 'chất lượng', 'tốt']
text_tok = word_tokenize(text, format="text")   # 'sản_phẩm này giao_hàng nhanh chất_lượng tốt'
```

> Nên **giữ nguyên các token đặc biệt** `<URL>`, `<PHONE>`, `<PRICE>` (không để tokenizer cắt thành `<`, `URL`, `>`).

---

## 5. Loại bỏ từ dừng (Stop words) & ký tự đặc biệt

**Từ dừng** (`là`, `và`, `của`, `một`, `những`, `có`...) xuất hiện nhiều nhưng ít giá trị phân biệt → giảm kích thước dữ liệu, tăng tốc độ, giảm nhiễu.

**Lưu ý riêng cho bài toán này:**
- Danh sách stopword tiếng Việt mặc định trong slide chứa cả `không`, `rất`, `quá`, `lắm`, `thật`, `nhiều`, `ít`, `tôi`, `bạn`... — đây là các từ **quan trọng để phân biệt Ham/Spam** (Ham thường dùng ngôi thứ nhất "tôi/mình", Spam thường dùng "bạn/quý khách/inbox").
- Nên **tùy chỉnh danh sách**: giữ lại phủ định (`không`, `chưa`), ngôi nhân xưng (`tôi`, `mình`, `bạn`, `quý khách`), từ nhấn mạnh.
- Dấu `!` có thể mang tín hiệu spam (`!!!`) → đếm làm đặc trưng trước khi xóa.

```python
STOPWORDS = {"là", "và", "của", "một", "những", "có", "đã", "sẽ",
             "này", "kia", "đó", "thì", "mà", "với", "trong", "trên"}
# Chủ động KHÔNG đưa: không, chưa, tôi, mình, bạn, quý khách, rất, quá...

SPECIAL = {"<URL>", "<PHONE>", "<PRICE>"}

def remove_stopwords(tokens):
    return [t for t in tokens if t in SPECIAL or t not in STOPWORDS]
```

---

## 6. Lấy từ gốc & phân tích ngữ pháp (tùy chọn)

### 6.1 Stemming / Lemmatization
- Tiếng Việt **ít biến đổi hình thái** → Stemming gần như **không cần thiết**.
- Lemmatization chủ yếu là **chuẩn hóa biến thể** (`đẹp quá`, `đẹp lắm` → `đẹp`) và đã được bao phủ bởi bước 3–5. **Có thể bỏ qua** trong pipeline cơ bản.

### 6.2 POS Tagging
- Gán nhãn từ loại để lọc từ khóa quan trọng (giữ danh từ, động từ, tính từ).
- Có thể tạo đặc trưng: **tỷ lệ danh từ riêng (Np)**, số lượng động từ mệnh lệnh (`liên hệ`, `inbox`, `mua ngay`...).

```python
from underthesea import pos_tag
pos_tag("Mua ngay tại đây giá rẻ")
```

### 6.3 Chunking / Dependency / Constituency Parsing
- Chủ yếu dùng khi cần **trích xuất cụm danh từ / quan hệ**.
- Với phân loại Spam/Ham bằng ML truyền thống, **không bắt buộc**; chỉ dùng khi muốn đặc trưng nâng cao (ví dụ: cụm động từ chèo kéo như `[VP liên hệ]`, `[VP đặt hàng]`).

---

## 7. Trích xuất đặc trưng (Feature Extraction) - bước sau, không thực hiện ở bước tiền xử lý

### 7.1 Đặc trưng văn bản
- **Bag-of-Words / TF-IDF** (unigram + bigram, ví dụ `ngram_range=(1,2)`).
- Có thể thử **PhoBERT / embeddings** nếu cần độ chính xác cao hơn.

### 7.2 Đặc trưng thủ công (tính từ văn bản **gốc**, trước khi làm sạch)

| Đặc trưng | Ý nghĩa |
|---|---|
| `has_url`, `has_phone`, `has_price` | Có chứa link / SĐT / giá |
| `text_length`, `num_words` | Spam thường quá ngắn hoặc quá dài |
| `num_exclamation` | Số dấu `!` |
| `caps_ratio` | Tỷ lệ chữ IN HOA |
| `emoji_count` | Số emoji |
| `digit_ratio` | Tỷ lệ chữ số |
| `repeated_char_ratio` | Tỷ lệ ký tự lặp (`ơiiii`) |
| `no_diacritics_ratio` | Tỷ lệ từ không dấu |
| `spam_keyword_count` | Số từ khóa spam (`inbox`, `zalo`, `ib`, `giảm giá`, `liên hệ`, `hotline`, `miễn phí`...) |

---

## 8. Chia dữ liệu & xử lý mất cân bằng

1. **Loại bỏ trùng lặp**: bình luận spam hay bị copy-paste y hệt → `drop_duplicates()` (tránh rò rỉ dữ liệu giữa train/test).
2. **Xử lý giá trị rỗng**: bỏ bình luận rỗng sau khi làm sạch.
3. **Chia Train/Val/Test** (ví dụ 70/15/15) với `stratify=y`.
4. **Fit TF-IDF / vectorizer CHỈ trên tập train**, sau đó `transform` cho val/test (tránh data leakage).
5. **Mất cân bằng lớp** (thường Ham ≫ Spam): dùng `class_weight="balanced"`, oversampling (SMOTE) hoặc undersampling.
6. **Đánh giá**: ưu tiên **Precision, Recall, F1 của lớp Spam** và PR-AUC, không chỉ Accuracy.

---

## 9. Pipeline tổng hợp (mã mẫu)

```python
from underthesea import word_tokenize

def preprocess(raw: str) -> str:
    text = normalize_unicode(raw)          # 2. Unicode NFC
    text = clean_text(text)                # 1. Làm sạch (giữ <URL>, <PHONE>, <PRICE>)
    text = reduce_repeated_chars(text)     # 2. Ký tự lặp
    text = fix_teencode(text)              # 3. Teencode / viết tắt
    tokens = word_tokenize(text)           # 4. Tách từ
    tokens = remove_stopwords(tokens)      # 5. Từ dừng (danh sách tùy chỉnh)
    return " ".join(t.replace(" ", "_") for t in tokens)

# Ví dụ
raw = "Sp tốt quá!!! Ib zalo 0987654321 giá chỉ 99k nhé 😊 http://shopxyz.com"
print(preprocess(raw))
# -> "sản_phẩm tốt quá nhắn_tin zalo <PHONE> giá chỉ <PRICE> nhé <URL>"
```

---

## 10. Checklist nhanh

- [ ] Giữ lại tín hiệu spam (URL, SĐT, giá) dưới dạng token/đặc trưng
- [ ] Chuẩn hóa Unicode NFC
- [ ] Rút gọn ký tự lặp
- [ ] Chuẩn hóa teencode, viết tắt, thêm dấu nếu cần
- [ ] Tách từ bằng `underthesea` / `VnCoreNLP` (không dùng split khoảng trắng)
- [ ] Stopword **tùy chỉnh**, không xóa phủ định/ngôi nhân xưng
- [ ] Bỏ qua Stemming; Lemmatization/POS/Chunking chỉ khi cần
- [ ] Loại trùng lặp, chia dữ liệu có `stratify`
- [ ] Fit vectorizer chỉ trên tập train
- [ ] Xử lý mất cân bằng lớp, đánh giá theo F1/Recall của Spam