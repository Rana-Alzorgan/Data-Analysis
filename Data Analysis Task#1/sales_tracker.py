sales_data={}
product_categories=set()

#إضافة منتج جديد بقائمة مبيعات فاضية 
def add_product ():
    product_name = input("Enter Product name: ").strip()
# عدم قبول مدخل فارغ لاسم المنتج
    if not product_name:
        print("Error: product name can't ba empty")
        return
#  في حالة كان المنتج مسجل فعليا يتم اعلام المستخدم بذلك
    if product_name in sales_data:
        print("Error: This product aleady exists")
        return
# طلب ادخال فئة المنتج و عدم قبول مدخل فارغ 
    category=input("Enter Product Category: ")
    if not category:
        print("Error: Category can't be empty: ")
        return
# اضافة اسم المنتج و فئته و رسالة تأكيد بان العملية تم تنفيذها بنجاح   
    sales_data[product_name]=[]
    product_categories.add(category)
    print(f"Product '{product_name}' and its category '{category}' added successfully")



#إضافة مبيعات شهرية لمنتج مضاف و رسالة بعدم وجود المنتج اذا تم ادخال اسم منتج غير موجود مسبقا
#عدم قبول اي قيمة سالبة
#رسالة خطأ في حال اذخال قيم غير صحيحه مثلا كلمات او رموز
def add_monthly_sale():
    product_name = input("Enter Product name:").strip()
    if product_name not in sales_data:
        print("Error: Product not found , please add product first")
        return
    try:
        sales_amount=float(input("Enter the sale amount for the new month :"))
        if sales_amount <0 :
            print("Error : sales amount can't be negative")
            return
        sales_data[product_name].append(sales_amount)
        print("sales amount recorded successfully")
    except ValueError:
        print("Error : Please enter valied number")

# عرض جدول بالمنتجات و المبيعات الشهريه يتضمن عنوان الجدول و عنوان برؤوس الاعمدة و عرض عمود ثابت لاسم المنتج و فاصل بين الاعمدة
def display_sales():
    if not sales_data:
        print("No product Added yet")
        return
    print("sales data table")
    print(f"{'product':<20} | {'Monthly Sales'}")
    print()
    for product , sales in sales_data.items():
        print(f"{product :<20} | {sales}")
    print()
    if product_categories :
        print(f"Registered Categories (Set): {product_categories}")

# حساب مجموع المبيعات لمنتج معين تم ادخاله سابقا
def calculate_total_sales():
    product_name = input("Enter product name: ").strip()
    if product_name in sales_data:
        total = sum(sales_data[product_name])
        print(f"Total sales for '{product_name}' is: {total}")
    else:
        print("Error: Product not found")


# حساب متوسط مبيعات منتج معين تم ادخاله سابقا
def calculate_average_sales():
    product_name = input("Enter product name: ").strip()
    
    if product_name not in sales_data:
        print("Error: Product not found.")
        return
        
    sales_list = sales_data[product_name]
    
    if len(sales_list) == 0:
        print(f"'{product_name}' has no sales recorded yet.")
    else:
        average = sum(sales_list) / len(sales_list)
        print(f" Average monthly sales for '{product_name}' is: {average:.2f}")

# عرض المنتج الاعلى مبيعا
def find_top_product():
    if not sales_data:
        print(" There is no products")
        return
    Max_sales=-1
    Top_product=None
    for product,sales in sales_data.items():
        total_sales=sum(sales)
        if total_sales > Max_sales:
            Max_sales=total_sales
            Top_product=product
    if Top_product and Max_sales >0 :
        print(f" The Top Product is : '{Top_product}' with maximun sales = '{Max_sales}")
    else:
        print("No sales recorded yet")

def main():
    while True:
        print("===Sales Tracker System ===")
        print("1. Add New Product")
        print("2. Record Monthly Sale")
        print("3. Display Sales")
        print("4. Calculate Total Sales for a Product")
        print("5. Calculate Average Sales for a Product")
        print("6. Show Top Selling Product")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == "1":
            add_product()
        elif choice == "2":
            add_monthly_sale()
        elif choice == "3":
            display_sales()
        elif choice == "4":
            calculate_total_sales()
        elif choice == "5":
            calculate_average_sales()
        elif choice == "6":
            find_top_product()
        elif choice == "7":
            print("Exiting program")
            break
        else:
            print("Error: Invalid option, please try again.")

if __name__ == "__main__":
    main()
