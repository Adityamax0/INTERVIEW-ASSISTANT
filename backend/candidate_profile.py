"""
candidate_profile.py

Structured knowledge base about Aditya Pandey.
Fill in each section with real information. Keep it factual —
whatever is here is what the AI is allowed to say, nothing more.
"""

CANDIDATE_PROFILE = {
    "personal_information": {
        "name": "Aditya Pandey",
        "location": "Kanpur, India",
        "email": "adityapandey9326@gmail.com",
        "phone": "+91 63876 87430"
    },

    "professional_summary": (
        "Systems-driven B.Tech student specializing in AI/ML orchestration and "
        "high-throughput pipelines. Deployed robust automation frameworks with a "
        "strong focus on risk mitigation and data analytics. Seeking to leverage "
        "algorithmic logic and process optimization workflows as an Operations "
        "Summer Analyst at Goldman Sachs."
    ),

    "education": [
        {
            "degree": "Bachelor of Technology in Computer Science & Engineering (AI & ML)",
            "institution": "Maharana Institute of Professional Studies (AKTU)",
            "location": "Kanpur, India",
            "year": "Sep 2024 - Jun 2028",
            "details": (
                "Current Cumulative CGPA: 7.20 / 10.00. "
                "Core Coursework: Data Structures, Database Management (DBMS), "
                "Network Security, Data Analytics."
            )
        }
    ],

    "technical_skills": [
        "Python (HackerRank 5-Star Gold Developer)",
        "JavaScript",
        "C++",
        "SQL",
        "Git",
        "GitHub",
        "Multi-Agent Systems",
        "High-Throughput Pipelines",
        "Deep Packet Inspection",
        "Raw Sockets",
        "Scikit-Learn",
        "Random Forest",
        "Predictive Modeling",
        "Pandas",
        "NumPy",
        "Plotly",
        "React.js",
        "Next.js",
        "Node.js",
        "Express",
        "Flask",
        "RESTful APIs",
        "Streamlit"
    ],

    "soft_skills": [
        "Bilingual fluency in English & Hindi",
        "Technical Communication",
        "System Auditing",
        "Risk Management"
    ],

    "projects": [
        {
            "name": "Scholar-Agent Pro (Automated High-Throughput Pipeline)",
            "tech_stack": ["Python", "Groq LLAMA", "Streamlit"],
            "description": (
                "Architected a 12-agent orchestration pipeline that ingests and "
                "processes complex data formats in under 10 seconds. "
                "Re-engineered context-window logic to scale down transaction "
                "tokens from 4,200 to 450, mitigating 100% of rate-limit risks. "
                "Established isolated execution pathways to guarantee absolute "
                "data integrity and clean compliance outputs."
            ),
            "impact": (
                "Cut token usage per transaction by ~89% (4,200 -> 450) and "
                "eliminated rate-limit failures entirely."
            )
        },
        {
            "name": "Deep Packet Inspection Engine (Real-Time Surveillance Engine)",
            "tech_stack": ["Python", "Scapy", "Flask", "Scikit-learn"],
            "description": (
                "Engineered a data surveillance tool utilizing raw byte-level "
                "packet parsing to audit network variables before handshake. "
                "Trained a predictive Random Forest model on 4,150 samples to "
                "isolate operational and security risks across 10+ live streams. "
                "Developed an interactive centralized dashboard to monitor system "
                "health and transaction flows in real-time."
            ),
            "impact": (
                "Model trained on 4,150 samples; monitored risk across 10+ "
                "concurrent live streams in real time."
            )
        },
        {
            "name": "MEMET (\"My Mate\") - AI Emotional Assistant",
            "tech_stack": ["Python", "NLP", "NLTK", "TextBlob", "Vercel"],
            "description": (
                "Built an AI assistant that detects emotional state across 5 "
                "levels using TextBlob-based sentiment analysis, aiming to "
                "respond to a user's underlying state of mind rather than just "
                "their literal words. Live and deployed at memet-lake.vercel.app. "
                "Currently extending it into MEMET v2, adding voice input via "
                "OpenAI Whisper for multi-modal (voice + text) emotion fusion."
            ),
            "impact": "Live deployed application; v2 (multi-modal) ~35% complete."
        },
        {
            "name": "SCAS (Smart Crop Advisory System)",
            "tech_stack": ["Python", "Scikit-learn", "Pandas", "NumPy", "PWA"],
            "description": (
                "Led a 5-developer team to build a full-stack ML platform that "
                "gives farmers data-driven fertilizer/crop recommendations "
                "instead of guesswork, using a Random Forest classifier on soil "
                "parameters (N, P, K, pH, temperature, humidity). Built as an "
                "offline-first Progressive Web App. Originated as a Smart India "
                "Hackathon (SIH) internal team project; architecture is "
                "complete but deployment is currently paused. Published as "
                "research on Zenodo and ResearchGate (see achievements)."
            ),
            "impact": (
                "Random Forest model achieved 95%+ accuracy on crop "
                "recommendation; led a team of 5."
            )
        },
        {
            "name": "LENS (Layout Error Navigation System)",
            "tech_stack": ["Node.js", "Puppeteer", "GitHub Actions", "AST", "CI/CD"],
            "description": (
                "Built a closed-loop visual regression testing framework that "
                "uses Puppeteer and AST transformation trees to automatically "
                "detect UI style regressions inside a GitHub Actions CI/CD "
                "pipeline, without manual QA review."
            ),
            "impact": "Reduced manual QA review time by ~80% across 3+ core UI components."
        },
        {
            "name": "Sentiment-Aware Conversational AI",
            "tech_stack": ["Python", "DialoGPT-medium", "HuggingFace", "PyTorch", "TextBlob"],
            "description": (
                "Built a conversational AI combining 5-level emotion detection "
                "(via TextBlob polarity) with DialoGPT-medium (345M parameters) "
                "for response generation, using recursive memory and "
                "nucleus sampling (top-p=0.9). A real transformer-based "
                "architecture, not keyword matching."
            ),
            "impact": "Functional end-to-end emotion-aware chatbot using a 345M-parameter transformer."
        }
    ],

    "internships": [
        # No formal/corporate internships yet.
    ],

    "experience": [
        {
            "role": "Independent AI Developer",
            "organization": "Self-directed",
            "duration": "Oct 2025 - Present",
            "details": (
                "Designing and building AI/ML systems independently end to "
                "end (Python, Scikit-learn, NLP/HuggingFace, Pandas, NLTK, "
                "Groq) rather than through a formal employer, resulting in "
                "six built projects, three of which are live and deployed."
            )
        },
        {
            "role": "Team Lead",
            "organization": "SIH (Smart India Hackathon) Internal Hackathon",
            "duration": "Sep 2025",
            "details": (
                "Led a 5-developer team to design and build SCAS (Smart Crop "
                "Advisory System), an agriculture advisory platform, during "
                "an internal college hackathon."
            )
        }
    ],

    "certifications": [
        "NPTEL Elite Certification: The Joy of Computing using Python (IIT Madras) "
        "- 83% Score (Verification: NPTEL26CS84S450300133)",
        "HackerRank Python Developer - 5-Star Gold Badge in advanced algorithmic "
        "problem solving"
    ],

    "achievements": [
        "HackerRank 5-Star Gold Developer in Python",
        "NPTEL Elite Certification (83% score) from IIT Madras",
        "Led team to win an SIH (Smart India Hackathon) internal college "
        "hackathon (Sep 2025) with SCAS, a Random Forest crop-advisory "
        "system achieving 95%+ accuracy",
        "Published research paper 'Smart Crop Advisory using Machine "
        "Learning' on Zenodo (Open Access, CC BY 4.0, DOI: "
        "10.5281/zenodo.17779600)",
        "Published extended research preprint on ResearchGate covering the "
        "full-stack SCAS platform (DOI: 10.13140/RG.2.2.30686.60485)"
    ],

    "strengths": [
        "Strong systems and automation orchestration skills (multi-agent pipelines)",
        "Practical experience with network-level programming and security auditing",
        "Comfortable across the full stack: ML/data (Scikit-Learn, Pandas) to web (React/Next.js/Node.js)"
    ],

    "areas_for_improvement": [
        "Hesitation - can be slow to commit to a decision or speak up in the "
        "moment, and is actively working on trusting his judgment faster.",
        "Communication - still developing his ability to explain technical "
        "work clearly and confidently to a non-technical audience, and is "
        "consciously practicing this.",
        "No formal/corporate internship experience yet - his experience so "
        "far comes from independent projects and one internal college "
        "hackathon rather than an employer setting."
    ],

    "career_goals": (
        "Seeking to apply algorithmic thinking and process optimization as an "
        "Operations Summer Analyst at Goldman Sachs, and grow further in "
        "AI/ML-driven systems and automation engineering."
    ),

    "preferred_roles": [
        "Operations Summer Analyst",
        "AI/ML Engineer",
        "Backend / Systems Engineer"
    ],

    "portfolio": (
        "adityapandeyportfolio-tau.vercel.app - a single-page developer "
        "portfolio showcasing 6 built projects (3 live and deployed: "
        "MEMET, Scholar-Agent Pro, and SCAS's earlier build), skill "
        "proficiency breakdowns, a career journey timeline from Sep 2024 "
        "to present, published research, and links to GitHub, LinkedIn, "
        "Zenodo, ResearchGate, LeetCode, and HackerRank. Tagline: "
        "'Building systems that actually understand humans - not just "
        "their words, but their intent, emotion, and context.'"
    ),
    "github": "github.com/Adityamax0",
    "linkedin": "linkedin.com/in/aditya-pandey-ai-ml",
    "resume": "adityapandey.pdf",
    "other_links": {
        "leetcode": "leetcode.com/adityapandey9326",
        "zenodo": "Published research, DOI 10.5281/zenodo.17779600",
        "researchgate": "Academic profile, DOI 10.13140/RG.2.2.30686.60485",
        "live_apps": {
            "MEMET": "memet-lake.vercel.app",
            "Scholar-Agent Pro": "live, deployed via Streamlit",
            "SCAS (earlier build)": "v0-smart-crop-advisory (deployment currently paused)"
        }
    },

    "faq": [
        {
            "question": "Why should we hire you?",
            "answer": (
                "I don't just study AI/ML in theory - I've built and shipped "
                "six real systems on my own, three of which are live in "
                "production, covering the full stack from raw network "
                "packet parsing to multi-agent LLM pipelines to full ML "
                "platforms. I'm comfortable owning a problem end to end "
                "rather than just contributing to one piece of it, and I "
                "back that up with published research, not just code."
            )
        },
        {
            "question": "Why do you want an Operations Summer Analyst role at Goldman Sachs?",
            "answer": (
                "My project work has consistently been about turning messy, "
                "high-volume processes into reliable, auditable systems - "
                "cutting token costs by 89% in one pipeline, eliminating "
                "rate-limit failures, building risk-classification models. "
                "That's fundamentally the same skill set Operations needs: "
                "process optimization, risk mitigation, and data-driven "
                "decision-making at scale, which is what draws me to the role."
            )
        },
        {
            "question": "What is your biggest weakness?",
            "answer": (
                "Hesitation - I can be slow to commit to a decision or speak "
                "up in the moment. I'm actively working on trusting my "
                "judgment and communicating it faster and more clearly, "
                "especially to non-technical audiences."
            )
        },
        {
            "question": "You don't have any internships - how do we know you can work in a real environment?",
            "answer": (
                "That's fair, I don't have a corporate internship yet. But I "
                "led a 5-developer team to win an internal Smart India "
                "Hackathon, and I've independently designed, built, and "
                "deployed six production-style projects since October 2025 - "
                "including managing scope, technical tradeoffs, and shipping "
                "under real constraints, just without a formal employer "
                "environment around it."
            )
        },
        {
            "question": "Tell me about a project you're most proud of.",
            "answer": (
                "Scholar-Agent Pro - a 12-agent AI pipeline that breaks down "
                "academic PDFs in under 10 seconds. The technically hardest "
                "part wasn't the agent orchestration itself, it was "
                "re-engineering the context-window logic to cut token usage "
                "per transaction from 4,200 to 450, which eliminated "
                "rate-limit failures entirely rather than just reducing them."
            )
        },
        {
            "question": "What are you working on right now?",
            "answer": (
                "MEMET v2 - extending my emotion-detection assistant to "
                "multi-modal input by fusing voice (via OpenAI Whisper) with "
                "text, so it can read tone as well as words. It's about 35% "
                "complete right now."
            )
        }
    ]
}
