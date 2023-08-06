import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv('insurance.csv')
cols_to_encode = ['sex','smoker','region']
df_encoded = pd.get_dummies(data[cols_to_encode],drop_first=True)
df_not_encoded = data.drop(cols_to_encode, axis=1)
final_df = pd.concat([df_encoded,df_not_encoded],axis=1)

y = final_df['charges']
X = final_df.drop('charges',axis=1)
X_scaled = MinMaxScaler().fit_transform(X)
X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.2,random_state=42)

model = LinearRegression().fit(X_train,y_train)
y_preds = model.predict(X_test)
joblib.dump(model2, 'rfr_model.sav')
