import streamlit as st
import random
import pandas as pd
import time
from datetime import datetime
import extra_streamlit_components as stx
import json

# --- 1. 頁面基本設定 ---
st.set_page_config(
    page_title="台南旅遊小幫手", 
    page_icon="🏯",
    layout="centered"
)

# --- 2. CSS 棕色系復古設計 ---
st.markdown("""
<style>
    /* ========== 全站主題變數 (棕色系) ========== */
    :root {
        --main-bg: #F4ECE1;       
        --card-bg: #Eaddcf;       
        --text-color: #4B3621;    
        --accent-color: #8B4513;  
        --border-color: #5D4037;  
    }

    /* ========== 背景與文字設定 ========== */
    .stApp {
        background-color: var(--main-bg);
        background-image: url("https://www.transparenttextures.com/patterns/cream-paper.png");
        background-size: auto;
    }
    .stApp, .stMarkdown, .stText, p, div, li, span, label {
        color: var(--text-color) !important;
        font-family: "Microsoft JhengHei", "微軟正黑體", sans-serif;
    }
    h1, h2, h3, h4 {
        color: var(--accent-color) !important;
        font-weight: 800;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    /* ========== 介面元件優化 ========== */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
        background-color: #FFFDF5 !important;
        color: #4B3621 !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 8px;
    }
    div[data-baseweb="popover"] div, div[data-baseweb="menu"] div {
        background-color: #FFFDF5 !important;
        color: #4B3621 !important;
    }

    /* ========== 按鈕設計 ========== */
    div.stButton > button {
        background-color: #D2B48C !important;
        color: #4B3621 !important;
        border: 2px solid #8B4513 !important;
        border-radius: 12px;
        font-weight: bold;
        box-shadow: 2px 2px 0px #8B4513;
        transition: all 0.2s;
    }
    div.stButton > button:hover {
        background-color: #8B4513 !important;
        color: #FFF !important;
        transform: translateY(2px);
        box-shadow: 0px 0px 0px #8B4513;
    }
    div.stButton > button[kind="primary"] {
        background-color: #8B4513 !important;
        color: #FFF !important;
        border: none !important;
    }

    /* ========== 卡片樣式 ========== */
    .result-card {
        background-color: var(--card-bg);
        border: 3px double var(--border-color);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.1);
    }
    .result-card h2, .result-card h3 {
        color: var(--border-color) !important;
        margin: 0;
        font-family: "DFKai-SB", "標楷體", serif;
    }
    .history-card {
        background-color: #fff;
        border-left: 5px solid #8B4513;
        padding: 10px;
        margin-bottom: 10px;
        font-family: monospace;
        color: #333 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🏯 台南旅遊小幫手")
st.markdown("---")

cookie_manager = stx.CookieManager()

tab1, tab2, tab3, tab4 = st.tabs(["🥢 時段美食", "🐦 抽籤決定", "💰 秒速分帳", "🛵 停車紀錄"])

# --- 功能 1: 依時段隨機推薦美食 ---
with tab1:
    st.header("🕑 餓了嗎？現在幾點？")
    try:
        df_food = pd.read_csv("food_list.csv")
        all_categories = df_food["時段"].unique()
        time_select = st.selectbox("請選擇時段：", all_categories)
        current_list = df_food[df_food["時段"] == time_select]["店名"].tolist()
        current_list = list(set(current_list))
        
        st.info(f"👉 這個時段口袋名單共有 **{len(current_list)}** 家店。")

        if st.button("🎲 幫我決定吃哪家！", type="primary"):
            with st.spinner("🔍 搜尋古都美食中..."):
                time.sleep(0.5)
            choice = random.choice(current_list)
            st.markdown(f"""
            <div class="result-card">
                <h3>🎉 推薦您去吃：{choice}</h3>
            </div>
            """, unsafe_allow_html=True)
            google_url = f"https://www.google.com/search?q=台南+{choice}"
            st.link_button(f"🔍 Google 搜尋「{choice}」", google_url)
    except FileNotFoundError:
        st.error("⚠️ 找不到 food_list.csv 檔案！")

# --- 功能 2: 抽籤決定 ---
with tab2:
    st.header("🐦 水雉大仙賜籤")
    st.write("呼喚台南市鳥「凌波仙子」，誠心祈求水雉大仙咬出籤王。")
    user_input = st.text_area("輸入候選店家 (每行一間)", height=150, 
                             placeholder="例如：\n富盛號碗粿\n炸雞洋行\n莉莉水果店")
    
    if st.button("🎋 請大仙咬籤！", type="primary"):
        if user_input.strip():
            shop_list = [line.strip() for line in user_input.split('\n') if line.strip()]
            if shop_list:
                animation_spot = st.empty()
                mp4_url = "https://raw.githubusercontent.com/d2756818/tainan-food/main/draw-lots.mp4"
                video_html = f"""
                    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                        <video width="300" autoplay muted playsinline style="border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
                            <source src="{mp4_url}" type="video/mp4">
                        </video>
                    </div>
                """
                animation_spot.markdown(video_html, unsafe_allow_html=True)
                time.sleep(4) 
                animation_spot.empty()
                winner = random.choice(shop_list)
                st.markdown(f"""
                    <div class="result-card">
                        <h2>🎋 籤王：{winner}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.warning("請輸入有效的店家名稱")
        else:
            st.warning("還沒輸入店家喔！")

# --- 功能 3: 自動結帳 (修復顯示問題版) ---
with tab3:
    st.header("💸 自動結帳")
    st.caption("這份帳單會自動存在手機裡，關掉網頁也不怕！")

    # 1. 確保 session_state 裡有 'expenses'
    if 'expenses' not in st.session_state:
        st.session_state.expenses = []

    # 2. 如果 session_state 是空的，嘗試從 Cookie 載入 (只做一次)
    # 這樣可以防止 Cookie 讀取延遲導致畫面閃爍
    cookie_data = cookie_manager.get(cookie="trip_expenses")
    if cookie_data and not st.session_state.expenses:
        try:
            st.session_state.expenses = json.loads(cookie_data)
        except:
            st.session_state.expenses = []

    # 3. 輸入區
    with st.container():
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1: item_name = st.text_input("項目", key="input_item")
        with c2: payer_name = st.text_input("付款人", key="input_payer")
        with c3: amount = st.number_input("金額", min_value=0, step=10, key="input_amount")
        
        if st.button("➕ 加入清單", use_container_width=True):
            if item_name and payer_name and amount > 0:
                # 步驟 A: 先更新 Session State (保證畫面立刻顯示)
                st.session_state.expenses.append({
                    "項目": item_name,
                    "付款人": payer_name,
                    "金額": amount
                })
                
                # 步驟 B: 再寫入 Cookie (保證關掉還在)
                cookie_manager.set("trip_expenses", json.dumps(st.session_state.expenses), 
                                 expires_at=datetime.now().replace(year=datetime.now().year + 1))
                
                st.success(f"已加入: {item_name}")
                time.sleep(0.5)
                st.rerun()      
            else:
                st.error("請輸入完整資料喔")

    st.divider()
    
    # 4. 顯示表格與結算 (讀取 st.session_state.expenses，不再依賴不穩定的 Cookie 變數)
    if st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        st.dataframe(df, use_container_width=True)
        total_cost = df["金額"].sum()
        payers = df.groupby("付款人")["金額"].sum().to_