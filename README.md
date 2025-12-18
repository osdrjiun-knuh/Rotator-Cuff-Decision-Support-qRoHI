# RoHI Decision Support System 🩺

### Developed by Ji Un Kim, M.D.
*Department of Orthopaedic Surgery, Kangwon National University Hospital*

## 📖 Overview
This application is a clinical decision support tool designed for orthopedic surgeons. It calculates the **Rotator Cuff Healing Index (RoHI)** based on the study by *Kwon et al. (AJSM 2019)* and suggests optimal surgical treatments (Repair vs. Patch vs. RTSA).

## 🚀 Key Features
1. **RoHI Scoring:** Calculates a 15-point score based on Retraction, Fatty Infiltration, Age, Tear Size, BMD, and Work Activity.
2. **Risk Stratification:** Classifies patients into Low Risk, Grey Zone, and High Risk.
3. **Advanced Decision Logic:** - Incorporates a **Fast-track RTSA algorithm** for elderly patients (>70) with severe muscle atrophy, even if the RoHI score is in the grey zone.
   - Suggests **Patch Augmentation** for intermediate risk groups.

## 💻 How to Use
This tool is written in Python. You can run it in any Python environment (e.g., Google Colab, Jupyter Notebook).

1. Download the `rohi_calculator.py` file.
2. Run the script.
3. Input patient data as prompted.

## ⚠️ Disclaimer
This tool is intended to assist clinical decision-making and does not replace the surgeon's professional judgment.

## 📄 License
This project is licensed under the **MIT License** - see the LICENSE file for details.
You are free to use, modify, and distribute this code, provided that the original author is credited.
