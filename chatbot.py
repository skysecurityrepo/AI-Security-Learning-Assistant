# ============================================================
# AI Security Learning Assistant - Version 1
# Author: Sandeep Yadav
#
# Description:
# This is a simple Rule-Based Chatbot built using Python.
# It demonstrates how traditional chatbots work before
# moving to NLP, Machine Learning, LLMs, RAG, and Agentic AI.
#
# Key Features:
# - Accepts user input
# - Matches input against predefined patterns
# - Returns predefined responses
# - Includes AI and Cyber Security knowledge
# - Provides a help menu
# - Handles unknown questions gracefully
#
# Future Enhancements:
# - NLP Intent Detection
# - OpenAI Integration
# - RAG Implementation
# - Agentic AI Features
# ============================================================

# ============================================================
# RESPONSE DICTIONARY
# ============================================================
# This dictionary acts as the chatbot's knowledge base.
# Keys = User Questions
# Values = Chatbot Responses
# ============================================================

responses = {

    # Basic Greetings
    "hello":
    "Hello! Welcome to the AI Security Learning Assistant.",

    "hi":
    "Hi there! How can I help you today?",

    "how are you":
    "I'm functioning as expected and ready to discuss AI and Cyber Security.",

    "what is your name":
    "I am AI Security Learning Assistant Version 1.",

    "what can you do":
    """I can help explain:

- Artificial Intelligence (AI)
- Machine Learning (ML)
- Generative AI
- Large Language Models (LLMs)
- Retrieval Augmented Generation (RAG)
- Model Context Protocol (MCP)
- Agentic AI
- AI Security Controls
- OWASP LLM Top 10
- Threat Modeling
- STRIDE
- MITRE ATLAS
- NIST AI RMF
""",

    # ========================================================
    # AI FUNDAMENTALS
    # ========================================================

    "what is ai":
    """Artificial Intelligence (AI) is the capability of machines
to simulate human intelligence such as learning, reasoning,
problem solving, decision making, and understanding language.""",

    "what is machine learning":
    """Machine Learning (ML) is a subset of AI that enables
systems to learn patterns from data and make predictions
without being explicitly programmed.""",

    "what is ml":
    """Machine Learning (ML) is a subset of AI that enables
systems to learn patterns from data and make predictions
without being explicitly programmed.""",

    "what is deep learning":
    """Deep Learning is a subset of Machine Learning that uses
multi-layer neural networks to learn complex patterns from data.""",

    "what is generative ai":
    """Generative AI is a type of AI capable of generating
new content such as text, images, videos, audio, and code
based on learned patterns.""",

    "what is llm":
    """Large Language Models (LLMs) are AI models trained on
massive datasets that can understand and generate
human-like language.""",

    "what is rag":
    """Retrieval Augmented Generation (RAG) combines
an LLM with external knowledge sources.

Flow:
User Question
     ↓
Document Retrieval
     ↓
Relevant Context
     ↓
LLM Response

This improves accuracy and reduces hallucinations.""",

    "what is mcp":
    """Model Context Protocol (MCP) is an open standard that
allows AI models to securely communicate with external tools,
applications, databases, APIs, and services.""",

    "what is agentic ai":
    """Agentic AI refers to AI systems capable of:

- Planning
- Reasoning
- Making decisions
- Using tools
- Performing actions

with minimal human intervention.""",

    # ========================================================
    # AI SECURITY
    # ========================================================

    "what are ai threats":
    """
Common AI Threats:

1. Prompt Injection
2. Data Poisoning
3. Model Theft
4. Hallucinations
5. Data Leakage
6. Jailbreak Attacks
7. Supply Chain Attacks
8. Insecure Plugins
9. Shadow AI
10. Excessive Agency
""",

    "ai threats":
    """
Common AI Threats:

1. Prompt Injection
2. Data Poisoning
3. Model Theft
4. Hallucinations
5. Data Leakage
6. Jailbreak Attacks
7. Supply Chain Attacks
8. Insecure Plugins
9. Shadow AI
10. Excessive Agency
""",

    "ai security controls":
    """
Top AI Security Controls:

1. Strong Authentication
2. Multi-Factor Authentication (MFA)
3. Role Based Access Control (RBAC)
4. Input Validation
5. Prompt Injection Protection
6. Data Encryption
7. Output Validation
8. Logging & Monitoring
9. Secure API Gateways
10. Continuous Security Testing
""",

    "top ai security controls":
    """
Top AI Security Controls:

1. Strong Authentication
2. Multi-Factor Authentication (MFA)
3. Role Based Access Control (RBAC)
4. Input Validation
5. Prompt Injection Protection
6. Data Encryption
7. Output Validation
8. Logging & Monitoring
9. Secure API Gateways
10. Continuous Security Testing
""",

    "top 10 ai security configurations":
    """
Top 10 AI Security Configurations:

1. Enable MFA
2. Enforce RBAC
3. Secure API Authentication
4. Encrypt Data at Rest
5. Encrypt Data in Transit
6. Enable Audit Logging
7. Configure Rate Limiting
8. Implement Prompt Filtering
9. Secure Secret Management
10. Continuous Monitoring
""",

    # ========================================================
    # OWASP LLM TOP 10
    # ========================================================

    "owasp llm top 10":
    """
OWASP Top 10 for LLM Applications

LLM01 - Prompt Injection

LLM02 - Sensitive Information Disclosure

LLM03 - Supply Chain Vulnerabilities

LLM04 - Data and Model Poisoning

LLM05 - Improper Output Handling

LLM06 - Excessive Agency

LLM07 - System Prompt Leakage

LLM08 - Vector and Embedding Weaknesses

LLM09 - Misinformation

LLM10 - Unbounded Consumption
""",

    "owasp agentic ai":
    """
Top Agentic AI Risks

1. Excessive Tool Permissions
2. Unauthorized Actions
3. Prompt Injection
4. Data Leakage
5. Tool Abuse
6. Memory Poisoning
7. Agent Spoofing
8. Excessive Autonomy
9. Lack of Human Oversight
10. Multi-Agent Manipulation
""",

    # ========================================================
    # THREAT MODELING
    # ========================================================

    "what is threat modeling":
    """Threat Modeling is a structured process used to identify,
analyze, and mitigate potential security threats during
the design phase of an application or system.""",

    "what is stride":
    """
STRIDE Threat Modeling Framework

S - Spoofing
T - Tampering
R - Repudiation
I - Information Disclosure
D - Denial of Service
E - Elevation of Privilege
""",

    "what is mitre atlas":
    """MITRE ATLAS is a knowledge base of adversarial tactics,
techniques, and procedures used against AI systems.""",

    "what is nist ai rmf":
    """NIST AI RMF (AI Risk Management Framework)
helps organizations identify, assess, manage,
and govern AI-related risks.""",

    # Exit Response
    "bye":
    "Goodbye! Keep learning AI, Security, and Generative AI."
}

# ============================================================
# WELCOME BANNER
# ============================================================

print("=" * 70)
print("        AI SECURITY LEARNING ASSISTANT")
print("        Rule-Based Chatbot Version 1")
print("=" * 70)
print("Type 'help' to view available topics")
print("Type 'bye' to exit")
print("=" * 70)

# ============================================================
# MAIN CHATBOT LOOP
# ============================================================
# The chatbot will continue running until the user types 'bye'
# ============================================================

while True:

    # ========================================================
    # USER INPUT
    # ========================================================

    user_input = input("\nYou: ").lower()

    # ========================================================
    # EXIT CONDITION
    # ========================================================

    if user_input == "bye":

        print("\nBot:")
        print("Goodbye! Have a great day.")

        break

    # ========================================================
    # HELP MENU
    # ========================================================

    if user_input == "help":

        print("""

=========================================================
AVAILABLE TOPICS
=========================================================

Basic
-----
• Hello
• How are you
• What is your name
• What can you do

AI Fundamentals
---------------
• What is AI
• What is Machine Learning
• What is ML
• What is Deep Learning
• What is Generative AI
• What is LLM
• What is RAG
• What is MCP
• What is Agentic AI

AI Security
-----------
• AI Threats
• AI Security Controls
• Top AI Security Controls
• Top 10 AI Security Configurations

OWASP
------
• OWASP LLM Top 10
• OWASP Agentic AI

Threat Modeling
---------------
• What is Threat Modeling
• What is STRIDE
• What is MITRE ATLAS
• What is NIST AI RMF

=========================================================

        """)

        continue

    # ========================================================
    # DEFAULT RESPONSE
    # ========================================================

    response = """
Sorry, I don't understand that question.

Type 'help' to view available topics.
"""

    # ========================================================
    # PATTERN MATCHING LOGIC
    # ========================================================

    for pattern in responses:

        if pattern in user_input:

            response = responses[pattern]

            break

    # ========================================================
    # PRINT BOT RESPONSE
    # ========================================================

    print("\nBot:")
    print(response)
