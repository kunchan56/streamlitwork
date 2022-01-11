from pickle import TRUE
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
      latest_iteration.text(f'Iteration {i+1}')
      bar.progress(i+1)
      time.sleep(0.1)
'Done!!!'
st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40],
})

st.write(df)

st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

"""
# 章

## 節

### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df1 = pd.DataFrame(
   np.random.rand(20,3),
   columns=['a','b','c']
)

st.line_chart(df1)

st.area_chart(df1)

st.bar_chart(df1)

df2 = pd.DataFrame(
  np.random.rand(100,2)/[50,50]+[35.69,139.70],
  columns=['lat','lon']
)

st.map(df2)

st.write('Display Image')

# if st.checkbox('Show Image'):
#   img = Image.open('night-view.jpg')
#   st.image(img,caption='night-view',use_column_width=TRUE)

option = st.selectbox(
  '好きな数字を教えろ。',list(range(1,11))
)

'あなたの好きな数字は、', option, 'だね'

st.write('Interactive Widgets')


# option = st.sidebar.text_input('あなたの趣味はなに？')
# cond = st.sidebar.slider('調子はどうですか？', 0, 100,50)

# 'あなたの趣味：', option
# 'あなたの調子：', cond

left_column, right_column = st.columns(2)
leftbtn = left_column.button('右カラムに文字を表示')
if leftbtn:
      right_column.write('ボタン押した？')

exp1 = st.expander('問合せ１')
exp1.write('問合せ1の解答')
exp2 = st.expander('問合せ2')
exp2.write('問合せ2の解答')

