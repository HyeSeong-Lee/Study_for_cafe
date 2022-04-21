"""
매개변수 설명
1. df: DataFrame (type:pd.DataFrame)
2. variable: variable that includes both feature and target.(type: list)
3. augmentation_size: how many data you want to make (type: int)

주의사항
variable에 feature와 target을 넣되, 
feature의 경우 무조건 numerical data여야하고,
target과 상관계수가 충분해야함.
"""
def data_augmentation(df,variable, augmentation_size):
  to_arg=df.sample(n=augmentation_size)
  to_arg.reset_index(drop=False,inplace=True)
  to_arg=to_arg[variable]
  to_arg2=to_arg.corr().to_numpy()
  m=to_arg.mean().to_numpy()
  sigma=to_arg.cov().to_numpy()
  w,v=np.linalg.eig(sigma)
  dic={}
  for i in range(len(w)):
    dic[w[i]]=v[:,i]
  items=sorted(dic.items(),key=lambda x: -x[0])
  A=np.array([[0]*len(items) for i in range(len(items))])
  U=np.array([[0]*len(items) for i in range(len(items))])
  for i in range(len(A)):
    A[i][i]=items[i][0]
  U=[[] for i in range(len(A))]
  for i in range(len(A)):
    for j in range(len(A)):
      U[j].append(items[i][1][j])
  U=np.array(U)
  x=to_arg.to_numpy()
  q=project_vector(U,x)
  q=pd.DataFrame(q)
  mq=q.mean().to_numpy()
  vq=np.array([0 for i in range(len(A))])
  for i in range(len(A)):
    vq[i]=A[i][i]
  q2=np.random.normal(mq,vq,4)
  x2=q2*U.T
  x_aug=np.concatenate((x,x2))
  return x_aug
