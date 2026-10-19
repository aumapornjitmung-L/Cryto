# 📈 พยากรณ์ Crypto ด้วย Machine Learning (QUSDT, BRUSDT, AGTUSDT)

แอป Streamlit ใช้ 2 โมเดลที่ดีที่สุดจากการเทียบแบบ walk-forward พยากรณ์ทิศทาง (ขึ้น/ลง) และราคาปิดล่วงหน้า

## ขั้นตอน
1. (ทางเลือกแต่แนะนำ) รัน `benchmark_colab.py` เพื่อเทียบ 5 โมเดลบนทั้ง 3 เหรียญ → ได้ `model_config.json`
   ที่ระบุ 2 โมเดลที่ดีที่สุด และบันทึก snapshot ข้อมูลไว้ใน `data/`
2. วาง `model_config.json` (และโฟลเดอร์ `data/` ถ้ามี) ไว้ข้าง `app.py`
3. ทดสอบ: `pip install -r requirements.txt && streamlit run app.py`
4. push ขึ้น GitHub แล้ว Deploy ที่ https://share.streamlit.io (Main file: `app.py`)

## แหล่งข้อมูล
แอปลองดึงตามลำดับ: Binance USDT-M Futures → Binance Spot → Bybit → ไฟล์ `data/<SYMBOL>_<interval>.csv` → อัปโหลด CSV เอง
เซิร์ฟเวอร์ของ Streamlit Cloud อยู่ในสหรัฐฯ ซึ่ง Binance/Bybit อาจบล็อก (HTTP 451/403)
กรณีนั้นให้ commit ไฟล์ snapshot ใน `data/` (ข้อมูลจะไม่สดใหม่) หรืออัปโหลด CSV ในแอป

> ไม่ใช่คำแนะนำการลงทุน
