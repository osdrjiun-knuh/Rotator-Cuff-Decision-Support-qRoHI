"""
RoHI Calculator (Rotator Cuff Healing Index & Treatment Decision Support System)

Author: Ji Un Kim, M.D.
Department of Orthopaedic Surgery, Kangwon National University Hospital
Copyright (c) 2025 Ji Un Kim. All rights reserved.

License: MIT License
(See the LICENSE file for details. You are free to use, modify, and distribute this software, 
provided that the original author attribution is retained.)

Based on: 
1. Kwon et al., "The Rotator Cuff Healing Index...", Am J Sports Med, 2019.
2. Modified Decision Algorithm by Dr. Ji Un Kim (Incorporating Fast-track RTSA logic).
"""

def calculate_rohi_and_decision():
    print("--- [RoHI Calculator by Dr. Kim] ---")
    print("Based on Kwon et al. (2019) & Modified Algorithm\n")

    try:
        age = int(input("1. Age (years): "))
        
        print("2. Work Activity Level")
        print("   (1: Low/Sedentary, 2: High/Heavy Labor)")
        work_input = input("   Select (1 or 2): ")
        is_high_work = True if work_input == '2' else False

        tear_size = float(input("3. AP Tear size (cm): "))
        retraction = float(input("4. Retraction (cm): "))
        bmd_score = float(input("5. BMD (T-score, e.g., -2.7): "))
        infra_fatty = int(input("6. Fatty Infiltration of Infraspinatus (Grade 0-4): "))

        print("\n--- Additional Info for RTSA Decision ---")
        infra_atrophy = int(input("7. Muscle Atrophy of Infraspinatus (Grade 0-4): "))
        subscap_input = input("8. Subscapularis Tear? (y/n): ")
        has_subscap_tear = True if subscap_input.lower() == 'y' else False
        
        subscap_fatty = 0
        if has_subscap_tear:
            subscap_fatty = int(input("   L Fatty Infiltration of Subscapularis (Grade 0-4): "))

    except ValueError:
        print("\n[Error] Please enter numbers correctly.")
        return

    # --- Calculation Logic ---
    rohi_score = 0
    details = []

    # 1. Retraction
    if retraction >= 3: rohi_score += 4; details.append("Retraction>3cm(+4)")
    elif retraction >= 2: rohi_score += 2; details.append("Retraction>2cm(+2)")
    elif retraction >= 1: rohi_score += 1; details.append("Retraction>1cm(+1)")
    
    # 2. Fatty Infiltration
    if infra_fatty >= 2: rohi_score += 3; details.append("InfraFatty>=Gr2(+3)")
    
    # 3. Age
    if age > 70: rohi_score += 2; details.append("Age>70(+2)")
    
    # 4. Tear Size
    if tear_size > 2.5: rohi_score += 2; details.append("Size>2.5cm(+2)")
    
    # 5. BMD
    if bmd_score <= -2.5: rohi_score += 2; details.append("Osteoporosis(+2)")
    
    # 6. Work
    if is_high_work: rohi_score += 2; details.append("HighWork(+2)")

    # --- Decision Logic ---
    is_rtsa_candidate = False
    if age >= 70:
        if infra_atrophy >= 3: is_rtsa_candidate = True
        elif has_subscap_tear and subscap_fatty >= 3: is_rtsa_candidate = True

    rec_title = ""
    rec_reason = ""

    if rohi_score >= 10:
        rec_title = "Primary RTSA Recommended"
        rec_reason = "High RoHI Score (>=10). Very high risk of healing failure."
    elif rohi_score >= 7:
        if is_rtsa_candidate:
            rec_title = "Primary RTSA Recommended"
            rec_reason = "Grey Zone Score (7-9), but Poor Tissue Quality (Red Flag) detected."
        else:
            rec_title = "Repair + Patch Augmentation"
            rec_reason = "Grey Zone Score (7-9). High risk of failure; Augmentation required."
    else:
        rec_title = "Standard Arthroscopic Repair"
        rec_reason = "Low Risk (Score < 7). Good healing potential expected."

    print("\n" + "="*45)
    print(f"RESULTS for Patient (Age: {age})")
    print("-" * 45)
    print(f"📊 RoHI Score : {rohi_score} / 15")
    print(f"   Details    : {', '.join(details)}")
    print("-" * 45)
    print(f"✅ Recommendation : {rec_title}")
    print(f"💡 Clinical Logic : {rec_reason}")
    print("="*45)

if __name__ == "__main__":
    calculate_rohi_and_decision()