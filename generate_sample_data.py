"""
Sample Data Generator for Resume Screening System
==================================================

Use this if you don't have Kaggle datasets yet.
Generates realistic sample resumes and job descriptions for testing.

Usage:
    python generate_sample_data.py
"""

import pandas as pd
import os

# Sample resumes by category
SAMPLE_RESUMES = {
    "Data Science": [
        """
        SARAH JOHNSON
        Data Scientist | Machine Learning Engineer
        sarah.johnson@email.com | San Francisco, CA
        
        PROFESSIONAL SUMMARY
        Experienced Data Scientist with 6+ years in machine learning, deep learning, and statistical analysis.
        Expert in Python, TensorFlow, and cloud deployment.
        
        WORK EXPERIENCE
        Senior Data Scientist, TechCorp Inc. (2020-Present)
        - Developed deep learning models using TensorFlow and PyTorch for image classification
        - Built end-to-end ML pipelines on AWS using Docker and Kubernetes
        - Performed data analysis with Pandas, NumPy, and Matplotlib
        - Led team of 5 data scientists and improved model accuracy by 30%
        - Implemented A/B testing framework for model validation
        
        Data Scientist, Analytics Solutions (2018-2020)
        - Created predictive models using scikit-learn for customer churn prediction
        - Conducted statistical analysis and hypothesis testing
        - Built interactive dashboards with Tableau and Plotly
        - Mentored junior data scientists
        
        EDUCATION
        M.S. Computer Science, Stanford University (2018)
        B.S. Mathematics, UC Berkeley (2016)
        
        TECHNICAL SKILLS
        Languages: Python, R, SQL, Java
        ML/DL: TensorFlow, PyTorch, Keras, scikit-learn, XGBoost, LightGBM
        Data: Pandas, NumPy, SciPy, Matplotlib, Seaborn
        Cloud: AWS (SageMaker, EC2, S3), Docker, Kubernetes
        Big Data: Spark, Hadoop, Kafka, Airflow
        Tools: Git, Jupyter, MLflow, DVC
        
        CERTIFICATIONS
        - AWS Certified Machine Learning - Specialty
        - TensorFlow Developer Certificate
        
        PUBLICATIONS
        - "Deep Learning for Time Series Forecasting" - KDD 2022
        - "Scalable ML Pipelines" - MLSys 2021
        """,
        
        """
        MICHAEL CHEN
        ML Engineer | AI Researcher
        
        EXPERIENCE
        Machine Learning Engineer, AI Labs (2019-Present)
        - Design and deploy NLP models for text classification using BERT and GPT
        - Build recommendation systems with collaborative filtering and neural networks
        - Implement MLOps practices with Kubernetes and MLflow
        - Work with large-scale datasets using Spark and distributed training
        - Deploy models on GCP and AWS
        
        Research Scientist Intern, Google AI (Summer 2019)
        - Developed novel neural network architectures for computer vision
        - Published paper at CVPR conference
        
        EDUCATION
        Ph.D. Machine Learning, MIT (2019)
        M.S. Computer Science, Carnegie Mellon (2016)
        
        SKILLS
        Python, TensorFlow, PyTorch, scikit-learn, NLP, Computer Vision,
        Deep Learning, Neural Networks, Pandas, NumPy, AWS, GCP, Docker,
        Kubernetes, Spark, Research, Leadership
        """,
        
        """
        EMILY RODRIGUEZ
        Junior Data Scientist
        
        EDUCATION
        B.S. Data Science, UC Berkeley (2022)
        GPA: 3.8/4.0
        
        RELEVANT PROJECTS
        Customer Segmentation Analysis
        - Performed clustering using scikit-learn K-means
        - Analyzed results with Pandas and visualized with Matplotlib
        - Achieved 85% accuracy in customer classification
        
        Image Classification System
        - Built CNN model with TensorFlow (90% accuracy)
        - Used data augmentation and transfer learning
        - Deployed on AWS using Flask API
        
        INTERNSHIP
        Data Science Intern, StartupXYZ (Summer 2021)
        - Performed exploratory data analysis on customer data
        - Built predictive models with Python and scikit-learn
        - Created visualizations and reports for stakeholders
        
        SKILLS
        Python, SQL, TensorFlow, scikit-learn, Pandas, NumPy,
        Matplotlib, Seaborn, Git, Jupyter, Machine Learning,
        Data Analysis, Statistics
        
        CERTIFICATIONS
        - Google Data Analytics Professional Certificate
        - AWS Cloud Practitioner
        """
    ],
    
    "Web Development": [
        """
        ALEX THOMPSON
        Full-Stack Developer
        
        EXPERIENCE
        Senior Full-Stack Developer, WebTech Solutions (2019-Present)
        - Built responsive web applications using React, Redux, and TypeScript
        - Developed RESTful APIs with Node.js and Express
        - Implemented CI/CD pipelines using Jenkins and Docker
        - Worked with MongoDB, PostgreSQL, and Redis
        - Led agile scrum team of 6 developers
        
        Web Developer, Digital Agency (2017-2019)
        - Created frontend applications with React and Vue.js
        - Built backend services with Django and Flask
        - Integrated third-party APIs and payment systems
        
        EDUCATION
        B.S. Computer Science, MIT (2017)
        
        SKILLS
        JavaScript, TypeScript, Python, React, Node.js, Express,
        Vue.js, Angular, Django, Flask, HTML, CSS, MongoDB,
        PostgreSQL, Redis, Docker, Kubernetes, AWS, Git,
        Agile, REST API, GraphQL
        """,
        
        """
        JESSICA PARK
        Frontend Developer
        
        WORK HISTORY
        Frontend Developer, TechStart Inc. (2020-Present)
        - Develop user interfaces with React and modern JavaScript
        - Implement responsive designs using CSS and Bootstrap
        - Collaborate with designers using Figma and Sketch
        - Write unit tests with Jest and React Testing Library
        
        Junior Developer, WebCo (2019-2020)
        - Built websites using HTML, CSS, and JavaScript
        - Used jQuery and Bootstrap for rapid development
        - Maintained WordPress sites for clients
        
        EDUCATION
        B.A. Web Design, NYU (2019)
        
        SKILLS
        JavaScript, React, HTML, CSS, Bootstrap, Tailwind,
        jQuery, Git, Figma, Responsive Design, UI/UX,
        Jest, Agile
        """
    ],
    
    "Java Developer": [
        """
        ROBERT WILLIAMS
        Senior Java Developer
        
        EXPERIENCE
        Senior Java Developer, Enterprise Solutions (2017-Present)
        - Design and develop enterprise applications using Java and Spring Boot
        - Build microservices architecture with Docker and Kubernetes
        - Implement RESTful APIs and integrate with databases
        - Work with Oracle, MySQL, and MongoDB
        - Lead code reviews and mentor junior developers
        
        Java Developer, FinTech Corp (2015-2017)
        - Developed banking applications using Java EE
        - Worked with Hibernate ORM and Spring Framework
        - Implemented security features and compliance requirements
        
        EDUCATION
        B.S. Computer Science, Stanford (2015)
        
        SKILLS
        Java, Spring Boot, Spring Framework, Hibernate, Maven, Gradle,
        JUnit, Mockito, Oracle, MySQL, MongoDB, Docker, Kubernetes,
        Microservices, REST API, Git, Jenkins, Agile
        """
    ],
    
    "DevOps Engineer": [
        """
        DAVID KIM
        DevOps Engineer
        
        PROFESSIONAL EXPERIENCE
        Senior DevOps Engineer, CloudNative Inc. (2018-Present)
        - Designed and maintained AWS infrastructure using Terraform
        - Built CI/CD pipelines with GitLab and Jenkins
        - Managed Kubernetes clusters for containerized applications
        - Implemented monitoring with Prometheus, Grafana, and ELK stack
        - Automated deployment processes with Ansible and Python scripts
        
        DevOps Engineer, TechOps (2016-2018)
        - Maintained Linux servers and Docker containers
        - Created automation scripts in Bash and Python
        - Set up monitoring and alerting systems
        
        EDUCATION
        B.S. Information Technology, Georgia Tech (2016)
        
        SKILLS
        AWS, Azure, Docker, Kubernetes, Terraform, Ansible,
        Jenkins, GitLab CI, Python, Bash, Linux, Nginx, Apache,
        Prometheus, Grafana, ELK Stack, Git, CI/CD, Monitoring
        """
    ]
}

# Sample job descriptions
SAMPLE_JOBS = [
    {
        "job_title": "Senior Machine Learning Engineer",
        "job_description": """
        We are seeking an experienced Senior Machine Learning Engineer to join our AI team.
        
        RESPONSIBILITIES:
        - Design and implement ML models using TensorFlow and PyTorch
        - Build deep learning architectures for NLP and computer vision
        - Develop MLOps pipelines for model deployment and monitoring
        - Work with large-scale datasets using Pandas, NumPy, and Spark
        - Deploy models on AWS using Docker and Kubernetes
        - Collaborate with data scientists and engineers
        - Conduct A/B testing and statistical analysis
        - Mentor junior team members
        
        REQUIRED QUALIFICATIONS:
        - 5+ years experience in machine learning or data science
        - Strong Python programming skills
        - Expert knowledge of TensorFlow, PyTorch, or Keras
        - Experience with deep learning and neural networks
        - Proficiency in Pandas, NumPy, SciPy, scikit-learn
        - Experience deploying ML models to production
        - Knowledge of AWS, GCP, or Azure cloud platforms
        - Strong understanding of statistics and mathematics
        - Experience with Git version control
        - Excellent problem-solving and analytical skills
        
        PREFERRED:
        - Experience with Docker and Kubernetes
        - Knowledge of Spark, Kafka, or Airflow
        - Familiarity with NLP or computer vision
        - Master's or Ph.D. in Computer Science or related field
        - Publications in ML conferences
        - Strong communication and leadership skills
        """,
        "organization": "TechCorp Inc.",
        "location": "San Francisco, CA"
    },
    {
        "job_title": "Full-Stack Developer",
        "job_description": """
        Looking for a talented Full-Stack Developer to build modern web applications.
        
        RESPONSIBILITIES:
        - Develop responsive web applications using React and Node.js
        - Build RESTful APIs and microservices
        - Work with MongoDB and PostgreSQL databases
        - Implement CI/CD pipelines
        - Collaborate in agile teams
        
        REQUIREMENTS:
        - 3+ years of web development experience
        - Strong JavaScript/TypeScript skills
        - Experience with React, Node.js, Express
        - Knowledge of HTML, CSS, and responsive design
        - Database experience (MongoDB, PostgreSQL)
        - Git version control
        - Agile methodology
        
        NICE TO HAVE:
        - Docker and Kubernetes
        - AWS or cloud platform experience
        - Vue.js or Angular
        """,
        "organization": "WebTech Solutions",
        "location": "New York, NY"
    },
    {
        "job_title": "Data Analyst",
        "job_description": """
        Seeking a Data Analyst to derive insights from data and support decision-making.
        
        RESPONSIBILITIES:
        - Analyze large datasets using SQL and Python
        - Create reports and dashboards with Tableau
        - Perform statistical analysis
        - Present findings to stakeholders
        
        REQUIREMENTS:
        - 2+ years of data analysis experience
        - Strong SQL skills
        - Python or R for analysis
        - Excel and data visualization tools
        - Statistical analysis knowledge
        - Communication skills
        """,
        "organization": "Analytics Corp",
        "location": "Boston, MA"
    }
]


def generate_sample_data(output_dir='data'):
    """
    Generate sample CSV files for testing.
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate resume dataset
    resume_records = []
    for category, resumes in SAMPLE_RESUMES.items():
        for i, resume_text in enumerate(resumes):
            resume_records.append({
                'Category': category,
                'Resume': resume_text.strip()
            })
    
    resume_df = pd.DataFrame(resume_records)
    resume_file = os.path.join(output_dir, 'Resume.csv')
    resume_df.to_csv(resume_file, index=False)
    print(f"✓ Generated {len(resume_df)} resumes → {resume_file}")
    
    # Generate job description dataset
    job_df = pd.DataFrame(SAMPLE_JOBS)
    job_file = os.path.join(output_dir, 'monster_com-job_sample.csv')
    job_df.to_csv(job_file, index=False)
    print(f"✓ Generated {len(job_df)} job descriptions → {job_file}")
    
    print(f"\n✅ Sample data generated successfully!")
    print(f"   Location: {output_dir}/")
    print(f"   Files: Resume.csv, monster_com-job_sample.csv")
    print(f"\nYou can now run the notebook with this sample data!")


if __name__ == "__main__":
    print("Generating sample data for testing...\n")
    generate_sample_data()
