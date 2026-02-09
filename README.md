# FUTURE_ML_03

# Resume Screening & Ranking System
## Automated Resume Processing from Kaggle Datasets

This notebook automatically loads and processes resumes from:
- **Resume Dataset** (CSV format)
- **Job Description Dataset** (CSV format)
- **PDF/TXT files** (optional)

---

### Data Loading:
1. **Automatic CSV Loading**: Reads Kaggle resume dataset directly
2. **PDF Support**: Can extract text from PDF resumes
3. **TXT Support**: Can read plain text resume files
4. **Flexible Format**: Adapts to different column names in datasets

### Text Processing:
1. **Cleaning**: Removes URLs, emails, phone numbers, special characters
2. **Normalization**: Converts to lowercase, removes extra spaces
3. **Stopword Removal**: Filters common words using NLTK

### Skill Extraction:
1. **Pattern Matching**: Uses regex to find skills in text
2. **Skill Database**: 150+ predefined technical and soft skills
3. **Variation Handling**: Recognizes different forms (e.g., sklearn = scikit-learn)

### Scoring Algorithm:

**Text Similarity (30%):**
- TF-IDF vectorization of resume and job description
- Cosine similarity calculation
- Measures overall content alignment

**Skill Match (70%):**
- Direct comparison of extracted skills
- Percentage of required skills present
- Identifies gaps in candidate profile

**Final Score:**
```
Final = (0.3 × Text_Sim) + (0.7 × Skill_Match)
```

### Why Candidates Rank Higher:
1. **More matching skills** with job requirements
2. **Similar terminology** to job description
3. **Relevant experience** mentioned in resume
4. **Technical depth** in required areas

### Interpreting Results:
- **70-100%**: Excellent fit, strong candidate
- **50-70%**: Good fit, worth interviewing
- **30-50%**: Moderate fit, consider other factors
- **0-30%**: Poor fit, likely not suitable

### Missing Skills Analysis:
- Shows specific skill gaps
- Guides interview questions
- Identifies training needs
- Helps set realistic expectations

---

This system provides data-driven insights to support hiring decisions, but should always be combined with human judgment and other assessment methods.


## Next Steps

### To Use This System:

1. **Download Datasets**:
   - Resume Dataset: https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset
   - Job Dataset: https://www.kaggle.com/datasets/PromptCloudHQ/us-jobs-on-monstercom

2. **Update Configuration** (Step 3):
   - Set correct paths to your CSV files
   - Adjust scoring weights if needed

3. **Run All Cells**:
   - Click Cell → Run All
   - Or run cells sequentially with Shift+Enter

4. **Review Results**:
   - Check rankings and scores
   - Analyze skill gaps
   - Export to CSV for further analysis

### Customization Options:

- **Add more skills**: Update SKILL_DATABASE in Step 4
- **Change weights**: Modify CONFIG in Step 3
- **Filter by category**: Add filtering in Step 11
- **Adjust top N**: Change CONFIG['top_n_candidates']

### Troubleshooting:

- **CSV not found**: Check file paths in CONFIG
- **No skills extracted**: Verify skill database covers your domain
- **Low scores overall**: May need to adjust skill database or weights
- **PDF not working**: Install PyPDF2 (`pip install PyPDF2`)

---
