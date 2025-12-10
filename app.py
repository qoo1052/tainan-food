import streamlit as st
import random
import pandas as pd
import time

# --- 1. 頁面基本設定 ---
st.set_page_config(
    page_title="台南旅遊小幫手", 
    page_icon="🏯",
    layout="centered"
)

# --- 2. CSS 古都美感設計 ---
st.markdown("""
<style>
    /* ========== 全站主題定義 ========== */
    :root {
        --brick-red: #8B3A3A;   /* 赤崁紅磚色 */
        --warm-beige: #FFF8F0;  /* 古樸米黃色 */
        --old-wood: #5C3317;    /* 舊木頭色 */
    }

    /* ========== 背景設計 ========== */
    .stApp {
        background-image: linear-gradient(rgba(255, 248, 240, 0.9), rgba(255, 248, 240, 0.9)), 
                          url("https://images.unsplash.com/photo-1605211698552-144e044d895e?q=80&w=2070&auto=format&fit=crop");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }

    /* ========== 文字與標題 ========== */
    h1, h2, h3, h4 {
        color: var(--brick-red) !important;
        font-family: "Microsoft JhengHei", "微軟正黑體", sans-serif;
        font-weight: bold;
    }
    .stMarkdown, .stText {
        color: #4A4A4A;
    }

    /* ========== 按鈕設計 ========== */
    div.stButton > button {
        background-color: var(--warm-beige);
        color: var(--brick-red);
        border: 2px solid var(--brick-red);
        border-radius: 12px;
        padding: 10px 24px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background-color: var(--brick-red);
        color: var(--warm-beige);
        border-color: var(--brick-red);
        box-shadow: 0 4px 8px rgba(139, 58, 58, 0.3);
        transform: translateY(-2px);
    }
    div.stButton > button[kind="primary"] {
        background-color: var(--brick-red);
        color: var(--warm-beige);
        border: none;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #A52A2A;
        box-shadow: 0 4px 12px rgba(165, 42, 42, 0.4);
    }

    /* ========== 輸入框優化 ========== */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div > div {
        border-color: var(--brick-red);
        background-color: #ffffff;
    }
    .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
        border-color: var(--brick-red);
        box-shadow: 0 0 0 1px var(--brick-red);
    }

    /* ========== 自定義結果卡片樣式 ========== */
    .result-card {
        background-color: #FDF5E6;
        border: 4px double var(--old-wood);
        border-radius: 8px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
    }
    .result-card h2, .result-card h3 {
        color: var(--old-wood) !important;
        margin: 0;
        font-family: "DFKai-SB", "標楷體", serif;
    }
</style>
""", unsafe_allow_html=True)

st.title("🏯 台南旅遊神隊友")
st.markdown("---")

# 分頁設定 (已更新名稱)
tab1, tab2, tab3, tab4 = st.tabs(["🥢 時段美食", "🐦 水雉抽籤", "💰 秒速分帳", "🛵 停車紀錄"])

# --- 功能 1: 依時段隨機推薦美食 ---
with tab1:
    st.header("🕑 餓了嗎？現在幾點？")
    
    # === 📝 你的美食名單 ===
    food_data = {
        "🌅 活力早餐 (06:00-11:00)": [
            "六千牛肉湯", "阿堂鹹粥", "富盛號碗粿", "勝利早點", 
            "阿公阿婆蛋餅", "呂 早餐", "豆奶宗"
        ],
        "☀️ 飽足午餐 (11:00-14:00)": [
            "葉家小卷米粉", "文章牛肉湯", "阿裕牛肉鍋", "丹丹漢堡", 
            "邱家小卷米粉", "集品蝦仁飯", "矮仔成蝦仁飯"
        ],
        "🍰 悠閒下午茶 (14:00-17:00)": [
            "義豐冬瓜茶", "NINAO 蜷尾家冰淇淋", "周氏蝦捲", "同記安平豆花", 
            "連得堂餅家", "深藍咖啡館 (千層蛋糕)", "双生綠豆沙牛奶"
        ],
        "🌙 晚餐與宵夜 (17:00-24:00)": [
            "阿明豬心冬粉", "十平 (日式丼飯)", "小豪洲沙茶爐", "大東夜市(需確認日期)", 
            "花園夜市(需確認日期)", "鬍鬚忠牛肉湯", "悅津鹹粥"
        ]
    }

    time_select = st.selectbox("請選擇時段：", list(food_data.keys()))
    current_list = food_data[time_select]
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

# --- 功能 2: 水雉抽籤 (名稱已更新) ---
with tab2:
    st.header("🐦 水雉大仙賜籤")
    st.write("呼喚台南市鳥「凌波仙子」，誠心祈求水雉大仙咬出籤王。")
    
    user_input = st.text_area("輸入候選店家 (每行一間)", height=150, 
                             placeholder="例如：\n阿堂鹹粥\n丹丹漢堡\n小豪洲沙茶爐")
    
    if st.button("🎋 請大仙咬籤！", type="primary"):
        if user_input.strip():
            shop_list = [line.strip() for line in user_input.split('\n') if line.strip()]
            
            if shop_list:
                animation_spot = st.empty()
                
                # =========================================================
                # ✅ 您提供的水雉影片連結
                mp4_url = "https://raw.githubusercontent.com/d2756818/tainan-food/main/draw-lots.mp4"
                # =========================================================
                
                video_html = f"""
                    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                        <video width="300" autoplay muted playsinline style="border-radius: 15px; box-shadow: 0 8px 16px rgba(0,0,0,0.2);">
                            <source src="{mp4_url}" type="video/mp4">
                            您的瀏覽器不支援影片標籤。
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

# --- 功能 3: 秒速分帳 ---
with tab3:
    st.header("💸 散會自動算帳")
    if 'expenses' not in st.session_state:
        st.session_state.expenses = []
        
    with st.container():
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1: item_name = st.text_input("項目", key="input_item")
        with c2: payer_name = st.text_input("付款人", key="input_payer")
        with c3: amount = st.number_input("金額", min_value=0, step=10, key="input_amount")
        
        if st.button("➕ 加入清單", use_container_width=True):
            if item_name and payer_name and amount > 0:
                st.session_state.expenses.append({"項目": item_name,"付款人": payer_name,"金額": amount})
                st.success(f"已加入: {item_name}")

    st.divider()
    if st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        st.dataframe(df, use_container_width=True)
        
        total_cost = df["金額"].sum()
        payers = df.groupby("付款人")["金額"].sum().to_dict()
        all_people = list(payers.keys())
        if len(all_people) > 0:
            avg_cost = total_cost / len(all_people)
            st.markdown(f"""
                <div style="background-color: var(--warm-beige); padding: 15px; border-radius: 10px; border-left: 5px solid var(--brick-red);">
                    <h4 style="margin:0;">💰 總金額: <span style="color: var(--brick-red);">${total_cost}</span> | 平均每人: <span style="color: var(--brick-red);">${avg_cost:.1f}</span></h4>
                </div>
                <br>
            """, unsafe_allow_html=True)
            
            st.subheader("📊 結算結果：")
            for person in all_people:
                paid = payers.get(person, 0)
                balance = paid - avg_cost
                if balance > 0: st.success(f"**{person}** 應收回 **${balance:.1f}**")
                elif balance < 0: st.error(f"**{person}** 應再付 **${abs(balance):.1f}**")
                else: st.info(f"**{person}** 結清")
        
        if st.button("🗑️ 清空帳目"):
            st.session_state.expenses = []
            st.rerun()

# --- 功能 4: 停車紀錄 ---
with tab4:
    st.header("🛵 我的機車停哪？")
    memo = st.text_area("輸入停車位置...", height=150, placeholder="例如：\n新光三越對面\n車牌 123-ABC")
    if memo: 
        st.markdown(f"""
        <div class="result-card" style="text-align: left;">
            <h4 style="margin-bottom: 10px;">📍 您的停車紀錄：</h4>
            <pre style="font-family: inherit; white-space: pre-wrap;">{memo}</pre>
        </div>
        """, unsafe_allow_html=True)