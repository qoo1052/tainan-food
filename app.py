import streamlit as st
import random
import pandas as pd
import time

# --- 頁面基本設定 ---
st.set_page_config(page_title="台南旅遊小幫手", page_icon="🏯")

# --- CSS 外觀設計 (台南古蹟風格) ---
# 這裡設定了背景圖、字體顏色與按鈕樣式
st.markdown("""
<style>
    /* 1. 設定背景圖片 (台南紅磚/古蹟氛圍) */
    .stApp {
        background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
                          url("https://images.unsplash.com/photo-1552427847-f32616a9a30d?q=80&w=2070&auto=format&fit=crop");
        background-attachment: fixed;
        background-size: cover;
    }
    
    /* 2. 標題文字顏色改為「磚紅色」 */
    h1, h2, h3 {
        color: #8B3A3A !important;
        font-family: "Microsoft JhengHei", sans-serif;
    }

    /* 3. 按鈕樣式優化 */
    .stButton>button {
        border-radius: 20px;
        font-weight: bold;
        border: 2px solid #8B3A3A;
        color: #8B3A3A;
        background-color: #FFF8F0;
    }
    .stButton>button:hover {
        background-color: #8B3A3A;
        color: white;
        border-color: #8B3A3A;
    }
    
    /* 4. 結果卡片的樣式 */
    .result-card {
        background-color: #FFF8F0;
        border: 3px double #8B3A3A;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🏯 台南旅遊神隊友")
st.markdown("**古都漫遊 | 美食抽籤 | 快速分帳 | 停車便條**")

# 分頁設定
tab1, tab2, tab3, tab4 = st.tabs(["🥢 時段美食", "🦜 玄鳳抽籤", "💰 秒速分帳", "🛵 停車紀錄"])

# --- 功能 1: 依時段隨機推薦美食 (含 Google 按鈕) ---
with tab1:
    st.header("🕑 餓了嗎？現在幾點？")
    
    # === 📝 你的美食名單編輯區 (在此處修改或新增) ===
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
    # ===============================================

    # 1. 讓使用者選擇時段
    time_select = st.selectbox("請選擇時段：", list(food_data.keys()))
    
    # 2. 顯示該時段有多少店家
    current_list = food_data[time_select]
    st.info(f"這個時段口袋名單共有 {len(current_list)} 家店。")

    # 3. 抽籤按鈕
    if st.button("🎲 幫我決定吃哪家！", type="primary"):
        # 模擬思考動畫
        with st.spinner("🔍 搜尋古都美食中..."):
            time.sleep(0.5)
        
        choice = random.choice(current_list)
        
        # 顯示結果
        st.markdown(f"""
        <div class="result-card">
            <h3 style="margin:0;">🎉 推薦您去吃：{choice}</h3>
        </div>
        """, unsafe_allow_html=True)

        # 4. Google 搜尋按鈕 (直接開啟新視窗)
        google_url = f"https://www.google.com/search?q=台南+{choice}"
        st.link_button(f"🔍 Google 搜尋「{choice}」", google_url)

# --- 功能 2: 玄鳳鸚鵡抽籤 (精緻動畫版) ---
with tab2:
    st.header("🦜 玄鳳大仙賜籤")
    st.write("輸入候選店家，誠心祈求玄鳳大仙咬出籤王。")
    
    user_input = st.text_area("輸入候選店家 (每行一間)", height=150, 
                             placeholder="例如：\n阿堂鹹粥\n丹丹漢堡\n小豪洲沙茶爐")
    
    if st.button("🎋 請大仙咬籤！"):
        if user_input.strip():
            shop_list = [line.strip() for line in user_input.split('\n') if line.strip()]
            
            if shop_list:
                animation_spot = st.empty()
                
                # --- 請在此處替換您的 GIF 連結 ---
                target_gif_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2RjOWRnMnV4d3g4a2hwcDV5aWF4NnJ6YjNmb3J6YjNmb3J6YjNmb3J6eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/l0HlPvbM3u0635u5a/giphy.gif"
                # --------------------------------
                
                animation_spot.markdown(
                    f"""
                    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                        <img src="{target_gif_url}" width="300" style="border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    </div>
                    """, unsafe_allow_html=True
                )
                time.sleep(3.5)
                animation_spot.empty()
                
                winner = random.choice(shop_list)
                st.markdown(f"""
                    <div class="result-card" style="background-color: #FDF5E6; border-color: #8B4513;">
                        <h2 style="color: #8B4513 !important; margin:0;">🎋 籤王：{winner}</h2>
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
            st.markdown(f"#### 💰 總金額: ${total_cost} | 平均每人: ${avg_cost:.1f}")
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
    if memo: st.info(f"📍 您的紀錄：\n{memo}")