import streamlit as st

st.set_page_config(page_title="الأستاذ المنزلي الشامل - 3AC", page_icon="📝", layout="wide")

st.title("👨‍🏫 الأستاذ المنزلي الذكي لثالثة إعدادي (مسار دولي - المغرب)")
st.write("مرحباً بكِ يا آية في نظامكِ الدراسي المتكامل. هنا تجدين الشرح العميق، التمارين الكاملة، الامتحانات القابلة للطباعة ومساعد المشاريع.")

menu = st.sidebar.selectbox("📚 تصفح الأقسام والمواد:", [
    "📅 روتينكِ اليومي الموازن",
    "📐 الرياضيات (Mathématiques)",
    "🧪 الفيزياء والكيمياء (PC)",
    "🧬 علوم الحياة والأرض (SVT)",
    "🇬🇧 اللغة الإنجليزية (English 3AC)",
    "🇫🇷 اللغة الفرنسية (Français)",
    "📝 الامتحانات الموحدة الكاملة (PDF / للطباعة)",
    "🛠️ مساعد المشاريع المدرسية والبحوث الذكي"
])

if menu == "📅 روتينكِ اليومي الموازن":
    st.header("🕒 روتين تنظيم وقت الدراسة والمدرسة")
    school_start = st.number_input("⏰ ساعة دخول المدرسة (صباحاً):", 0, 23, 8)
    school_end = st.number_input("⏰ ساعة الخروج من المدرسة (مساءً):", 0, 23, 16)
    
    if st.button("🚀 توليد الجدول اليومي"):
        study_start = school_end + 2
        st.success("✅ تم موازنة جدولكِ!")
        st.info(f"🏫 **وقت المدرسة:** من {school_start}:00 إلى {school_end}:00.")
        st.warning(f"🍔 **راحة وغداء:** من {school_end}:00 إلى {study_start}:00.")
        st.success(f"💻 **وقت Mذاكرة والتمارين مع الأستاذ:** يبدأ في تمام الساعة {study_start}:00!")

elif menu == "📐 الرياضيات (Mathématiques)":
    st.header("📐 مادة الرياضيات - المسار الدولي")
    tab1, tab2 = st.tabs(["📖 شرح الدروس الكامل", "📝 سلسلة التمارين والتصحيح"])
    
    with tab1:
        st.subheader("1. درس مبرهنة فيتاغورس (Théorème de Pythagore)")
        st.markdown("""
        * **Théorème Direct (المباشرة):** Si un triangle $ABC$ est rectangle en $A$, alors : $BC^2 = AB^2 + AC^2$. 
        * **Théorème Réciproque (العكسية):** Si dans un triangle $ABC$ on a $BC^2 = AB^2 + AC^2$, alors le triangle est rectangle en $A$.
        """)
        st.subheader("2. درس الحساب المثلثي (Calcul Trigonométrique)")
        st.markdown("""
        Dans un triangle rectangle, pour un angle aigu $\alpha$ :
        * $\cos(\alpha) = \\frac{\\text{Côté adjacent}}{\\text{Hypoténuse}}$
        * $\sin(\alpha) = \\frac{\\text{Côté opposé}}{\\text{Hypoténuse}}$
        * **Formule Dorée (القاعدة الذهبية):** $\cos^2(\alpha) + \sin^2(\alpha) = 1$
        """)
        
    with tab2:
        st.subheader("سلسلة تمارين الرياضيات الكاملة")
        ans1 = st.text_input("Q1: ABC rectangle en A, AB=6, AC=8. Calculez BC :")
        ans2 = st.text_input("Q2: Sachant que cos(α) = 0.6, calculez sin(α) :")
        
        if st.button("🔍 تصحيح السلسلة كاملاً"):
            score = 0
            if ans1.strip() == "10": score += 1; st.success("Q1: صحيح! $BC=10$.")
            else: st.error("Q1: خطأ. تذكر أن $BC^2 = AB^2 + AC^2$.")
            if ans2.strip() == "0.8": score += 1; st.success("Q2: صحيح! $\sin(\\alpha) = 0.8$.")
            else: st.error("Q2: خطأ. راجع قاعدة الحساب المثلثي.")
            st.metric("نقطتك الإجمالية في السلسلة:", f"{score}/2")

elif menu == "🧪 الفيزياء والكيمياء (PC)":
    st.header("🧪 مادة الفيزياء والكيمياء - Physique et Chimie")
    tab1, tab2 = st.tabs(["📖 شرح الدروس الكامل", "📝 سلسلة التمارين والتصحيح"])
    
    with tab1:
        st.subheader("1. درس أمثلة لبعض المواد المستعملة في حياتنا اليومية")
        st.markdown("نميز بين الأجسام والمواد. الجسم يُصنع من مادة أو أكثر.")
        st.subheader("2. درس أكسدة المواد في الهواء (Oxydation)")
        st.markdown("""
        * **Oxydation du Fer:** $4Fe + 3O_2 \\implies 2Fe_2O_3$ (Oxyde de fer III). C'est la rouille.
        * **Oxydation de l'Aluminium:** $4Al + 3O_2 \\implies 2Al_2O_3$ (Alumine).
        """)
        
    with tab2:
        st.subheader("سلسلة تمارين الفيزياء")
        q_pc = st.radio("L'équation chimique de la formation de la rouille est :", ["2Fe + O2 -> 2FeO", "4Fe + 3O2 -> 2Fe2O3"])
        if st.button("🔍 تصحيح تمرين الفيزياء"):
            if q_pc == "4Fe + 3O2 -> 2Fe2O3": st.balloons(); st.success("ممتاز! معادلة أكسدة الحديد صحيحة ومتوازنة.")
            else: st.error("إجابة خاطئة.")

elif menu == "🧬 علوم الحياة والأرض (SVT)":
    st.header("🧬 علوم الحياة والأرض - SVT")
    tab1, tab2 = st.tabs(["📖 شرح الدروس الكامل", "📝 سلسلة التمارين والتصحيح"])
    
    with tab1:
        st.subheader("1. الهضم والامتصاص المعوي (Digestion et Absorption)")
        st.markdown("تحول الأغذية إلى مواد القيت تحت تأثير الأنزيمات الهضمية. ويتم الامتصاص في الأمعاء الدقيقة.")
    with tab2:
        st.subheader("سلسلة تمارين SVT")
        q_svt = st.radio("Où se déroule l'absorption des nutriments ?", ["L'estomac", "L'intestin grêle"])
        if st.button("🔍 تصحيح تمرين SVT"):
            if q_svt == "L'intestin grêle": st.success("صحيح! الزغابات المعوية توجد في الأمعاء الدقيقة وهي مقر الامتصاص.")
            else: st.error("خاطئ.")

elif menu == "🇬🇧 اللغة الإنجليزية (English 3AC)":
    st.header("🇬🇧 English - 3rd Year Secondary School (Maroc)")
    tab1, tab2 = st.tabs(["📖 Grammar & Vocabulary Explanations", "📝 Practice Exercises"])
    
    with tab1:
        st.subheader("1. Greeting and Introducing People")
        st.markdown("* Hello, my name is Aya. I am a student.\n* This is my friend.")
        st.subheader("2. Present Simple Tense")
        st.markdown("* Rule: He/She/It + Verb+(s/es)\n* Example: He studies English every day.")
    with tab2:
        st.subheader("English Practice Test")
        eng_ans = st.text_input("Fill in the blank: He ________ (go) to school at 8 AM.")
        if st.button("🔍 Check English Answer"):
            if eng_ans.strip().lower() == "goes": st.balloons(); st.success("Correct!")
            else: st.error("Incorrect. Remember the Present Simple rule.")

elif menu == "🇫🇷 اللغة الفرنسية (Français)":
    st.header("🇫🇷 Langue Française - 3AC")
    st.write("دروس الدورة الأولى تركز على القصة والرسالة وقواعد التعبير عن السبب والنتيجة.")
    fr_q = st.text_input("Complétez avec l'expression de cause correcte: Il est absent ______ il est malade. (car / comme)")
    if st.button("🔍 Corriger"):
        if fr_q.strip().lower() == "car": st.success("Bravo! 'car' se place au milieu pour exprimer la cause.")
        else: st.error("Faux.")

elif menu == "📝 الامتحانات الموحدة الكاملة (PDF / للطباعة)":
    st.header("📝 بنك الامتحانات الموحدة المحلية والجهوية")
    st.write("إليك نموذج امتحان موحد جهوي كامل في مادة الرياضيات. يمكنك نسخه وطباعته أو حله ورقياً:")
    st.markdown("""
    ### 📄 Examen Régional Blanc - Mathématiques 3AC
    #### Exercice 1 (6 Points) - Équations
    1. Résoudre l'équation suivante : $3x - 5 = x + 7$
    2. Résoudre l'équation : $(2x - 3)(x + 4) = 0$
    #### Exercice 2 (4 Points) - Pythagore
    Soit $EFG$ un triangle rectangle en $E$ tel que $EF = 3$ et $EG = 4$.
    1. Calculer la valeur du côté $FG$.
    """)
    st.info("💡 يمكنك الضغط على زر (Ctrl + P) في لوحة المفاتيح لحفظ هذه الصفحة كملف PDF وطباعتها!")

elif menu == "🛠️ مساعد المشاريع المدرسية والبحوث الذكي":
    st.header("🛠️ مساعد البحوث والمشاريع المدرسية والبحث التلقائي")
    user_project = st.text_input("اكتبي موضوع البحث هنا:")
    if st.button("✨ ابحث وولد لي مشروعاً كاملاً"):
        if user_project:
            st.success(f"📋 تم إنشاء هيكل البحث الكامل لموضوع: ({user_project})")
            st.markdown(f"#### 1. المقدمة:\nيعتبر موضوع {user_project} من أهم المواضيع التي تشغل المجتمع المغربي.\n#### 2. المحاور:\n* المحور الأول: التعريف بالظاهرة.\n* المحور الثاني: الأسباب والحلول.")
        else:
            st.warning("الرجاء كتابة اسم الموضوع أولاً!")



