"""Supporting check for the proposed Week 4 corrections: Q10 Part D replay with adjustments signed from running_balance.
Usage: python3 -I q10_replay_signed_adjustments_check.py <repository root>   (reads week-02/reports/week_02/merged)"""
import pandas as pd, numpy as np, sys
M=sys.argv[1]+"/week-02/reports/week_02/merged/"
L=pd.read_csv(M+"stock_ledger_enriched.csv",low_memory=False,parse_dates=["movement_date"])
I=pd.read_csv(M+"inventory_with_ledger.csv"); K=["product_id","branch_id"]
ix=I.set_index(K)
L["file_order"]=np.arange(len(L))
Lf=L.sort_values(K+["file_order"]).copy()
Lf=Lf.merge(I[K+["opening_stock"]],on=K)
Lf["prev"]=Lf.groupby(K).running_balance.shift(); fst=Lf.groupby(K).cumcount()==0
Lf["prev"]=np.where(fst,Lf.opening_stock,Lf.prev); Lf["step"]=Lf.running_balance-Lf.prev
Lf["sgn_signed"]=np.where(Lf.movement_type=="ADJUSTMENT",np.sign(Lf.step),Lf.movement_type.map({"IN":1,"OUT":-1}))
Lf["sgn_pos"]=Lf.movement_type.map({"IN":1,"OUT":-1,"ADJUSTMENT":1})
Lq=L.sort_values(K+["movement_date","movement_id"]).copy()  # Q10 ordering
Lq["sgn_pos"]=Lq.movement_type.map({"IN":1,"OUT":-1,"ADJUSTMENT":1})
def replay(df,sgncol,k):
    r=[];between=0
    for (p,b),x in df.groupby(K):
        q=np.where(x.movement_type=="IN",x.quantity/k,x.quantity)*x[sgncol].values
        bal=ix.opening_stock[(p,b)]+np.cumsum(q)
        r.append((bal.mean(),(bal<0).mean(),(bal>ix.max_stock[(p,b)]).mean()))
        between+= (0<=bal[-1]<=ix.max_stock[(p,b)])
    r=np.array(r).mean(0); return r[0],r[1],r[2],between
ratio=L[L.movement_type=="IN"].quantity.sum()/L[L.movement_type=="OUT"].quantity.sum()
rows=[]
for k in (1,10,15,ratio,20):
    for nm,df,col in [("Week 4 method (date+movement_id order, adjustments +)",Lq,"sgn_pos"),("file order, adjustments +",Lf,"sgn_pos"),("file order, adjustments signed from running_balance",Lf,"sgn_signed")]:
        a,b,c,btw=replay(df,col,k); rows.append(dict(k=round(k,2),method=nm,avg_balance=round(a),below_zero=round(b,4),above_max=round(c,4),pairs_end_between_0_and_max=int(btw)))
print(pd.DataFrame(rows).to_string(index=False))
