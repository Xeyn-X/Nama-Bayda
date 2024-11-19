# Nama Bayda (နာမဗေဒ)


***ဟိန်းထက်အာကာမောင်***<br><br>
***နိုဝင်ဘာလ၊ ၂၄ရက်***

---
***Paper အပြည့်အစုံအား https://docs.google.com/document/d/1WOhaStRVrdnoBiJTP_x7PKUSIM4tM9_aUE2IEUp0dPM/edit?tab=t.0 တွင် ဖော်ပြထားသည်။***
---

## Abstract

  နိုင်ငံတကာတွင် AI နည်းပညာသည် သိသိသာသာ တိုးတက်နေပြီး ယခုအချိန်တွင် GPT 4 ထိရောက်ရှိနေပြီ ဖြစ်သော်လည်း မြန်မာစာ၊ မြန်မာဘာသာစကား၌မူ အားနည်းနေ သေးသည်ကို တွေ့ရှိရပါ သည်။ထိုသို့အားနည်းနေ ခြင်းမှာ ဘာသာဗေဒဆိုင်ရာ အားနည်းနေခြင်း၊ မြန်မာစာ၊ မြန်မာဘာသာစကား နှင့်ပတ်သက်သော Data အချက်အလက်များ လုံလောက်စွာမရှိခြင်းတို့ကြောင့် ဖြစ်သည်ဟုထင်မှတ်မိသဖြင့် မြန်မာစာ၊ မြန်မာဘာသာစကား တိုးတက်လာစေရန် ရည်ရွယ်၍ ချဥ်းကပ်ခဲ့ခြင်းဖြစ်သည်။  <br><br>
  Generative Ai ၌ အားနည်းနေသေးသဖြင့် Traditional method ဖြစ်သည့် Recurrent Neural Network (RNN) [5][6] ကိုသုံးပြီး Train ထားပါသည်။ Dataset ကိုမူ မြန်မာနိုင်ငံရှိ တက္ကသိုလ်များမှ ကျောင်းသား၊ ကျောင်းသူများ၏ နာမည်များကို ကိုယ်တိုင် စရင်းပြုစုပြီး စုဆောင်းထားသည်။ လက်ရှိတွင် Data ပေါင်း လေးထောင်ကျော် ရှိနေပြီ ဖြစ်သည်။ API အဖြစ် Google မှ released ထားသော Tensorflow API ကိုသုံးထားသည်။ <br><br>
  မြန်မာလူမျိုးများ၏ အမည်များသည် တစ်လုံးချင်း၌ အဓိပ္ပာယ်ရှိနေသဖြင့် ( ဥပမာ - ကောင်းမြတ် ဆိုသောအမည်တွင် "ကောင်း" ဟူသည် "ကောင်းမွန်ခြင်း" ဟုအဓိပ္ပာယ်ရပြီး "မြတ်" ဟူသည် "မြင့်မြတ်ခြင်း" ဟုအဓိပ္ပယ်ရသည်။ ) Generate လုပ်ရာတွင် ၎င်းအချက်ကိုလည်း ထည့်သွင်းစဥ်းစားထားပြီး တစ်လုံးနှင့်တစ်လုံး ချိတ်ဆက်ရာတွင်လဲ လှပ၍အဓိပ္ပယ်ရှိစေရန် အဓိကထားခဲ့သည်။<br><br>

---

## Introduction

  နာမဗေဒဟူသည် မြန်မာနာမည်နှင့်ပတ်သတ်ပြီး လုပ်ဆောင်ချက်များပါရှိသော နေရာတစ်ခုဖြစ်သည်။ ရုံးလုပ်ငန်းများအတွက် ပိုမိုလွယ်ကူစွာ Generate လုပ်နိုင်စေရန် Online Tool အဖြစ် ဖန်တီးတည်ဆောက် ထားသည်။ နာမဗေဒတွင် အပိုင်းလေးပိုင်းပါရှိသည်။ အဓိကအပိုင်းဖြစ်သည့် Burmese Name Generator ၊ Burmese Name Romanizer၊ Burmese Name Gender Detector ၊ Burmese Name Meaning Explainer တို့ဖြစ်ပါသည်။<br><br> 
  Burmese Name Genertor ဆိုသည်မှာ AI နည်းပညာဖြင့် မြန်မာနာမည်ကိုထုတ်ပေးခြင်း ဖြစ်သည်။ သက်ရှိသက်မဲ့ အရာရာတိုင်းတွင် နာမည်သည်မရှိမဖြစ် လိုအပ်သောအရာဖြစ်ပြီး ပြီးစလွယ် မှားပေးမသင့်သော အရာလဲဖြစ်ပါသည်။ ဤသို့အရေးကြီးသောအရာကို ဂရုတစိုက် ရွေးချယ်ရာတွင် အကြံအဉာဏ်ပေး ကူညီပေးနိုင်စေရန်အတွက် (အထူးသဖြင့် မြန်မာနာမည်လိုအပ်နေသော နိုင်ငံခြားသားများ) Burmese Name Generator ကိုဖန်တီးခဲ့ခြင်းဖြစ်သည်။<br><br>
  NLP အတွက်ဆိုလျှင်လည်း မြန်မာဘာသာနှင့် Dataset တစ်ခုတိုးလာခဲ့ပြီး မြန်မာစာ  ကို မည်သို့မည်ပုံ Manage လုပ်ရသည်ကို သိရှိရမည်ဖြစ်သည်။ Datasetကို အစားထိုးလိုက်ယုံဖြင့်လည်း  တခြားသောနာမည်များ (အိမ်မွေးတိရိစ္ဆန်နာမည်၊ လမ်းနာမည်၊ လုပ်ငန်းနာမည်၊ အစရှိတာတွေ) ကိုဖန်တီးနိုင်ပါသည်။<br><br>
  Burmese Name Romanizer ဆိုသည်မှာ မြန်မာနာမည််ကို မြန်မာစာမှ အင်္ဂလိပ်သို့၊ အင်္ဂလိပ်မှ မြန်မာစာသို့ ပြောင်းပေးခြင်း ဖြစ်သည်။ Data အများအပြားကိုင်တွယ်ရသော နေရာများ (ဥပမာ Data Analysis) တွင် အလွယ်တကူပြောင်းပေးနိုင်စေရန် ရည်ရွယ်၍ ဖန်တီးခဲ့ခြင်းဖြစ်သည်။<br><br> 
  Burmese Name Gender Detector ဆိုသည်မှာ AI နည်းပညာဖြင့် မြန်မာနာမည်ကို ယောက်ျား၊ မိန်းမ ခွဲပေးခြင်း ဖြစ်သည်။ Data Analysis ကဲ့သို့သော အပိုင်းတွင် များစွာအထောက်အကူပြုစေနိုင်သည်ဟု ထင်မိ၍ ဖန်တီးခဲ့ခြင်းဖြစ်သည်။<br>
  Burmese Name Meaning Explainer ဆိုသည်မှာ မြန်မာနာမည််တွင် စာလုံးတစ်လုံးစီတိုင်းအတွက် အဓိပ္ပာယ်ကိုယ်စီဖြင့် ဖွဲ့စည်းထားသဖြင့် ယင်းအဓိပ္ပာယ်ကို သိချင်သောသူများ (အထူးသဖြင့် မြန်မာနာမည် လိုအပ်နေသော နိုင်ငံခြားသားများ)  အတွက် များစွာအထောက်အကူပြုစေနိုင်ရန် ရည်ရွယ်၍ ဖန်တီးခဲ့ခြင်းဖြစ်သည်။<br><br>
  စမ်းသပ်သုံးကြည့်ပြီး လိုအပ်သည်များကို အကြံဉာဏ်ပေးနိုင်စေရန်အတွက် Streamlit cloud ပေါ်တွင်တင်ထားပေးပါသည်။<br><br>
  Streamlit Link: https://nama-bayda-ue44squejirjyddmylit3m.streamlit.app/
 <br>Github: https://github.com/Xeyn-X/Nama-Bayda

---

## Methodology

### 1. Burmese Name Generator
 နာမဗေဒ မှ Burmese name generator ကို Traditional method ဖြစ်သော Recurrent Neural Network (RNN) ကိုသုံးပြီး တည်ဆောက်ထားပါသည်။ တည်ဆောက်ပုံအဆင့်ဆင့်မှာ အောက်ပါအတိုင်း ဖြစ်ပြီး Model အား Train ထားသည့် Coding ကိုလည်း Sharing လုပ်ထားပေးပါသည်။<br>
Kaggle: https://www.kaggle.com/code/heinhtetahkarmg/burmese-name-generator

### 1.1. Data Collection
  ခေတ်နှင့်အညီ လှပေသာ နာမည်များ ရရှိစေနိုင်ရန်အတွက် နာမည်များကို မြန်မာနိုင်ငံရှိ တက္ကသိုလ်များမှ ကျောင်းသား၊ ကျောင်းသူများ၏ နာမည်များကို စုဆောင်း၍ စာရင်းပြုစုထားသည်။ လက်ရှိတွင် Data ပေါင်း ၄၀၀၀ ကျော်ခန့် စုဆောင်းထားပါသည်။ Dataset link ကို အောက်တွင်ဖော်ပြထားပါသည်။<br>
Dataset link: https://www.kaggle.com/datasets/heinhtetahkarmg/burmese-name

### 1.2. Data Preprocessing
  မြန်မာစာများသည် အင်္ဂလိပ်စာများကဲ့သို့ Space ခြားပြီးမရေးရသဖြင့် Tokenize လုပ်သောအခါ Character အလိုက် ခွဲလျှင် အက္ခရာတစ်လုံးစီ ပြန့်ကွဲသွားမည်ဖြစ်သည် (ဥပမာ “မြန်မာ” - “မ ြ န ် မ ာ”) ။ထို့ပြင် Character အလိုက် Tokenize လုပ်၍ Model ကို Train သောအခါ Result မကောင်းသောကြောင့် Tokenize လုပ်သည့်အခါ Syllable လုပ်၍ ခွဲရမည်။ Syllable ဆိုသည်မှာ စကားအသံကို လိုက်၍ခွဲခြင်း ဖြစ်သည်။ (ဥပမာ “ကျွန်တော်သည်” ကိုခွဲမည်ဆိုလျှင် “ကျွန် တော် သည်” ဟူ၍ ဖြစ်သည်။ ပထမဦးစွာ အထက်ပါနည်းအတိုင်း Tokenize လုပ်သည်။ [1][2]<br><br>
ထို့နောက် Tokenize လုပ်ထားသော စာလုံးများကို Out of Vocab (OOV) ဟုခေါ်သည့် နည်းလမ်းကိုသုံး၍ Sequence များအဖြစ်သို့ ပြောင်းသည်။ Sequence သို့ပြောင်းရခြင်းမှာ Y အား Predict လုပ်သောအခါ Syllable ပြောင်းထားသော စာလုံးများအတိုင်း ရရှိရန်ဖြစ်သည် (ဥပမာ X = “ကောင်းမြတ်”, Y = “မင်း”)။ ပြောင်းလိုက်သည့် Sequence များကို စာပိုဒ်ကြီးတစ်ခုကဲ့သို့ Concat လုပ်လိုက်ပြီး Model Train ရန် Sequence Length ကို ၁၀ ထားပြီး X နှင့် Y အဖြစ် ခွဲထုတ်လိုက်ပါသည်။ ထို့နောက် ရရှိလာသော X နှင့် Y ကို Sequence မှ One-hot Encoding ပြောင်းပါသည်။ [3][4]

### 1.3. Model Training	
Model တည်ဆောက်ရန်အတွက် Advanced RNN Architecture တစ်ခုဖြစ်သော LSTM ကိုသုံးထားပြီး Flatten Layer တစ်ခု၊  Relu Activation Function ကိုသုံးထားသော Dense Layer တစ်ခုနှင့် Softmax Activation Function ကိုသုံးထားသော Dense Layer တစ်ခုကို သုံးထားပါသည်။ Optimizer အဖြစ် Adam ကိုသုံးထားပြီး Loss တွင် categorical_crossentropy ကိုသုံးထားပါသည်။ထို့နောက် Batch Size အား ၆၄ ထားကာ Epoch အကြိမ်ရေ  ၁၀၀ ဖြင့် Model ကို Train ပါသည်။	 

### 1.4. Result and Evaluation
Accuracy မှာ  ၀.၈ ရရှိပြီး Loss မှာ ၀.၅ ရရှိသဖြင့် Genenrate လုပ်သည့်အခါ Result ကောင်းနိုင်သည့်အတွက် Evaluation အဆင့်သို့ ဆက်လက်လုပ်ဆောင်ပါသည်။<br><br>
Evaluation အဆင့်တွင် ပထမဦးစွာ X ကိုရရှိရန် Concat လုပ်ထားသော Sequence ထဲမှ နာမည်သုံးလုံးကျော်ခန့် အရှည်ရှိသော Sequence အတိုတစ်ခုအား random ယူသည်။  ထို့နောက် ၎င်း X ကိုသုံး၍ Y ကို Predict ပြီး နာမည်အသစ်တစ်ခုကို စတင်ပြုလုပ်ပါသည်။ X ထဲရှိ Enter(\n) အထိကို Predict ပြီးသောအခါ  နာမည်အသစ်တစ်ခုကို  ရရှိပါသည်။<br><br>
	ရရှိလာသော နာမည်များသည် ရလဒ်ကောင်းမွန်သဖြင့် Model အား Keras File Type ဖြင့် Save လိုက်ပါသည်။ ထို့နောက် Streamlit ကိုအသုံပြု၍ User Interface များထည့်သွင်းတည်ဆောက်ပါသည်။ ထို့နောက် ပိုမိုကောင်းမွန်စေရန် Generate ထုတ်မည့်အရေအတွက်နှင့် ကျား၊မ ခွဲထုတ်ပေးသည့် Filter များကိုပါ ဆက်လက်ထည့်သွင်းထားပြီး နာမည်အသစ်များ၏ အဓိပ္ပာယ်များကိုပါ တွဲဖက်၍ ထည့်သွင်းထားသည်။ ကျား၊မ ခွဲပေးသည့် ကဏ္ဍ နှင့် နာမည်များ၏ အဓိပ္ပာယ်ကို ဖော်ပြပေးသော ကဏ္ဍ  တို့ကို အောက်ပိုင်းတွင် အသေးစိတ် ဖော်ပြပေးသွားပါမည်

### 2. Burmese Name Gender Detector
  နာမဗေဒမှ နောက်ထပ်အပိုင်းတစ်ခုဖြစ်သည့် Burmese name gender detector ကိုလည်းပဲ Traditional method ဖြစ်သော Recurrent Neural Network (RNN) ကိုသုံးပြီး တည်ဆောက်ထားပါသည်။ တည်ဆောက်ပုံ အဆင့်ဆင့်မှာ အောက်ပါအတိုင်း ဖြစ်ပြီး Model အား Train ထားသည့် Coding ကိုလည်း Sharing လုပ်ထား ပေးပါသည်။<br>
Kaggle: https://www.kaggle.com/code/heinhtetahkarmg/gender-detection-for-burmese-name

### 2.1. Data Collection
  အထက်တွင်ဖော်ပြခဲ့သော Burmese Name Generator ရှိ Dataset မှ နာမည်များကို ကျား၊မ Column တစ်ခုထပ်တိုး၍ စာရင်းအသစ် ပြန်လည်ပြုစုထားသည်။ Dataset link ကို အောက်တွင်ဖော်ပြထားပါသည်။<br>
Dataset link: https://www.kaggle.com/datasets/heinhtetahkarmg/burmese-name-with-gender

### 2.2. Data Preprocessing
ပထမဦးစွာ Burmese Name Generator တွင်ဖော်ပြခဲ့သည့် နည်းအတိုင်း Syllable အလိုက် Tokenize လုပ်ပြီး training dataset နှင့် testing dataset ဟူ၍ နှစ်ခုခွဲလိုက်သည်။ ထို့နောက် training dataset အတွင်းရှိ Syllable လုပ်ထားသော နာမည်များကို Out of Vocab (OOV) ဟုခေါ်သည့် နည်းလမ်းကိုသုံး၍ Sequence များအဖြစ်သို့ ပြောင်းသည်။

### 2.3. Model Training
  Model တည်ဆောက်ရန်အတွက် Advanced RNN Architecture တစ်ခုဖြစ်သော LSTM ကိုသုံးထားပြီး Flatten Layer တစ်ခု၊  Relu Activation Function ကိုသုံးထားသော Dense Layer နှစ်ခုနှင့် Sigmoid Activation Function ကိုသုံးထားသော Dense Layer တစ်ခုကို သုံးထားပါသည်။ Optimizer အဖြစ် Adam ကိုသုံးထားပြီး Loss တွင် binary_crossentropy ကိုသုံးထားပါသည်။ ထို့နောက် Epoch အကြိမ်ရေ  ၂၀ ဖြင့် Model ကို Train ပါသည်။	

### 2.4. Result and Evaluation
Training Dataset တွင် Accuracy မှာ  ၀.၉၉ ရရှိပြီး Loss မှာ ၀.၀၀၄ ရရှိပြီး Testing Dataset တွင်မူ Accuracy Score မှာ ၉၄.၈%၊ Precision Score မှာ ၉၄.၇%၊ Recall Score မှာ ၉၄.၇%၊ F1 Score မှာ ၉၄.၇% ရရှိပါသည် ။ ထို့နောက် Evaluation အဆင့်သို့ဆက်လက်လုပ်ဆောင်ပါသည်။<br><br>
 ရရှိလာသော ရလဒ်များသည် ကောင်းမွန်သဖြင့် Model အား Keras File Type ဖြင့် Save လိုက်ပါသည်။ ထို့နောက် အထက်တွင်ဖော်ပြခဲ့သော User Interface တွင်ထပ်ပေါင်း ထည့်သွင်းတည်ဆောက်ပါသည်။ 

### 3. Burmese Name Romanizer
  နာမဗေဒမှ နောက်ထပ်အပိုင်းတစ်ခုဖြစ်သည့် Burmese name romanizer ကို AI နည်းပညာကို သုံးရန်မလိုအပ်သဖြင့် Formula ကိုသာ အသုံးပြုခဲ့သည်။  တည်ဆောက်ပုံအဆင့်ဆင့်မှာ အောက်ပါအတိုင်း ဖြစ်သည်။   Coding ကိုလည်း Github ပေါ်တွင် တင်ပေးထားပြီး Link အား Introduction တွင် Sharing လုပ်ထားပေးပါသည်။

### 3.1. Data Collection
အထက်တွင်ဖော်ပြခဲ့သောအပိုင်းမှ OOV သုံးလိုက်သဖြင့် ရရှိလာသော စာလုံး Index များ (ဥပမာ ‘အောင်’၊ ‘စု’၊ စသည်ဖြင့်)ကို CSV File Type အဖြစ် သိမ်းထားပြီး ၎င်း File အား English Romanize Column တစ်ခု ထပ်တိုး၍ စာရင်းအသစ် ပြန်လည်ပြုစုထားသည်။ Dataset ကိုလည်း Github တွင် ထည့်ထားပေးပါသည်။ 
 
### 3.2. Data Preprocessing
ပထမဦးစွာ တချို့မြန်မာနာမည်များသည် Romanize လုပ်သည့်အခါ တဆက်တည်းပေါင်းရေးရသည် (ဥပမာ ‘အာကာ’ ဆိုလျှင် ‘Arkar’ ဟုပေါင်းရေးသည်)။ ထို့ကြောင့် တဆက်တည်းပေါင်းရေးရသည့် နာမည်များကို ထူးခြားနာမည်များအဖြစ် ထပ်မံစရင်းပြုစု၍ CSV File Type အဖြစ် သိမ်းထားသည်။ <br><br>
မြန်မာစာ Unicode တွင် တစ်ချို့စာလုံးများကို ရေးသည့်အခါ ရေးသားနည်း တစ်ခုထက်မက ရှိသည် (ဥပမာ ‘သိမ့်’ ဟူသောစာလုံးတွင် အသတ်(်) ရေးပြီးနောက်တွင်မှ အောက်ကမြစ်(့) ကိုရေးသည့် ပုံစံ နှင့် အောက်ကမြစ်(့) ရေးပြီးနောက်တွင်မှ အသတ်(်) ကိုရေးသည့် ပုံစံ ဟူ၍ရှိသည်) ။ ထိုစာလုံးများကို ပုံသေ တစ်မျိုးတည်း ဖြစ်အောင် ညှိပြီး ပြောင်းရသည်။ထို့နောက် နာမည်များကို Syllable အလိုက် Tokenize ဦးစွာလုပ်ပြီး Romanize လုပ်ပါသည်။အင်္ဂလိပ်မှ ပြောင်းပြန် Romanize လုပ်သည့်အခါ အထက်၌ဖော်ပြခဲ့သော ပုံ ၃.၁(က) မှ Dataset ကို Column အရှေ့အနာက်ပြောင်းပြီး Dataset အသစ်တည်ဆောက်ပါသည်။ ထို့နောက် နာမည်များကို ပြောင်းပြန် Romanize လုပ်ပါသည်။

### 3.3. Integration
  မြန်မာမှအင်္ဂလိပ်၊ အင်္ဂလိပ်မှမြန်မာ ပြောင်းပေးသည့် Filter တစ်ခု ထည့်ထားသည်။ မြန်မာမှအင်္ဂလိပ် သို့ Romanize သည့်အပိုင်းတွင် CSV File ကိုပါ Upload လုပ်ပြီး Romanize နိုင်ပြီး ရရှိလာသောရလဒ်ကိုပင် CSV File အဖြစ် Download ပြီး ကိုယ်ပိုင် Device ထဲသို့ Save ထားနိုင်သည်။ <br><br>
အင်္ဂလိပ်မှမြန်မာသို့ Romanize သည့်အပိုင်းတွင်  တချို့သော နာမည်များသည် စာလုံးများ တူနေသောကြောင့် ဖြစ်နိုင်သော နာမည်များကို ထုတ်ပြပေးထားပါသည် (ဥပမာ ‘San’ ဟူသော နာမည်ကို Romanize လုပ်မည်ဆိုလျှင် ‘စံ’ ၊ ‘စန်း’၊ ‘စမ်း’၊ ‘စန်’၊ ‘စမ်’ ဟူသော ရလဒ်များ ရှိသည်) ။ အင်္ဂလိပ်စာလုံး ကြီး၊သေး Format အား တစ်မျိုးတည်း ဖြစ်အောင် ညှိပြီး ပြောင်းထားသည်။ ထို့နောက် အထက်တွင်ဖော်ပြခဲ့သော User Interface တွင်ထပ်ပေါင်း ထည့်သွင်းတည်ဆောက်ပါသည်။

### 4. Burmese Name Meaning Explainer
  နာမဗေဒမှ နောက်ထပ်အပိုင်းတစ်ခုဖြစ်သည့် Burmese name meaning explainer ကို AI နည်းပညာကို သုံးရန်မလိုအပ်သဖြင့် Formula ကိုသာ အသုံးပြုခဲ့သည်။  တည်ဆောက်ပုံအဆင့်ဆင့်မှာ အောက်ပါအတိုင်း ဖြစ်သည်။   Coding ကိုလည်း Github ပေါ်တွင် တင်ပေးထားပြီး Link အား Introduction တွင် Sharing လုပ်ထားပေးပါသည်။

### 4.1. Data Collection
အထက်တွင်ဖော်ပြခဲ့သောအပိုင်းမှ OOV သုံးလိုက်သဖြင့် ရရှိလာသော စာလုံး Index များ (ဥပမာ ‘အောင်’၊ ‘စု’၊ စသည်ဖြင့်)ကို စာလုံးတစ်ခုစီ၏ အဓိပ္ပာယ်ဖွင့်ပြီး json File Type အဖြစ် သိမ်း၍ စာရင်းပြုစုထားသည်။ json File ကိုလည်း Github တွင် ထည့်ထားပေးပါသည်။

### 4.2. Data Preprocessing and Integration
ပထမဦးစွာ မြန်မာနာမည်ကို Syllable Tokenize လုပ်ရသည်။ တချို့သော မြန်မာနာမည်များသည် တစ်လုံးချင်း၌ အဓိပ္ပာယ်မရှိဘဲ ပေါင်းရေးမှသာ အဓိပ္ပာယ်ဖွင့်၍ ရပါသည် (ဥပမာ ‘ရတနာ’ ဟူ၍ ပေါင်းရေးမှ  ‘Treasure’ ဟူသော အဓိပ္ပာယ်ဖွင့်၍ရသည်)။ ထို့ကြောင့် ပေါင်းရေးရမည့် စာလုံးများနှင့် အဓိပ္ပာယ်များကို Dictionary List အဖြစ် တည်ဆောက်ထားသည်။ ထို့နောက် အထက်တွင်ဖော်ပြခဲ့သော User Interface တွင်ထပ်ပေါင်း ထည့်သွင်းတည်ဆောက်ပါသည်။

---

## Challanges and Limitions

### 1. Challanges
အဓိကအားဖြင့် တွေ့ရသော Challange များမှာ အောက်ပါအတိုင်း ဖြစ်သည်။
1.  Data သည် အားသာချက်ဖြစ်သကဲ့သို့ အားနည်းချက်လဲ ဖြစ်သည်။ Dataset ထဲရှိ နာမည်များသည် Clean မဖြစ်သဖြင့် (ဥပမာ Font မမှန်ခြင်း၊ စာလုံးပေါင်း မမှန်ခြင်း၊ တိုင်းရင်းသား နာမည်များ၊ ရှေးဆန်သော နာမည်များ ပါဝင်မှု များနေသောကြောင့်) ရလဒ်မကောင်းခြင်း၊ ရလဒ်မမှန်ခြင်းများ ဖြစ်စေသည်။ ထို့ကြောင့် Data များကို Clean ဖြစ်အောင် ဦးစွာ စီမံခဲ့ရသည်။ 
2.  နာမည်များကို Random Generate လုပ်သောကဏ္ဍတွင် နာမည်အစအား Word Index မှ Random ယူပြီး Generate သောအခါ နာမည်များ မမှန်သည်ကို ကြုံခဲ့ရသည်။ ထို့ကြောင့် Concat လုပ်ထားသော Sequence ထဲမှ နာမည်သုံးလုံးကျော်ခန့် အရှည်ရှိသော Sequence အတိုတစ်ခုအား Random ယူပြီး Generate လုပ်လိုက်သောအခါမှ နာမည်များ မှန်ကန်ပြီး ရလဒ်ကောင်းများ ရရှိခဲ့သည်။
3.  ကျား၊ မ Data အား တစ်ကြောင်းစီ ထည့်သွင်းရ၍ အချိန်ပေးခဲ့ရသည်။
4.  Save ထားသော Model အား Load လုပ်၍ Predict လုပ်သောအခါ  Model ကို Train သောကဏ္ဍမှ အချို့ Data များကို ပြန်လည်အသုံးချရန် လိုအပ်သည်ကို တွေ့ရသည်။ ထို့ကြောင့် ၎င်းလိုအပ်သော Data များကို pkl File Type ဖြင့် သိမ်းပြီး ပြန်သုံးခဲ့ရသည်။
5.  မြန်မာစာ Unicode တွင် တစ်ချို့စာလုံးများကို ရေးသည့်အခါ ရေးသားနည်း တစ်ခုထက်မက ရှိသဖြင့် ၎င်းတို့ကို ရှာဖွေပြီး ညှိယူခဲ့ရသည်။
6.  အင်္ဂလိပ်မှ မြန်မာသို့ Romanize သည့်အပိုင်းတွင်  တချို့သော နာမည်များသည် စာလုံးများ တူနေသောကြောင့် ဖြစ်နိုင်သော နာမည်များကိုသာ ထုတ်ပြပေးထားပြီး Limitation အဖြစ်သာ သတ်မှတ်လိုက်သည်။
7.  တချို့သော မြန်မာနာမည်များသည် တစ်လုံးချင်း၌ အဓိပ္ပာယ်မရှိဘဲ ပေါင်းရေးမှသာ အဓိပ္ပာယ်ရှိသဖြင့် ၎င်းတို့ကို ရှာဖွေပြီး စီမံခဲ့ရသည်။
8.  တချို့သော မြန်မာနာမည်များသည် အဓိပ္ပာယ် ရေရေရာရာ မရှိဘဲ အလှ သီးသန့်သာဖြစ်သည်။ တစ်ချို့သည်လည်း ပါဠိ၊ အင်္ဂလိပ်၊ ဟိန္ဒူ စသည်မှ ဆွဲယူထားသည်။ ထို့ကြောင့် ထိုနာမည်များကို အဓိပ္ပာယ်ဖွင့်ရာ၌ အခက်အခဲများစွာ ရှိခဲ့သည်။

### 2. Limitations
အဓိကအားဖြင့် တွေ့ရသော Limitation များမှာ အောက်ပါအတိုင်း ဖြစ်သည်။
1.  AI ဆိုသည်မှာ ဖြစ်နိုင်ချေအများဆုံးကို ခန့်မှန်းခြင်းဖြစ်သဖြင့် ၁၀၀% မှန်ကန်သည်ဟူ၍ မရှိပါ။
2.  တိုင်းရင်းသား နာမည်များ၊ ရှေးဆန်သော နာမည်များ ပါဝင်မှု များနေလျှင် ရလဒ်မကောင်းခြင်း၊ ရလဒ်မမှန်ခြင်းများ ဖြစ်စေသည်။
3.  တစ်ချို့နာမည်များသည် ကျား၊ မ နှစ်မျိုးလုံးတွင် သုံးသည့်အတွက် ရလဒ်မမှန်ခြင်းများ ဖြစ်စေသည်။
4.  Romanize လုပ်သည့်အပိုင်းတွင် Formula ကိုသာ သုံးထားသဖြင့် Dataset ထဲ၌မရှိသော နာမည်စာလုံးများ (အထူးသဖြင့် တိုင်းရင်းသားနာမည်များ) ကို Romanize မလုပ်နိုင်ပါ။
5.  အင်္ဂလိပ်မှ မြန်မာသို့ Romanize သည့်အပိုင်းတွင်  တချို့သော နာမည်များသည် စာလုံးများ တူနေသောကြောင့် ဖြစ်နိုင်သော နာမည်များကိုသာ ထုတ်ပြပေးထားသည်။
6.  အဓိပ္ပာယ်ဖွင့်ဆိုပေးသည့် အပိုင်းတွင်လည်း Formula ကိုသာ သုံးထားသဖြင့် Dataset ထဲ၌မရှိသော နာမည်စာလုံးများကို အဓိပ္ပာယ်မဖွင့်ပေးနိုင်ပါ။

---

## Conclusion

  အကျဥ်းချုပ်အားဖြင့် ဆိုရသော် နာမဗေဒသည် မြန်မာနာမည်နှင့်ပတ်သတ်ပြီး လုပ်ဆောင်ချက်များပါရှိပြီး တိုးတက်လာသော AI နည်းပညာ၌ မြန်မာစာ၊ မြန်မာဘာသာစကား၌မူ အားနည်းနေမှုကို ဖြေရှင်းရန် ပထမခြေလှမ်း ဖြစ်သည်။ ထို့အပြင် ရုံးစရင်းအခန်းကဏ္ဍ၊ Data Analysis ကဏ္ဍ များတွင် တစ်နေရာရာ၌ အထောက်အကူ ပေးနိုင်သည်။ NLP အခန်းကဏ္ဍအတွက်တွင်လည်း မြန်မာ Dataset များပေါ်များလာခြင်း၊ မြန်မာစာနှင့် ပတ်သတ်သော အခြေခံများ၊ ထူးခြားချက်များကို Reference ယူနိုင်သည်။ မြန်မာဘာသာဗေဒကို လေ့လာနေသူများ အတွက်လည်း တစ်နည်းနည်းဖြင့် အထောက်အကူ ပေးနိုင်သည်။

### Future Work
နောက်ထပ် ခြေလှမ်းသစ်များအနေဖြင့်  မြန်မာစာ၊ မြန်မာဘာသာစကားကို အခြေခံသော မြန်မာဘာသာပြန်များ (Burmese Translator)၊ စာလုံးပေါင်းသတ်ပုံစစ်ဆေးခြင်း (Spell Checker)၊ စာလုံးများ ကြိုတင်ခန့်မှန်းခြင်း (Text Predition)၊ Burmese Chatbot များ၊ အမုန်းစကားများစစ်ဆေးခြင်း (Hatespeech Detector)၊ စာသားကိုကြည့်ပြီး စိတ်နေစိတ်ထား ခန့်မှန်းခြင်း (Emotional Detector) အစရှိသည်တို့ကို တစ်ခုပြီးတစ်ခု တစ်ဆင့်ပြီးတစ်ဆင့် ဆက်လက် အကောင်အထည်ဖော်သွားရန် ရည်မှန်းထားသည်။ ထို့ပြင် RNN အပြင် အခြားနည်းလမ်းများကိုလည်း လေ့လာအသုံးပြု၍  ဆက်လက် အကောင်အထည်ဖော်သွားပါမည်။

---

## References

1.  Myanmar Syllable https://www.slideshare.net/slideshow/myanmar-syllable-239356703/239356703
2.  myWord: Burmese Syllable Segmentation Tool by Mr. Ye Kyaw Thu https://github.com/ye-kyaw-thu/myWord
3.  Arabic Name Generator with RNN in Keras by Ouassim Adnane https://www.kaggle.com/code/ishivinal/arabic-name-generator/notebook
4.  Indian Baby Names Generator: Text-Processing+RNN by Meet Ranoliya https://www.kaggle.com/code/meemr5/indian-baby-names-generator-text-processing-rnn
5.  Introduction to Recurrent Neural Networks by geeks for geeks https://www.geeksforgeeks.org/introduction-to-recurrent-neural-network/
6.  What is LSTM - Long Short-Term Memory? By geeks for geeks https://www.geeksforgeeks.org/deep-learning-introduction-to-long-short-term-memory/
