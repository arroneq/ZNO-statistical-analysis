import SA
import UI

df = UI.loading_data()
subject, label = UI.choosing_subject()

cleaned_df = SA.data_cleaning(df,subject,label)

while True:
    section = UI.choosing_section()
    if (section == "Initial data histogram"): 
        SA.initial_data_histogram(section,label,subject,cleaned_df)
    if (section == "Chi-squared homogeneity hypothesis"): 
        SA.homogeneity_hypothesis(section,label,subject,cleaned_df)
    if (section == "Confidence interval"): 
        SA.confidence_interval(section,label,subject,cleaned_df)