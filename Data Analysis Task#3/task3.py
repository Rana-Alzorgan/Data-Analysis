
# %% [markdown]
# الخطوة 1: بناء الدوال الإحصائية الأساسية 

# %%
def calculate_count(numbers):
    count = 0
    for i in numbers:
        count += 1
    return count



def calculate_sum(numbers):

    n = len(numbers)
    if n == 0 :
        return None
    total = 0
    for i in numbers:
        total += i
    return total



def calculate_mean(numbers):

    n = len(numbers)
    if n == 0 :
        return None
    total = 0
    for i in numbers:
        total += i
    return (total/n)


def calculate_median(numbers):

    n = len(numbers)

    if n == 0 :
        return None
    
    for i in numbers:
        if not isinstance(i,(float,int)):
            return "القيم المدخلة خاطئة يرجى ادخال قيم عددية فقط"
        
    middle_index = n//2
    sorted_numbers = sorted(numbers)

    if n%2 != 0:
        median = sorted_numbers[middle_index]
    else:
        median = (sorted_numbers[middle_index] + sorted_numbers[middle_index - 1])/2
    return median



def calculate_mode(numbers):

    for i in numbers:
        if not isinstance(i,(float,int)):
            return "يجب ادخال قيم عددية فقط"

    max_count =0
    mode_value = []
    for y in numbers :
        count = 0
        for x in numbers :
            if x == y :
                count += 1

        if count > max_count :
            max_count = count
            mode_value = [y]
        elif count == max_count and y not in mode_value :
            mode_value.append(y)
    
    if max_count == 1:
        return ("لا يوجد منوال")

    return (mode_value)


def calculate_variance(numbers):

    n = len(numbers)

    if n < 2:
        return None
    for i in numbers :
        if not isinstance (i,(float,int)):
            return "يجب ادخال قيم عددية فقط"

    mean = sum(numbers) / n
    total = 0

    for num in numbers:
        total += (num - mean) ** 2

    variance = total / (n-1)

    return variance


def calculate_std(numbers):

    n = len(numbers)

    if n < 2:
        return None
    
    for i in numbers :
        if not isinstance (i,(float,int)):
            return "يجب ادخال قيم عددية فقط"
        
    mean = sum(numbers) / n
    total = 0

    for num in numbers:
        total += (num - mean) ** 2

    std = (total / (n-1)) ** 0.5

    return std

    
def calculate_min_max(numbers):

    if len(numbers) == 0 :
        return None
    for i in numbers :
        if not isinstance(i,(float,int)):
            return "يجب ادخال قيم عددية فقط"
        
    max_number = numbers[0]
    min_number = numbers[0]

    for num in numbers:
            if num > max_number :
                max_number = num
            if num < min_number :
                min_number = num
    return (min_number , max_number)


def calculate_range(numbers):

    if len(numbers) == 0:
        return None
    for i in numbers:
        if not isinstance(i,(float,int)):
            return "يجب ادخال قيم عددية فقط"
        
    max_number = numbers[0]
    min_number = numbers[0]
    
    for num in numbers :
        if num > max_number :
            max_number = num
        if num < min_number :
            min_number = num
    range_ = max_number - min_number       
    return range_


def calculate_quartiles(numbers):

    n = len(numbers)

    if n < 2:
        return "يجب ان تحتوي القائمة على عنصرين على الاقل"
    
    for i in numbers :
        if not isinstance (i,(float,int)):
            return "يجب ادخال قيم عددية فقط"

    sorted_numbers = sorted(numbers)
    middle_index = n // 2

    if n % 2 == 0:
        lower_half = sorted_numbers[:middle_index]
        upper_half = sorted_numbers[middle_index:]
    else:
        lower_half = sorted_numbers[:middle_index]
        upper_half = sorted_numbers[middle_index +1:]
    
    def median(data):
        m = len(data)

        if m == 0:
            return None

        if m % 2 == 0:
            return (data[m//2] + data[m//2 - 1]) / 2
        else:
            return data[m//2]

    q2 = median(sorted_numbers)
    q1 = median(lower_half)
    q3 = median(upper_half)

    return q1, q2, q3


def detect_outliers_iqr(numbers):

    quartiles = calculate_quartiles(numbers)

    if isinstance(quartiles,str):
        return quartiles
    
    q1, q2, q3 = quartiles
    IQR = q3 - q1

    upper_limit = q3 + 1.5 * IQR
    lower_limit = q1 - 1.5 * IQR

    outliers = []

    for number in numbers:
        if number > upper_limit or number < lower_limit:
            outliers.append(number)

    if not outliers:
        return "لا يوجد قيم شاذة"

    return outliers


# %% [markdown]
# الخطوة 2: التعامل مع المدخلات اعمل دالة get_numbers_from_user()

# %%
def get_numbers_from_user():
    while True:
        user_input = input("ادخل أرقام مفصوله بفاصله").strip()
        if user_input == "":
            print("الرجاء ادخال قيمة واحدة على الاقل")
            continue 

        numbers = []

        try:
            for num in user_input.split(","):
                numbers.append(float(num))
            return numbers

        except ValueError:
            print ("يرجى ادخال قيم عددية فقط, مفصولة بفاصلة  (,)")


# %%
def display_statistics(numbers):
    print("=== نتائج التحليل الاحصائي ===")
    
    count = calculate_count(numbers)
    summation = calculate_sum(numbers)
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers)
    std = calculate_std(numbers)
    min_max = calculate_min_max(numbers)
    minimum = min_max[0]
    maximum = min_max[1]
    calculated_range = calculate_range(numbers)
    quartiles = calculate_quartiles(numbers)
    if isinstance (quartiles,str):
        q1= quartiles
        q3= quartiles
    else:
        q1 = quartiles[0]
        q3 = quartiles[2]
    outliers = detect_outliers_iqr(numbers)

    print("عدد القيم :  ",count)
    print("المجموع :  ",f"{summation:.2f}")
    print("المتوسط :  ",f"{mean:.2f}")
    print("الوسيط :  ",f"{median:.2f}")
    print("المنوال :  ",mode)
    if variance is not None:
        print("التباين :  ",f"{variance:.2f}")
    else:
        print("التباين :  ","خطأ : يجب ان تحتوي القائمة عنصرين على الاقل ")
    if std is not None:
        print("الانحراف المعياري :  ",f"{std:.2f}")
    else:
        print("الانحراف المعياري :  ","خطأ : يجب ان تحتوي القائمة عنصرين على الاقل ")   
    print("اقل قيمة :  ",minimum)
    print("اعلى قيمة :  ",maximum)
    print("المدى :  ",calculated_range)
    print("الربع الأول  :  ",q1)
    print("الربع الثالث  :  ",q3)
    print("القيم الشاذة :  ",outliers)



# %%
def data_analysis_program():
    last_numbers = None
    while True:
        print("=== القائمة الرئيسية ===")
        print("1. إدخال قائمة أرقام جديدة وتحليلها")
        print("2. عرض آخر نتيجة تحليل")
        print("3. خروج")

        choice = input("اختر رقمًا: ")

        if choice == "1":
            last_numbers = get_numbers_from_user()
            display_statistics(last_numbers)

        elif choice == "2":
            if last_numbers is None:
                print("لا توجد نتائج تحليل سابقة.")
            else:
                display_statistics(last_numbers)

        elif choice == "3":
            print("تم إنهاء البرنامج.")
            break

        else:
            print("اختيار غير صحيح")

data_analysis_program()


