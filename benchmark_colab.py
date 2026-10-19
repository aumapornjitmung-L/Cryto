# =====================================================================
#  รันใน Colab (หรือในเครื่อง): เทียบโมเดลทั้งหมดแบบ walk-forward บนทั้ง 3 เหรียญ
#  แล้วเลือกเฉพาะ "2 โมเดลที่ดีที่สุด" เขียนลง model_config.json ให้แอป Streamlit ใช้
#
#  เตรียมใน Colab:  1) อัปโหลด crypto_ml.py   2) !pip -q install xgboost
#  หมายเหตุ: Colab ใช้ IP ของสหรัฐฯ ซึ่ง Binance/Bybit อาจบล็อก ถ้าดึงไม่ได้ให้ดาวน์โหลดแท่งเทียนจาก
#  ที่อื่นแล้วอัปโหลดเป็นไฟล์ data/<SYMBOL>_<interval>.csv (คอลัมน์ time,open,high,low,close,volume)
# =====================================================================
import json
from crypto_ml import benchmark, DEFAULT_SYMBOLS, MODEL_LABELS

SYMBOLS = DEFAULT_SYMBOLS      # ["QUSDT", "BRUSDT", "AGTUSDT"]
INTERVAL = "4h"                # 15m / 1h / 4h / 1d
HORIZON = 1                    # พยากรณ์ล่วงหน้ากี่แท่ง
TOTAL = 1500                   # จำนวนแท่งที่ดึง

res, summary = benchmark(SYMBOLS, INTERVAL, HORIZON, TOTAL)

print("\n=== ผลรายเหรียญ ===")
print(res.round(4).to_string(index=False))
print("\n=== สรุปเฉลี่ยทุกเหรียญ (เรียงตาม AUC) ===")
print(summary.round(4).to_string())

top2 = list(summary.index[:2])
print("\nโมเดลที่เลือก:", [MODEL_LABELS[m] for m in top2])

with open("model_config.json", "w", encoding="utf-8") as f:
    json.dump({
        "models": top2, "interval": INTERVAL, "horizon": HORIZON,
        "symbols": SYMBOLS, "summary": summary.round(4).reset_index().to_dict("records"),
    }, f, ensure_ascii=False, indent=2)

try:
    from google.colab import files
    files.download("model_config.json")
except ImportError:
    pass
