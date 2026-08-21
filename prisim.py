import streamlit as st
import math

# 海運費
p_kaiun = 1000000
# 登録検査費用
p_kensa = 160000

st.write("# HYMER Japan - Price Simulator")
st.write("金額は消費税抜きで入力してください。")
st.write(f"この試算では、海運費（¥{int(p_kaiun):,}）、登録検査費用（¥{int(p_kensa):,}）で設定しています。")

st.divider()

# 仕入原価
p_genka = st.number_input("海外支払車両代金", min_value = 2000000, max_value = 50000000, value = 10000000, step = 10000)


# 日本仕様費用
jpn_ctg = {
    "モーターホーム": 800000,
    "キャンパーバン": 390000,
    "トレーラー": 260000
    }
jpn_ctg_selected = st.selectbox(
        label = "日本仕様",
        options = list(jpn_ctg.keys()),
        format_func = lambda x: x
        )
p_jpn = jpn_ctg[jpn_ctg_selected]


top_col1, top_col2 = st.columns(2)

with top_col1:
        p_haigas = st.number_input("排ガス試験費用", min_value = 0, max_value = 1000000, value = 800000, step = 1000)
with top_col2:
        p_souon = st.number_input("騒音試験費用", min_value = 0, max_value = 1000000, value = 60000, step = 1000)


mid_col1, mid_col2 = st.columns(2)

with mid_col1:
        p_rikusou = st.number_input("試験等陸送費", min_value = 0, max_value = 500000, value = 150000, step = 1000)
with mid_col2:
        p_hojo = st.number_input("予備費", min_value = 0, max_value = 1000000, value = 150000, step = 10000)

st.divider()


# 自社利益
p_rieki = st.slider(
        label = "自社利益（％）",
        min_value = 7.0,
        max_value = 10.0,
        value = 10.0,
        step = 0.5,
        format = "%.1f"
        )

# 業販マージン
p_margin = st.slider(
        label = "業販マージン（％）",
        min_value = 5.5,
        max_value = 8.5,
        value = 7.0,
        step = 0.5,
        format = "%.1f"
        )


# 計算
price_sim = (p_genka + p_kaiun + p_jpn + p_haigas + p_souon + p_rikusou + p_kensa + p_hojo + (p_genka * (p_rieki / 100))) / (1 - (p_margin / 100))
formated_price = math.ceil(price_sim / 10000) * 10000
jisya_rieki = formated_price - (p_genka + p_kaiun + p_jpn + p_haigas + p_souon + p_rikusou + p_kensa + p_hojo) - (formated_price * (p_margin / 100))

st.divider()


col1, col2 = st.columns(2)

with col1:
        st.metric("想定店頭価格（消費税別）", f"¥{int(formated_price):,}")
        st.write(f"業販マージン： ¥{int(formated_price * (p_margin / 100)):,}")
        st.write(f"自社利益： ¥{int(jisya_rieki):,}")
with col2:
        st.metric("想定店頭価格（消費税込）", f"¥{int((formated_price * 1.1)):,}")

