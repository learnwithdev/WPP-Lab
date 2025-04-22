import pandas as pd # type: ignore

dt = pd.to_datetime("2012-01-15")
print(dt)
dt_local = dt.tz_localize("Asia/Kolkata")
print(dt_local)
dt_local = dt.tz_localize("Asia/Kolkata").date()
print(dt_local)
dt_present =pd.to_datetime("today").date()
print(dt_present)
tm_present =pd.to_datetime("today").time()
print(tm_present)