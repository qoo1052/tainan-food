import streamlit as st
import random
import pandas as pd
import time  # 引入時間模組，為了做抽籤的延遲效果

# 設定網頁標題與圖示
st.set_page_config(page_title="台南旅遊小幫手", page_icon="🏯")

st.title("🏯 台南旅遊神隊友 (精簡版)")
st.write("移除置物櫃功能，合併美食推薦，並請來了玄鳳大神幫忙抽籤。")

# 更新：只剩下四個功能 (移除置物櫃)
tab1, tab2, tab3, tab4 = st.tabs(["🍤 隨機美食", "🦜 玄鳳抽籤", "💰 秒速分帳", "🛵 停車紀錄"])

# --- 功能 1: 隨機推薦美食 (已合併新舊店家) ---
with tab1:
    st.header("🤤 今天吃什麼？")
    st.write("不管老店還是新店，好吃的都放在一起隨機抽！")
    
    # 合併後的清單
    food_list = [
        "阿堂鹹粥", "六千牛肉湯", "富盛號碗粿", "阿明豬心冬粉", "葉家小卷米粉", 
        "義豐冬瓜茶", "周氏蝦捲", "十平 (日式丼飯)", "NINAO 蜷尾家冰淇淋", 
        "Bar Home (特色酒吧)", "StableNice BLDG (老宅咖啡)", "糯夫米糕",
        "丹丹漢堡", "文章牛肉湯", "阿裕牛肉鍋"
    ]

    if st.button("🎲 隨機推薦一家"):
        # 加上一點點隨機的驚喜感
        choice = random.choice(food_list)
        st.success(f"🎯 命運的選擇是： **{choice}**")

# --- 功能 2: 玄鳳鸚鵡抽籤 (取代氣球動畫) ---
with tab2:
    st.header("🦜 玄鳳大仙幫你選")
    st.write("輸入大家想吃的店，請玄鳳從傳統木籤筒中咬出一支！")
    
    user_input = st.text_area("輸入候選店家 (每行一間)", height=150, 
                             placeholder="例如：\n阿堂鹹粥\n丹丹漢堡\n小豪洲沙茶爐")
    
    if st.button("🎋 請玄鳳賜籤！"):
        if user_input.strip():
            shop_list = [line.strip() for line in user_input.split('\n') if line.strip()]
            
            if shop_list:
                # 步驟 1: 模擬思考/抽籤的時間 (儀式感)
                with st.spinner('🦜 玄鳳鸚鵡正在木籤筒裡挑選... (喀勒喀勒...)'):
                    time.sleep(2)  # 讓程式停頓 2 秒，製造緊張感
                
                # 步驟 2: 抽出結果
                winner = random.choice(shop_list)
                
                # 這裡可以用文字畫出一個簡單的籤
                st.markdown("---")
                st.markdown(f"### 🦜 鸚鵡咬出的籤上寫著：")
                st.markdown(
                    f"""
                    <div style="
                        border: 2px solid #8B4513; 
                        background-color: #FDF5E6; 
                        padding: 20px; 
                        text-align: center; 
                        border-radius: 10px; 
                        color: #8B4513;
                        font-family: 'DFKai-SB', 'BiauKai', serif;
                        font-size: 24px;
                        font-weight: bold;">
                        🎋 籤王：{winner}
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                st.markdown("---")
            else:
                st.warning("請輸入有效的店家名稱")
        else:
            st.warning("還沒輸入店家喔！")

# --- 功能 3: 紀錄分攤餐點金額 (無變動) ---
with tab3:
    st.header("💸 散會自動算帳")
    
    if 'expenses' not in st.session_state:
        st.session_state.expenses = []

    with st.container():
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1:
            item_name = st.text_input("項目", key="input_item")
        with c2:
            payer_name = st.text_input("付款人", key="input_payer")
        with c3:
            amount = st.number_input("金額", min_value=0, step=10, key="input_amount")
            
        if st.button("➕ 加入清單"):
            if item_name and payer_name and amount > 0:
                st.session_state.expenses.append({
                    "項目": item_name,
                    "付款人": payer_name,
                    "金額": amount
                })
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
                if balance > 0:
                    st.success(f"**{person}** 應收回 **${balance:.1f}**")
                elif balance < 0:
                    st.error(f"**{person}** 應再付 **${abs(balance):.1f}**")
                else:
                    st.info(f"**{person}** 結清")
                    
        if st.button("🗑️ 清空帳目"):
            st.session_state.expenses = []
            st.rerun()

# --- 功能 4: 停車紀錄 (原本的 Tab 5 往前移) ---
with tab4:
    st.header("🛵 我的機車停哪？")
    memo = st.text_area("輸入停車位置、地標或樓層", height=150, 
                       placeholder="例如：\n新光三越對面\n車牌 123-ABC")
    if memo:
        st.success("紀錄中...")
        st.info(memo)