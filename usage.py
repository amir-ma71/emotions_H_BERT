from src.HebEMO import *

HebEMO_model = HebEMO()

# HebEMO_model.hebemo(input_path = 'examples/text_example.txt')
# return analyzed pandas.DataFrame
txt = "אתמול כלב תקף, זה היה כל כך נורא שכעסתי על עצמי "
hebEMO_df = HebEMO_model.hebemo(
    text=txt)

print(hebEMO_df)