wt_calculate = input("원하는 계산은 무엇인가요?:")

#도수율
if wt_calculate == "도수울":
    def wt_calculate_Fr(Fra,Frb):
        return (int(Fra) / int(Frb)) * 1000000
    print("Fr=재해건수/연근로자수 x 1000000")
    Fra = input("재해건수를 입력하시오:")
    Frb = input("연근로자수를 입력하시오:")
    result = wt_calculate_Fr(Fra,Frb)
    print("근로시간 100만 시간당 재해발생건수는", result, "입니다.")

#강도율
elif wt_calculate == "강도율":
    def wt_calculate_SR(Sra,Srb):
        return (int(Sra) * 300 / 365) * 1000 / int(Srb)
    print("Sr=근로손실일수/근로총시간 x 1000\n""근로손실일수=휴업일수x300/365")
    Sra = input("휴업일수를 입력하시오:")
    Srb = input("근로총시간을 입력하시오:")
    result = wt_calculate_SR(Sra,Srb)
    print("근로시간 1,000시간 당 근로손실 일수는", result, "입니다.")

#연천인율
elif wt_calculate == "연천인율":
    def wt_calculate_YIN_1000(DP,GP):
        return (int(DP) / int(GP))*1000
    print("(재해자수/연평균근로자수) x 1000")
    DP = input("재해자수를 입력하시오:")
    GP = input("연평균 근로자수를 입력하시오:")
    result = wt_calculate_YIN_1000(DP,GP)
    print("근로자 1000명 당 발생하는 재해자수 비율", result, "입니다.")

#종합재해 지수(FIS)

elif wt_calculate == "종합재해지수":
    def wt_calculate_Fr_and_Sr(Fr_ans1, Sr_ans1):
        return ((int(Fr_ans1) * int(Sr_ans1)) ** (1 / 2))
    print("root(강도율 x 도수율)")
    Fr_ans1 = input("도수율을 입력하시오.:")
    Sr_ans1 = input("강도율을 입력하시오.:")
    result = wt_calculate_Fr_and_Sr(Fr_ans1, Sr_ans1)
    print("종합재해지수는 ", result, "입니다.")

#재해율

elif wt_calculate == "재해율":
    def wt_calculate_100L(DP,GP):
        return ((int(DP)/int(GP))*100)
    print("(재해자수/근로자수) x 100")
    DP = int(input("재해자 수를 입력하시오.:"))
    GP = int(input("근로자 수를 입력하시오.:"))
    result = wt_calculate_100L(DP,GP)
    print("재해율은", result, "입니다.")

#사망인율

elif wt_calculate == "사망만인율":
    def wt_calculate_D10000(JP,GP):
        return (int(JP)/int(GP))*10000
    print("(사망자수/근로자수) x 10,000")
    JP = int(input("사망자수를 입력하시오:"))
    GP = int(input("근로자수를 입력하시오:"))
    result = wt_calculate_D10000(JP,GP)
    print("근로자 10,000명 당 발생하는 사망재해자 수의 비율은",result,"입니다.")

#환산도수율(GFr)

elif wt_calculate == "환산도수율":
    def wt_calculate_GFr(GFra,GFrb):
        return (int(GFra) / int(GFrb)) * 1000000
    print("GFr=재해자수/근로총시간 x 100,000\n""도수율 x 1/10")
    GFra = input("재해자수를 입력하시오:")
    GFrb = input("근로총시간를 입력하시오:")
    result = wt_calculate_GFr(GFra,GFrb)
    print("환산 도수율은", result, "입니다.")

#안전관리비

elif wt_calculate == "안전관리비":
    def calculate_safety_management_cost(total_cost, safety_percent):
        return total_cost * (safety_percent/100)
    print("프로젝트 총비용 x 안전관리비율(%)")
    toC = float(input("프로젝트 총 비용을 입력하시오.:"))
    syp = float(input("안전관리비 비율을 입력하시오.(%):"))
    result = calculate_safety_management_cost(toC,syp)
    print("안전관리비는",result,"원 입니다.")
#환산강도율

elif wt_calculate == "환산강도율":
    def wt_calculate_GSR(GSra,GSrb):
        return (int(GSra) * 300 / 365) * 100000 / int(GSrb)
    print("GSr=근로손실일수/근로총시간 x 100,000\n""근로손실일수=휴업일수x300/365\n""강도율 x 100")
    GSra = input("휴업일수를 입력하시오:")
    GSrb = input("근로총시간을 입력하시오:")
    result = wt_calculate_GSR(GSra,GSrb)
    print("환산 강도율은", result, "입니다.")

#평균강도율

elif wt_calculate == "평균강도율":
    def wt_Sr_averge(Sr,Fr):
        return (int(Sr)/int(Fr)*1000)
    print("Sr_averge=(강도율/도수율) x 1,000")
    Sr = input("강도율을 입력하시오.:")
    Fr = input("도수율을 입력하시오.:")
    result = wt_Sr_averge(Sr,Fr)
    print("재해 1건 당 평균 근로손실일수는",result, "입니다.")


#안전하중

elif wt_calculate == "안전하중":
    def calculate_safe_load(yield_strength, safety_factor, cross_sectional_area):
        # 허용응력 계산
        allowable_stress = yield_strength / safety_factor

        # 안전하중 계산
        safe_load = allowable_stress * cross_sectional_area

        return safe_load


    yield_strength = float(input("재료의 항복강도 (MPa): "))
    safety_factor = float(input("안전계수: "))
    cross_sectional_area = float(input("단면적 (m²): "))

    safe_load = calculate_safe_load(yield_strength, safety_factor, cross_sectional_area)

    print(f"안전하중은 {safe_load:.2f} 메가뉴턴입니다.")

#종합재해위험지수

elif wt_calculate == "종합재해위험지수":
    def wt_event_total(Sr,Fr):
        return int(Sr)*int(Fr)
    print("Event_Total=(강도율 x 도수율)")
    Sr = input("강도율을 입력하시오.:")
    Fr = input("도수율을 입력하시오.:")
    result = wt_event_total(Sr,Fr)
    print("종합재해위험지수는",result, "입니다.")

#재해손실일수
elif wt_calculate == "재해손실일수":
    def calculate_loss_days(disability_grade):
        if 1 <= disability_grade <= 3:
                return 7500
        elif disability_grade == 4:
                return 5500
        elif disability_grade == 5:
                return 4000
        elif disability_grade == 6:
                return 3000
        elif disability_grade == 7:
                return 2200
        elif disability_grade == 8:
                return 1500
        elif disability_grade == 9:
                return 1000
        elif disability_grade == 10:
                return 600
        elif disability_grade == 11:
                return 400
        elif disability_grade == 12:
                return 200
        elif disability_grade == 13:
                return 100
        elif disability_grade == 14:
                return 50
        else:
            return None


    disability_grade = int(input("장애 등급을 입력하세요 (1~14): "))

    loss_days = calculate_loss_days(disability_grade)
    if loss_days is not None:
        print(f"장애 등급 {disability_grade}에 따른 재해 손실 일수는 {loss_days}일 입니다.")
    else:
        print("잘못된 등급이 입력되었습니다.")

else:
    print("다른 계산을 시도하십시오.")

#무재해운동 n일차
import time

def track_days():
    day_count = 0
    while True:
        print(f"무재해 운동 {day_count}일차 입니다.")
        day_count += 1
        time.sleep(5) #테스트를 위해 1일을 5초로 설정 실제는(24*60*60)

track_days()
# 무재해 운동 일수를 계속 기억 시키고 이어가게 하려면
# 조금 더 공부가 필요할듯..