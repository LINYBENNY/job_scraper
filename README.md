# Techvantage Job Scraper

This Python script **automatically collects job listings** from Techvantage's careers page and **saves them into an Excel file**.

##  What It Does

* Visits TechVantage's careers page
* Extracts details such as:
  * Job Title
  * Location
  * Experience Required
  * Skills Required
  * Job URL
  * Posting Date
  * Salary (if available)
* Saves all information into an Excel file named `Techvantage_Jobs.xlsx`

---

##  Requirements

### ✅ Step 1: Create a virtual environment

```bash
python -m venv venv
```

### ✅ Step 2: Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### ✅ Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

##  How to Use

1. Ensure Python is installed on your system  
2. Open a terminal and navigate to the project folder  
3. Follow the steps in the **Requirements** section to set up the environment  
4. Run the scraper:

```bash
python techvantage_scraper.py
```

If successful, the Excel file `Techvantage_Jobs.xlsx` will be created in the same folder.

---

##  Output

The Excel file includes:

- **JobTitle** – Position name  
- **Location** – Job location  
- **ExperienceRequired** – Years of experience needed  
- **SkillsRequired** – Technical skills extracted from job details  
- **Salary** – Salary information (if specified)  
- **JobURL** – Direct link to the job posting  
- **Date Posted** – When the job was posted  

---

## 💡 Notes

- Scrapes all job listings from the careers page  
- Visits individual job pages to extract detailed skill requirements  
- Implements 1-second delays between requests for respectful scraping  
- If TechVantage updates their website layout, the script may require adjustments  
