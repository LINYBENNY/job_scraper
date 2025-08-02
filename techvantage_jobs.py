import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time

def scrape_job_details(job_url, headers):
    try:
        response = requests.get(job_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        skills = []
        blog_section = soup.find('section', id='blog')
        if blog_section:
            all_text = blog_section.get_text()
            
            # Find skills section
            if 'Requirements:' in all_text or 'skills' in all_text.lower():
                all_li = blog_section.find_all('li')
                for li in all_li:
                    skills.append(li.text.strip())
        
        return ', '.join(skills[:5]) if skills else 'N/A'
    except:
        return 'N/A'

def scrape_techvantage_jobs():
    base_url = "https://www.techvantagesystems.com/careers/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    all_jobs = []
    
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    job_listings = soup.find_all('div', class_='job-listing')
    
    for job in job_listings:
        job_data = {
            'JobTitle': 'N/A',
            'Location': 'N/A',
            'ExperienceRequired': 'N/A',
            'SkillsRequired': 'N/A',
            'Salary': 'N/A',
            'JobURL': 'N/A',
            'Date Posted': 'N/A'
        }
        
        # Extract all text content from the job listing
        all_text = job.get_text(separator='|', strip=True)
        parts = all_text.split('|')
        
        # Title
        title_elem = job.find('h4', class_='job__title')
        if title_elem and title_elem.find('a'):
            job_data['JobTitle'] = title_elem.find('a').text.strip()
            job_data['JobURL'] = urljoin(base_url, title_elem.find('a')['href'])
        
        # Experience
        for part in parts:
            if 'years' in part.lower():
                job_data['ExperienceRequired'] = part.strip()
        
        # Location
        for part in parts:
            if 'Trivandrum' in part or 'Kerala' in part:
                job_data['Location'] = part.strip()
        
        # Posted date
        for i, part in enumerate(parts):
            if 'Posted on' in part and i + 1 < len(parts):
                job_data['Date Posted'] = f" {parts[i + 1].strip()}"
        
        # Fetch skills from job page
        if job_data['JobURL'] != 'N/A':
            job_data['SkillsRequired'] = scrape_job_details(job_data['JobURL'], headers)
            time.sleep(1)
        
        all_jobs.append(job_data)
    
    df = pd.DataFrame(all_jobs)
    df.to_excel('Techvantage_Jobs.xlsx', index=False, engine='openpyxl')
    
    print(f"Scraped {len(all_jobs)} jobs")
    return all_jobs

if __name__ == "__main__":
    scrape_techvantage_jobs()