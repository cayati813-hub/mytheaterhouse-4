import streamlit as st

st.set_page_config(page_title="الأستاذ المنزلي الشامل - 3AC", page_icon="📝", layout="wide")

# العنوان الرئيسي للتطبيق
st.title("👨‍🏫 الأستاذ المنزلي الذكي لثالثة إعدادي (مسار دولي - المغرب)")
st.write("مرحباً بكِ يا آية في نظامكِ الدراسي المتكامل. هنا تجدين الشرح العميق، التمارين الكاملة، الامتحانات القابلة للطباعة ومساعد المشاريع.")

# القائمة الجانبية المتطورة
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

# ==================== قسم الروتين اليومي ====================
if menu == "📅 روتينكِ اليومي الموازن":
    st.header("🕒 روتين تنظيم وقت الدراسة والمدرسة")
    school_start = st.number_input("⏰ ساعة دخول المدرسة (صباحاً):", 0, 23, 8)
    school_end = st.number_input("⏰ ساعة الخروج من المدرسة (مساءً):", 0, 23, 16)
    
    if st.button("🚀 توليد الجدول اليومي"):
        study_start = school_end + 2
        st.success("✅ تم موازنة جدولكِ!")
        st.info(f"🏫 **وقت المدرسة:** من {school_start}:00 إلى {school_end}:00.")
        st.warning(f"🍔 **راحة وغداء:** من {school_end}:00 إلى {study_start}:00.")
        st.success(f"💻 **وقت المذاكرة والتمارين مع الأستاذ:** يبدأ في تمام الساعة {study_start}:00!")

# ==================== 1. الرياضيات ====================
elif menu == "📐 الرياضيات (Mathématiques)":
    st.header("📐 مادة الرياضيات - المسار الدولي")
    tab1, tab2 = st.tabs(["📖 شرح الدروس الكامل", "📝 سلسلة التمارين والتصحيح"])
    
    with tab1:
        st.subheader("1. درس مبرهنة فيتاغورس (Théorème de Pythagore)")
        st.markdown("""
        * **Théorème Direct (المباشرة):** Si un triangle $ABC$ est rectangle en $A$, alors : $BC^2 = AB^2 + AC^2$. 
          * *الهدف:* حساب طول ضلع (غالباً الوتر) عندما يكون المثلث قائم الزاوية ومعلوم فيه ضلعان.
        * **Théorème Réciproque (العكسية):** Si dans un triangle $ABC$ on a $BC^2 = AB^2 + AC^2$, alors le triangle est rectangle en $A$.
          * *الهدف:* البرهنة وإثبات أن المثلث قائم الزاوية.
        """)
        st.subheader("2. درس الحساب المثلثي (Calcul Trigonométrique)")
        st.markdown("""
        Dans un triangle rectangle, pour un angle aigu $\alpha$ :
        * $\cos(\alpha) = \\frac{\\text{Côté adjacent}}{\\text{Hypoténuse}}$
        * $\sin(\alpha) = \\frac{\\text{Côté opposé}}{\\text{Hypoténuse}}$
        * $\\tan(\alpha) = \\frac{\\text{Côté oppposé}}{\\text{Côté adjacent}} = \\frac{\\sin(\alpha)}{\\cos(\alpha)}$
        * **Formule Dorée (القاعدة الذهبية):** $\cos^2(\alpha) + \sin^2(\alpha) = 1$
        """)
        
    with tab2:
        st.subheader("سلسلة تمارين الرياضيات الكاملة")
        ans1 = st.text_input("Q1: ABC rectangle en A, AB=6, AC=8. Calculez BC (le côté hypoténuse) :")
        ans2 = st.text_input("Q2: Sachant que cos(α) = 0.6, calculez sin(α) :")
        
        if st.button("🔍 تصحيح السلسلة كاملاً"):
            score = 0
            if ans1.strip() == "10": score += 1; st.success("Q1: صحيح! $BC^2 = 36 + 64 = 100 \\implies BC=10$.")
            else: st.error("Q1: خطأ. تذكر أن $BC^2 = AB^2 + AC^2$.")
            
            if ans2.strip() == "0.8": score += 1; st.success("Q2: صحيح! استخدام القاعدة $\sin^2(\\alpha) = 1 - 0.6^2 = 0.64$.")
            else: st.error("Q2: خطأ. راجع قاعدة $\cos^2(\\alpha) + \sin^2(\\alpha) = 1$.")
            st.metric("نقطتك الإجمالية في السلسلة:", f"{score}/2")

# ==================== 2. الفيزياء والكيمياء ====================
elif menu == "🧪 الفيزياء والكيمياء (PC)":
    st.header("🧪 مادة الفيزياء والكيمياء - Physique et Chimie")
    tab1, tab2 = st.tabs(["📖 شرح الدروس الكامل", "📝 سلسلة التمارين والتصحيح"])
    
    with tab1:
        st.subheader("1. درس أمثلة لبعض المواد المستعملة في حياتنا اليومية")
        st.markdown("نميز بين **الأجسام (Objets)** و **المواد (Matériaux)**. الجسم يُصنع من مادة أو أكثر (مثال: الكأس جسم، الزجاج مادة).")
        st.subheader("2. درس أكسدة المواد في الهواء (Oxydation)")
        st.markdown("""
        * **Oxydation du Fer (أكسدة الحديد):** Forme la rouille (الصدأ) selon l'équation : $4Fe + 3O_2 \\implies 2Fe_2O_3$ (Oxyde de fer III). C'est une couche poreuse (منفذة للهواء).
        * **Oxydation de l'Aluminium (أكسدة الألومنيوم):** Forme l'alumine : $4Al + 3O_2 \\implies 2Al_2O_3$. C'est une couche non poreuse qui protège le métal.
        """)
        
    with tab2:
        st.subheader("سلسلة تمارين الفيزياء")
        q_pc = st.radio("L'équation chimique de la formation de la rouille est :", ["2Fe + O2 -> 2FeO", "4Fe + 3O2 -> 2Fe2O3", "Fe + O2 -> FeO2"])
        if st.button("🔍 تصحيح تمرين الفيزياء"):
            if q_pc == "4Fe + 3O2 -> 2Fe2O3": st.balloons(); st.success("ممتاز! معادلة أكسدة الحديد صحيحة ومتوازنة.")
            else: st.error("إجابة خاطئة. الحديد يتفاعل مع ثنائي الأكسجين ليعطي أكسيد الحديد الثالث.")

# ==================== 3. علوم الحياة والأرض ====================
elif menu == "🧬 علوم الحياة والأرض (SVT)":
    st.header("🧬 علوم الحياة والأرض - SVT")
    tab1, tab2 = st.tabs(["📖 شرح الدروس الكامل", "📝 سلسلة التمارين والتصحيح"])
    
    with tab1:
        st.subheader("1. الهضم والامتصاص المعوي (Digestion et Absorption)")
        st.markdown("""
        * **الهضم الهضمي والميكانيكي:** تحول الأغذية إلى **مواد القيت (Nutriments)** تحت تأثير الأنزيمات الهضمية (Les enzymes).
        * **الامتصاص:** يتم في الأمعاء الدقيقة بواسطة **الزغابات المعوية (Les villosités intestinales)** التي تنقل القيت إلى الدم واللمف.
        """)
    with tab2:
        st.subheader("سلسلة تمارين SVT")
        q_svt = st.radio("Où se déroule l'absorption des nutriments ?", ["L'estomac (المعدة)", "L'intestin grêle (الأمعاء الدقيقة)", "Le gros intestin"])
        if st.button("🔍 تصحيح تمرين SVT"):
            if q_svt == "L'intestin grêle (الأمعاء الدقيقة)": st.success("صحيح! الزغابات المعوية توجد في الأمعاء الدقيقة وهي مقر الامتصاص.")
            else: st.error("خاطئ. راجعي دور الأمعاء الدقيقة في الامتصاص المعوي.")

# ==================== 4. اللغة الإنجليزية ====================
elif menu == "🇬🇧 اللغة الإنجليزية (English 3AC)":
    st.header("🇬🇧 English - 3rd Year Secondary School (Maroc)")
    tab1, tab2 = st.tabs(["📖 Grammar & Vocabulary Explanations", "📝 Practice Exercises"])
    
    with tab1:
        st.subheader("1. Greeting and Introducing People")
        st.markdown("""
        * **Introducing yourself:** "Hello, my name is Aya. I am a student."
        * **Introducing others:** "This is my friend, she is in 3rd prep."
        """)
        st.subheader("2. Present Simple Tense")
        st.markdown("""
        Used for habits and facts. 
        * *Rule:* I/You/We/They + Verb | He/She/It + Verb+(s/es)
        * *Example:* "I **study** English every day." | "She **studies** mathematics."
        """)
    with tab2:
        st.subheader("English Practice Test")
        eng_ans = st.text_input("Fill in the blank: He ________ (go) to school at 8 AM.")
        if st.button("🔍 Check English Answer"):
            if eng_ans.strip().lower() == "goes": st.balloons(); st.success("Correct! With 'He', we add 'es' to the verb 'go'.")
            else: st.error("Incorrect. Remember the Present Simple rule for He/She/It (go -> goes).")

# ==================== 5. اللغة الفرنسية ====================
elif menu == "🇫🇷 اللغة الفرنسية (Français)":
    st.header("🇫🇷 Langue Française - 3AC")
    st.write("دروس الدورة الأولى تركز على القصة والرسالة وقواعد التعبير عن السبب والنتيجة.")
    fr_q = st.text_input("Complétez avec l'expression de cause correcte: Il est absent ______ il est malade. (car / comme)")
    if st.button("🔍 Corriger"):
        if fr_q.strip().lower() == "car": st.success("Bravo! 'car' se place au milieu pour exprimer la cause.")
        else: st.error("Faux. 'Comme' se place au début de la phrase.")

# ==================== 6. الامتحانات الموحدة الكاملة والطباعة ====================
elif menu == "📝 الامتحانات الموحدة الكاملة (PDF / للطباعة)":
    st.header("📝 بنك الامتحانات الموحدة المحلية والجهوية")
    st.write("إليك نموذج امتحان موحد جهوي كامل في مادة الرياضيات. يمكنك نسخه وطباعته أو حله ورقياً:")
    
    st.markdown("""
    ---
    ### 📄 Examen Régional Blanc - Mathématiques 3AC
    **Durée : 2 Heures | Coefficient : 3**
    
    #### Exercice 1 (6 Points) - Équations et Inéquations
    1. Résoudre l'équation suivante : $3x - 5 = x + 7$
    2. Résoudre l'équation : $(2x - 3)(x + 4) = 0$
    3. Résoudre l'inéquation : $2x + 3 \\leq 7$
    
    #### Exercice 2 (4 Points) - Théorème de Pythagore
    Soit $EFG$ un triangle rectangle en $E$ tel que $EF = 3$ et $EG = 4$.
    1. Calculer la valeur du côté $FG$.
    2. Soit $M$ un point tel que le triangle soit vérifié par la réciproque.
    
    #### Exercice 3 (5 Points) - Calcul Trigonométrique
    1. Soit $x$ un angle aigu. Simplifier l'expression : $A = \cos^2(20^\\circ) + \cos^2(70^\\circ) + \sin(30^\\circ) - \\frac{1}{2}$
    ---
    """)
    st.info("💡 **نصيحة الأستاذ للطباعة:** يمكنك الضغط على زر (Ctrl + P) في لوحة المفاتيح لحفظ هذه الصفحة بالكامل كملف PDF أو طباعتها مباشرة على ورق لكي تحلي الامتحان بيدكِ!")

# ==================== 7. مساعد المشاريع والبحوث الذكي ====================
elif menu == "🛠️ مساعد المشاريع المدرسية والبحوث الذكي":
    st.header("🛠️ مساعد البحوث والمشاريع المدرسية والبحث التلقائي")
    st.write("أدخلي عنوان المشروع أو العرض (Exposé) المطلوب منكِ في الإعدادي، وسأعطيكِ خطة البحث الكاملة، وطرق البحث والمراجع:")
    
    user_project = st.text_input("اكتبي موضوع البحث هنا (مثلاً: أزمة الماء في المغرب، أخطار التلوث، التغذية المتوازنة):")
    
    if st.button("✨ ابحث وولد لي مشروعاً كاملاً"):
        if user_project:
            st.success(f"📋 تم إنشاء هيكل البحث الكامل لموضوع: ({user_project})")
            st.markdown(f"""
            ### 📑 ملف المشروع المدرسي جاهز للنسخ:


